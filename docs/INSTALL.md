# Install INKAVA Video Director

Packaging revision: 2.0.1, updated 6 November 2026. Installation formats checked against official documentation on 5 November 2026.

Version 2 uses adapted SeeCut helpers as the execution foundation and the accumulated INKAVA guides as creative direction. Its upstream license and modification notices are included under `upstream/seecut`; the SeeCut software declares PolyForm Noncommercial 1.0.0, and installation does not provide commercial rights. Read `references/seecut-foundation.md` for the combined workflow and runtime setup. The existing plugin identity remains `inkava-video-director`.

## Choose the correct package

| File | Intended destination |
|---|---|
| `inkava-video-director-codex-plugin.zip` | The Codex plugin ZIP importer shown in the error screenshot |
| `inkava-video-director-claude-skill.zip` | Claude's custom-skill upload, or extract for a local skill installation |
| `inkava-video-director-gemini-skill.zip` | Gemini Apps skill upload where that feature is available |
| `inkava-video-director-multi-ai.zip` | Extract first: contains all packages, the portable skill folder, and a local installer |
| `INKAVA-video-director-full.md` | Complete standalone instructions for systems that accept knowledge documents |

The legacy filename `inkava-video-director-skill.zip` now contains the corrected Codex plugin package. Use the explicit filenames above to avoid confusing a plugin ZIP with a skill ZIP.

## 1. Codex plugin upload

Upload `inkava-video-director-codex-plugin.zip` directly to the plugin importer. Do not upload the installation-kit ZIP or the standalone Markdown file there.

The plugin ZIP has these paths at its archive root:

```text
plugin.json
.codex-plugin/plugin.json
.claude-plugin/plugin.json
skills/
  inkava-video-director/
    SKILL.md
    references/
```

The previous ZIP contained only `inkava-video-director/SKILL.md` and its references. That is a standalone skill layout; it did not expose the plugin manifest or root `skills/<name>/SKILL.md` path expected by the displayed importer. The revised package includes a portable manifest and compatibility manifests, with no extra enclosing folder. [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins)

After importing, enable/select INKAVA Video Director in a new chat and verify that its skill is available. Installing the package copies its helpers but does not install FFmpeg, the isolated runtime dependencies, official brand fonts, a CapCut file adapter, or AI-service accounts. A local runtime prepared on one machine does not travel inside the ZIP.

## 2. Claude custom-skill upload

Use `inkava-video-director-claude-skill.zip` in **Customize > Skills > add/create > Upload a skill**, then enable it. This archive contains one top-level `inkava-video-director` folder with `SKILL.md` and all reference files. Its metadata uses a short description, and the folder matches the skill name. Code execution must be enabled for the corresponding Claude skill functionality. [Claude custom skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [Claude skill packaging](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

For a local Claude Code installation, use the installer below or copy the complete skill folder to `~/.claude/skills/inkava-video-director/`. Project scope uses `.claude/skills/inkava-video-director/`. A terminal skill folder and an account-uploaded skill are different distribution routes; use the route matching the session you intend to run. [Claude Code skill locations](https://code.claude.com/docs/en/skills)

## 3. Gemini Apps and Gemini CLI

Where Gemini Apps exposes **Customize > Skills**, choose **Create > Upload** and use `inkava-video-director-gemini-skill.zip`. Its archive root contains `SKILL.md` and the references, without plugin manifests. Upload the whole package so the reference files accompany the instructions. Review the imported skill and finish creating/enabling it. Account availability and interface rollout can differ. [Gemini Apps skill uploads](https://support.google.com/gemini/answer/17094296?hl=en)

For Gemini CLI, extract the installation kit and either run the installer with `--target gemini`, or use the CLI's supported local-directory installation:

```sh
gemini skills install ./skill/inkava-video-director
```

Then verify with `/skills list`; use `/skills reload` if needed. Direct local placement uses `~/.gemini/skills/inkava-video-director/` for user scope or `.gemini/skills/inkava-video-director/` for workspace scope. [Gemini CLI skills](https://geminicli.com/docs/cli/skills/), [Gemini discovery tutorial](https://geminicli.com/docs/cli/tutorials/skills-getting-started/)

If your Gemini account still has Gems rather than the Skills interface, use the complete Markdown as a knowledge/instruction document in a custom Gem. This is a document-based fallback, not the Codex plugin importer. [Gem instructions and knowledge files](https://support.google.com/gemini/answer/15146780?hl=en)

## 4. Antigravity

Extract the kit, then run the installer with `--target antigravity`. The current documented global location is `~/.gemini/config/skills/inkava-video-director/`; workspace scope uses `.agents/skills/inkava-video-director/`. The standalone IDE also documents support for its legacy global skill directory. Keep the `references` folder beside `SKILL.md`, then inspect active skills in the agent's customization interface. [Antigravity skill locations](https://antigravity.google/docs/skills?app=antigravity-ide)

## 5. Cursor and GitHub Copilot in VS Code

Cursor: use `--target cursor`, or copy the skill to `~/.cursor/skills/inkava-video-director/` for personal use or `.cursor/skills/inkava-video-director/` in the workspace. Cursor also documents shared `.agents/skills` discovery. [Cursor skills](https://prod.cursor.com/help/customization/skills)

GitHub Copilot in VS Code: use `--target copilot`. The documented personal location is `~/.copilot/skills/inkava-video-director/`; workspace scope uses `.github/skills/inkava-video-director/`. Confirm the skill is available in the relevant agent session and settings. [VS Code skill locations](https://code.visualstudio.com/docs/agent-customization/agent-skills)

For another tool that implements Agent Skills, copy the complete portable skill folder into that tool's documented discovery directory. A Markdown upload is a fallback for document-aware systems, not a claim that every chatbot has an identical skill installer.

## 6. Local installation helper

Extract `inkava-video-director-multi-ai.zip` and open a terminal in its `inkava-video-director-kit` folder. Python 3 is required; the script uses only its standard library.

Preview the destination without writing:

```sh
python3 install.py --target antigravity --dry-run
```

Install for one selected local agent:

```sh
python3 install.py --target claude
python3 install.py --target gemini
python3 install.py --target antigravity
python3 install.py --target cursor
python3 install.py --target copilot
```

Run only the command for the product you want. `--target codex` installs a standalone local skill to `~/.agents/skills`; this is an alternative to the Codex plugin importer, not a second required installation. Avoid installing multiple same-named copies into overlapping discovery locations unless you intentionally want them.

For a workspace-specific installation, supply the actual workspace directory:

```sh
python3 install.py --target antigravity --scope workspace --workspace "/path/to/your/workspace"
```

If a previous installation exists, the script stops instead of overwriting it. To update while retaining a backup:

```sh
python3 install.py --target antigravity --replace
```

The script copies only the packaged skill. It does not edit agent settings, launch or modify CapCut, install software, call external services, or install into every product automatically. Backups are stored outside active skill discovery folders. It also supports `--destination` for an explicitly chosen full skill directory; use `--help` for options.

## 7. Verify the installation and available execution access

Ask the target AI to identify the INKAVA skill and read its offline CapCut and creative-variety guidance. If it cannot find those references, check that the whole skill folder was copied and that there is not an extra wrapper directory between the discovery root and `inkava-video-director/SKILL.md`.

For actual editing, use a local or appropriately connected agent that can access the intended CapCut draft, its linked media, and suitable media-processing tools. Loading instructions in a hosted chat does not by itself grant access to your Mac's draft folders. The default remains: the user imports footage/voice-over into CapCut, closes CapCut, and the AI edits the existing draft offline while preserving a backup.

The same English production content is included across all packages: content cuts and assembly according to the brief, full subtitles, brand rules, distinct creative treatments within one style, proactive B-roll, and useful AI illustration/motion. No example video, source frame, font binary, or production logo is bundled.

## 8. Verification status for this release

Archive structure, manifest JSON, skill metadata, reference paths, matching packaged content, and installer behavior are checked locally. Where available, a host's validation command is also used. This does not mean that upload or full video editing has been tested in every account or product. No installation is performed in your real agent profiles merely by creating these packages.
