#!/usr/bin/env python3
"""Rebuild every archive in dist/ from skills/inkava-video-director (deterministic timestamps).

Usage: python3 tools/build_dist.py
Packages: Claude skill ZIP, Codex plugin ZIP, Antigravity skill ZIP, Gemini skill ZIP, multi-AI kit ZIP.
The standalone INKAVA-video-director-full.md is maintained by hand next to the references.
"""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "inkava-video-director"
DIST = ROOT / "dist"
NAME = "inkava-video-director"
STAMP = (2026, 11, 10, 9, 0, 0)
VERSION = json.loads((ROOT / "plugin.json").read_text())["version"]


def write_zip(path, entries):
    """entries: archive path -> bytes (sorted for reproducible output)."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arc in sorted(entries):
            info = zipfile.ZipInfo(arc, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, entries[arc])


def skill_files(prefix):
    out = {}
    for p in SKILL.rglob("*"):
        if p.is_file():
            out[prefix + p.relative_to(SKILL).as_posix()] = p.read_bytes()
    return out


ANTIGRAVITY_INSTALL = """# Install for Antigravity (INKAVA Video Director __VERSION__)

This archive contains one folder, inkava-video-director/, with SKILL.md, references/, scripts/, runtime/ and upstream/.

Extract it so that SKILL.md ends up at one of these paths:

| Scope | Location |
|---|---|
| Global (current documented path) | ~/.gemini/config/skills/inkava-video-director/SKILL.md |
| Workspace | <project>/.agents/skills/inkava-video-director/SKILL.md |
| Legacy global (standalone IDE) | ~/.gemini/antigravity/skills/inkava-video-director/SKILL.md |

macOS / Linux example:

    mkdir -p ~/.gemini/config/skills
    unzip inkava-video-director-antigravity-skill.zip -d ~/.gemini/config/skills

Keep references/ beside SKILL.md. Start a new agent session, then check that the skill appears in Antigravity's customization view.

Licence note: the bundle includes adapted SeeCut helpers under PolyForm Noncommercial 1.0.0
(see inkava-video-director/upstream/seecut/LICENSE). Installation does not grant commercial rights.
FFmpeg, runtime dependencies, official brand fonts, the production logo and any service accounts are not included.
""".replace("__VERSION__", VERSION)


def main():
    DIST.mkdir(exist_ok=True)
    claude = skill_files(NAME + "/")
    gemini = skill_files("")
    antigravity = dict(claude)
    antigravity["INSTALL-ANTIGRAVITY.md"] = ANTIGRAVITY_INSTALL.encode()
    codex = skill_files("skills/" + NAME + "/")
    codex["plugin.json"] = (ROOT / "plugin.json").read_bytes()
    codex[".codex-plugin/plugin.json"] = (ROOT / ".codex-plugin" / "plugin.json").read_bytes()
    codex[".claude-plugin/plugin.json"] = (ROOT / ".claude-plugin" / "plugin.json").read_bytes()
    codex["README.md"] = (ROOT / "packaging" / "codex-plugin-README.md").read_bytes()

    outputs = {
        NAME + "-claude-skill.zip": claude,
        NAME + "-codex-plugin.zip": codex,
        NAME + "-antigravity-skill.zip": antigravity,
        NAME + "-gemini-skill.zip": gemini,
    }
    for fname, entries in outputs.items():
        write_zip(DIST / fname, entries)

    sums = {f: hashlib.sha256((DIST / f).read_bytes()).hexdigest() for f in outputs}
    kitdir = NAME + "-kit/"
    kit = {
        kitdir + "INKAVA-video-director-full.md": (DIST / "INKAVA-video-director-full.md").read_bytes(),
        kitdir + "INSTALL.md": (ROOT / "docs" / "INSTALL.md").read_bytes(),
        kitdir + "install.py": (ROOT / "install.py").read_bytes(),
        kitdir + "package-checksums.json": (json.dumps(sums, indent=2) + "\n").encode(),
    }
    for fname in outputs:
        kit[kitdir + "packages/" + fname] = (DIST / fname).read_bytes()
    kit.update(skill_files(kitdir + "skill/" + NAME + "/"))
    write_zip(DIST / (NAME + "-multi-ai.zip"), kit)

    # Legacy filename: the Codex plugin package, as in earlier releases.
    legacy = DIST / (NAME + "-skill.zip")
    if legacy.exists():
        legacy.write_bytes((DIST / (NAME + "-codex-plugin.zip")).read_bytes())
    for f in sorted(DIST.iterdir()):
        print("%10d  %s" % (f.stat().st_size, f.name))
    print(json.dumps(sums, indent=2))


if __name__ == "__main__":
    main()
