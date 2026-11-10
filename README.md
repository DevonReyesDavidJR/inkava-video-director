# INKAVA Video Director

Version **2.1.0** combines the **SeeCut execution foundation** with INKAVA's accumulated creative direction: expressive typography, complete speech subtitles, brand fonts and colors, B-roll, original illustration, motion, covers, and variation across a series.

The default workflow edits an existing CapCut draft while CapCut is closed, resolving footage and narration already imported into that project. The plugin keeps its existing `inkava-video-director` identity.

## What's new in 2.1.0

Adds `references/motion-graphics-remotion.md`: 4K 60 fps Remotion motion templates for CapCut, full-screen openers and endings, ElevenLabs v4 voice scripts, background-music prompts, retiming to the real voice, figure-honesty and NDA rules, and the macOS headless-render fix. SKILL.md gains principle 11 (render motion graphics as 4K H.264) and a reading-map entry. New package: `inkava-video-director-antigravity-skill.zip`.

## Install

Download the appropriate archive from [dist/](dist/). For Codex's plugin ZIP importer, use [inkava-video-director-codex-plugin.zip](dist/inkava-video-director-codex-plugin.zip). Claude, Gemini, Antigravity (dedicated ZIP) and other agent options are described in [the installation guide](docs/INSTALL.md); archive names in that guide are located in `dist/` here.

For a local skill installation from this checkout:

```sh
python3 install.py --target codex --dry-run
python3 install.py --target codex --replace
```

Other supported installer targets include `claude`, `gemini`, `antigravity`, `cursor`, and `copilot`. The installer backs up an existing destination before replacing it. Start a new agent session after installation.

A repository marketplace is included at `.agents/plugins/marketplace.json`. The plugin package is at the repository root, and its skill source is under [skills/inkava-video-director/](skills/inkava-video-director/).

## Runtime and direction

Read [the combined workflow](skills/inkava-video-director/references/seecut-foundation.md) and invoke the helper from the skill directory:

```sh
python3 scripts/seecut.py doctor
```

The isolated runtime convention is `~/.local/share/inkava-seecut`; dependency manifests are bundled under the skill's `runtime/` directory. Copying the plugin does not install runtime dependencies or service accounts on another machine. Official INKAVA fonts and logo artwork must come from the real project.

For tools that accept a single knowledge document, use [the complete English Markdown](dist/INKAVA-video-director-full.md). That document supplies directions; use the complete skill kit for executable helpers and their licenses.

## Validation and current limits

Rendering and geometry checks were exercised on synthetic local test compositions. Clean layouts and repeated-word timing passed; intentional obstruction of a protected action region correctly failed. The account plugin and distribution packages were read back and checked.

The complete automated AI review loop is **not yet validated**: Antigravity denied a headless command permission, and other attempts timed out. A media-content call alone did not establish reliable temporal judgment. Native CapCut compatibility has not been tested on a real project for this integration. See [the verification report](docs/integration-review.md).

No footage, example videos, source frames, private CapCut drafts, model weights, account credentials, or internal review logs are included.

## Licensing and attribution

This is an adaptation of [YeJe-cpu/SeeCut](https://github.com/YeJe-cpu/SeeCut) at revision `b05d7ed27404a064060e0d370402f562b0c0c02e`, combined with INKAVA-specific direction. SeeCut declares **PolyForm Noncommercial 1.0.0**. Installation or access to this repository does not grant commercial rights.

Read the bundled [SeeCut license](skills/inkava-video-director/upstream/seecut/LICENSE), [third-party notices](skills/inkava-video-director/upstream/seecut/NOTICE), and [modification record](skills/inkava-video-director/upstream/seecut/INKAVA-MODIFICATIONS.md). The bundled drawing helpers and supporting font retain their own Apache 2.0 and OFL notices; that font is not an approved INKAVA brand substitute. No new general license is assigned to the INKAVA-specific materials by this packaging step.
