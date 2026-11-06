#!/usr/bin/env python3
"""Install only the packaged skill files; no network, editor launch, or media changes."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys
import tempfile

SKILL_NAME = 'inkava-video-director'
USER_ROOTS = {
    'codex': '.agents/skills',
    'claude': '.claude/skills',
    'gemini': '.gemini/skills',
    'antigravity': '.gemini/config/skills',
    'cursor': '.cursor/skills',
    'copilot': '.copilot/skills',
    'shared': '.agents/skills',
}
WORKSPACE_ROOTS = {
    'codex': '.agents/skills',
    'claude': '.claude/skills',
    'gemini': '.gemini/skills',
    'antigravity': '.agents/skills',
    'cursor': '.cursor/skills',
    'copilot': '.github/skills',
    'shared': '.agents/skills',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=USER_ROOTS, required=True)
    parser.add_argument('--scope', choices=['user', 'workspace'], default='user')
    parser.add_argument('--workspace', type=Path, help='Required for workspace scope.')
    parser.add_argument('--destination', type=Path, help='Optional explicit full destination skill directory.')
    parser.add_argument('--dry-run', action='store_true', help='Show the plan without writing.')
    parser.add_argument('--replace', action='store_true', help='Back up an existing skill, then replace it.')
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    source = next((base / folder / SKILL_NAME for folder in ['skills', 'skill'] if (base / folder / SKILL_NAME / 'SKILL.md').is_file()), base / 'skills' / SKILL_NAME)
    if not (source / 'SKILL.md').is_file():
        parser.error('Packaged skill missing. Extract the complete installation kit first.')
    if args.scope == 'workspace' and args.workspace is None and args.destination is None:
        parser.error('--workspace is required for workspace scope.')
    if args.destination is not None:
        target = args.destination.expanduser().absolute()
        if target.name != SKILL_NAME:
            parser.error('--destination must end with ' + SKILL_NAME)
    elif args.scope == 'workspace':
        workspace_root = args.workspace.expanduser().resolve()
        if not workspace_root.is_dir():
            parser.error('Workspace directory does not exist.')
        target = workspace_root / WORKSPACE_ROOTS[args.target] / SKILL_NAME
    else:
        target = Path.home() / USER_ROOTS[args.target] / SKILL_NAME
    if target.is_symlink():
        parser.error('Destination is a symlink; choose an explicit regular directory instead.')
    if target.exists() and not target.is_dir():
        parser.error('Destination exists but is not a directory.')
    source_files = sorted(p for p in source.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in source.rglob('*')):
        parser.error('Packaged skill contains a symlink.')
    print('Target:', args.target)
    print('Skill destination:', target)
    print('Files:', len(source_files))
    print('Action:', 'backup and replace' if target.exists() else 'new install')
    if args.dry_run:
        print('Dry run: no files changed.')
        return 0
    if target.exists() and not args.replace:
        parser.error('Skill already exists. Use --replace to preserve a backup and update it.')
    target.parent.mkdir(parents=True, exist_ok=True)
    staging_parent = Path(tempfile.mkdtemp(prefix='.inkava-install-', dir=target.parent))
    staged = staging_parent / SKILL_NAME
    backup = None
    try:
        shutil.copytree(source, staged)
        for original in source_files:
            if original.read_bytes() != (staged / original.relative_to(source)).read_bytes():
                raise RuntimeError('Staged-file verification failed.')
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            backup_root = target.parent.parent / 'skill-backups'
            backup_root.mkdir(parents=True, exist_ok=True)
            backup = backup_root / (SKILL_NAME + '-' + stamp)
            target.rename(backup)
        try:
            staged.rename(target)
        except Exception:
            if backup is not None and not target.exists():
                backup.rename(target)
                backup = None
            raise
    finally:
        shutil.rmtree(staging_parent)
    print('Installed skill files:', target)
    if backup is not None:
        print('Previous skill backup:', backup)
    print('Refresh/restart the target agent and verify that the skill is listed.')
    print('This installs skill files and bundled helpers; it does not launch CapCut or configure AI-service accounts.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, RuntimeError) as exc:
        print('Installation failed:', exc, file=sys.stderr)
        sys.exit(1)
