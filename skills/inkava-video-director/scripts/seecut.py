#!/usr/bin/env python3
"""Run the bundled SeeCut foundation with the INKAVA profile and isolated dependencies."""
import argparse
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / 'upstream' / 'seecut' / 'scripts'
RUNTIME = Path(os.environ.get('INKAVA_SEECUT_RUNTIME', str(Path.home() / '.local/share/inkava-seecut'))).expanduser().resolve()


def environment():
    env = dict(os.environ)
    env['PATH'] = os.pathsep.join([str(RUNTIME / 'python/bin'), str(RUNTIME / 'node/node_modules/.bin'), env.get('PATH', '')])
    env['NODE_PATH'] = os.pathsep.join([str(RUNTIME / 'node/node_modules'), env.get('NODE_PATH', '')])
    return env


def run(command, *, timeout=None, cwd=None):
    return subprocess.run(command, env=environment(), cwd=cwd, timeout=timeout).returncode


def python():
    candidate = RUNTIME / 'python/bin/python3'
    return str(candidate) if candidate.exists() else sys.executable


def validate_build(directory):
    build = Path(directory).expanduser().resolve()
    cfg = json.loads((build / 'project.json').read_text())
    if cfg.get('profile') != 'inkava':
        raise ValueError('Set project.json profile to inkava; see references/seecut-foundation.md.')
    for key in ['fps', 'width', 'height', 'duration']:
        value = cfg.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError('Invalid project property: ' + key)
    for key, default in [('html', 'master.html'), ('person_dir', 'person')]:
        target = (build / cfg.get(key, default)).resolve()
        if not target.is_relative_to(build) or target == build:
            raise ValueError(key + ' must remain inside the build directory.')
    frames = (build / cfg.get('person_dir', 'person')).resolve()
    source = (build / cfg['source']).resolve() if cfg.get('source') else None
    if source and source.is_relative_to(frames):
        raise ValueError('Source media must not be stored in the generated-frame directory.')
    if frames.exists():
        for item in frames.iterdir():
            if item.name == '.extracted.json' or (item.name.startswith('p') and item.name[1:-4].isdigit() and item.suffix == '.jpg'):
                continue
            raise ValueError('Generated-frame directory contains unrelated data: ' + str(item))
    for region in cfg.get('protected_regions', []):
        rect = region.get('rect', [])
        if len(rect) != 4 or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in rect) or rect[2] <= 0 or rect[3] <= 0:
            raise ValueError('Invalid protected region rectangle.')
        if not region.get('id') or not 0 <= region.get('start', -1) < region.get('end', -1) <= cfg['duration']:
            raise ValueError('Invalid protected region interval.')
        if not 0 <= region.get('max_overlap', 0) <= 1:
            raise ValueError('Invalid protected region overlap tolerance.')
    return build


def doctor(ping):
    env = environment()
    checks = {}
    for name in ['node', 'ffmpeg', 'ffprobe', 'agy', 'hyperframes']:
        checks[name] = shutil.which(name, path=env['PATH'])
    checks['faster_whisper'] = subprocess.run([python(), '-c', 'import faster_whisper'], env=env, capture_output=True).returncode == 0
    checks['playwright_core'] = subprocess.run(['node', '-e', "require('playwright-core')"], env=env, capture_output=True).returncode == 0 if checks['node'] else False
    checks['runtime'] = str(RUNTIME)
    checks['video_review'] = 'not tested by local dependency discovery'
    print(json.dumps(checks, indent=2), flush=True)
    missing = [k for k in ['node', 'ffmpeg', 'ffprobe', 'agy', 'hyperframes', 'faster_whisper', 'playwright_core'] if not checks[k]]
    if missing:
        print('Missing: ' + ', '.join(missing), file=sys.stderr)
        return 2
    if ping:
        with tempfile.TemporaryDirectory(prefix='inkava-seecut-ping-') as directory:
            return run([checks['agy'], '--sandbox', '--mode', 'accept-edits', '--settings', '{"toolPermission":"proceed-in-sandbox"}', '--new-project', '--add-dir', '.', '--model', 'gemini-3.8-flash-high', '-p', 'Reply exactly OK. Do not use tools, read files, or make any changes.', '--print-timeout', '30s', '--output-format', 'json'], timeout=45, cwd=directory)
    return 0


def transcribe(arguments):
    ap = argparse.ArgumentParser(prog='seecut.py transcribe')
    ap.add_argument('audio', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--language')
    ap.add_argument('--model', default='small')
    args = ap.parse_args(arguments)
    if importlib.util.find_spec('faster_whisper') is None:
        return run([python(), str(Path(__file__).resolve()), 'transcribe', *arguments]) if python() != sys.executable else 2
    if args.out.resolve() == args.audio.resolve():
        raise ValueError('Transcript output must not replace the source media.')
    from faster_whisper import WhisperModel
    model = WhisperModel(args.model, device='cpu', compute_type='int8')
    segments, info = model.transcribe(str(args.audio), language=args.language, word_timestamps=True)
    result = {'language': info.language, 'segments': [], 'words': []}
    for segment in segments:
        words = [{'word': word.word, 'start': word.start, 'end': word.end, 'probability': word.probability} for word in segment.words or []]
        result['segments'].append({'start': segment.start, 'end': segment.end, 'text': segment.text, 'words': words})
        result['words'].extend(words)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command', choices=['doctor', 'render', 'geometry', 'read', 'judge', 'layers', 'plan', 'transcribe'])
    ap.add_argument('arguments', nargs=argparse.REMAINDER)
    args = ap.parse_args()
    rest = args.arguments
    if args.command == 'doctor':
        if rest not in [[], ['--ping']]:
            ap.error('doctor accepts only --ping')
        return doctor(bool(rest))
    if args.command == 'transcribe':
        return transcribe(rest)
    if args.command in ['render', 'geometry', 'layers']:
        if not rest:
            ap.error(args.command + ' requires a build directory')
        build = validate_build(rest[0])
        file = {'render': 'render.mjs', 'geometry': 'geom-check.mjs', 'layers': 'jianying_layers.mjs'}[args.command]
        return run(['node', str(ENGINE / file), str(build), *rest[1:]])
    if args.command == 'read':
        return run(['zsh', str(ENGINE / 'agy_read.sh'), *rest])
    if args.command == 'judge':
        return run([python(), str(ENGINE / 'agy_judge.py'), *rest])
    return run([python(), str(ENGINE / 'jianying_plan.py'), *rest])


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print('SeeCut integration: ' + str(error), file=sys.stderr)
        sys.exit(2)
