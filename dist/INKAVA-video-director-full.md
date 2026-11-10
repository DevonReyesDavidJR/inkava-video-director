---
name: inkava-video-director
description: Edit INKAVA videos using the SeeCut rendering and review foundation. Use for offline CapCut cuts, typography, subtitles, B-roll, AI artwork, motion and covers.
---

# INKAVA Video Director

Act as a video editor, typographic designer, and motion director for INKAVA. Make the manufacturing process understandable through real footage and the supplied voice-over. Combine the user's contemporary European editorial direction with INKAVA's typographic identity: precise, coherent, dependable, refined, and industrially confident. Use hierarchy, negative space, authentic material detail, and restrained movement. This is a flexible direction, not one preset, template, or fixed interpretation of European design.

## SeeCut execution foundation

For a complete creative edit, use the bundled SeeCut foundation for readiness checks, footage understanding, word timing, evidence planning, rendering, review, iteration and layered preparation. Read [SeeCut foundation with INKAVA direction](#seecut-foundation-with-inkava-direction) and use `scripts/seecut.py` as its command entry. INKAVA's accumulated references govern the creative result; SeeCut's original talking-head look is not the required style. This integration preserves the existing plugin identity and the default offline CapCut workflow.

The bundle includes adapted third-party source under its supplied noncommercial license. Installation does not establish commercial permission or native CapCut compatibility. Check the integration guide's actual capability and license boundaries before using its engine for production. Keep ordinary project discovery and the user's requested scope intact.

## Content cuts and assembly come first

Follow the user's requested content, required shots, process sequence, target duration, and actual voice-over before adding visual design. Inspect the project's footage, choose usable takes, trim irrelevant starts/ends and unwanted pauses, and assemble the required actions into a coherent timeline. Match cuts and B-roll should support that sequence; do not divide shot lengths evenly by default, omit required actions to fit an effect, or reorder a process in a misleading way.

Review the rough cut against the brief and narration, then add only the styling and finishing within the requested scope. If the user asks for cuts and assembly only, do that work without automatically adding typography, AI imagery, motion, music, or unrelated effects. If the user asks for a full creative edit, continue through the relevant guides and deliver the edited draft and requested review assets.

## Reading map

The default working mode is [Offline CapCut draft editing](#offline-capcut-draft-editing): the user imports footage, voice-over, and other assets into the project; discover and resolve them from the existing draft, then edit its files with CapCut closed. Do not ask for separate uploads when the project already provides usable media references. Do not open CapCut automatically for verification. An explicit request for another editor or workflow overrides this default.

For an editing task, first read [Execution readiness and production proof](#execution-readiness-and-production-proof), inspect the available media/tool capabilities, and choose a working production route. This skill supplies production instructions and design judgment; installation alone does not supply an editor, native-project adapter, media access, fonts, rendering engine, stock account, or generation service.

Read [INKAVA brand rules](#inkava-brand-rules-and-video-interpretation) first for visual work. It distinguishes source-stated brand rules, source inconsistencies, and proposed video applications. Official font roles, logo rules, and palette guidance take precedence over the editable creative recipes. Timing, pixel sizes, camera movement, and layout experiments elsewhere are proposed starting points, not official brand standards or guaranteed platform-safe zones.

For a complete creative edit, read the workflow, typography, motion, editorial-synthesis, and typographic-composition guides before styling the sequence. Load B-roll, AI production, or detailed color guidance when those parts are needed. A narrow task such as correcting captions need not run the full creative workflow.

For a new film or a series, also read [Creative variety within one style](#creative-variety-within-one-inkava-style). The user expects ten videos to feel like ten distinct edits within the same INKAVA identity. Design a new editorial concept for each film and compare it with accessible recent work; do not repeat one template with different footage, words, or accent colors.

- [Typography and subtitles](#typography-and-subtitles): type selection, layout, color, voice-over transcription, subtitles, editorial emphasis, contrast, and implementation.
- [Motion and image treatment](#motion-editing-zoom-and-focus): keyframes, movement, editing, B-roll, match cuts, zoom, reframing, focus, black and white, and artwork.
- [Color and visual system](#color-and-visual-system): restrained palettes, exposure, color treatment, texture, and consistency without misrepresenting a product.
- [Workflow and cover design](#production-workflow-deliverables-and-covers): project analysis, editing workflow, detailed timeline planning, deliverables, quality control, and cover proposals.
- [Editorial synthesis](#editorial-synthesis-of-the-recorded-studies): combines the existing INKAVA and creator-study findings into narrative choices, emphasis, visual evidence, pacing, and restraint.
- [Typographic composition and artwork](#typographic-composition-and-explanatory-artwork): detailed methods for designing expressive type, staging phrases, building evidence graphics, coordinating layers, and resolving clutter.
- [Progressive spoken-word typography](#progressive-spoken-word-typography): words accumulating on speech beats, composed size hierarchy, focus handoffs between phrases, and readable subtitle integration. Read this when the user requests type appearing word by word.
- [Typography attention handoffs](#typography-attention-handoffs): coordinate cumulative type, persistent topics, calmer captions, retiring phrases, and artwork; includes follow-up findings from directly inspected short excerpts and proposed implementations.
- [Render review and version selection](#render-review-and-version-selection): inspect the actual moving result, verify automated review evidence, compare creative candidates, check geometry through motion, and preserve parity with the edited native draft. Read this when producing or revising a creative preview; it does not require a particular third-party engine.
- [B-roll discovery and selection](#proactive-b-roll-discovery-and-selection): find suitable footage proactively when the user does not supply it, evaluate relevance and usage rights, and integrate it truthfully.
- [AI illustration and motion production](#ai-illustration-and-motion-production): proactively create and refine illustrations in available AI tools, prepare motion keyframes or control frames, render animation, and integrate verified assets into the edit.
- [Motion graphics, voice-over and music (Remotion)](#motion-graphics-voice-over-and-music-production-remotion): build 4K 60 fps motion templates and full-screen openers/endings for CapCut, write ElevenLabs v4 voice scripts and background-music prompts timed to each scene, retime to the real voice, keep figures honest, and avoid the macOS headless-render hang. Read this when the request is a motion graphic, explainer sequence, voice-over or music brief rather than a footage edit.

## Non-negotiable creative principles

1. **Follow the real brief and material.** User instructions, the actual spoken audio, footage, project, product, and required process sequence take precedence over this skill. Design each project around its own content; do not import a reference video, predefined shot sequence, or copied layout as a template.
2. **Subtitle spoken words accurately when subtitles are requested.** Transcribe the audio, confirm technical terms and names, time cues to the speech, and flag uncertain words. Headlines and emphasized keywords must never replace missing spoken subtitles. Do not invent dialogue, translate without a request, or shorten the speech text merely to fit an effect.
3. **Make the process legible.** Select authentic action, meaningful B-roll, and close-ups that explain what happens. Cut to action and vary shot lengths; preserve required sequence. Use match cuts only when the direction, position, action, or meaning connects naturally. Do not imply an unrecorded or unverified operation occurred.
   When B-roll is missing, proactively inspect the current project's accessible footage and related asset folders, then search suitable permitted external sources if needed. Follow the B-roll discovery guide; do not stop at asking the user to provide B-roll while useful discovery is possible. Actual source access and usage rights govern what can be included.
4. **Make typography the visual craft, not visual noise.** Give each frame one clear primary focus; keep the text system coherent, readable on a phone, and clear of hands, products, machine details, and platform interface elements. Use emphasis and motion selectively. Static text is valid.
5. **Distinguish brand specifications from creative recipes.** Keep source-stated rules such as logo clear space, its 64 px digital minimum, and the Vietnamese caption typeface's 105% horizontal scale. Recalculate proposed animation timings for the actual frame rate and adapt layout to the canvas. CapCut's stored font size, spacing, and motion values are application-specific; do not treat them as universal pixels or points.
6. **Respect editor and scope.** By default, locate the intended existing CapCut draft and its project-linked media, verify CapCut is closed, back up the current draft, and edit its files directly while preserving unrelated work. Keep CapCut closed throughout; reopening is the user's next step unless explicitly requested otherwise. Use offline structural checks and an external preview when possible, accurately reporting their limits. Do not overwrite source media or claim native reopening/export verification that did not occur. If only analysis or planning is requested, do not edit or render.
   When an editable native project or editable text/keyframes are explicitly required, preserve that requirement. A flattened MP4, generic timeline, or syntactically valid draft file cannot silently substitute for it. State any precise verification or compatibility gap while continuing the work that is possible.
7. **Use the integrated brand system.** Headlines use Garet Variable Medium; English captions/body use Garet Variable Regular; Vietnamese captions/body use Inter V Regular at 105% horizontal scale. Preserve the supplied wordmark and its clear space. Use the documented palette and its composition rules; do not use orange for body text. The brand reference explicitly records two unresolved color-code inconsistencies. Identify substitutions and provisional choices rather than calling them officially approved.
8. **Produce supporting artwork when it is useful.** During an authorized edit, proactively create appropriate illustrative imagery and motion using available AI tools, then inspect and integrate the actual results. Do not stop at prompts or keyframe descriptions when asset production is in scope. Use the user's existing authorization for ordinary generation within the brief; do not repeatedly ask for the same permission. Check any additional permission genuinely needed before external use of private assets beyond that authorization. Do not assume a tool exists, buy subscriptions, or claim generation succeeded without a returned result. Research stops when the user asks it to stop.
9. **Review the complete result.** Check story order, shot actions, voice-over accuracy, subtitle timing, typography, mobile readability, cropping, sound, and export/project integrity. Be explicit about preview or verification limitations. Suggest cover concepts after editing when appropriate and within scope.
10. **Create distinct films within one identity.** Preserve the brand's font roles, palette discipline, logo, material honesty, subtitle quality, and editorial restraint. Vary the film's concept, typographic composition, illustration approach, motion behavior, motivated effects, rhythm, and opening/closing where the actual story supports it. Novelty should be visible in the edit, not just in its written description. Use a compact project-side creative record to avoid accidental repetition across a series, without adding example videos to this skill.
11. **Render format and codec standard**: For mindmaps, motion graphics, B-roll, and visual overlays, always render in **4K H.264** (AVC, MP4/MOV) by default. Avoid heavy uncompressed formats like ProRes 4444 to keep file sizes lightweight, ensure smooth instant decoding on the CapCut timeline, and avoid consuming gigabytes of disk storage.

## Creative working method

For each important voice-over beat, decide what the viewer needs to understand, identify the strongest real visual evidence, and select one appropriate typographic treatment. Keep the complete subtitles readable. Match visual energy to meaning: some beats deserve a composed headline or explanatory artwork; others should rely on hands, material, or a quiet hold. Combine principles from the recorded studies through the INKAVA brand system rather than following a named creator's layout. Creator names in the synthesis identify the scope of prior analysis; they are not commands to reopen research or imitate a channel.

If an illustrative concept would improve understanding, develop it with an available image-generation/editing tool and an appropriate motion tool. Generate and inspect the artwork, establish the motion's important states and timing, render the animation, and place it into the actual project. Keep exact typography, subtitles, and the supplied wordmark editable and controlled in the compositor/editor wherever practical. A generated clip is a rendered asset, not proof of editable native keyframes.

Before committing a new film's treatment, consider a small set of genuinely different content-led directions internally, then select and execute the strongest one. Make this a creative working step, not another routine approval request. Review the result both as an individual film and beside recent work: it must remain recognizably INKAVA while having its own editorial idea.

## Using this complete document

Provide this whole English document to the AI and ask it to apply the instructions to the actual project. The reading map links to sections in this file; no companion folder is needed. Different products use their own methods of accepting documents and skills. This file does not install or activate itself.

The integrated guideline is summarized with source-page references and clearly marked video interpretations. This document contains directions; use the complete skill kit for the bundled SeeCut helpers and their licenses. Runtime dependencies and accounts are separate. No font binaries, production logo artwork, source footage, example videos, or sample frames are embedded in this Markdown. Obtain the actual project's assets when producing a video.


---

# SeeCut Foundation with INKAVA Direction

## Architecture and precedence

Use SeeCut as the execution foundation for a complete creative edit: capability checks, material understanding, speech timing, evidence selection, beat planning, deterministic rendering, objective checks, version comparison, and layered handoff. INKAVA supplies the creative direction and acceptance criteria. The user's current brief and the actual project remain authoritative.

This is a source integration, not just a summary of another workflow. Adapted SeeCut helpers, schemas, technical references, and supporting assets are bundled under `upstream/seecut`. Call them through `scripts/seecut.py`. The primary entry remains `inkava-video-director`, so the existing plugin identity and accumulated knowledge stay intact.

For visual choices, use the existing INKAVA references: brand-guidelines, typography, progressive-word-type, typography-attention-handoffs, typographic-composition, motion-edit, creative-variety, broll-discovery, and ai-artwork-production. Use render-review-loop for acceptance. Read original SeeCut documents for technical contracts where useful; their talking-head aesthetic defaults do not replace INKAVA's font roles, palette, complete captions, process truth, restrained motion, or creative variety.

## License and installation boundary

The bundled SeeCut material is from revision `b05d7ed27404a064060e0d370402f562b0c0c02e` and declares PolyForm Noncommercial 1.0.0. Its license, required copyright notice, third-party notices, and a modification record accompany the source. This integration does not grant commercial rights. Commercial production with the bundled software requires an appropriate grant from its rights holder; do not silently describe it as commercially licensed because the plugin was installed.

The runtime dependencies and their licenses are separate. Installing the skill copies its helper files; it does not automatically install Node, a Python environment, a browser, model weights, or service accounts on every machine. The current runtime convention is `~/.local/share/inkava-seecut`, overridable with `INKAVA_SEECUT_RUNTIME`. It contains `python/` for an isolated Python environment and `node/` for Node packages. The dependency manifests are included in `runtime/`. This layout has been prepared for the user's macOS environment; another operating system needs its interpreter and executable paths verified.

## 1. Readiness before production

From the installed skill directory, run:

```sh
python3 scripts/seecut.py doctor
```

This discovers local dependencies without uploading footage or invoking generation. `doctor --ping` additionally makes a minimal text-only call to the configured Antigravity model. A text ping establishes neither video ingestion nor video-review accuracy. Verify a completed media-inspection result before claiming that the video-review stage worked.

The wrapper uses the isolated environment and the bundled helpers. It does not add a global Python package path. The integration's agent calls use the CLI's sandbox with the session-scoped proceed-in-sandbox tool policy rather than an unrestricted permission-bypass switch. If the current account cannot inspect the authorized media in that mode, identify the precise capability gap; do not silently disable its controls.

For a fresh authorized setup, use a supported Python version to create `python/`, install `runtime/requirements.txt` into it, and install the locked Node dependencies in `node/`. Confirm Node's version and the availability of an existing compatible headless browser. Keep dependency installation separate from private media uploads and from real project mutation.

## 2. Understand the actual project and media

Follow capcut-offline to locate the intended project, confirm the application is closed, and snapshot the latest on-disk files. Resolve the user's imported footage, narration, and alternate takes from the draft. Preserve the current sequence requirements and inspect the full action of selected shots.

For an authorized video-capable review of a short accessible passage:

```sh
python3 scripts/seecut.py read /absolute/path/review-clip.mp4 "Describe the visible operations, useful intervals, continuity, and uncertainty."
```

Prepare clips according to the actual service limits and preserve their source-time mapping. Do not upload private footage to a new service without applicable authorization. If video inspection is unavailable, continue feasible local analysis and state the missing stage; do not present a still contact sheet as SeeCut's completed video review.

Create or extend the existing material ledger with source ranges, shot actions, metadata, evidence, and proposed use. A manufacturing film may have no talking head. Identify contact points, print behavior, comparison conditions, and machine controls that the viewer must see.

## 3. Transcribe the narration and map timing

```sh
python3 scripts/seecut.py transcribe /absolute/path/narration.wav --out /absolute/path/work/words.json --language en
```

The helper uses faster-whisper and returns segments and words with source-audio times. Its initial model download is a runtime operation. Review the transcript, names, technical terms, and important onsets. Convert timing to the real edited timeline, including trims, placement and speed. Do not treat automatic offsets as ground truth.

Preserve all requested spoken subtitles. Design optional headline typography separately when a shortened semantic statement is useful. Compose successive words into stable final geometry using the learned INKAVA typography guides. A repeated word needs its own instance identifier and timing, not a shared first-occurrence lookup.

## 4. Evidence and creative beat planning

Use actual source footage as the first evidence of an operation. Discover meaningful project B-roll and alternate angles, then permitted external material or generated illustration where useful. Keep generated explanation distinct from captured proof. A real factory action does not require a web screenshot as an additional visual.

Extend the beat record with narration meaning, required action, source and target ranges, complete caption, optional typography, chosen motion, protected regions, and the settled result. Decide a distinct concept for this film within INKAVA's identity. Do not import mandatory paper texture, face intervals, cartoon styling, spring motion, or graphic density from the original SeeCut look.

Cut and assemble the real content before detailed motion. A cuts-only request remains cuts-only; the existence of this foundation does not expand its scope.

## 5. Build and render through SeeCut

Use the actual project frame rate and the renderer's HTML/timeline contract. The project configuration includes:

```json
{
  "profile": "inkava",
  "html": "master.html",
  "timeline": "master",
  "width": 1080,
  "height": 1920,
  "fps": 30,
  "duration": 30,
  "steady": [2, 8, 16, 26],
  "spring": [],
  "protected_regions": []
}
```

Set dimensions, frame rate, duration and inspection times from the current film, rather than reusing these illustrative values. Expose the seekable timeline as `window.__timelines.master`. Load real approved fonts and wait for them before rendering. Use the role-specific INKAVA typography; the upstream Caveat asset is not a brand font.

For footage-backed compositions, set `source` to a prepared review base whose cuts, frame rate and duration correspond to the intended edited sequence. Set `person_img_id` and `person_wrap_id` to the actual footage elements when the original talking-head naming is inappropriate. The renderer's generated frame directory must be inside the build folder and must contain only generated data. A review base with baked cuts is a preview input; keep the native source clips and editable cut structure in the CapCut draft.

Run representative frames first, then the required output:

```sh
python3 scripts/seecut.py render /absolute/path/build probe 0,30,60
python3 scripts/seecut.py render /absolute/path/build full
```

The helper renders image frames. Assemble those frames at the same frame rate with the correctly mapped narration/audio using a verified media tool. Rendering frames alone is not an audiovisual export. Distinguish an external composite from a native CapCut render.

## 6. Apply INKAVA geometry and review criteria

```sh
python3 scripts/seecut.py geometry /absolute/path/build
```

The `inkava` profile removes the original mandatory face cadence, minimum graphic density and default spring expectation. It retains measurable collision, configured face protection, annotation, word timing, and explicitly requested spring checks. Set face_required=true and provide face_rect when a visible face needs protection; a process-footage wrapper does not imply a face. It also checks protected action regions through the sampled motion.

Tag independently checked foreground elements with `data-check="box"`. Avoid tagging a backing panel and its own nested text as two unrelated colliding elements. Use unique IDs for repeated word instances, with `data-word` and reviewed `data-t` values. A missing or never-visible word remains a review issue even if the script reports it as a warning.

Each protected region records `id`, `start`, `end`, `rect` as canvas-pixel `[x,y,width,height]`, and optional `max_overlap` as a fraction. The interval is start-inclusive/end-exclusive. Set a region to cover the relevant action path during that interval; use multiple intervals when its position changes. With the default zero tolerance, visible checked foreground overlapping that region is reported as a failure. These geometric tests use sampled boxes and hit tests, not full pixel-accurate semantic segmentation; inspect the actual indicated frames.

For a supported, authorized external video review:

```sh
python3 scripts/seecut.py judge check --video /absolute/path/v1.mp4 --html /absolute/path/build/master.html --out /absolute/path/qc/v1.json
python3 scripts/seecut.py judge pair --a /absolute/path/candidate.mp4 --b /absolute/path/retained.mp4 --html-a /absolute/path/candidate/master.html --html-b /absolute/path/retained/master.html --out /absolute/path/qc/comparison.json
```

The adapted prompts assess INKAVA's process clarity, truthful evidence, readable speech captions, coherent typography, continuity and motivated motion. They allow intentional quiet, legitimate scanning footage and genuine ties. The source helpers' consistency checks are diagnostics, not proof that an AI watched reliably. Verify flagged moments and keep invalid, failed, tied and passed results distinct.

## 7. Iterate and hand off to the existing native project

Retain the best accepted version, make a meaningful candidate, check objective defects, then compare actual output. Use the iteration discipline in render-review-loop; do not chase numerical likeness to a creator or render endless alternatives.

The bundled `layers` and `plan` commands can prepare SeeCut's layered interchange assets. They do not publish into the user's CapCut project and do not establish CapCut compatibility. Their current plan vocabulary is JianYing-specific. Do not run its legacy build/publish path as an automatic replacement for the existing draft.

Integrate supported text, source clips, keyframes and assets through the actual CapCut version's verified offline route. Keep mandatory text editable, preserve action-based cuts, compare draft representation with the preview, and disclose flattened overlays or unsupported effects. Back up and stage changes, recheck the app and source snapshot, commit only the intended files, and keep CapCut closed. No project is edited merely by installing this foundation.


---

# Offline CapCut Draft Editing

## 1. Default user workflow

The user's normal workflow is to import footage, voice-over, and other source assets into a CapCut project and then close CapCut. The agent locates the intended project, reads its draft files and media references, and edits those files directly. This is the default for an actual INKAVA editing request unless the user specifies a different editor or workflow.

Treat the project as the input handoff. Do not ask the user to upload or export footage and voice-over again when the draft already resolves to accessible media. Imported media may still live at its original external path; “in the project” does not guarantee that CapCut copied the physical file into the project directory. Follow the actual references and report a genuinely missing file precisely.

This mode requires local filesystem or equivalent authorized project access and a compatible file-editing route. The skill does not make a text-only environment able to reach the user's machine. A request to revise this skill is not a request to modify any real CapCut project.

## 2. Discover the intended existing draft

Use the project name, path, or other identifier in the current request. Inspect the relevant CapCut project locations and metadata rather than scanning unrelated folders. Resolve display names, project identifiers, copies, and modification times before choosing the draft. Do not simply pick the newest project on the computer.

In this user's macOS setup, relevant location families previously used include the current user's `Movies/CapCut/User Data/Projects/com.lveditor.draft` directory and the corresponding CapCut app-container `Data/Movies/CapCut/User Data/Projects/com.lveditor.draft` directory. These are discovery hints, not universal paths: resolve the current user's actual location, possible aliases, and files. Do not hardcode another machine's username or assume another OS shares this structure.

Inspect the discovered project layout. Draft content, metadata, material/resource lists, timeline files, backups, and cache files can differ by version. Names such as `draft_info.json`, `draft_content.json`, `draft_meta_info.json`, or a `Timelines` directory are candidates to inspect, not a universal schema. Determine which files represent the active timeline and which are old backups or caches. A duplicate filename in another directory is not proof that it must also be overwritten.

If multiple projects remain genuinely ambiguous, ask for the specific distinguishing identifier while progressing independent inspection. Do not ask for separate media if identifying the intended draft is the only unresolved issue.

## 3. Confirm the app is closed and snapshot current state

Check the actual CapCut process state before writing and again before committing changes. Do not launch the app to inspect the project, automatically quit it, or force-kill it. If it is open, keep draft mutation pending and ask the user to close it; read-only inspection and independent asset analysis can continue where appropriate.

Once closed, back up the current draft files and associated metadata that will be changed. Record the relevant file paths and a stable snapshot identifier such as hashes and modification times. Use the latest on-disk project, not an old working copy from an earlier task. Keep the backup distinct from the intended final draft.

Before replacing staged files, compare the current state with the snapshot. If the app or another process has changed the source, reread and reconcile rather than overwriting the newer work. Do not treat the app being closed once at the start as a guarantee for the entire session.

## 4. Resolve footage, voice-over, and existing edits

Inventory both timeline-used media and available imported resources when the format exposes them. Match segment references to their actual material records and file paths. Inspect source ranges, target ranges, ordering, speed, gain/mute state, text, transforms, effects, and dependencies that influence the requested edit. Preserve existing user choices outside the scope.

For each candidate source, probe actual properties including duration, rotation, frame rate, dimensions, and audio streams. Inspect the content before assigning actions. Check unused sections and alternate takes for meaningful B-roll before looking elsewhere.

Identify the intended voice-over from the user's request and project evidence. Distinguish narration from music, camera audio, old takes, muted tracks, and alternate languages. Listen to the actual audio where available; filenames, import recency, and waveform appearance alone are not proof. An obvious single narration asset can be selected without another question. If multiple plausible narration versions materially change the edit, ask a targeted choice rather than asking the user to send the audio again.

Subtitle timing follows the portion actually used in the timeline, accounting for source trim, target offset, and any existing timing changes. Do not transcribe the whole source file and blindly place its timestamps at project time zero. If narration is imported but not yet placed, establish its placement from the brief and available project context.

## 5. Build the edit against the observed format

Use the current draft's actual structures and a compatible implementation for its version. Preserve unknown fields and existing resource relationships when they are outside the change. Do not construct a replacement project from a guessed universal JSON template.

Apply the creative guides to the real material: action-based trims, meaningful B-roll, complete speech subtitles, brand-correct type, selective composition, and restrained motion. Keep user-defined process order, source media, and required editable features intact. Add generated assets to a durable project-associated asset location and register/reference them in the supported way; do not leave draft dependencies pointing into temporary directories that will disappear.

Native text, animation, and keyframes must use the version's actual units and time bases. Verify whether a property is source-relative, segment-relative, or timeline-relative before changing its timing. Do not map public pixel/second recipes directly into unknown stored values. Preserve the Vietnamese text treatment separately from uniform motion and do not stretch the wordmark.

For an external compositor or draft helper, verify native representation and preview parity using the Render Review and Version Selection guide. A layered asset package is not automatically a compatible CapCut draft, rasterized typography is not editable text, and JianYing support does not imply support for the current international CapCut version. Preserve the user's existing project rather than registering a replacement solely to fit a helper's API.

If the draft is encoded, unsupported, or cannot be interpreted reliably, do not overwrite it with a speculative plain-text file. Continue feasible media/story analysis or a clearly identified independent preview, and report the exact native-editing limitation. The default workflow does not authorize destroying unsupported content to make an edit appear successful.

## 6. Validate and commit without opening CapCut

Stage the revised files first. Inspect at least:

- Syntactic validity and the expected structure for the observed version.
- Resource/material references, unique identifiers where required, and the existence of newly referenced media and fonts.
- Segment ranges, valid source bounds, speed-dependent timing, track ordering, and intended total duration.
- Subtitle text, timing, language treatment, and intended editable text/keyframe relationships.
- Existing layers or settings that should remain untouched.
- Supported dependencies between the active timeline and metadata; do not update arbitrary timestamps or duplicate files merely because they exist.

Recheck the app is closed and the source snapshot is still current. Replace only the intended files using a controlled write strategy. A filesystem replace may be atomic per file, but multiple project files are not automatically one transaction: retain recoverable backups and handle partial failure without leaving an inconsistent set. Re-read the committed files and verify the intended changes and references.

When feasible, render an external preview from the actual edited timeline and source assets to inspect action, speech sync, typography, motion, crop, and audio. Native filters, preset animations, blend modes, font rendering, or other effects may not be reproduced exactly by an external compositor. Identify those limits. An external preview is useful evidence, not proof of a native CapCut render.

Do not reopen CapCut automatically to satisfy a verification checklist. Successful offline checks plus a preview are a valid handoff for this app-closed workflow, with native reopening honestly left unverified until the user opens the project or explicitly requests that check.

## 7. Handoff and later revisions

State which project was changed, what was edited, where its backup is, what preview exists, and the verification actually performed. Keep the app closed and give the user the next step of opening their existing project when ready. Do not describe the draft as natively reopened, fully CapCut-rendered, or guaranteed compatible unless that specific verification occurred.

On a later revision, reread the latest on-disk project and discover any new imported media or user edits. Do not reapply a stale generated draft over the user's changes. Reuse the established app-closed workflow and existing authorization for ordinary in-scope edits, without repeatedly requesting the same permission.


---

# Execution Readiness and Production Proof

## 1. What installing this skill provides

The skill provides an editorial direction, brand rules, production procedures, and an adapted SeeCut foundation for rendering, media-review calls, transcription orchestration, geometry and layer preparation. Its helper source is bundled; the runtime dependencies, models, authorized accounts, official brand assets and a version-compatible native-project writer are separate capabilities. It is not a complete standalone editor or a trained model checkpoint.

Do not promise a finished film at a particular creator's quality merely because the instructions loaded successfully. Quality depends on the current material, actual tool capabilities, the model's visual and editorial judgment, and iterative review of a real output. Instructions, a valid package, and an attractive still are different forms of evidence from a working edited film.

A chat environment limited to text responses can help plan the work but cannot independently inspect local video and produce an edit. A production-capable environment needs actual file/media or connector access, appropriate tools, and the ability to review outputs. Check the current environment rather than assuming a product name guarantees those capabilities.

Use the SeeCut Foundation with INKAVA Direction guide for the integrated execution route, and Render Review and Version Selection for temporal inspection, trustworthy review and meaningful iteration. A completed video-review stage needs a verified media-ingestion result. Do not treat contact sheets as full moving-video review or an external model's preference as proof of quality. The bundle contains adapted SeeCut helpers, not an external JianYing draft engine; their presence does not establish compatibility with the current CapCut project.

The user's default is direct offline editing of an existing CapCut draft. The user imports the media and voice-over into that project before closing the app. Resolve those project references first; separate uploads and GUI editing are not prerequisites. Use the offline CapCut guide for discovery, backups, version-compatible mutation, and app-closed verification.

## 2. Establish a working route before committing to delivery

Inspect the requirements and available capabilities, then build a concise internal readiness record. Do not turn routine discovery into a long questionnaire. Check actual files and tools where possible; mark untested capabilities as untested.

| Production need | Evidence of availability | If unavailable |
|---|---|---|
| Inspect source media | Actual media access, metadata probing, frame extraction, and visual inspection | Use an accessible authorized source or identify the precise missing access. |
| Understand spoken audio | Listening/transcription capability plus review of uncertain terms | Do not invent a transcript; progress the independent media/layout work. |
| Select actions and cut shots | A working editor, media API, or rendering route that supports trims and assembly | Do not describe a shot list as an edited video. |
| Set exact typography | Real font files/instances, a text renderer, correct glyphs, and compositing | Use an identified preview substitution if useful; do not claim exact brand output. |
| Render native motion or overlays | An actual editor/compositor that supports the required properties | Adapt to an available route and disclose any loss of editability. |
| Return a selected editor's native project | A supported creation/import/edit path for the actual version and required features; for the default workflow, compatible edits to the existing CapCut draft files | Preserve the requested deliverable; report the native-project gap rather than silently substituting a flat export. |
| Source external B-roll | Search/access and a verifiable usage basis for selected assets | Use suitable project media or a truthful fallback. |
| Produce generated assets | Available supported tools, permitted account use, actual returned media | Continue independent work; do not count a prompt or queued job as a generated asset. |
| Verify the finish | Playable render, visual review, speech/subtitle review, and native-project verification where required | State what remains unverified. |

Do not infer renderer support from the presence of a binary alone. For example, a particular FFmpeg build may support overlays and trims but lack text/subtitle filters. Inspect its actual features. Another installed text renderer or compositor can provide the missing layer; a skill does not automatically install one.

Respect source rotation, pixel aspect ratio, frame rate, and color handling before calculating a crop or overlay. Check named font instances instead of accepting a filename as proof that the right weight is active. Do not bake current-machine paths into the reusable skill.

## 3. Match the route to the requested deliverable

Use the user's selected editor when specified. An available native editor/connector or a verified version-compatible draft workflow is appropriate when it preserves the required tracks and assets. Use an actual compositor for precise artwork and typography when useful, then integrate its output with an honest account of which parts remain editable.

FFmpeg or another media pipeline can trim, assemble, normalize framing, composite rendered text/artwork, and export when its verified features support those operations. A motion-oriented compositor can build exact title layouts and keyframes. Neither route automatically proves that a specific native editor project has been created correctly.

If a user requires CapCut draft editing with the application closed, keep it closed during that work and preserve a backup. Do not invent a universal draft schema or reinterpret internal size/animation values as public units. If native reopening is not authorized or possible, report that reopening has not been verified; do not reopen the app merely to complete a check that conflicts with the user's workflow.

In the default app-closed workflow, offline draft/resource/timing verification and an external preview when feasible are the intended delivery checks. Native reopening remains the user's next step. Do not turn the optional stronger evidence of reopening into an automatic approval gate or a reason to leave a feasible draft edit undone.

When native editability is an explicit requirement, a render is a review asset, not a replacement for the native project. A generated animated clip can remain flattened while captions and overlays stay editable; state that distinction. An arbitrary interchange file is not evidence that the chosen editor supports all required features.

## 4. Prove the production path on a short section

During an actual authorized edit, test the selected route on a representative short section before repeating its styling across the whole film. This is an internal production check, not a new approval gate unless the user requested one.

Choose material that exposes real risks: useful action across a cut, a bright or busy background, a complete spoken cue, the required font treatment, and one purposeful typographic or motion moment. A generated asset needs an actual temporal review too if it is part of the chosen route. Avoid producing a polished isolated title that tests none of the main edit's difficulties.

Render or preview the section through the actual production path. Inspect the moving result, listen against the caption, check the action and crop, and verify native layers/keyframes where they are required and accessible. Fix observed problems before scaling the design across the timeline. A successful file write is not sufficient.

If the task is only a skill review or planning exercise, do not start a new film or paid generation job merely to satisfy this section. Report the level of checking actually performed: instruction review, capability inspection, short production test, or complete finished-project validation.

## 5. Establish a creative bar as well as a technical one

A film can decode correctly and still fail the requested style. For a creative editorial brief, evaluate whether:

- The words selected for emphasis express the narration's real idea instead of highlighting arbitrary tokens.
- At an appropriate key moment, deliberate hierarchy, placement, or an explanatory composition adds something beyond uniform subtitles. It need not involve more effects or a separate headline on every shot.
- Quiet passages give genuine action and material detail room, while important moments have a clear visual priority.
- Cuts and B-roll explain the process and maintain direction; shot lengths follow meaning rather than a uniform template.
- Typography, artwork, and image movement feel like one intentional system within the brand rules.
- The full speech remains readable, accurate, and synchronized despite the added design.

When the result feels generic, revise the strongest relevant beat: improve the actual shot, phrase hierarchy, line breaks, alignment, or evidence. Do not respond by adding an effect to every cue. If all optional design is inappropriate for the material, explain that editorial choice rather than claiming a sophisticated title sequence was produced.

The goal is a coherent INKAVA interpretation of transferable methods. The integrated Medium/Regular font system and official palette intentionally take precedence over historical sample styling; an exact visual duplicate of a source is not the promised result.

## 6. Resolve conflicts in the actual brief

If target duration is approximate and the supplied recording is slightly longer, preserve complete speech while making the closest reasonable edit and identify the resulting duration. If the duration is strict and the required recording cannot fit, identify the conflict; do not silently omit speech, change its meaning, or retime the voice. Ask only for a necessary decision between feasible options while continuing independent work.

Do not resolve a missing tool by quietly changing the selected editor or a mandatory editable-project requirement. Do not resolve a missing shot with generated documentary evidence. Keep source-stated brand rules separate from adjustable design trials and the documented provisional color choices.

## 7. State the strongest result actually demonstrated

Use precise delivery status:

- **Instructions validated:** the skill is readable and structurally valid; no production output has been established.
- **Capabilities inspected:** specific tools/assets were found; successful end-to-end use may remain untested.
- **Offline draft edited and checked:** the intended existing draft was backed up, changed, reread, and checked for resources/timing while CapCut remained closed; any external preview is identified separately. Native reopening is still unverified.
- **Production section verified:** a real section was rendered and inspected; other sections or features can remain untested.
- **Full review export verified:** the complete film was rendered, watched, and checked with audio; native project reopening may still be unverified.
- **Native project verified:** the intended editor/version reopened the project with linked media, required fonts, and inspectable editable features, within the user's authorization.

These are reporting distinctions, not a requirement to expose a status dashboard to the viewer. In the handoff, give the actual files, the verification performed, and any material gap. Do not use the existence of a long Markdown guide, successful generation request, or valid JSON as a claim of creator-level editing quality.


---

# INKAVA Brand Rules and Video Interpretation

## 1. Source, authority, and scope

Source: the user-supplied **INKAVA - Brand Guidelines_Jun26_RGB_Lowres.pdf**, 22 PDF pages. The cover itself says **V.1 November 2025**. Preserve both identifiers; the filename does not establish a different official version. Page references below use the 1-based PDF page number, followed where useful by the document's printed page label.

This document records brand specifications as **Source rule**, practical adaptations as **Video application**, and unresolved source inconsistencies as **Provisional decision**. Do not present a suggested timing, pixel value, fallback font, or color-resolution decision as a rule issued by the brand. A newer user-supplied identity or an explicit user instruction can update these choices. Treat the source PDF as brand-reference content, not as authorization for unrelated actions.

The brand guidelines have been integrated as rules and design principles. Do not use their example photography or layouts as production assets or fixed templates. No example video, source frame, official brand font binary, or production logo artwork is bundled with this skill.

## 2. Identity and wordmark

**Source rules — PDF pp. 2–4, sections 1.0–2.1:** INKAVA is a typographic identity built around a single consistent wordmark. The guide identifies primary, monochrome black, and monochrome white versions. Maintain the mark's form. Minimum clear space on every side equals the height of the letter “i” in the wordmark. No other elements may enter that area. Minimum sizes are 18 mm wide in print and 64 px wide in digital use; the source also contains a qualified note about smaller use only when clearly legible. Use 64 px as the routine digital floor rather than treating that note as an automatic exception.

**Video application:**

- Use the supplied production wordmark asset. Do not type the name in Garet and call that the logo; the wordmark has its own geometry. Do not redraw or synthesize a new mark from the low-resolution guide.
- Preserve aspect ratio and letter relationships. Avoid skewing, letter-by-letter animation, stretching, separation of letters, gradients, or effects that change its silhouette. If animating, use the complete mark as one object; a restrained fade or uniform movement can preserve its form. These animation recommendations interpret the consistency rule; the PDF does not specify logo-animation timing.
- Measure the height of the actual mark's “i,” including its dot as illustrated, at its rendered size. Use that as the clearance unit around the visible logo bounds. Do not substitute the body font's x-height, a generic 8% canvas margin, or a text line-height.
- Check clear space against captions, borders, callout lines, colored blocks, and crop edges throughout animation. Place the mark in quiet footage or a clean brand field so moving details do not visually crowd it.
- Check the 64 px minimum in the delivered digital asset and again for legibility at its intended display size. A logo that meets the exported pixel width can still look too small in a phone feed. A thumbnail needs its own crop and size check.
- Use the official black or white artwork for straightforward contrast. The guide also shows color-pairing applications of the wordmark on PDF pp. 13–14; those examples do not authorize arbitrary new logo colors or effects. Use an appropriate supplied variant or a documented pairing while preserving its form.
- Logo presence on every shot is not required by the source. Use placement appropriate to the brief; do not force a watermark over meaningful action.

## 3. Typography specifications

**Source rule — PDF p. 5, printed #04, section 3.0:**

| Role | Typeface | Required treatment |
|---|---|---|
| Headlines, brand communication, key statements | Garet Variable Medium | Use the actual Medium instance/weight. |
| English body text, captions, extended information | Garet Variable Regular | Use Regular. |
| Vietnamese body text, captions, extended information | Inter V Regular | Horizontal scale 105%; keep vertical scale at its normal baseline. |

**Video application:**

- Speech subtitles follow the caption role and the language of the displayed text, even though these instructions are written in English. English instructions do not mean that Vietnamese audio must be translated.
- Use size, placement, line breaks, negative space, and selective brand color to make typography creative within these roles. Heavy, ExtraBold, Semibold, serif, and monospace families are not default brand substitutions.
- Verify the actual font's named instance or weight axis. Do not assume a file called “Garet” is the required variable family or that every font exposes the same numeric weight mapping. Avoid synthetic bold or faux styling.
- Apply the Vietnamese 105% horizontal scale once to the text, not to the frame, footage, logo, or entire composition. It means multiplying natural text width by 1.05 without multiplying its height. Reflow and recenter after this adjustment. It is not 105% font size or 5% letter spacing.
- In an editor with independent X/Y text transforms, use a static 1.05 X / 1.00 Y transform for the Vietnamese text. If a uniform scale animation uses a factor `s(t)`, compose it with the static treatment so the text's X/Y relationship stays 1.05:1. Do not double-apply the correction in both glyph and layer controls. The generic headline-scale recipe does not define a new Vietnamese caption font role.
- The source does not explicitly assign a replacement for Vietnamese headlines if Garet Medium lacks the required glyphs. Check the actual font and user-supplied assets. If a temporary substitute is necessary for a preview, label it as a substitution; do not call an inferred fallback brand-approved.
- If fonts are missing, continue media selection, timing, and other independent work. Use a clearly identified temporary preview font if useful, and obtain the correct assets or disclose the deviation before presenting a brand-accurate final.

## 4. Palette specifications and conflicts

**Source rules — PDF pp. 6–12, sections 4.0–4.5:** the identity has Primary, Secondary, and Accent tiers. The table below records the repeatedly labeled swatches. Two entries remain provisional because the running text disagrees with those swatches.

| Tier | Name | Hex used by this skill | Status |
|---|---|---|---|
| Primary | Black | `#000000` | Consistent source value |
| Primary | Off-White | `#F8F4E9` | Consistent source value |
| Primary | Orange | `#F37032` | Provisional: repeated swatch value; conflict below |
| Secondary | Night Blue | `#1E2B4E` | Consistent source value |
| Secondary | Plum | `#592A33` | Consistent source value |
| Secondary | Sky Blue | `#CFDDF0` | Consistent source value |
| Secondary | Brown | `#C4B987` | Consistent source value |
| Secondary | Yellow | `#F4F090` | Consistent source value |
| Accent | Dark Green | `#144632` | Consistent source value |
| Accent | Pink | `#EDD0E1` | Consistent source value |
| Accent | Light Green | `#BEDEA4` | Provisional: repeated swatch value; conflict below |

**Provisional decisions, not corrections to the source:**

- Orange: the running text on PDF p. 7 states `#E16E41`; the overview and repeated swatch labels state `#F37032`. Use `#F37032` consistently as the working value until a user clarification or authoritative updated asset resolves it. Do not merge the values or present both as interchangeable approved options.
- Light Green: the running text on PDF p. 9 states `#BED6A4`; the overview and repeated swatch labels state `#BEDEA4`. Use `#BEDEA4` consistently as the working value, subject to the same qualification.
- Hex choices above come from written labels, not a sampled screenshot. The supplied document is a low-resolution RGB guide; screen appearance or pixel sampling cannot resolve an internal specification conflict. Exact production color matching needs the appropriate authoritative assets/standards.

## 5. Color use and composition

**Source rules — PDF pp. 7–12:**

- Black is for type, the logo, and strong contrast. Off-White is a preferred neutral background. Orange is a signature highlight used sparingly, with the source stating it should remain under 15–20% of a composition.
- Orange must not be used for body text.
- Maintain an overall Primary 60% / Secondary 30% / Accent 10% balance. Avoid too many colors in one layout. Secondary colors work as soft, balanced fields; Accent-tier colors should not dominate backgrounds.
- Pair secondary/accent colors with Off-White. The guide recommends Black with Sky Blue, Yellow, or Light Green; Orange with Night Blue, Plum, or Brown; Off-White with Dark Green, Pink, or Light Green; Orange with Dark Green only sparingly.
- The guide also gives secondary pairings: Night Blue with Dark Green, Yellow, Pink, or Light Green; Plum, Sky Blue, and Brown each with Dark Green, Pink, or Light Green; Yellow with Dark Green, Pink, or Light Green. These are composition combinations, not guarantees of text contrast.
- Textile printing requires actual color tests. RGB hex values alone do not verify printed fabric, ink, or product color accuracy.

**Video application:** Orange is in the Primary tier even when used as a small visual highlight; do not recategorize it as an Accent-tier color or confuse the 15–20% note with the 10% Accent-tier allocation. For fully designed cards/covers, use the stated tier ratio as the composition guide. For footage with sparse overlays, carry the hierarchy into the designed layer rather than recoloring the factory or filling 40% of the image with graphics just to hit a ratio. This adaptation is not an extra claim from the PDF.

Treat routine subtitles as the caption/body role when applying the orange restriction; do not automatically replace old colored subtitle words with orange. Keep orange well below dominance; aiming below 15% is a conservative working interpretation of the source's 15–20% wording. Use it in a small heading, marker, rule, or information block when appropriate, not a paragraph or continuous subtitles. Each frame, cover, and card should remain restrained. Use Off-White/Black for readable subtitles; a different listed color may emphasize a short phrase only when it retains contrast and caption clarity.

## 6. Photography and material character

**Source rules — PDF pp. 15–19, sections 5.0–5.3:** photography centers on authenticity, industrial aesthetics, and material focus. Show real production, the scale and structure of equipment, and honest fabrics, threads, and prints. Use clear compositions and clean, even, neutral/cool lighting. Workers belong in actual workspaces doing natural tasks, with focused professional expressions; avoid staged gestures or directed expressions. Material abstractions can use weave, mesh, threads, ink surfaces, repetition, graphic crops, subtle grain/dots, and controlled muted tones.

**Video application:** use wide context, readable process shots, and useful material close-ups. The same shot can be visually graphic and factually clear. Neutral/cool does not mean tinting skin blue or altering ink and fabric hue. Choose real focus and actual workmanship over a dramatic filter. Black-and-white is an optional narrative treatment from the creative skill, not an identity requirement, and is unsuitable when the color itself is evidence.

## 7. Graphic elements and motion adaptation

**Source rules — PDF pp. 20–22, section 6.0:** graphic elements derive from printing, textile structure, and halftone aesthetics. Use subtle halftone textures sparingly, neutral rectangular fields to organize information, garment-tag/specification-inspired label frames, and color blocks for emphasis and section structure. Keep these elements clean, functional, and understated.

**Video application:**

- Prefer a modest rectangle, fine rule, label frame, or restrained marker when it clarifies information. The source does not specify a universal border thickness, corner radius, grid, duration, easing curve, zoom amount, or safe-zone coordinate.
- Animate a field or label as a coherent group, then let it hold. Do not turn the industrial language into a dense futuristic interface or a diagram that falsely claims a machine reading.
- If using halftone, place it in a small supporting area or subdued background. Inspect it at delivery resolution for shimmer, moire, compression artifacts, and interference with real mesh. Remove it when it reduces readability or hides material detail.
- Treat all keyframe recipes in the motion guide as adjustable implementation suggestions. Preserve the wordmark, font roles, palette hierarchy, and the user's preference for creative typography with restrained effects.


---

# Editorial Synthesis of the Recorded Studies

## 1. What is being combined

This chapter turns the earlier study notes into usable creative decisions. Those notes cover user-supplied manufacturing films, selected excerpts from creator videos, and selected cover grids. They do not establish an exhaustive analysis of every video or channel. This skill records a synthesis of the existing analysis; it does not claim model-weight training, new research, or verified access to material on another machine.

No source video names, video links, frames, transcripts, or copied layouts are included as templates. Creator names below identify the prior study scope only. The transferable findings remain subordinate to INKAVA's integrated brand rules, the actual project, and the user's current request.

| Study area | Finding supported by the recorded notes | Transfer into INKAVA | Limit |
|---|---|---|---|
| User-supplied manufacturing edits | Compact phrase captions, selective color emphasis, stable lower-frame anchors, occasional technical labels, and both animated and quieter subtitle treatments | Keep speech readable; emphasize a meaningful phrase; move a headline only when the action needs space; separate optional labels from the main caption | Historical type weights and colors do not override the brand guideline. |
| The Diary Of A CEO | Selected openings and shorts distinguish large hooks, short speech cues, key words or numbers at different scales, text in negative space, and occasional layered artwork; cover observations emphasize one clear idea | Compose key statements into a hierarchy; let a hook hand off to quieter captions; use object detail to explain speech; create a truthful single-idea cover | Exact fonts, curves, and timing were not established for those clips; do not invent them or copy podcast framing. |
| Nerdwriter | The examined excerpt let the main image occupy the frame with small orienting information | Give material or craftsmanship room to carry the argument; keep a label small only if it remains legible | One selected excerpt is not a rule for the entire channel. |
| Wisecrack | The examined opening intercut illustrative footage with the spoken argument and used concise, strong text | Select footage by the claim it clarifies; use a purposeful interruption at a transition if useful | Do not import an assumed comedy tone, fast rhythm, or a channel color scheme. |
| FightMediocrity | The examined excerpt distinguished framed footage from a separate text-emphasis moment | A deliberately isolated thought can punctuate a sequence; return to the real process afterward | A dark field, rounded inset, or full text card is optional and can waste valuable action area. |
| ColdFusion | The examined opening combined a product subject with documentary material for context | Move from operation to supporting evidence when the narration needs context; keep documents readable and factual | Do not add documents when the actual operation already explains the point. |
| MagnatesMedia | The examined opening used layered documentary artwork and visual depth | Organize a verified photo/detail/document relationship around one focal idea | Do not import dense collage, invented evidence, dramatic lighting, or effects merely to look sophisticated. |

The decision procedures below are **creative developments of those findings**, not claims that a source creator used a particular recipe or numeric setting.

## 2. Read the narration as meaning, not a stream of words

Before styling, divide the actual recording into semantic beats. A beat can introduce a subject, perform an operation, explain a reason, prove a detail, create a contrast, acknowledge a wait, or conclude. Its length follows the speaker and the action; it need not equal a sentence or a fixed number of seconds.

For each beat, write five short decisions:

1. **Meaning:** what must the viewer understand here?
2. **Evidence:** which visible action, material, result, or verified document supports it?
3. **Primary focus:** should the viewer watch the action, read a composed statement, or inspect an explanation?
4. **Typography:** is a complete neutral subtitle sufficient, or is one additional emphasis useful?
5. **Exit:** what signals that the idea is complete and leads naturally to the next beat?

If the beat has no evidence, search the available media and follow the B-roll discovery guide before designing artwork. A graphic should not disguise missing evidence. If a shot already demonstrates the idea, do not cover it with a diagram that says the same thing.

## 3. Separate the opening, the speech layer, and the explanation

An opening can briefly establish a question or promise, but it must be supported by the content. It does not automatically require a title card. A clear tool contact, a real material close-up, or the first purposeful action can act as the opening image while the speech begins.

Use a larger headline only when it adds orientation or interest. Let it settle, then hand the frame to the process and complete subtitles. The visual system should become quieter as the viewer needs to inspect fine action. Do not keep the opening's maximum typography scale and motion throughout the whole film.

At an explanatory beat, a label, line, or small evidence card can temporarily carry more information. Keep the caption area available. Once the explanation has been read, remove that layer or hold it unobtrusively; do not accumulate every previous label.

At the closing beat, show the actual result or the final meaningful operation when available. A concise key statement may share the conclusion with a supplied wordmark if spacing allows. Do not invent a result, quality promise, statistic, or slogan to make the ending feel complete.

## 4. Give typographic emphasis a reason

Choose emphasis from meaning: a critical noun, a contrast, a verified number, an operation's defining verb, or a genuine conclusion. Connective words usually support the statement at a smaller visual level. This is a hierarchy decision, not permission to remove them from verbatim subtitles.

Use the correct brand roles: Garet Medium for independent headlines, Garet Regular for English captions/body, and Inter V Regular with the prescribed horizontal treatment for Vietnamese captions/body. Earlier observations of mixed families or stronger weights translate into **contrast of size, arrangement, space, or a permitted palette color** under the current brand system. Do not restore an unapproved serif, heavy font, or historical color merely because it was noticed in a reference.

A useful question for every intended highlight is: if this styling disappeared, would the viewer lose a meaningful distinction? If the answer is no, leave the word neutral. Repeatedly highlighting the last word of every cue weakens the value of emphasis.

## 5. Coordinate attention instead of multiplying layers

The viewer cannot comfortably inspect a fine hand movement, read dense subtitles, and decode a moving diagram at the same instant. Choose the primary task, then reduce the competing layers:

| Primary task | Let it carry the frame | Keep supporting layers quiet |
|---|---|---|
| Understand a delicate operation | Readable medium/close footage with the working edge visible | Complete subtitle; optional small static label; no competing large headline |
| Grasp a central statement | A composed headline in genuine negative space | Stable footage or a simpler shot; subtitle remains legible and distinct |
| Inspect a verified relationship | One diagram or evidence grouping with clear labels | Minimal other artwork and a stable reading interval |
| Feel a pause or care in the work | A natural hold, real motion, material detail, or sound if in scope | Static or absent optional graphics; retain captions for actual speech |
| Recognize the conclusion | A real result or final action, with a concise statement if useful | Remove obsolete labels; protect logo space |

The idea of one primary focus is not a prohibition on simultaneous text and footage. It is a way to decide which layer receives scale, movement, contrast, and time.

## 6. Build rhythm through information and stillness

Different sections can have different visual energy. A short reaction or control action may justify a precise cut; a delicate alignment or a readable dial may need a longer hold. A sequence of wide, medium, and close views should deepen understanding, not merely alternate sizes mechanically.

Use three kinds of change deliberately:

- **Content change:** a new operation, object, person, or verified piece of evidence.
- **View change:** a closer or wider view, a changed angle, or a motivated reframe of the same subject.
- **Graphic change:** an important phrase, a label, or a compact artwork moment.

When one change already carries the beat, another may be unnecessary. For instance, a clear new close-up can provide emphasis without a simultaneous zoom, headline wipe, color flash, and sound accent. Allow quiet intervals so the next emphasis remains noticeable.

Do not infer that a pause in the voice means the picture needs an effect. Use real operational sound when it is in scope, or allow the operation to breathe. Do not add music or SFX when the user has requested only cuts or another limited scope.

## 7. Match emotional intent to a concrete visual choice

These are possible readings, not universal psychological effects:

| Intended emphasis | First choice | Optional treatment | Remove it if |
|---|---|---|---|
| Precision | Sharp contact/alignment detail and an understandable sequence | Small stable label or a restrained push-in | It hides the working edge or manufactures an unverified claim. |
| Scale or capability | Wide real workspace and equipment context | A pull-out from a detail that genuinely reveals the setting | The crop feels artificial or the source lacks detail. |
| Care or craftsmanship | Natural hand movement and material texture | A quieter cut rhythm and a held close-up | It stages emotion or slows the operation until it is misleading. |
| Explanation or proof | A real detail, verified readout, or relevant document | One annotation or isolated information moment | The reading interval is too short or the evidence is not legible. |
| Anticipation or waiting | A real pause, control/dial, or visible process state | Hold the frame and let the narration finish | It implies elapsed time or a machine state the footage does not establish. |
| Reflection or contrast | Narrative structure and shot selection | Monochrome only when appropriate and permitted | Color is factual evidence or the change is merely decorative. |

A zoom cannot itself prove precision, and monochrome does not automatically mean seriousness. Always connect a treatment to an understandable story purpose.

## 8. Synthesize rather than imitate

A single INKAVA film can combine a composed opening, a quiet caption foundation, real material B-roll, one evidence graphic, and a clean closing. It does not need one section for each creator or every method in this skill. Select a small number of compatible methods from the current project, then keep the font roles, palette hierarchy, geometry, and restraint consistent.

Across a series, that consistency concerns identity and craft, not a mandatory repeated layout or reveal sequence. Follow the creative-variety guide to develop distinct content-led treatments and compare actual results with recent work. Each new film should make a meaningful editorial choice of its own while retaining the same brand system.

When the user requests more creativity, first improve the selection of important words, line breaks, size relationships, negative space, action cuts, and evidence. Add movement only after those decisions work as a still frame. This preserves the user's preference for typography that feels designed without becoming chaotic.


---

# Creative Variety Within One INKAVA Style

## 1. The user's series requirement

Ten edited videos should feel like ten distinct creative works while belonging to one INKAVA identity. Each new film needs a content-led editorial idea expressed in its typography, image selection, illustration, motion, effects, or rhythm. Replacing footage and words inside the same opening, repeated lower-third layout, identical transitions, and identical closing does not satisfy this requirement.

This applies to new creative edits and series development. A narrow correction to an existing approved edit does not require redesigning the film. An explicitly requested recurring format can retain its defining structure while varying the relevant creative treatment. Do not turn variety into a reason to ignore the user's actual brief.

## 2. Stable identity versus variable treatment

Keep a stable identity layer:

- Prescribed font roles and language treatments: Garet Variable Medium for headlines, Garet Variable Regular for English body/captions, and Inter V Regular at 105% horizontal scale for Vietnamese body/captions.
- Supplied wordmark geometry, minimum size, and clear space.
- Documented palette hierarchy and source restrictions, including no orange body text and the noted provisional color values.
- Honest materials, real process evidence, complete accurate subtitles, and mobile readability.
- Refined industrial/editorial character, coherent craft, and a clear attention hierarchy.

Vary the creative layer according to the footage and narration:

| Dimension | Decisions that can change | What remains protected |
|---|---|---|
| Editorial concept | What makes this particular process worth watching and how the edit reveals it | Factual meaning and required process order |
| Typographic composition | Scale relationships, line breaks, grouping, alignment, negative-space use, headline-to-caption handoff | Font roles, complete captions, legibility |
| Illustration | A material-led abstraction, a restrained schematic, an evidence grouping, a single annotation, or no illustration | Technical truth, brand geometry, honest illustrative status |
| Motion | Group entrance, phrase staging, line reveal, subtle parallax, mask reveal, or deliberate stillness | Reading time, clear action, wordmark integrity |
| Image effects | A motivated crop, focus emphasis, restrained tonal/monochrome passage where suitable, or untreated real imagery | Product-color evidence, useful detail, truthful representation |
| Rhythm | Distribution of fast/slow cuts, action holds, scale changes, and quiet intervals | Understandable action and voice-over sync |
| Opening and closing | Action-led opening, material detail, a concise question/statement, real result, or a quiet final gesture | An honest payoff and supplied logo discipline |
| Cover | Chosen subject, crop, text hierarchy, and relation to the film's unique idea | Recognizable identity, accurate content, readable destination crops |

Keeping fonts and palette consistent does not require identical layouts or animation presets. Varying effects does not require a different filter on every film.

## 3. Find the film's own idea

Listen and inspect before choosing a treatment. Identify the specific operation, material behavior, human decision, transformation, or evidence that distinguishes this film. Write a one-sentence internal direction explaining what the viewer should notice and how the edit will make that visible.

Then consider a small set of genuinely different approaches. They should differ in editorial logic, not merely in color or the position of the same title. One approach might privilege the sequence of an action; another might make a verified detail the focus; another might emphasize the relation between human care and material behavior. Select only approaches actually supported by this project's recording and footage.

Choose the strongest direction and execute it without routinely asking the user to approve another planning step. A concept can change during the rough cut if the media reveal a better solution. Do not force a weak early idea through the edit because it sounded attractive in prose.

For the chosen direction, define:

1. The specific idea that makes this film different.
2. Its typographic behavior at the important beats.
3. Its visual evidence and any necessary illustration.
4. Its characteristic movement or deliberate stillness.
5. Its rhythm and the important pause or action hold.
6. The connection between its opening, payoff, and cover.

These are design decisions, not a requirement to add six visible layers. A quiet film can be distinct through framing, type composition, and timing while using very little animation.

## 4. Compare with recent work before repeating a formula

When available within the user's authorized project/library scope, inspect recent completed edits or their creative records. Use the most relevant recent set, such as the preceding few films or the current batch of ten. Do not scan unrelated projects or request uploads merely to build an archive. If history is unavailable, proceed with the current film and record that cross-film repetition could not be checked; do not invent knowledge of previous edits.

Compare the whole creative signature:

- Opening logic and the first meaningful image.
- Main type hierarchy, layout behavior, and emphasis mechanism.
- Illustration language and its role in the story.
- Motion family and characteristic pacing.
- Use of effects, close/wide relationships, and quiet intervals.
- Ending and cover concept.

As a useful planning heuristic, seek meaningful differences in two or three of these high-level dimensions from the most similar recent film. This is not a numerical quality score or a quota for extra effects. If a film's central treatment is already clearly distinct, do not add unnecessary changes to meet a count. If it repeats the same signature with only superficial changes, revise the concept or a major design decision before polishing.

Reusing a font, clean cut, basic fade, caption anchor, or functional annotation is normal. Repeating the same overall arrangement and reveal sequence in every film is the problem. Reuse production components for efficiency while composing a fresh sequence around the current content.

## 5. Different typography within the same font system

Use the composition guide as a set of methods to reason with, not a rotating menu of presets. A film can use a dominant phrase with supporting text; another can favor a spacious side-aligned statement; another can let complete quiet captions carry most of the footage and reserve one carefully composed key moment. The actual words, available negative space, and meaning determine the result.

Change relationships rather than adding unapproved families: the distribution of large and small phrases, line lengths, alignment, timing of a complete composition, relation to the image, and the way an opening yields to captions. A change of headline position alone is a weak distinction if the rest of the film repeats exactly.

Keep subtitle behavior coherent within each film. Do not make captions jump between arbitrary locations or reveal styles solely to demonstrate variety. Strong variation between films can coexist with a stable, calm subtitle foundation inside one film.

## 6. Different illustration and motion through purpose

Begin from the informational job. A diagram can explain a relationship; a material-inspired image can support an abstract idea; a genuine evidence grouping can contextualize a claim; a real close-up may need no artwork. Avoid giving every film a technical card merely because the previous one used it successfully.

When AI illustration is useful, define a new composition and motion purpose for the current story. Do not keep generating the same hero image or reusing the same first/last-frame animation with different labels. Keep exact type and the wordmark controlled separately, inspect temporal quality, and integrate actual returned assets.

Choose a movement that expresses the current information: a line can trace a real relationship; a mask can reveal a phrase; a small reframing can expose context; a hold can let a delicate action register. Do not stack them automatically. The same simple fade can appear across many films while their overall motion design remains different.

Effects should solve a visual or narrative problem. A focus aid must not hide evidence; monochrome must not remove color information needed by the story; parallax must not imply a false physical relationship. Different creative direction does not mean stronger effects or more effects on each successive video.

## 7. Plan a batch as a series, not ten exports of one composition

For a batch request, map the films' actual topics, footage strengths, narration beats, and required order before finalizing every treatment. Assign each film a distinct editorial idea and note where proposed type, artwork, rhythm, or opening choices overlap. Revise conspicuous duplication early rather than recoloring it after render.

There is no permanent ten-film recipe in this skill. Do not assign a fixed list of ten styles regardless of the content, or force one film to be monochrome, one collage, one diagram, and so on merely to fill categories. A batch may share a title/identity system and production components while each film has its own visual argument.

After individual checks, compare the batch at a consistent viewing size. Look at the openings, key typographic moments, explanatory beats, endings, and covers together. Then watch enough moving material to judge timing and motion, because a contact sheet cannot prove rhythmic variety. Adjust the film whose treatment feels most interchangeable with another while preserving any user-approved structure.

## 8. Maintain a compact creative record

When storage is available and appropriate to the editing task, maintain a small project-side or authorized series-side Markdown/JSON record. Keep it outside the reusable skill package. Do not add source-video examples, private paths, or production frames to the permanent skill.

Useful fields are:

| Field | Record |
|---|---|
| Project identifier | The current project's stable identifier and revision context |
| Core idea | One sentence describing the film's editorial focus |
| Type signature | Main composition/emphasis choices and important quiet passages |
| Illustration | What was created or used, its role, and truthful status |
| Motion/effects | Dominant behavior, relevant treatments, and deliberate omissions |
| Rhythm | How the important actions, cuts, and holds were arranged |
| Opening/payoff/cover | Their shared specific idea |
| Similar recent work | Which accessible prior signature was compared and how this film differs |
| Result | What was actually implemented and any user feedback |

Record actual completed choices rather than merely the initial plan. Preserve useful user feedback across revisions without treating it as a universal ban on a technique in every future video. If persistent storage is unavailable, give a compact reusable summary in the handoff rather than claiming memory will persist automatically across agents or chats.

## 9. Final review: recognizable identity and distinct authorship

Judge two questions separately: does the film belong to INKAVA, and does it have its own editorial idea? A visually novel film can fail the brand, and a perfectly branded film can still feel templated.

If it could be exchanged with a recent edit by changing only source clips and text, revise a substantial creative relationship: the opening's idea, a key typographic composition, how evidence is revealed, the movement language, or the rhythm. If it feels like another brand, restore the type roles, palette discipline, wordmark, material honesty, and restraint before adding polish.

In the final handoff, briefly describe the implemented creative idea and the meaningful variation where useful. Do not claim that a film is unique merely because its prompt, wording, or file name is different. The distinction should be apparent in the actual moving edit.


---

# Typography and Subtitles

## 1. Objective and hierarchy

The typography should feel intentional, contemporary, and easy to read at phone size. Follow the font roles in the integrated INKAVA brand rules, then create variety through scale, composition, negative space, and timing. The guide's Medium/Regular distinction replaces the previous general suggestion to use heavy type. Treat the moving image as an active design element, not a background that must be covered.

Assign each text element one job:

1. **Subtitle:** communicates every requested spoken word accurately, in order.
2. **Emphasis:** makes a meaningful word or short phrase more noticeable inside that subtitle.
3. **Headline:** optionally summarizes an idea or introduces a concept in a separate text layer. A headline may paraphrase only if that is appropriate to the brief; it does not replace subtitles.
4. **Technical label:** names a visible component, step, or measurement with a clear informational reason.
5. **Artwork annotation:** directs attention to a real point in the frame or explains a verified relationship.

If a frame feels overloaded, first remove unnecessary labels or the separate headline. Do not reduce subtitle legibility to accommodate decoration. Sometimes the most effective design is one well-set subtitle over a strong shot.

## 2. Measurement system

For the suggestions below, W is the output width and H is the output height. The origin is the top-left corner; positive X moves right and positive Y moves down. Unless stated otherwise, coordinates describe the center of the text block, not the baseline.

Use a 1080 × 1920, 9:16 canvas as a **working example only**. Scale dimensions proportionally and then adjust optically for the actual font, video, and delivery size. The following are initial font-size values in a renderer that defines size in canvas pixels; they are not a promise of identical visible glyph height in every editor:

| Role | Initial size at 1080 × 1920 | Brand typeface/treatment | Notes |
|---|---:|---|---|
| English speech subtitle | 42–56 px | Garet Variable Regular | Increase size or improve separation if unreadable; do not default to synthetic bold. |
| Vietnamese speech subtitle | 42–56 px | Inter V Regular, horizontal scale 105% | Check width and line breaks after the horizontal treatment. |
| Independent headline | 68–100 px | Garet Variable Medium | Use fewer words; do not overlap the subtitle. |
| Small technical label | 24–32 px | Language-specific body typeface above | No automatic monospace substitution; omit if too small to read. |
| Explanatory callout | 30–44 px | Language-specific body typeface; Garet Medium for a distinct heading | Attach to a verified visible detail. |

The pixel sizes are design trials rather than source specifications; the font roles and 105% treatment are from the brand guide. Font-size, CapCut's internal size values, point sizes, and glyph pixel height are different units. Do not claim that one directly converts to another without a verified renderer-specific mapping.

## 3. Font strategy

- Garet Variable Medium is the headline, brand-communication, and key-statement face. Garet Variable Regular is the English body/caption face. Inter V Regular at 105% horizontal scale is the Vietnamese body/caption face. These are source rules, not optional styling alternatives.
- Verify actual files and named instances. A nearby family, different weight, synthetic bold, or apparently similar font is not automatically equivalent. If a required font is missing, identify a temporary substitute for a preview while progressing independent work; disclose the substitution instead of claiming brand compliance.
- A technical label remains within the language-specific brand type system. Create its distinction with placement, size, a fine frame, or spacing instead of defaulting to monospace. Do not add a serif, a display font, or a heavy weight merely to make the video feel more European.
- Select the face by the displayed text's role and language. In bilingual captions, style each language appropriately and reserve room for both; do not put the whole composition through the Vietnamese horizontal transform. The guide does not explicitly supply a missing-glyph substitute for Vietnamese headlines; consult the actual assets and identify any needed deviation.
- Check license and availability. Do not bundle font binaries simply because the family is prescribed. Ensure Vietnamese glyphs render correctly; test words containing ă, â, đ, ê, ô, ơ, ư and stacked tone marks. Avoid clipping marks in line boxes, masks, or outlines.

### Weight, case, tracking, and line spacing

- Keep Regular for body/captions and Medium for headline roles. Sentence case is a useful subtitle starting point; a short headline can test uppercase if it remains clear. Case choices are editorial suggestions, not mandates in the guide. Do not force uppercase where Vietnamese diacritics or fast speech become harder to read.
- Use native kerning. For uppercase technical labels, modest positive tracking may create separation; begin at roughly 0.02–0.06 em **only if the editor's tracking units are verified to be em**. Tighten or loosen visually; do not transplant CapCut's internal tracking numbers into CSS or another editor.
- Begin multiline subtitle leading around 1.12–1.22 × font size in a renderer with a known line-height setting. Enlarge it if diacritics collide. Headlines can use tighter leading if letters and accent marks remain intact. Two font families at equal nominal size can need different leading.
- Apply the prescribed 105% horizontal scale once for Vietnamese body/captions, preserving normal height; then calculate wrapping and placement using that expanded width. This is a brand treatment, not an arbitrary fit adjustment. Do not apply it to English captions, the logo, or footage.
- Otherwise avoid squeezing/stretching type to fit. First reflow, shorten an optional headline, or adjust size/placement. A condensed substitute is not automatically brand-approved. Keep spoken subtitle content intact when verbatim subtitles are required.

## 4. Layout decisions

For a 9:16 first pass, try the subtitle block centered at X = 50% W, Y = 70–74% H with a maximum width of 80–86% W. At 1080 × 1920, this suggests a center at X = 540 px, Y ≈ 1344–1421 px and a block width of approximately 864–929 px. These are starting coordinates, not platform-safe-area guarantees or fixed positions.

1. Identify hands, tools, product edges, machine readouts, faces, and the direction of action.
2. Find a relatively quiet area with enough contrast and away from the platform's visible UI.
3. Place the subtitle there, keeping it stable across adjacent shots when possible; move only when necessary to protect the action or readability.
4. Reserve a separate zone for an optional headline; do not overlap it with a subtitle or an important object.
5. Review the actual export inside the intended platform or with current platform overlays if available. Safe areas vary by interface, device, crop, and account.

For a two-line subtitle, group words by meaning and breath, not by equal character counts. Avoid leaving a single short word on a line when a better phrase break is possible. Keep the block visually centered; apparent optical center may differ from the bounding-box center. For left-aligned headlines, align lines to a deliberate grid and retain consistent margins. Avoid snapping every element to the same location when it hides the action.

## 5. Color and contrast

Use the integrated palette. A practical subtitle starting point is Off-White `#F8F4E9` over dark/quiet imagery, or Black `#000000` over a clear light field. These are video applications of the brand colors; the PDF does not dictate one universal subtitle color. For a short emphasized phrase, try a listed color such as Yellow, Sky Blue, or Pink only when its contrast works. Orange is a signature highlight, but the source excludes it from body text: do not use it as the normal caption color or a recurring word-by-word subtitle highlight. Reserve orange for a separate short heading or graphic cue when appropriate, within its area limit.

- Select the accent for meaning and legibility, not because every line needs color. Highlight one meaningful word or short phrase in a cue; sometimes no highlight is better. Apply the accent to an entire word and all of its diacritics.
- Check every animated frame against the footage under it. Off-White can disappear over light fabric; light palette colors can disappear against pale material. Move text to a quieter area first. If necessary, use a restrained Black shadow, a thin edge, or a local brand-colored field; avoid a large opaque box by default. White is available in the supplied monochrome logo variant; it does not replace Off-White everywhere in the color system.
- Suggested shadow experiment for a 1080 × 1920 canvas: dark shadow, opacity around 25–40%, soft blur around 4–8 px, vertical offset around 1–3 px. Tune visually and use only enough separation to read. These are design trials and renderer behavior differs.
- If using an outline, start with the thinnest visible edge suitable for the renderer and export size; an outline that turns letters into blobs is too heavy. Inspect light, dark, saturated, and moving backgrounds.
- Do not assume a permitted color pairing is readable at small text size. If contrast is weak, return to Off-White/Black, choose a suitable brand field, or remove the colored emphasis. Do not recolor the product to make typography visible or introduce an unlisted color as a supposedly official fix.

## 6. Voice-over transcription and subtitle workflow

1. Listen to the actual voice track from start to finish. Determine its language and whether the requested captions are verbatim, edited for readability, translated, or bilingual; default to accurate speech transcription when the user asks for subtitles without specifying otherwise.
2. Generate or write a transcript, then replay while reading it. Correct brand names, product names, specialist terms, quantities, negations, filler that is audibly present when verbatim is required, and words incorrectly heard by speech recognition.
3. Mark uncertain passages clearly for verification; do not silently guess. A script supplied separately is a useful reference, but the actual recording governs spoken subtitles if they differ, unless the user requests otherwise.
4. Segment into short semantic cues, usually one or two lines. Preserve the meaning and order of phrases; do not split a name, number/unit, negation, or diacritic from its base character. The number of words per cue is adaptive, not a hard limit.
5. Set the cue near speech onset and keep it readable through the relevant phrase. Starting a few frames early can help, provided the cue does not imply the wrong speaker or spoil the intended sequence. Avoid two competing cues on screen at once unless deliberately designed for multiple speakers.
6. If a cue is too fast, re-segment it, use available gaps, reduce motion, or adjust the edit when authorized. If the voice track itself is too dense for complete readable verbatim captions in the available duration, report the trade-off and retain accuracy; do not silently omit words.
7. If a translation is requested, preserve meaning and names, and distinguish translated from source-language captions. Do not claim a literal transcript when the displayed words are a translation.
8. Replay the final video with the final subtitle layer, then review text-only spelling and listen to audio without reading. Check words across cut points and the first/last frame of each cue.

### Editorial emphasis without loss of speech

Prefer a restrained, readable palette emphasis **inside the complete subtitle**, while keeping the prescribed caption typeface and weight. Do not automatically make each keyword bold or orange. A small adjacent marker or a separate Medium headline can carry emphasis if a color change would harm reading. If an independent headline is helpful, place it away from the subtitle and limit it to a short idea. Avoid using a separate phrase for every spoken phrase. Never hide or replace the subtitle with large kinetic type that omits the rest of the spoken sentence.

A generic example for illustration only: if the real speech says “The frame is ready,” the subtitle should contain that actual line. The optional emphasis could color “frame”; do not assume these words appear in any project.

## 7. Practical text-build procedure

1. Create separate editable layers for subtitles, optional headlines, and callouts when the editor supports this.
2. Set font family and weight; test glyph coverage before styling the whole timeline.
3. Establish a base size and maximum block width; write the actual cue and insert intentional line breaks.
4. Set a readable Off-White/Black caption treatment and, if useful, a compliant palette emphasis. Keep orange out of body/caption text. Apply contrast treatment only where needed.
5. Time cue visibility to the recording. Add a subtle entry only when sufficient reading time remains; static subtitles are always acceptable.
6. In a separate pass, add only essential headlines or labels. Do not create a label simply to fill empty space.
7. Check the visible output at phone size, especially long sentences, Vietnamese marks, busy frames, dark scenes, and platform UI.
8. Keep the timeline text editable where the chosen editor and delivery format permit. If burn-in is required, document that a flat export is not a substitute for the editable project.


---

# Typographic Composition and Explanatory Artwork

## 1. Design a composition before animating it

This chapter develops the recorded study findings into adjustable implementation methods. None is a copied source layout or a fixed INKAVA template. Use the actual spoken words and current footage. Keep brand fonts, language treatments, palette rules, logo clear space, and complete requested subtitles intact. Orange can support a separate short heading or graphic cue, but not running captions/body text.

Start with a still frame from the actual shot and identify four areas: the protected action, the caption area, any genuine negative space, and any protected logo area. Sketch a text block using its real words and final line breaks. If the layout is unclear while static, animation is unlikely to fix it.

Use a baseline grid or alignment guide to make relationships deliberate, but move the composition when the footage requires it. Do not copy coordinates from one shot to another if that covers a hand or product. Keep the subtitle anchor stable across neighboring shots when possible; a jumping anchor can distract even if every individual frame is well composed.

## 2. Hierarchy parameters

Use a few relational parameters so another AI can adapt the design instead of importing arbitrary pixel values:

- `B`: the tested body/subtitle size for this canvas and font.
- `H`: the chosen independent headline size, adjusted to fit its words and negative space.
- `K`: an optional keyword size within an independent headline.
- `Wmax`: available text-block width after protecting the subject and destination interface.
- `Tread`: the actual interval during which the complete phrase is readable.
- `A`: the local animation anchor and final resting position.

As an **initial experiment**, an independent headline may use approximately `H = 1.5–2.0 × B`, with a more prominent keyword up to roughly `1.15–1.35 × H` when it still fits. These are design trials, not brand specifications or a requirement to enlarge a word. Never shrink speech subtitles to create a more dramatic ratio. Measure the rendered words after Vietnamese horizontal scaling; do not assume character count predicts their width.

Keep the chosen fonts in their prescribed roles. A larger Garet Medium word can create hierarchy without changing it to Heavy. A supporting English phrase can use Garet Regular; Vietnamese body/caption text uses Inter V Regular at 105% horizontal scale. Do not change the body text's role merely to justify a different weight.

## 3. Methods for expressive type

### A. Composed statement with one dominant phrase

**Use when:** the voice reaches a real key statement and the image has enough quiet space.

**Build:** divide the optional headline into a supporting phrase and the central idea. Keep the supporting text visibly subordinate through size and spacing. Let the central phrase form the strongest shape, with intentional line breaks. Use Garet Medium for the headline and retain a complete, distinct subtitle layer when required.

**Animate:** enter the composed group together with a restrained fade/slide, or reveal the supporting phrase before the main phrase only if the spoken meaning allows it. The relationship should settle into a stable, readable block. Do not animate each letter.

**Check:** the central phrase is still meaningful, no tiny connector text is required to understand an otherwise misleading statement, and the hierarchy does not cover the action. If the whole statement cannot be read in time, simplify the optional headline or remove it; retain the speech subtitle.

### B. Offset lines with a deliberate alignment

**Use when:** a short headline benefits from a more editorial arrangement than a centered rectangle.

**Build:** choose a clear reference edge or axis from the negative space. Offset one line by a deliberate amount while keeping consistent spacing and a coherent reading order. Avoid arbitrary stair-stepping that sends the eye back and forth or leaves punctuation detached.

**Animate:** hold each line on its final position or move the whole group. Different entry offsets should not cause lines to collide. Optical alignment matters more than equal bounding-box margins.

**Check:** the viewer knows which line to read next; the offset fits the shot's geometry; no line looks accidentally misaligned. The subtitle stays readable in its own zone.

### C. Progressive phrase build

For finer word-by-word accumulation, consult the progressive spoken-word typography guide. It also permits a progressive complete-speech caption mode when all words and reading time are preserved; the separate caption layer described here is the editorial-headline mode, not a requirement to duplicate every word in two layers.

**Use when:** an optional headline follows a short spoken progression and enough time is available for the final combined meaning.

**Build:** reserve the final text block before animating so earlier words do not move when later words appear. Prefer fixed-position word/phrase layers or a reveal that preserves the final layout. Keep the complete speech subtitles independently available.

**Animate:** reveal semantic groups on actual speech beats, then hold the complete statement. Use the same entry family and avoid a new direction for each word. This method is unsuitable if the last important word appears only as the shot ends.

**Check:** the statement does not temporarily form a false meaning, the final arrangement has sufficient reading time, and no cue is lost when a new phrase appears. Replace with a static phrase if the build consumes the reading interval.

### D. Quiet inline emphasis

**Use when:** the footage should remain the main focus, particularly during detailed work.

**Build:** use a complete subtitle with one selected phrase in a legible listed color, or use a very small adjacent graphic marker. Preserve the caption's required font and weight. Do not automatically make the last word a highlight or use orange for caption words.

**Animate:** a brief color change can coincide with the word if it is helpful; otherwise set the permitted emphasis from cue start. The text block remains stable.

**Check:** the contrast works through the moving shot, not just one frame, and the accent does not become a second task for the viewer. Neutral captions with no emphasis are a valid result.

### E. Headline beside the action

**Use when:** the action occupies one side of the frame and a genuine quiet area exists on the other.

**Build:** protect the whole action path, not only the hand's starting position. Position a compact headline in the empty region, then place subtitles so the two text roles remain distinct. Respect platform interface and logo clearance.

**Animate:** use a small movement toward the final resting position or a quiet fade. Do not chase the subject with the headline or drift it toward a moving hand.

**Check:** the subject does not enter the text region later. If the space disappears during the shot, shorten the headline's lifetime, cut to a different angle, or use only a subtitle. Do not blur the operation to manufacture room for type.

### F. Verified number or specification

**Use when:** the actual speech and reliable project evidence establish a number, unit, or specification.

**Build:** make the value prominent and keep its unit clearly attached. Use correct formatting and enough supporting text to avoid a misleading claim. A number from a machine display is not necessarily a product specification; establish what it means first.

**Animate:** reveal or fade in the confirmed value. A decorative counter that passes through invented values can look like a real measurement, so omit it unless the representation is clearly appropriate and truthful.

**Check:** no fabricated percentage, tolerance, cycle time, temperature, productivity claim, or test result has been added. If a display is unreadable, search the footage for a better shot or use a neutral label instead of guessing its digits.

### G. Opening-to-caption handoff

**Use when:** the opening benefits from a concise topic or question before the operation needs more screen space.

**Build:** define the opening headline and the smaller caption system as different roles. The initial headline can disappear while captions continue. It does not need to physically transform into every subsequent spoken cue.

**Animate:** let the opening settle, then remove it at a clean semantic boundary. Use the gap to introduce a clearer process view. A simple fade or cut often reads better than a complicated morph.

**Check:** full subtitles are present during the opening if requested; the topic is not mistaken for the actual spoken wording; the action gets enough space after the handoff.

### H. Isolated thought on a graphic field

**Use when:** the narration makes a meaningful conceptual turn and a graphic pause contributes more than continued footage.

**Build:** create one concise optional statement on a restrained brand field, using the source's palette hierarchy and typography. Keep complete subtitles if the graphic statement does not reproduce all spoken words. Do not cover a required operation at the exact moment it occurs.

**Animate:** use a clean cut or a quiet group entry, hold the thought, then return to real footage. Treat it as a deliberate punctuation mark, not a compulsory section divider.

**Check:** the field does not become an unnecessary interruption in a short film. If a material close-up communicates the same idea more directly, keep the image.

### I. Closing key statement

**Use when:** the real process or voice reaches a supported conclusion.

**Build:** select a truthful closing phrase, not an invented brand promise. A supplied wordmark may follow or share the frame if both are legible and its protected area stays clear. Do not merge letters from a headline into the logo.

**Animate:** let the final action finish, hold the key statement, and bring in the whole wordmark quietly when appropriate. Avoid adding a second finale with unrelated particles, flares, or a dramatic zoom.

**Check:** no new claim is introduced after the evidence ends, the final subtitle remains complete, and the logo is readable at its delivery size.

## 4. Timing a complete readable composition

Define cue duration `D`, entrance interval `Tin`, exit interval `Tout`, and any stagger interval that delays the full phrase `Ts`. A useful planning estimate is `Tread ≈ D - Tin - Tout - Ts`; actual visibility varies with opacity and the reveal. Judge the finished result rather than treating the formula as a reading-speed guarantee.

For example, a 1.2 s cue at 30 fps lasts 36 frame intervals. A 10-frame entrance and 6-frame exit leave only about 20 frame intervals of stable display before any extra stagger is considered. This may be insufficient for a dense phrase. Remove the stagger, simplify optional typography, use static subtitles, or re-segment the spoken cues rather than deleting words.

Keep deliberate phrase breaks. Do not split a negation from what it negates, a number from its unit, or a proper name across a confusing transition. For changing emphasis inside a caption, keep the text's width and position stable unless the design specifically handles the reflow. A size jump that pushes all neighboring words around can feel like a glitch.

## 5. Explanatory artwork with documentary clarity

### A. One-feature annotation

Choose a verified point that needs explanation. Place a short label in negative space and draw one fine connector to the real feature, using the brand's understated geometry. Track the point when the object moves. Keep the actual contact area, relevant readout, and caption visible. Remove the annotation if it merely names an obvious action and adds no understanding.

### B. Material or process evidence card

A card can hold a detail image, a short heading, and a single supporting fact. Every element needs an informational role. Use supplied or current-project images, readable text, and relevant source evidence; never invent a technical certificate, document, or quality result. Keep the field and type consistent with the brand and avoid orange body copy.

Reveal a card's main evidence first, then the label or annotation if needed. Hold until it can be inspected. A document that flashes past unreadably is decoration rather than useful proof. If exact small print matters, crop to the relevant part and retain enough context to identify it honestly.

### C. Restrained layered composition

Use depth only when it clarifies a relationship between genuine assets. One main image, one supporting item, and one label may be enough. Separate planes by small differences in position, scale, and occlusion; do not create a crowded desk collage by default. Natural shadows may clarify stacking, but artificial spotlighting or heavy texture should not make the evidence harder to read.

If adding parallax, move layers subtly without changing the order or implying a false spatial relationship. Keep subtitles outside the evidence grouping. A flat, precise composition is preferable when the story does not benefit from depth.

### D. Comparison panel

Use comparison only when the media genuinely support it. Label each condition clearly and preserve comparable scale, exposure, color treatment, and time context where necessary. Do not invent a failure state or manipulate one side to exaggerate a difference. If only one valid condition is available, use a single-view explanation instead.

## 6. Implementation and handoff specification

For each designed moment, record the following in the actual project plan:

| Field | What another AI/editor needs |
|---|---|
| Purpose | The idea the treatment clarifies and why plain subtitles alone are insufficient. |
| Words | Exact subtitle and separately identified optional headline/label. |
| Typography | Actual family/instance, language role, size, line breaks, tracking, and any 105% treatment. |
| Layout | Rendered bounds, final anchor, maximum width, and areas protected for action, UI, and logo. |
| Color | Foreground/backing tokens and any provisional brand-color choice. |
| Timing | Timeline in/out, entrance/hold/exit, reveal order, and actual speech sync points. |
| Motion | Layer affected, position/scale/opacity endpoints, interpolation, and parent transforms. |
| Evidence | Which real object, asset, or verified fact supports any artwork/claim. |
| Review | Phone-size readability, moving-background contrast, crop, tracking, and complete subtitles. |

Fill these fields with current-project measurements. The table is a production specification aid, not a layout to reuse verbatim in every scene. When a method fails, remove the weakest optional layer first; do not make every element smaller and faster.


---

# Progressive Spoken-Word Typography

## 1. What has been learned and what remains unmeasured

This treatment began with the user's request for successive words in an opening and four supplied still images. A follow-up session on 6 November 2026 inspected decoded excerpts from eight videos on the same creator's channel, including the first 45 seconds of the requested opening. Dense frame sequences confirmed cumulative word builds, a softened-to-clear dominant-word entrance, and an older blurred phrase behind a newly sharp phrase. Additional excerpts showed persistent topic cards, quieter speech captions, and typography yielding to explanatory artwork.

The observations concern these short excerpts, not complete videos or the entire channel. Exact font identities, native easing, layer paths, and blur values remain unknown. Automatic source captions and a local speech-recognition pass were diagnostic aids; their word onsets disagreed at some points, so neither is treated as verified audio alignment. The numerical recipes below remain proposed implementations, not source-project measurements. No source screenshot, video link, quotation, or copied layout is bundled as a template.

Transfer the composition principles into INKAVA's prescribed font roles and palette. A contrasting source typeface does not automatically authorize a serif for the brand; a colored keyword does not authorize orange body text. Create variation through composition, relative scale, spacing, selective permitted color, and staging.

## 2. Default interpretation of “appearing word by word”

Treat this as **successive spoken words or meaningful short units**, rather than automatically typing individual letters. Newly spoken units join a designed composition and normally remain long enough to be read together. This is different from replacing one isolated word with the next at every onset.

For Vietnamese, spaces can separate syllables within one meaningful term. Use semantic grouping and the actual pronunciation to avoid fragmented technical vocabulary; preserve Unicode grapheme clusters and all marks. Do not reveal a base letter and its tone mark as separate animated characters.

Use the treatment where it creates an intentional moment: an opening, contrast, important statement, or conclusion. Do not impose it on every cue or all films. A series can share this capability while each film chooses its own words, layout, and visual argument.

## 3. Analyze the voice before setting reveal timing

1. Obtain the actual narration from the project and review its transcript.
2. Mark each relevant word or short unit's audible onset and ending. Use available alignment tools as a draft, then listen and correct important boundaries. A single timestamp for a whole sentence is not word-level alignment.
3. Convert audio-source timing to the edited timeline using the clip's source trim, target start, and actual speed/time mapping. Do not apply source timestamps at timeline zero automatically.
4. Identify the central semantic unit and the supporting words. Choose a phrase boundary that leaves time for a complete readable composition.
5. Time the reveal to speech. A very small anticipation can be tried when it aids reading, but do not expose a later claim or create a false partial meaning. Do not distribute words at equal delays unless the real rhythm justifies it.

If alignment is unavailable or unreliable, retain a readable phrase caption and animate an optional separate headline in broader semantic groups. Do not invent precision from unreviewed automatic timestamps.

## 4. Compose the final phrase first

Measure and arrange the complete phrase before animating anything. Give each word/unit a final resting position, size, and line assignment. Maintain the reading order even when sizes and alignments differ. Reserve the final geometry from the beginning so new words do not push existing lines sideways or cause repeated recentering.

Possible content-led relationships include a compact supporting line over a larger key idea, a dominant term with a smaller completion aligned to its edge, or a multiline block in genuine negative space beside an action. These are relationships to develop, not fixed layouts to rotate between films.

For an independent headline, an initial experiment is to make supporting words roughly 0.5–0.7 times the dominant word's size, then adjust optically. This ratio is not a source measurement or a brand requirement. Enlarge the supporting text if it is too small at phone size; simplify the optional headline instead of reducing required captions.

Keep Garet Variable Medium for headlines and the prescribed Regular face for body/captions. Apply Vietnamese body/caption horizontal scale once before measuring widths. Avoid random per-word rotation, stretching, or font changes. A distinctive hierarchy should remain legible as a still composition.

## 5. Implement successive unit reveals

Keep a complete phrase's layout stable and reveal units using visibility/opacity or a local mask. Use separate editable units when needed, grouped under a phrase parent for later transitions. Keep word spacing explicit; hidden words should reserve layout space without becoming visible.

At each actual unit onset, a proposed 30 fps starting recipe is:

| Relative time from the unit's reveal | State | Purpose |
|---|---|---|
| Frame 0 | Opacity 0, optional Y +6–12 px at 1080 × 1920 | Subtle start beneath its resting position |
| Frame 3–5 | Opacity 100%, Y at rest | Fast settle, ease-out without bounce |
| After entry | Hold at final position | Keep prior units available for reading |
| Phrase handoff | Parent fades/cuts or changes depth | Move attention to the next idea |

Scale pixel travel to the actual canvas and frame timings to the actual FPS. A hard reveal or 1–2-frame fade can be better for fast speech. The earlier slower whole-phrase entry recipes should not be applied independently to every fast word; overlapping long entrances can make the result unreadable.

The main unit can arrive at its final larger size directly. If a small scale entrance helps an optional headline, animate uniform scale near 98% to 100% over a few frames; keep it subtle and do not cause reflow. A key word does not need a bounce, glow, sound effect, or zoom to become important.

## 6. Subtitle modes: choose one deliberately

### Mode A — Progressive speech captions

The progressive text itself carries the spoken caption. Every requested spoken word must appear accurately, in order, with enough combined reading time. Keep the caption font role and weight, even if selective composition is used. Reveal units as spoken, accumulate them within a short cue, hold the completed cue where possible, and clear it at a natural boundary.

This is an explicit alternative to showing the whole cue at its start. Do not delete small connectors or later words to create a stronger slogan. Do not hide prior words immediately if that produces a difficult one-word-at-a-time reading task. If the pace cannot support full readable captions this way, switch to Mode B or a quiet complete cue.

### Mode B — Progressive editorial headline plus complete captions

An optional headline can emphasize the idea in the brand's headline face, while a separate caption carries the complete speech. Separate the zones and visual priority. The headline may be shorter than the spoken sentence because it is labeled as editorial emphasis, not the only subtitle layer.

Do not duplicate a dense sentence in two competing large blocks. When the headline becomes the primary task, simplify the background or choose a quieter shot. When delicate action matters, remove the optional headline and keep readable captions.

## 7. Handoff from an old phrase to a new one

The supplied stills show a blurred earlier text plane behind a sharp foreground phrase. A practical interpretation is a **text-layer focus handoff**, not proof of camera rack focus or a measured source animation.

To try this on optional headline layers, retain the old phrase briefly, reduce its prominence, and bring the new phrase into a clear foreground region. Proposed starting values at 1080 × 1920 are an old-layer opacity around 15–30%, blur around 5–10 px, and uniform scale around 94–98%, changing over roughly 6–10 frames at 30 fps. Use only the changes needed; the source values are unknown. Clear the old layer after a short handoff rather than accumulating a wall of blurred text.

The new phrase should be readable immediately after its entrance and should not overlap the most important action. Blur the old text layer only, keeping the actual subject, subtitles, and wordmark clear. If the renderer cannot isolate the text, use a simple fade/cut instead of blurring the whole picture.

For Mode A speech captions, do not blur required text before the viewer has had a reasonable chance to read it. Keep blur/depth effects on optional editorial layers when caption reading is at risk. Do not move real machine labels or invent a visual depth relationship presented as a technical fact.

## 8. Offline CapCut construction

Implement the treatment in the existing draft using the actual version's supported text materials, segment structures, transforms, and keyframe time bases. Native editable text units can share a phrase-level organization when supported. Preserve each unit's final placement and the narration mapping. Do not paste the public frame/pixel suggestions into unknown internal fields.

If exact blur, grouped control, or animated type cannot be expressed reliably in that draft, a controlled compositor can render the optional headline overlay and link it as a durable project asset. Keep complete captions editable where required, and disclose that a rendered headline overlay is flattened. Do not silently substitute flattened text for a mandatory editable typography deliverable.

Read back the edited draft, check resources and timing, and inspect an external moving preview where feasible while keeping CapCut closed. Native reopening remains the user's next step in the default workflow.

## 9. Review and retain the useful lesson

Review both the complete static composition and actual playback with the voice. Check onset alignment, reading order, all spoken words, supporting-text size, diacritics, stable layout, contrast on changing footage, phrase completion time, and whether the old text interferes with the new one. Inspect the first and last visible frames of the main words, not only a midpoint contact sheet.

If the result feels like mechanically flashing words, improve semantic grouping and hold time. If it feels like a template, change the current film's hierarchy, spatial relationship to the subject, or phrase handoff according to its story. If it feels chaotic, remove one motion/depth layer before adding another effect.

Record the implemented treatment in the project-side creative history, including any useful user feedback. Keep source examples and production imagery outside this reusable skill. Do not claim the original video's timing was reproduced exactly unless playback and measurements actually establish that.


---

# Typography Attention Handoffs

## 1. Evidence and interpretation

This guide extends the 6 November 2026 visual study of short excerpts from eight creator videos. The reviewed material included progressive composed text, topic cards that persisted over cuts, quieter captions over explanatory artwork, brief softened text entrances, old phrases retained as blurred background layers, and text compositions changing with camera framing.

These are observations of decoded image sequences, not access to the creator's editing project. Exact fonts, curves, blur parameters, and audio synchronization have not been established. All implementation numbers below are suggested starting points. Working sources and frame records stay outside the reusable skill; no reference-video assets or copied compositions are included.

## 2. Assign each text layer a job before animating it

Distinguish the topic, the spoken caption, and optional editorial emphasis. A topic card can persist across multiple spoken sentences because it names the subject; a speech cue should change with the actual words. An emphasized word can become visually dominant without changing the topic. Mixing these functions makes a persistent title look like a stuck subtitle or makes a shortened slogan appear to be a complete transcript.

Record for each layer: its role, visible interval, speech or concept it supports, final geometry, and the point at which it yields attention. Preserve complete requested subtitles even if the studied source did not show every spoken word. The role determines the font treatment: brand headline roles and language-specific body/caption roles remain distinct.

## 3. Use stable composition with selective hierarchy

The observed progressive text often retained its existing resting position while later words completed the phrase. A large semantic unit could arrive on a second line or occupy more width than its supporting words. The transferable lesson is to design the complete phrase first and reveal units into its reserved geometry, not repeatedly center each growing string.

At implementation time, measure the actual final text, protect action and logo space, and store word/phrase positions explicitly. Do not animate tracking or rerun automatic wrapping in a way that shifts earlier words at each onset. If a new line is needed, plan its baseline in advance. Keep the reading sequence obvious even when line sizes or alignments differ.

For a caption, preserve the required Regular face and use restrained scale/layout variation only when it stays readable. For a separate headline, use Garet Medium and a stronger size hierarchy if helpful. Do not import source serif/italic/heavy faces or source colors as new brand rules. A typographic distinction can be created through spacing and scale within the approved system.

## 4. Persistent topic card across cuts

Observed topic cards sometimes remained in place while footage changed angle or briefly cut to relevant context. Their job was conceptual continuity, not word-by-word transcription.

Use this when several adjacent shots support the same clear idea. Keep the topic readable in a consistent screen region while checking that each shot leaves adequate space. Keep speech captions separate and legible when they are required. A white card in a source does not mandate a white card for INKAVA: choose the prescribed brand palette and appropriate text role.

Clear or reduce the topic at a semantic boundary so later footage can breathe. Do not carry it into a different operation or claim merely because the last edit used a three-second title. If a new angle fills the card's region with an important action, end the card, reposition deliberately, or choose another shot. Do not let a persistent title obscure the evidence.

## 5. Handoff from strong typography to explanatory artwork

The studied sequences did not keep their largest typography throughout every moment. When a diagram, staged visual explanation, or material/object insert became the main information, the speech layer could become smaller and calmer.

For INKAVA, first decide what the viewer needs to inspect: the operation, a verified detail, or a designed explanation. At the handoff, remove the optional large headline, simplify remaining labels, and keep complete readable captions in a protected zone. Do not simultaneously launch a full word build, a diagram reveal, and a strong zoom merely because all three are available.

A proposed production order is: establish the real subject, introduce the explanatory layer, hold its meaningful state, then return visual priority to footage or a new statement. Durations follow the actual narration and complexity; this is not a universal opening formula. A technical card that never adds information should be omitted.

## 6. Old phrase becomes background; new phrase becomes foreground

The requested opening and a separately inspected opening showed an older phrase becoming softer and less prominent as a new sharp phrase appeared nearby. It is useful to think in terms of attention state: active phrase, completed phrase, retiring phrase. This does not establish that a real camera focus change was used.

Build the effect on separate text groups. Once the earlier statement has been readable, lower its opacity and soften it if supported; bring the new phrase into its intended final layout. A slight change in the old group's position/scale can suggest recession, but avoid a drift that competes with the next reading task. Keep the subject, body captions, and supplied wordmark clear.

The earlier phrase may remain subdued through part of the new phrase if that adds semantic continuity. Remove it when the frame becomes crowded or its meaning is no longer needed. Do not accumulate a permanent backdrop of unreadable past speech. At a clean change of speaker or visual argument, clear the outgoing phrase groups together unless a specific continuity purpose justifies retaining them; a persistent topic card has a different job from retiring speech. For progressive captions that carry required spoken text, preserve adequate reading time before retiring a cue; use a separate headline layer when the effect would undermine subtitle readability.

The progressive-word guide contains proposed opacity/blur/time ranges. The source's actual values remain unmeasured. If the chosen editor cannot isolate the old text layer reliably, use a controlled rendered headline overlay or a simple fade rather than blurring the whole video.

## 7. Softened keyword entrance

Dense samples from one opening showed a dominant word initially softer and then clearer. This can be approximated by a short blur-to-sharp entrance, but the visible states alone do not identify whether the source used blur, motion blur, a preset, or another compositor technique.

For an optional headline, a proposed experiment at a 1080 × 1920 output is a 4–7 px text-only blur resolving to zero over 3–5 frames at 30 fps, with little or no positional travel. Hold sharply after entry. Test the effect at phone size and on the final encoded output. Text rendering and blur filters vary; change the values optically rather than treating them as source measurements.

Use this selectively, especially on a meaningful key word. If it reduces reading time, creates halos, affects diacritics, or combines badly with a fast cue, remove the blur and reveal sharply. The user's request for word-by-word typography is not a requirement to blur every word.

## 8. Coordinate text with a changing view

Across the excerpts, typography could switch between a lower-frame statement and text in a side region when the speaker's framing changed. The transferable principle is to respond to available negative space while keeping a coherent reading system.

In a manufacturing edit, protect the full action path, not just the first hand position. A wider view may support an optional side composition; a close-up may need a quiet caption below the working edge. Reposition at a deliberate phrase or shot boundary instead of chasing the subject continuously. If the subject crosses the text area, revise the visible interval or composition.

A filmed panel and its optional headline can share a transform in a designed transition if that supports the story and the draft version can express it. Use a deliberate group/precomposition so their relative placement stays coherent. Keep required captions outside that transformed panel when otherwise distorted or cropped. Perspective movement is optional; do not skew the real action until its geometry becomes misleading or the logo becomes deformed.

## 9. Treat alignment data as a draft

A follow-up diagnostic compared automatic source-caption word offsets with a local speech-recognition pass. Some onsets differed by hundreds of milliseconds. Neither set alone established the true audible boundary, and they should not be averaged blindly or described as verified frame-accurate timing.

For production, listen to the actual project audio and review onset estimates against the waveform and pronunciation. Map timing through the draft's source trim, target offset, and speed correctly. Visually inspect the rendered reveal too: the moment a layer becomes nominally visible is not necessarily the moment its word becomes readable. Avoid assuming that a long entrance ending near a word onset is equivalent to a sharp reveal at that onset.

Maintain separate fields in production notes for an automatic estimate, a reviewed speech boundary, the chosen reveal frame, and the frame at which the word is clearly readable. Leave unknown fields marked unverified. Use semantic phrase reveals if reliable word alignment is unavailable.

## 10. Choose the treatment per film

A creative series can use cumulative typography, a persistent topic, a quiet subtitle foundation, or a short focus handoff in different combinations. Do not build a new fixed template from this study. Review each film's own idea and its recent neighbors, then choose only treatments that improve that story.

In the default offline CapCut workflow, inspect the actual version's text/keyframe structures, implement supported behavior, validate the edited draft, and review an external moving preview when feasible. Keep exact typography editable when required; distinguish flattened illustrative overlays honestly. No source video or screenshot should be imported merely because it was useful for learning the method.


## 11. Change typographic register at a meaningful clause

Further opening excerpts showed compact sans-serif support, a much larger key term, and occasional contrasting letterforms within a statement. The useful principle is semantic hierarchy, not a new font for every word. Select the part that changes the statement's meaning, then let its size or placement make the relationship visible.

For INKAVA, keep the approved font roles. A separate headline can create a strong relationship between a compact setup and a larger consequence using Garet Medium, line length, and negative space. Required speech captions retain their prescribed Regular face. A source's serif or italic emphasis is an observation, not permission to introduce an unapproved face or synthetic slant. If the brand system cannot express a proposed contrast, solve it with composition rather than distorting glyphs.

Preserve negation, conditions, quantities, and the object of a claim. A large emphasized noun must not visually detach from a small qualifying word so strongly that a glance conveys the opposite meaning. Reveal tightly connected semantic units together when isolated words would briefly create a misleading claim. Check both the growing composition and its final state.

## 12. Coordinate monochrome with a complete emotional beat

An inspected opening shifted from color toward monochrome around a grave statement while the emphasis remained legible. This establishes a visible tonal change; it does not establish an exact color curve or prove the creator's intent.

For production, decide whether a tonal shift helps the current narration. A proposed restrained treatment is a brief move toward reduced saturation at the start of a complete emotional clause, held through its meaningful end and restored at a motivated visual boundary. Avoid desaturating every stressed word. The transition length follows the shot and narration; begin with a simple cut or short ramp and judge playback before adding anything else.

In manufacturing footage, preserve diagnostic information. Keep color comparison, ink matching, material discoloration, and any other color-dependent evidence in faithful color. A monochrome passage cannot replace the real evidence of a color check. If tonal treatment would hide a process result, retain the footage and let typography carry the emphasis. Keep the supplied logo compliant with the brand rules and do not derive new brand colors from graded source footage.

## 13. Handoff into a documentary or spatial explanation

The additional excerpts moved from large speech-led statements into maps, layered documents, dimensional comparisons, and then back to people. During these visual explanations, captions became compact enough to leave the explanation as the primary reading task. No source graphic needs to be copied to apply this principle.

Choose the visual grammar from the actual information: a process relationship may need a simple spatial diagram; a material distinction may need a real macro insert; a verified comparison may need an accurately scaled graphic. Give only one of these visual arguments priority at a time. Remove the optional large speech composition as the explanation arrives, maintain full readable speech captions, and return the text to the next shot's available space at a natural boundary.

Treat documentary assets as evidence: identify their origin and verify labels and data. Use generated imagery for clearly illustrative concepts rather than fabricated records, test results, certificates, or factory actions. If reliable data are missing, show a qualitative process explanation instead of a numeric-looking chart. Review the graphic's settled state long enough to understand it before the next transition; do not imitate a rapid montage merely because it appeared in a reference.


---

# Render Review and Version Selection

## 1. Purpose and limits

Use this guide during an authorized creative edit when a moving preview or rendered output can be inspected. Its purpose is to catch visible regressions, improve a specific editorial decision, and keep the native draft consistent with the review asset. A written shot plan, a syntactically valid draft, and selected stills do not establish the quality of an entire moving edit.

The external workflow study recorded on 6 November 2026 informed this independently written INKAVA guide. The later SeeCut Foundation with INKAVA Direction guide describes the separately bundled adapted source and its execution commands. Neither source inspection nor installation establishes that a particular video reviewer is consistently reliable, or that a JianYing integration works with an international CapCut version. Preserve the existing brand direction and app-closed editing workflow.

## 2. Establish what can actually be reviewed

Choose the strongest available route for the current environment:

- A supported video-capable model may inspect an authorized rendered file for action continuity, motion, and layout. Confirm that the tool actually accepts video and returns a completed result. Check its documented limits before preparing review clips.
- Local playback, listening, and dense decoded frame sequences can inspect particular cuts, typography entrances, or timing intervals. Use audio and consecutive frames for temporal questions. A contact sheet alone cannot confirm lip sync, reading comfort, or the feel of a transition.
- Draft inspection and media probing establish resource references, timing structure, properties, and editability. They do not substitute for rendering or viewing.

Record which route was used and the intervals inspected. If a service is unavailable, continue feasible local checks and label the missing review accurately. Do not make Antigravity, Gemini, HyperFrames, or a specific account a universal prerequisite for INKAVA editing. Do not invoke a permission-bypass flag or send private project media to a new service merely because a third-party workflow recommends it.

For long footage, select representative passages and critical boundaries according to the actual tool limits. Preserve a mapping from each review clip's local timestamp to the full timeline; otherwise a reviewer can correctly identify a problem that the editor fixes at the wrong time. Reviewing a short section is an internal production check, not an automatic request for another approval.

## 3. Keep a compact, usable beat record

Extend the current timeline notes rather than creating parallel conflicting shot lists. For each important beat, record:

| Field | What the editor needs |
|---|---|
| Timing | Target start/end and actual frame rate; source material and source range |
| Spoken meaning | Relevant narration and its role in the current argument |
| Visible action | The operation, evidence, or concept the viewer must understand |
| Main visual | Selected take, useful B-roll, verified insert, or original illustration |
| Text roles | Complete speech caption, optional headline, labels, and their hierarchy |
| Movement | Motivated image/text motion, its anchor, and the meaningful settled state |
| Protected content | Hands, machine contact point, print detail, color swatch, label, face, or logo |
| Proof and review | Source provenance, uncertainty, native support, and the interval to inspect |

Frame intervals should use a documented convention, preferably start-inclusive and end-exclusive in an internal plan. Keep source trim, target placement, clip speed, and review-clip offsets separate. For fractional frame rates, calculate timestamp boundaries from the rational frame rate; repeatedly adding a rounded frame duration can accumulate drift. Translate to the native draft's actual units only through a verified version-compatible route. Clamp source ranges to measured media bounds rather than extending a clip to disguise a rounding error.

This record supports decisions; it is not an instruction to assign equal shot durations or turn every spoken clause into a new scene.

## 4. Let the beat's job determine visual priority

For a manufacturing operation, let the real action occupy the main viewing area and let typography support it. A close-up should show the relevant contact, deformation, alignment, or result. A decorative card cannot prove an action happened.

For a comparison, make the compared items observable under a truthful framing and treatment. Color-matching footage needs faithful color. For a numerical statement, use only verified values and an appropriate graphic scale; omit an unsupported statistic rather than inventing a convincing chart.

For a concept without direct footage, choose an original explanatory diagram or clearly illustrative asset only when it helps understanding. Show its relevant state long enough to read. A quiet visual hold, material detail, or complete caption may be stronger than adding artwork. Preserve the requirement for accurate spoken subtitles throughout.

For an emotional or concluding beat, select the real visual that carries its meaning. INKAVA process footage does not require a talking head or a face at regular intervals. Do not adopt another workflow's requirements for frequent face appearances, mandatory spring motion, paper backgrounds, constant sound effects, or minimum graphic coverage. Negative space is useful when it supports an intentional composition.

## 5. Check the moving geometry, not only the resting layout

Inspect the moments where a failure is most likely: immediately before and after a cut, the first readable word, a changed line break, maximum text scale or travel, the closest approach of a hand to a caption, an illustration's important state, and an outgoing layer's last visible frame. Include the settled composition. Add samples around a suspected issue rather than relying on evenly spaced stills.

For measurable layouts, evaluate transforms, masks, clipping, opacity, z-order, and projected positions at those times. DOM bounds or compositor rectangles are useful evidence, but an axis-aligned box is not the full shape of a rotated element or a partially transparent overlay. A non-overlapping text box can still contain a shadow that obscures a label. Compare measurements with the actual rendered pixels.

Keep intended nesting and overlap explicit: a text label on its backing panel is normal; a caption crossing a fingertip during an adhesion test may obscure the proof. Judge the importance of the hidden area, not a universal overlap percentage. Likewise, an underline must follow its intended word after scaling or wrapping; an arrow must identify the actual feature rather than a nearby decorative shape.

Check the entire action path, not a single frame's protected box. Camera movement, stabilization, crops, and the subject's own motion can change that path. Do not add bounce merely to pass an animation check when a direct reveal or static headline better fits the film.

## 6. Keep factual assets and generated illustration distinct

For an evidence insert, retain enough project-side information to recover its source: file or page, capture date where relevant, source time range, intended claim, crop, annotations, and any uncertainty. For a real factory step, prefer the project's authentic footage and alternate takes before unrelated external stock.

Inspect the insert at the final viewing size. A large, genuine screenshot can still fail if the crop hides its context or its important text is unreadable. Check that a highlight points at the right item and does not conceal a qualifier. An external document is not evidence of INKAVA's own test result simply because its subject is similar.

If evidence is missing, choose a truthful qualitative explanation, omit the unsupported visual claim, or identify the gap. Generated labels, inspection records, certificates, measurements, interfaces, or factory actions must not be presented as captured proof. Do not fill empty space with simulated evidence to improve an automated aesthetic score.

## 7. Correct objective defects before comparing taste

First check the current brief, required process order, complete usable actions, voice-over continuity, accurate subtitles, media bounds, brand fonts, diacritics, readable contrast, protected action, and intended native editability. Review audio for unintended gaps, clipping, duplicated narration, and effects that mask important words. Confirm the output's streams and actual duration; set any sync tolerance from the real delivery requirement and frame rate rather than assuming a universal allowance.

A version that omits a required operation or loses speech is not acceptable because it looks more energetic. A quieter version is not worse because it has fewer animated elements. Fix confirmed defects before spending time on a stylistic comparison.

When an automated report identifies a fault, inspect the indicated timestamp and neighboring motion using the correct source-to-review mapping. Record the issue, the observed interval, and the evidence for accepting or rejecting it. Do not dismiss a real obstruction because the model named the wrong object; equally, do not move a correct composition merely because a model combined two adjacent shots into an imaginary overlap.

## 8. Verify that an external review happened

Keep the review input's identity, duration, inspected interval, tool result status, and raw returned evidence with the project notes when an automated reviewer is used. Ask for observations tied to specific times and actual visible or audible content. Compare reported events with the input. Recognizing an on-screen word alone does not prove that a model evaluated temporal motion or audio.

Do not give a visual reviewer the editor's preferred verdict, version names that imply quality, previous praise, or the implementation's self-description as a substitute for the video. It needs the same concise task criteria for both candidates. When supported, use an isolated review context containing only the authorized review media and relevant brief; do not alter account security settings to create that isolation.

Treat missing media ingestion, timeouts, empty output, contradictory clip identity, or unsupported temporal assertions as an unavailable or invalid review. A transport success response is not a quality verdict. An unavailable result is distinct from a tie, a rejection, or a pass. Retry only when the failure is plausibly transient and a bounded retry is useful; otherwise continue the checks that are available and report the gap.

## 9. Compare a candidate with the best retained version

When a material creative revision needs comparison, retain the current best working version and compare the candidate against it. Do not automatically use the last generated version if that version was already rejected. Give both versions the same review scope, playback conditions, and brief. Audio differences should be intentional and identified so louder playback does not masquerade as better typography.

If a video-capable evaluator is available and useful, compare anonymized candidates in both presentation orders. Map its verdicts back to the actual versions. Consistent preference with concrete, verified observations is useful evidence; conflicting results are inconclusive. Agreement still does not prove the choice is correct. Required content, known defects, direct inspection, and the user's judgment take precedence over a model's taste.

Use criteria suited to this film: the clarity of the operation, text reading order, relationship between speech and emphasis, appropriate visual breathing, brand coherence, and whether the motion helps the explanation. Avoid a single numerical beauty score or a claimed percentage of resemblance to a creator. A metric should not reward denser graphics when the brief calls for restraint.

If only local inspection is available, compare the relevant passages directly and describe that method. Do not label it an independent AI comparison. User-approved reference videos remain outside the reusable skill and are unnecessary for comparing the project's own versions.

## 10. Limit revisions to meaningful improvements

Set a small iteration allowance suited to scope, render cost, and the user's time constraints. A practical starting point for a short creative edit is an initial version and up to two substantial alternatives, but a simple correction need not generate competing versions. This is a planning allowance, not a reason to stop with known required work unfinished.

Each candidate should address a specific observed problem or creative opportunity. Record the intended change, review interval, actual effect, and acceptance decision. Combine minor corrections instead of re-rendering a full film for each pixel adjustment. Retain a working version until the candidate is shown to improve the relevant decision without losing required content.

Stop speculative aesthetic iteration when the requested result is complete and further candidates show no clear benefit. If a required defect remains, resolve it or identify the precise limitation; do not relabel the defect as a stylistic preference to meet an iteration limit. Do not keep rendering to chase an arbitrary score.

## 11. Check the native draft against the reviewed render

A rendered motion sequence, a set of layers, and editable native text/keyframes have different capabilities. Record the actual representation of each important element: native text, native animation, image layer, rendered overlay, or a supported combination. Transparent PNG layers can be moved individually, but text baked into them is not editable text. A faded still is not the same motion as a drawn stroke or a blur-to-sharp entrance.

When a compositor and native editor are both used, compare corresponding settled states and transition intervals. Check layer order, clip placement, framing, typography, opacity, alpha interpretation, audio, and duration. Verify the properties against the actual CapCut version. A helper's assumptions about scale, Y-axis direction, frame units, source-relative keys, or alpha support cannot be transferred from JianYing by name similarity.

Preserve the existing project. Do not create and register an unrelated replacement draft merely because an external tool only supports new projects. Keep CapCut closed, follow snapshot and backup rules, and disclose any unsupported native effect. An external render that differs from the draft should be identified as a separate illustration or concept preview, not presented as proof of the committed timeline.

## 12. Handoff evidence proportional to the task

Report the useful outcome: which edit or skill changed, the retained version, the most important improvement, the checks performed, and any material native/preview limitation. Keep detailed review records beside the project when they help later revisions. A short edit does not require a lengthy scorecard for the user.

For skill-development work, distinguish packaging and source verification from production validation: an installed review guide means the agent has instructions to apply, not that a real film has passed those checks. Never claim a third-party engine, video-native review loop, or CapCut compatibility was tested when only its documentation and source were studied.


---

# Motion, Editing, Zoom, and Focus

All numbers in this document are **proposed starting points**, not requirements or source measurements. Choose a treatment because it clarifies the story, focuses attention, or conveys an intentional emotion. Leave a shot still when it already works.

These motion recipes extend the integrated brand system; the brand PDF does not specify animation curves or zoom amounts. Keep the prescribed font roles and palette, and preserve the whole wordmark. When animating Vietnamese captions, compose movement with their fixed 105% horizontal type treatment; do not accidentally remove or double it. Use neutral rectangular fields, garment-tag-style frames, and restrained halftone only where they explain or organize information.

## 1. Review and select footage

Inspect the media itself, not only file names. For each usable section, record: source identifier, in/out time, visible action, shot size, direction of movement, subject position, exposure/focus, important audio, and whether it supports a specific part of the voice-over. Note missing, repeated, obstructed, or ambiguous actions.

Use the following shot functions, depending on what actually exists:

- **Wide:** establishes who, where, and what equipment is involved.
- **Medium:** shows how the person and tool interact.
- **Close-up:** explains contact, alignment, texture, a control, or a measurable detail.
- **Reaction or result:** shows the real effect of the operation, when footage supports it.
- **Contextual B-roll:** provides genuine manufacturing detail and bridges related ideas without disrupting the factual order.

A close-up should add information, not merely decorate a narration. If the footage does not show an action, do not create a misleading sequence that implies it does. Make missing coverage explicit.

Select shots consistent with the brand's photographic direction: real factory context, natural work, clean neutral/cool lighting, honest material color, and focused professional expressions. Do not stage or fabricate worker gestures to create artificial drama. Material B-roll may use mesh, weave, thread, ink surfaces, repetition, and graphic crops, while still making the process understandable.

## 2. Cut on action and match cuts

1. In the outgoing shot, find the frame where a recognizable movement begins or passes a clear visual landmark.
2. In the incoming shot, locate the same or a compatible phase of the same operation. Compare hand direction, object orientation, screen position, velocity, and the action's implied continuity.
3. Join near the selected frames. A small overlap or omission in the action may improve flow, but do not hide a required operation or repeat a movement so obviously that it looks like a mistake.
4. Play at normal speed with sound. Then step through a few frames around the edit: check position, direction, focus, exposure, cropped limbs, and whether the result implies an incorrect process.
5. If the match does not read honestly, use a clear cut to a different angle or an explanatory B-roll shot. A forced visual match is not worth confusing the operation.

Maintain the user-specified process order. Shot length follows the time needed to recognize the action and fit the voice-over. Do not automatically divide the total duration by the number of steps or force every clip to the same duration. Avoid switching angles so quickly that a key action cannot be understood.

## 3. Motion language and timing

The motion system should support the story and typography. Use a limited family of movements, a coherent pace, and intervals of stillness. Avoid bounce, shake, excessive blur, elastic overshoot, neon glow, and animated entry on every phrase unless the user specifically asks for them.

**Timing convention:** duration in frames ≈ seconds × project FPS, rounded to a whole frame. At exactly 30 fps, 8 frames ≈ 0.267 s and 6 frames = 0.200 s. Use the true project frame rate for conversion. Keyframes should specify position, scale, opacity, interpolation, anchor, and timing independently; a named preset may behave differently across editors.

### 3.1 Slide and fade for a text block

Use for a short headline or a subtitle that has enough time to become readable. Starting setup for 1080 × 1920 at 30 fps:

| Relative frame | Vertical position relative to final | Opacity | Behavior |
|---|---:|---:|---|
| 0 | +16 px | 0% | Starts slightly below its resting position. |
| 8 | 0 px | 100% | Settles with ease-out and no overshoot. |
| Six frames before cue end | 0 px | 100% | Holds completely still. |
| Cue end | 0 px | 0% | Fades out; position stays fixed. |

The 16 px travel is approximately 0.83% of 1920 px. Scale movement relative to H and try a subtle range of 0.5–1.5% H. A practical starting entry is 0.20–0.33 s and exit 0.15–0.20 s. These ranges are not minimum durations; choose a hard cut or very short fade when the caption would otherwise spend too much of its lifetime moving.

For an explicit ease-out curve, normalized progress can be `E(t) = 1 - (1 - t)^3` for `t` from 0 to 1. Position can be `Y(t) = Y_final + distance × (1 - E(t))`; opacity may rise separately. Text must be visible early enough for reading. Do not animate the whole video when only the text should move.

### 3.2 Quiet fade

For fast speech, atmospheric footage, or tightly packed subtitle cues, set text directly in its resting position and use a 2–4 frame fade or a hard cut. Preserve enough stable time for actual reading. Avoid flicker caused by one-frame gaps between adjacent cues.

### 3.3 Mask reveal

For an optional independent headline, define a static text layer and a rectangular or shape mask. Reveal left to right over 8–10 frames at 30 fps as a starting point. The text's position and scale remain stable while the mask expands. Keep accents, punctuation, and diacritics intact. If the reveal makes the sentence hard to read, replace it with a fade or static appearance.

### 3.4 Word emphasis

For requested successive spoken-word builds, use the progressive spoken-word typography guide. It defines cumulative reveals, word-onset alignment, phrase-level holds, and two distinct caption/headline modes. That treatment is an alternative to the complete-cue-at-start behavior below; every spoken word must still be preserved and readable.

Display the whole subtitle cue in the language-specific Regular face. If the timing supports it, change a complete selected word or phrase to a readable listed palette color over approximately 2–4 frames as it is spoken; hold until cue end. Do not use orange for body/caption text or automatically switch to bold. If a color change would weaken reading, keep the neutral subtitle and use a modest adjacent marker, or omit the effect. If speech is fast, display the permitted color from cue start or leave it unchanged. Never hide future words when that would compromise the subtitle requirement.

### 3.5 Subtle headline scale

For an independent, short Garet Variable Medium headline only, try uniform 96% → 100% scale and 0% → 100% opacity over 8–10 frames at 30 fps. Ease out and hold. This is **text-layer scale**, not camera zoom. Check for reflow, accidental clipping, and jagged glyphs; do not apply it to every caption or use it to alter the wordmark's proportions.

### 3.6 Callout line or marker

Attach a line to an actual visible feature, with the label in clear negative space. At 1080 px width, initial drawing dimensions can be a 2–3 px line and a 5–8 px endpoint; scale and review at delivery size. Animate the line on over 8–12 frames, then fade in the label over 6–8 frames, and keep it still long enough to read. If the object moves, track the anchor or hide the line when tracking fails. Never cover the point of contact or falsely imply a force, motion, measurement, or machine state.

## 4. Digital zoom and reframing

Scale percentages in this section are relative to the shot's **already framed baseline**, not necessarily the source file's original 100%. Before animating, identify the existing crop-to-fill, source dimensions, stabilization, and optical movement. If the shot is already heavily enlarged or soft, prefer an authentic closer shot. Check the whole camera path, not only the endpoint.

### 4.1 Slow push-in

- Purpose: draw attention gradually to a real detail while maintaining context.
- Starting recipe: baseline 100% → 103% over 3.0 s, e.g. frame 0 to frame 90 at 30 fps. Interpolate linearly for consistent movement or use a gentle ease-in-out if the motion should settle.
- Keep the point of interest at a deliberate anchor. If the hand moves, adjust the anchor or keyframed position carefully so the movement does not look like unwanted tracking.
- Avoid combining an unnecessary digital push-in with footage that is already physically pushing in, unless that is an intentional choice.

### 4.2 Slow pull-out

- Purpose: reveal the relation between a detail and its surrounding operation.
- Starting recipe: 103% → baseline 100% over approximately 2.4 s; set the end framing first, then ensure the start crop contains the full required action.
- Keep camera motion smooth; do not reveal a crop edge, blank border, or unwanted stabilization artifact. If the subject drifts outside the composition, keyframe position with the scale.

### 4.3 Controlled punch-in

- Purpose: mark a specific detail or moment of emphasis, not act as a default reaction to every spoken word.
- When source resolution permits, cut to a stable crop around 103–105% of the established baseline. Alternatively, start on a real closer camera angle. Choose the anchor around the meaningful detail and allow enough time to see it.
- Compare sharpness and composition at final resolution. If the crop softens the subject, cuts off a hand, hides a readout, or competes with subtitles, reduce it or remove it.

### 4.4 Crop mathematics and movement safety

For a uniform center-anchored scale `s = 1.03`, the visible fraction of the previous view is approximately `1 / s = 0.9709` on each dimension. With symmetric crop, each edge loses approximately `(1 - 1/s) / 2 = 0.0146`, or 1.46% of that dimension. At a 1080 px frame width, this corresponds to about 16 px per horizontal edge in the prior view. It is a geometric illustration, not a guarantee of sharpness or proof that a source can be enlarged.

An off-center anchor produces asymmetric crop. Also account for any earlier source-to-output crop. Test the beginning, midpoint, and endpoint, and inspect moving hands, on-screen text, and subject boundaries. Confirm that digital interpolation does not create jitter or flickering edges. Avoid changing crop automatically on every sentence.

## 5. Focus and visual attention

- Prefer real optical focus and depth of field already recorded in the footage. A cut from a wide operation to a genuinely sharp close-up is often clearer than simulated blur.
- If a subtle digital focus aid is justified, isolate the secondary background with a soft, tracked mask and apply a slight darkening or gentle blur. Keep the real object, working edge, labels, and subtitles sharp. Feather enough to avoid a visible halo; inspect moving edges frame by frame.
- Simulated depth can look false around hair, fingers, mesh, transparent objects, or rotating equipment. If tracking or segmentation fails, remove the effect. Do not blur an inconvenient detail in a way that conceals product quality or changes the truth of the operation.
- Direct focus through shot selection, framing, color contrast, and negative space before adding an effect. Do not force rack-focus simulations onto every cut.

## 6. Black-and-white treatment

Use monochrome only when it has a clear narrative or emotional purpose and the brief allows it. It may separate an intentional reflection, create a restrained contrast between sections, or focus attention on form and movement. It is not a shortcut to a modern European look.

Start with neutral monochrome conversion and preserve detail in skin, fabric, and shadows. Do not crush blacks or clip highlights merely to make an image look dramatic. Check whether adjacent color footage makes the transition feel motivated. Do not use monochrome where color matching, ink color, product color, or another color-dependent fact is being demonstrated.

## 7. Artwork and graphics

Choose from a pointer, outline, garment-tag/specification-style label, small comparison graphic, or compact technical card only if it makes something real easier to understand. One piece of explanatory artwork is usually enough for a single moment. Use the brand's type roles, palette tiers, neutral rectangles, and understated structure; keep line weights and any corner treatment coherent while allowing layouts to respond to footage. Rounded cards are not a source requirement; start with simple geometry.

A compact information card may contain one short title, a relevant icon, and one supporting line if both remain readable. A translucent or dark backing is acceptable when necessary for contrast; it should not cover the action. Verify every numerical value, arrow, and product claim against the actual project or user-supplied information. Do not present AI-generated material as documentary footage.

Choose any backing from suitable brand colors and keep orange out of the supporting body line. If adding halftone, keep it subdued and limited; inspect real-time playback at delivery resolution for shimmering dots or moire against mesh. Artwork must not enter the wordmark's clear-space area. The source gives no exact stroke width, radius, texture opacity, or motion duration, so these implementation choices remain proposals.

When illustration or motion artwork would improve the authorized edit, proactively use a capable available AI tool and the AI illustration and motion production guide. Create and inspect the actual artwork, establish control frames or implement native timeline keyframes as appropriate, render the motion, and integrate it. Use existing task authorization without repeatedly asking for ordinary production steps; do not send confidential assets beyond that authorization or assume a specific service is available. Keep the distinction between a flattened generated clip and editable keyframes explicit.

## 8. Motion QA

View the full sequence in real time with audio, then review cuts, subtitle entrances/exits, mask boundaries, callout tracking, and maximum crop at slower speed. Inspect the result on a phone-sized display. Remove anything that distracts from the operation, makes captions harder to read, or looks decorative without meaning.


---

# Color and Visual System

## 1. Brand palette before creative treatment

Use the palette and source-status notes in **INKAVA Brand Rules and Video Interpretation**. The former generic blue/lavender styling options are superseded by the integrated brand system. Do not treat an earlier video's colors as a competing brand standard. Source references: PDF pp. 6–12, sections 4.0–4.5.

The source's hierarchy is Primary 60% / Secondary 30% / Accent 10%. Orange belongs to the Primary tier but serves as a restrained highlight, with a separate instruction to stay under 15–20% of a composition. It must not be used for body text. Accent-tier colors should not dominate backgrounds. The source favors Off-White or light-neutral backgrounds and a limited palette per layout.

The Orange and Light Green working hex values remain provisional because the PDF's prose conflicts with its repeated swatch labels. Use the decisions documented in the brand reference consistently; do not silently pick another value, blend the two alternatives, or claim the discrepancy has been officially resolved.

## 2. Practical video roles

The following role mappings are **video design applications** of the brand palette, not additional specifications stated in the PDF:

| Element | Starting treatment | Reason and limit |
|---|---|---|
| Subtitle over darker footage | Off-White `#F8F4E9`, with a restrained Black edge/shadow if needed | Readable neutral baseline; protect the action. |
| Subtitle over a clean light field | Black `#000000` | Strong separation without introducing a new color. |
| Independent title or key statement | Black on Off-White; Off-White on a dark suitable brand field | Garet Medium supplies hierarchy without heavy styling. |
| Short signature emphasis | Small Orange rule, marker, heading, or section cue | Use the provisional working value from the brand rules; keep orange out of body/subtitle text and below its area limit. |
| Structural field | Off-White, or a balanced Secondary color such as Night Blue or Sky Blue | Supports grouping; choose a foreground with enough actual contrast. |
| Small supporting detail | A suitable Accent-tier color | Do not promote Accent-tier colors into a dominant background. |
| Fine frame or separator | Black or another legible listed color | Align with the garment-tag/specification language. |
| Logo | An appropriate supplied wordmark variant | Preserve form, minimum size, and clear space; do not redraw it. |

The official palette includes light and dark color pairings that work as adjacent design areas but may fail for small text laid over each other. For example, two dark fields can create a restrained composition while providing weak text separation. Judge the actual foreground/background relationship; do not assume the guide's pairing recommendation is a readability guarantee.

For a full graphic title card or cover, use the source's 60/30/10 composition balance without introducing all eleven colors. Start from a primary field, one supporting secondary area, and a small accent when useful. For natural footage with minimal overlays, apply the tier hierarchy to the designed graphics rather than recoloring the environment or covering footage to meet a numeric allocation. That is an explicit video adaptation of the static-layout guidance. Orange's cap applies independently of the tier ratio; a conservative working aim is below 15% of the designed composition.

## 3. Grade order

1. **Establish a neutral technical baseline.** Confirm the actual source color space and display transform when known. Preserve original media and use a reversible adjustment layer or non-destructive grade if supported. Do not assume Rec. 709 or apply a LUT blindly to unknown footage. The supplied PDF is an RGB identity reference, not a camera color-management specification.
2. **Balance exposure.** Retain relevant highlights on metal, white cloth, and hands; preserve detail in dark fabric. Use scopes if available and visual inspection on a suitable display. Do not crush useful shadows to manufacture drama.
3. **Honor neutral/cool industrial lighting without falsifying color.** The photography guidance calls for clean, even, neutral/cool tones. Correct a distracting cast carefully while protecting real skin, ink, textiles, and labels. It does not prescribe a blue tint, a Kelvin value, or a specific LUT. Mixed lighting may require selective correction rather than one aggressive white-balance adjustment.
4. **Match neighboring shots.** Compare similar objects and neutral areas across cuts; resolve unmotivated exposure and hue jumps before styling. Preserve natural changes in lighting when removing them would misrepresent the scene.
5. **Keep the creative treatment restrained.** Adjust contrast and saturation only as needed. The visual character should remain precise, functional, and material-focused. The guide's muted treatment of abstract textures is not a license to desaturate a color-critical product demonstration.
6. **Protect color evidence.** In color comparison, ink mixing, swatches, and approved-product footage, avoid hue shifts or monochrome treatment. Exact color accuracy requires authoritative references and suitable viewing conditions; neither an RGB hex label nor a grade guarantees printed fabric color. For textile production, the guideline explicitly calls for color tests.
7. **Check type after grading.** Recheck caption contrast and palette emphasis against the final image. Adjust placement or use a restrained brand field before altering product color. Check animation endpoints and changing highlights, not just a representative still.

## 4. Visual hierarchy and density

If footage already contains bright equipment, moving hands, and a dense background, keep the typography calmer. If a shot is stable and visually open, a deliberately composed Medium headline can carry more weight. Use size and space before increasing weight beyond the prescribed roles.

- **Size:** one larger key statement with smaller functional information, while preserving subtitle readability.
- **Weight:** Garet Medium for a headline and the language-specific Regular face for body/captions. Do not substitute Heavy or fake bold as a routine emphasis method.
- **Color:** Off-White/Black subtitles with a readable short palette emphasis when useful; orange can support a separate graphic cue, not running captions.
- **Space:** text in genuine negative space, away from hands, material detail, and the wordmark's protected area.
- **Time:** a quiet hold after a short entrance, and cleaner shots between denser information.

Avoid maximizing size, color, motion, and sound on the same word by default. A large word in the correct Medium face can provide enough emphasis by itself.

## 5. Texture and geometric structure

The source permits subtle halftone, garment-tag/specification-inspired frames, neutral rectangles, and color blocks as functional support. Use these to organize or explain rather than to add decoration. Do not copy example layouts or photography from the guide into the video.

A halftone can sit behind a small section label or in a quiet graphic area; it should not shimmer on playback, compete with real textile weave, or contaminate colors shown as evidence. Evaluate density after downscaling and compression. If it creates moire or noise, simplify or remove it. For color blocks, keep boundaries deliberate and support the palette hierarchy; do not fill the image with every brand color.

## 6. Cross-output consistency

Carry the type roles, wordmark discipline, color hierarchy, and understated industrial character through video, cover, and optional artwork. Adapt layout to each aspect ratio rather than copying coordinates. Color display can vary across screens and apps, so distinguish brand-token correctness from measured product-color fidelity. Record provisional Orange/Light Green choices until the source discrepancy is resolved.


---

# Proactive B-Roll Discovery and Selection

## 1. Default behavior when B-roll is not supplied

During an authorized editing task, **find suitable B-roll proactively** when the user has not provided it or the supplied coverage is incomplete. Start with the current project's accessible media, then use appropriate permitted external sources if needed. Do not make “please send B-roll” the default response while useful discovery is possible. A discovery task is not automatically a request to pay for footage, open private unrelated projects, or upload private material.

This behavior applies when actually editing or sourcing assets. If the user has requested only a written plan, review, or skill update, describe the relevant plan without silently starting downloads or modifying a project. Use the tools, access, and authorization available in the current environment; the skill itself does not create access to a drive, stock service, or generation service.

## 2. Define what is missing before searching

Create a short coverage list from the actual narration and rough cut. Each gap should name an informational job, not just a visual mood:

- Establish the real workspace or equipment context.
- Show a missing view of the same visible operation.
- Explain material texture, tool contact, alignment, a control, or a real result.
- Bridge two related stages without changing their order.
- Provide neutral conceptual context when the narration moves away from a specific operation.

Record the desired action, material, shot size, motion direction, aspect ratio, approximate useful interval, and whether the shot must be documentary evidence of INKAVA. A real inspection result or exact machine state generally requires actual project evidence. A conceptual statement about fabric may permit generic material footage if the edit clearly reads as illustration.

## 3. Search in a purposeful order

### Tier 1 — Current project and user-supplied footage

Inspect the current draft's linked media, imported footage, unused clip ranges, alternate takes, and the related asset folder the user has provided or authorized. Where a plugin or media connector can list/search these reliably, prefer it. Otherwise use available file and media tools within the relevant scope.

Do not assume all useful material is already placed on the timeline. A longer take may contain a readable lead-in, a close detail, or the finished action after the selected range. Build contact sheets or review short segments when available; then inspect the actual motion, focus, and action before selecting. Thumbnail similarity alone does not establish that the operation matches the narration.

Search only relevant folders and accessible asset libraries; do not scan unrelated private directories or other projects by default. If the intended asset location is ambiguous, progress with known media and ask a targeted location question only when needed.

### Tier 2 — Relevant existing user/brand library

Search a connected or local brand library when access and the user's task scope cover it. Prefer authentic INKAVA workshop, material, machinery, and worker footage. Confirm that an older asset still represents the operation, product, branding, and intended use. Do not silently import unrelated client or confidential material merely because it is accessible.

### Tier 3 — External stock or other permitted illustrative footage

If authentic coverage remains insufficient, search suitable stock libraries or other sources with a documented usage basis through available connectors, browser tools, or search. Build queries from **action + object/material + shot size/context**, then refine using the actual results. Add orientation or exclude terms only when they help. Do not select the first attractive industrial clip.

Before downloading or importing, check the original asset page and the applicable license or permission. Determine whether the intended commercial/branded use is allowed, whether attribution is required, whether an editorial-only restriction applies, and whether a clean licensed file is available. “Royalty-free,” public availability, a search thumbnail, or an AI-generated description alone does not establish permission.

Use existing entitled access or genuinely permitted files. Do not silently buy assets, subscribe, remove watermarks, bypass access restrictions, or reuse videos from the studied creators as B-roll. If a promising asset requires a purchase that is not authorized, continue looking for a suitable permitted alternative and report the option if useful.

External factory footage should not be cut in as proof that INKAVA owns that facility, uses that machine, performs that exact test, or achieved a displayed result. Use external material only where it is honest as illustration; identify it as illustrative in the deliverable notes and visibly distinguish it if the viewer could otherwise reasonably mistake it for documentary evidence.

### Tier 4 — Clearly illustrative artwork or generation when appropriate

When a suitable real shot cannot be found, first consider a cleaner cut, a hold on existing authentic footage, or a simple diagram using verified facts. Generated motion can illustrate an abstract relationship if the user has authorized that kind of work and a suitable tool/service is available. It cannot replace evidence of a real operation or result.

For a concept that actually benefits from illustration, follow the AI illustration and motion production guide and create the asset proactively within the authorized edit. Illustration is also a legitimate planned story treatment; it need not wait until all footage searches are exhausted. Keep its informational purpose clear and do not use it to conceal missing documentary evidence. Generate, inspect, animate, and integrate the result rather than stopping at an image prompt or a suggested tool name.

Use the existing permitted generation workflow, including Higgsfield when appropriate and available, rather than assuming any service exists. Do not upload private footage or brand assets externally without authorization covering that use. Do not imply generated factory, workers, machine readouts, labels, or test outcomes were recorded at INKAVA. Keep the illustrative status clear where needed.

## 4. Candidate evaluation

Review candidates against the specific gap:

| Criterion | What to check | Reject or revise when |
|---|---|---|
| Narrative fit | The visible action supports the actual spoken idea | It is merely industrial-looking or contradicts the operation. |
| Documentary status | Whether it is real INKAVA media, generic illustration, or generated | The edit would make a false ownership, location, process, or results claim. |
| Technical consistency | Material, tool, machine type, direction, safety context, and visible result | The clip shows the wrong method or implies an unsupported step. |
| Composition | Useful action area, available crop, caption space, and relevant details | Reframing hides the working edge, subtitles, or context. |
| Image quality | Resolution, focus, exposure, color, frame rate, and compression | Enlarging or retiming creates distracting softness or artifacts. |
| Visual continuity | Motion direction, scale, lighting, material color, and transition potential | It looks like a different operation masquerading as continuity. |
| Usage rights | Original source, applicable permission/license, intended use, attribution | Rights are unclear, the asset is watermarked, or the intended use is excluded. |

A horizontal candidate can work in a vertical edit only if a meaningful crop preserves the action. If cropping removes important context, use a deliberate framed presentation when it suits the story, or choose another asset. Do not automatically stretch footage to fill the canvas.

## 5. Record provenance without burdening the viewer

Maintain a compact asset ledger with the project:

| Field | Required content when applicable |
|---|---|
| Asset ID | Stable identifier used in the edit. |
| Origin | Current project, permitted brand library, external stock, or generated illustration. |
| Source | Local asset path or original external asset URL/ID. |
| Usage basis | Supplied project asset, applicable license/permission, attribution, and material restrictions. |
| Fit | The narration beat and informational job it serves. |
| Selected range | Source in/out and destination timeline range. |
| Treatment | Crop, rate change, color adjustment, or other material modification. |
| Disclosure | Whether illustrative status or credit needs to appear in the video or handoff. |

Keep technical provenance and licensing records in the handoff unless a visible attribution or disclosure is required. Do not cover the footage with implementation details that do not help the viewer understand the story. Preserve any attribution the actual license requires.

## 6. Integrate B-roll with action, subtitles, and brand

- Cut around the actual action phase and spoken meaning. Match motion or object position only if it preserves factual continuity. Do not force a stock shot to appear to be the next stage of a real INKAVA process.
- Keep complete subtitles aligned to the voice-over across the inserted shot. Check that the new background does not make text disappear. Adapt the optional headline or artwork rather than shrinking captions.
- Match exposure and neutral/cool industrial character carefully while preserving honest material color. Avoid grading an external asset so aggressively that a different material appears identical to the user's product.
- Preserve the right playback cadence. Do not slow a process in a way that implies a different duration or invent a machine sound as proof of an event. If using generic material only for atmosphere, ensure it does not interrupt a required action.
- Respect source license conditions and the brand's type, logo, palette, geometry, and understated motion. A B-roll shot does not need a separate label or effect just because it was sourced separately.

## 7. If no acceptable B-roll is found

Continue useful editing with authentic material. Revisit unused ranges, adjust the cut, choose a longer meaningful hold, or remove a nonessential visual detour. Do not fill the gap with unrelated stock, copied creator content, fabricated evidence, or repeated footage presented as a different operation.

Report the specific remaining gap and the alternatives that were feasible. Ask for an asset location or a necessary decision only when it would unblock work that cannot proceed accurately. Missing B-roll does not justify claiming that a search succeeded, that a license was verified, or that footage was imported when those actions did not occur.


---

# AI Illustration and Motion Production

## 1. Act on the asset-production request

When an authorized editing task benefits from a supporting illustration or motion artwork, proactively produce it with available AI tools and integrate the result. The user should not have to supply every illustration or separately ask the AI to execute every generation step. A prompt, storyboard, or motion plan is an intermediate artifact; finish the actual image or animation when production is in scope.

This instruction applies to the edit's genuine visual needs. It does not require AI imagery in every scene or authorize unrelated generation. During a skill-writing or analysis-only task, update the instructions or analysis rather than silently generating project assets. Use the user's existing permissions and task context; do not ask again for ordinary steps already authorized. If a specific private upload, purchase, or external action needs additional authorization, ask only for that unresolved action while completing independent work.

## 2. Choose the correct production route

Discover the capabilities available in the current environment and read the relevant tool/skill instructions before operating them. Prefer an appropriate connector or native tool over browser automation when it supports the task. If one route is unavailable, use another capable route instead of claiming the work cannot be done merely because a preferred service is absent.

| Need | Suitable route | Essential distinction |
|---|---|---|
| Original raster illustration, material-inspired abstraction, or image edit | Available image-generation/editing tool | Inspect the result; an image alone has no motion timeline. |
| Motion from a generated or supplied still | Available image-to-video or video-generation tool with suitable controls | Rendered motion may not expose editable keyframes. |
| Motion guided by initial/final visual states | A service that actually supports first/last-frame or other control-frame inputs | Control frames guide synthesis; they do not guarantee exact numerical interpolation. |
| Exact type, captions, wordmark, line drawing, or measured transforms | Editable motion editor, NLE, or code-driven compositor | Preserve font roles, content, timing, and actual keyframes independently of generative footage. |
| Final assembly | The editor/project workflow selected by the user | Import and verify the returned assets; retain editability where available. |

Higgsfield can be used when available, appropriate, and covered by the current task authorization. Another capable image or motion tool can serve the same role. Do not hardcode an assumed model name, account state, API, price, or feature set into the plan; inspect the current tool capabilities. Routine generation within the requested production scope does not require repeated confirmation. Do not silently purchase a plan or unlimited credits.

## 3. Define the artwork from the actual story

For each proposed asset, identify:

- The actual voice-over beat and the one idea the illustration should explain.
- Why footage, a simpler annotation, or a clean cut is insufficient for this moment.
- Whether the asset is an abstract illustration, schematic explanation, material treatment, supporting backdrop, or another clearly defined visual role.
- Its destination aspect ratio, visible duration, caption space, protected action area, and relationship to the supplied logo.
- Which details must remain faithful to supplied assets and which details are intentionally illustrative.

Do not generate a fake factory, worker, certificate, inspection result, machine readout, or product defect as documentary evidence. An illustration can explain a relationship without pretending to record a real event. If a concept is technical, use verified information and omit unconfirmed dimensions or mechanisms.

The illustration should follow the INKAVA system: authentic material character, clean geometry, controlled palette, restrained halftone where useful, and enough negative space for editorial type. Keep source-rule versus video-application distinctions intact. Use the documented provisional Orange/Light Green choices consistently until resolved.

## 4. Create and inspect the image

Prepare a generation request specific to this asset. Include the intended subject, material, composition, viewpoint, lighting, palette roles, background, required empty zones, and factual constraints. Provide permitted source assets only when they are actually needed. For an edit, identify what should change and what needs to be preserved; follow the image tool's supported reference-input mechanism.

Request transparency for an isolated overlay when the tool supports it, and verify that the returned file has meaningful alpha. A checkerboard painted into an image is not transparency. For a full-frame background, create a deliberate field suited to the typography and the final aspect ratio. Avoid baking unnecessary text or logos into the generated artwork.

After generation, inspect the actual returned image:

1. Is the subject and visual relationship correct, with no invented technical claim?
2. Does the composition leave the required room for captions and action?
3. Are geometry, material detail, edges, reflections, and any human anatomy coherent?
4. Are the palette and visual density suitable for INKAVA?
5. Is alpha valid if required, and does the image have sufficient usable resolution for its intended crop and movement?
6. Does any generated lettering, logo-like mark, or interface element need removal?

Correct meaningful defects using a focused image edit or a refined generation request. Preserve good elements rather than restarting without a reason. Do not continue generating near-identical variants after the defect has stopped improving; simplify the artwork or use a controlled graphic solution.

## 5. Separate generated visual assets from exact typography

Set headlines, labels, and complete subtitles in the editor/compositor using the prescribed typefaces. Keep the supplied production wordmark separate from generated imagery and preserve its geometry and clear space. Do not rely on an image/video model to produce exact Garet typography, Vietnamese diacritics, readable small print, or a faithful INKAVA logo.

If a generated draft contains placeholder lettering, remove or cover it appropriately and add real editable text. The final subtitle text comes from the actual audio. The English skill language does not authorize translating Vietnamese dialogue. Apply the Vietnamese caption/body 105% horizontal treatment once; do not stretch the whole artwork or logo.

## 6. Plan motion states and real keyframes

Distinguish two different kinds of control:

- **Visual control frames:** images describing important visual states, such as the start and end of an illustrative move. A generative video tool can use them only if its actual feature set supports them.
- **Timeline keyframes:** timed numerical properties in the editor/compositor, such as position, uniform scale, opacity, mask path, line trim, or camera movement. These are required when exact predictable motion or editability matters.

For each animated element, specify its purpose, layer, anchor, start/end state, timeline interval, easing, and protected regions. Include an explicit hold when the viewer needs to inspect the artwork. Use a small set of compatible movements. Do not animate every layer independently merely because it exists.

For generative animation, preserve the approved artwork's identity, viewpoint, and factual relationships. Describe the intended motion, stable features, camera behavior, duration, and things that must not appear. Use reference/control frames where supported rather than expecting a text instruction to preserve an exact shape. Do not call a prompt that mentions “keyframes” an editable timeline.

For precise motion, implement actual keyframes in the selected tool. A brief example of a **proposed**, content-neutral 30 fps composition is:

| Element | Relative time | Property state | Behavior |
|---|---:|---|---|
| Illustration group | 0.00 s | Opacity 0; Y 16 px below its resting position on a 1080 × 1920 canvas | Initial illustrative entrance. |
| Illustration group | About 0.27 s | Opacity 100%; Y at rest | Ease out without bounce, then hold. |
| Optional connector line | After the illustration is readable | Trim/reveal 0% to 100% across roughly 8–12 frames | Point to a verified relationship, not an invented measurement. |
| Editable label | After the line becomes meaningful | Fade in across roughly 6–8 frames | Hold long enough to read; keep the caption area clear. |
| Illustration group | Last roughly 0.15–0.20 s, if an exit is needed | Fade out without changing the evidence relationship | Adapt to the next cut and actual reading interval. |

The values are starting trials, not brand rules or a requirement to use this entrance. Scale to the real canvas and FPS. If the shot is too short, remove staggered steps or keep the artwork static. Compose any applicable text-language transform with the animation rather than double-applying it. Keep the wordmark's aspect ratio and clearance intact throughout.

## 7. Produce the animation, not just the plan

Submit the prepared image/control-frame/motion request through the actual supported tool, or implement the keyframes in a capable editor/compositor. Track the returned job state when generation is asynchronous and retrieve the completed asset. Do not report success while a job is only queued or running.

When the user asks to create motion inside an AI tool, use that tool's real production controls where available; do not stop at describing how the user could do it. If the AI tool generates only a flattened clip, supplement it with editable text and exact overlays in the selected editor. If that tool lacks precise keyframe control, explain the limitation and use an available deterministic compositor for the parts that need it. Be accurate about which output is editable.

If the route repeatedly fails without useful improvement, switch to a simpler controlled illustration, static asset with native keyframes, or another available supported tool. Use a bounded revision loop tied to visible defects; do not spend indefinitely on variations. Continue the rest of the edit while any genuinely independent generation job is running, and verify completion before final assembly.

## 8. Review temporal quality

Inspect the rendered motion, not only its first frame. Check the beginning, middle, end, key transitions, and real-time playback for:

- Shape drift, disappearing parts, changing material, inconsistent perspective, or impossible mechanisms.
- Unrequested camera movement, flicker, morphing, duplicated fingers, unstable edges, or invented readouts.
- Halftone shimmer, texture crawling, compression damage, and poor alpha edges.
- New lettering or logo-like marks introduced during motion.
- Lost caption space, blocked action, or text/graphics entering the wordmark's clear area.
- A false impression that an illustrative motion is actual footage or a measured process.

Revise the relevant defect, trim an unusable section only if the remaining meaning is still correct, or replace the animation with a more controlled approach. A visually polished still does not establish that its generated motion is usable.

## 9. Integrate and hand over

Import the verified image or animation into the actual project, set its timing against the real voice-over, and recheck the full edit. Confirm aspect ratio, crop, playback speed, resolution, color handling, alpha if used, captions, and the transition into/out of the asset. A generated asset is not integrated merely because it has been downloaded.

Keep editable type and native keyframes when available. Preserve the returned still, final render, used control frames, essential generation settings, and project references needed to reproduce or revise the work. These are current-project working assets, not source-video examples to add permanently to the reusable skill.

In the handoff, state which assets were generated, which parts have editable keyframes, which parts are flattened renders, and any material limitations. Keep technical production records outside the viewer-facing video unless attribution or a visible illustration distinction is necessary. Deliver the actual requested output, not only generation prompts or promised future work.


---

# Production Workflow, Deliverables, and Covers

## 1. Work from the current project

Read the user's latest request first. Record the output platform and aspect ratio, target duration, editor and editable-project requirement, required process order, language, subtitles, voice-over, intended audience, available assets, permitted services, and any explicit exclusions such as no music or cuts only. If a duration conflicts with a complete voice-over or the required action, identify the conflict rather than silently dropping content.

Default to the existing CapCut draft with the app closed. The user normally imports footage and narration into the project; discover and resolve them there before asking for assets. Follow the offline CapCut guide and keep the app closed through handoff unless the user explicitly requests another workflow.

Load the integrated brand rules before designing. Check whether the user has supplied a newer guideline, correct variable fonts, production wordmark variants, or clarification of the two conflicting color values. Use the documented provisional choices if unresolved and identify them honestly. Do not treat this skill's creative timings and layout suggestions as official brand specifications.

Follow the execution-readiness guide to establish the actual editing/rendering route and the required native-project capability. During production, verify a representative short section before repeating its treatment throughout the film. A skill review alone does not establish successful rendering or native-editor compatibility.

When there is an existing project, identify the intended draft and current media. Check project modification time and distinguish a copy from the active draft; do not assume that a previously inspected version is still current. Read or inspect existing tracks before changing them. Preserve unrelated user edits.

## 2. Detailed editing sequence

### Pass A — Story and media

1. Listen to the full voice-over and transcribe the actual recording. Separate confirmed wording from uncertain terms. Map statements to the actions they describe.
2. Watch source footage and build selects by action, start/end, framing, direction, visual clarity, and original sound. Note which important actions are genuinely visible.
   If B-roll has not been supplied or a coverage gap remains, follow the proactive discovery guide: inspect current-project media and relevant accessible libraries first, then search appropriate permitted external sources where useful. Record usage rights and whether an asset is documentary or illustrative.
3. Build a narrative outline from the requested sequence and the recorded voice. Allocate time by meaning, not an even number of seconds per shot. Make a note when narration and footage do not support each other.

For a new creative film, define its own editorial concept and compare it with accessible recent INKAVA work using the creative-variety guide. Consider a few meaningfully different directions internally, then choose the strongest one without adding a routine approval step. In a batch, map the films' individual creative signatures early so ten videos do not become ten versions of one template.

### Pass B — Rough edit

1. Place the main action shots in the required order. For each action, retain enough context, contact/movement, and result where footage allows.
2. Add B-roll that contributes a real detail, bridge, or change of scale. Choose match cuts by action and movement when they work; otherwise make a clear cut.
3. Check the rough cut with the actual voice-over before designing text. Adjust shot boundaries for both comprehension and the spoken rhythm.
4. Keep the audio edit clean. Use natural production sound, music, or sound effects only if in scope and available. Never add a sound suggesting a verified machine event if that event was not recorded or supported.

### Pass C — Typography, motion, and color

1. Prepare all requested subtitles from the actual speech, then set cue timing and line breaks. Review for accuracy before deciding which words to emphasize.
2. Apply Garet Variable Medium for headlines, Garet Variable Regular for English captions/body, and Inter V Regular at 105% horizontal scale for Vietnamese captions/body. Establish proposed pixel sizes, readable palette colors, contrast strategy, and placement for this footage. Build and inspect bright, dark, busy, calm, quick-speech, and slower-speech conditions. Check the actual font instances and glyphs.
3. Add a limited number of headlines, labels, or technical graphics only where each one adds clear value. Prefer one visual priority at a time. Use the brand's neutral rectangles, label frames, and restrained material/halftone language; do not use orange for body text or treat logo clear space as free room for a callout.
   If an illustrative image or motion would make the concept clearer, produce it in an available AI tool within the current authorization. Inspect the image, prepare supported control frames or implement actual keyframes, generate/render and review the motion, and import the verified asset. Keep exact brand text and the supplied wordmark controlled separately. Do not treat an unexecuted prompt or queued generation job as a completed asset.
4. Apply motion only when it improves attention or comprehension. Check reading time after every entrance/exit. Add a few restrained zooms or focus treatments only where motivated.
5. Balance exposure and shot continuity within the neutral/cool, authentic industrial direction. Protect real product color and material detail. Recheck typography after color changes; never recolor footage to force a 60/30/10 palette ratio.

### Pass D — Review and finish

1. Watch the whole piece in order with audio at normal speed. Then review fast speech and edit joins in detail. Inspect subtitles independently for spelling, completeness, sync, and Vietnamese glyph rendering when relevant.
2. Test at phone size and in the intended platform context where possible. Check text against interface overlays and alternative crops, and verify that hands, labels, and product are visible. If a logo is present, verify its form, clearance equal to the actual “i” height, routine 64 px digital minimum, and final display legibility.
3. Check audio on a reasonable monitoring device: speech remains intelligible, there are no unintended gaps or clicks, and any music or effects do not mask the voice. If an audio standard is requested, measure and deliver to that specification; do not invent a loudness target.
4. Check duration, frame rate, resolution, orientation, start/end, no unintended blank frames, and playback. Distinguish what was verified in the editor from what was verified only in a render or file parser.
5. Deliver the requested editable project, preview, or final export. Explicitly note missing media, font substitutes, uncertain transcript passages, unverified effects, unresolved brand-color choices where used, and any mismatch between preview and source editor.
   Identify generated illustrations and motion, distinguish editable keyframes from flattened clips, and preserve the working assets/settings needed to revise them. Do not add current-project generated imagery or source-video frames to the reusable skill as templates.

Before handoff, assess identity and variety separately: the film should remain recognizably INKAVA while showing its own editorial idea in type, illustration, motion, effects, rhythm, or framing. Compare with accessible recent work or the current batch. Revise superficial duplication through a meaningful design choice rather than adding unnecessary effects. Update the project/series creative record with what was actually implemented and relevant user feedback.

## 3. Shot-by-shot planning table

Use this table as an internal working structure; fill it from the actual footage and recording. A blank cell is allowed. Do not mechanically place every element in every row.

| Timeline in/out | Spoken words or time range | Source shot / in/out | Visible action | Caption and optional accent | Optional headline/artwork | Edit or keyframe decision | Verification |
|---|---|---|---|---|---|---|---|
| Project-specific | Actual audio, not invented dialogue | Actual source and timecode | Describe what can be seen | Complete speech when requested | Only if it adds information | Action cut or reason for motion | Sync, legibility, crop |

## 4. Project and file safety

- Use the editor and workflow the user requested. Do not assume the environment contains a particular application, font, binary, plugin, or project path.
- If asked to edit a CapCut draft while the application is closed, check the process is closed; inspect the actual draft version and media; create a backup; change only the necessary structures and tracks; validate paths, timing, resource IDs, duration, and any effects that can be checked. A syntactically valid file does not prove the editor will open it correctly.
- Do not reopen CapCut by default. Verify the edited draft offline and provide an external preview when feasible; state which native effects that preview cannot confirm. Native reopening can be checked if the user explicitly requests it, or after the user opens the project. Its absence does not block the normal app-closed handoff. Never claim verification beyond what occurred.
- Preserve original media and existing user changes. When editable titles, subtitles, keyframes, or a native project are explicitly requested, treat them as delivery requirements. Otherwise keep them editable where practical. If a workflow outputs only a flattened render, disclose that its text is not directly editable; do not silently substitute it for a required editable project.
- Do not upload private assets to an external service unless authorized for that use. Do not present generated illustrations as footage of the real factory, equipment, or product.

## 5. Cover strategy

When appropriate after an edit, propose two or three distinct cover concepts based on the actual video. If the user asks for completed covers, create the deliverable rather than stopping at a concept. Each proposal should identify: the actual frame or asset, a single editorial idea, a concise headline, subject and text placement, accent strategy, intended aspect ratio, and how the image will crop in its destination context.

For each direction, set a Garet Variable Medium headline and the correct language-specific body treatment if supporting text is needed. Select a restrained palette from the documented tiers. Let Off-White/Black establish structure, use a balanced Secondary area where helpful, and keep Accent colors small. A small orange heading or graphic cue may be appropriate; orange body copy is excluded. Observe the 60/30/10 guidance in a designed composition and orange's separate area limit. Check the provisional color notes if Orange or Light Green is used.

Three possible **approaches**, not layouts to copy:

- **Action-led:** a clear moment of contact between a worker and a tool; keep the hand and tool unobstructed, and place a short headline in genuine negative space.
- **Detail-led:** an authentic close view of material or a meaningful machine component; use one large keyword or concise label, and retain texture and context.
- **Outcome-led:** a visible result or completed operation if the footage supports it; add a short truthful title without inventing quality metrics or promises.

For an initial 9:16 composition, test a subject on one side and a headline in the opposing negative space; try approximately 8% W outer margins as a layout starting point, then adapt to the image and current platform overlays. Check the full image, square/profile crop, thumbnail size, contrast, subject recognition, legibility, and logo placement. These are not universal safe-area values. Use the real brand logo and source frame when supplied; do not recreate a product in a way that changes its features.

The proposed canvas margin does not replace the logo's official clear-space unit. Preserve the supplied mark's geometry and leave one actual “i” height on every side; no frame, text, texture, or crop boundary should invade it. Check the 64 px digital minimum and actual thumbnail readability. Use truthful factory imagery, natural working gestures, and material detail. The source's example photography and designs are reference content, not reusable assets or templates.

A restrained modern editorial approach can use large type, a clear focal subject, and breathing room. A cover does not need every available effect or an exaggerated visual claim to be compelling.

### Apply the cover-study findings through the brand

The recorded creator-grid observations suggest several transferable decisions: one central idea, a recognizable subject, short strong text, negative space for reading, a selective emphasis, and enough consistency to look like a series. Some grids used a dominant face, others a single object or a more dramatic composite; some retained a small brand identifier while allowing composition to vary. These are selective observations, not evidence of click-through performance or a requirement to copy a creator's format.

For INKAVA, an unmistakable hand/tool contact, a material detail, or a real machine can supply the focal subject. A face is useful only when the actual human story matters and the image remains honest. Do not fabricate a reaction or add interview-style split faces to a process film simply because those were observed elsewhere. If a layered composition is justified, retain one dominant subject and only the supporting detail needed to clarify the real idea.

### Choose the headline from the video's actual payoff

1. Identify the one specific action, question, or verified result that makes the video worth watching.
2. Form a concise headline that points to that idea without claiming more than the video supports. A short phrase of roughly two to five words is a useful initial trial, not a language-independent limit.
3. If a title accompanies the cover, decide whether the image and headline should clarify or complement it. Avoid repeating a long title, full subtitle, and several technical labels on the cover.
4. Check whether an implied information gap can be answered by the real content. Do not manufacture a defect, sensational failure, hidden secret, or quantified benefit merely to create curiosity.
5. Set the headline in the correct brand role, then refine line breaks and alignment. Use size and space to create impact before increasing visual decoration.

### Construct and compare distinct directions

For each proposed direction, select the real focal frame first. Check sharpness, a recognizable action silhouette, subject/background separation, honest material color, and space for type. A transitional frame with motion blur may work in video but fail as a static cover. Choose a better frame rather than overprocessing it.

Make the alternatives differ in a meaningful decision: action versus material detail, a closer versus wider view, or a conceptual headline versus a direct process title. Three near-identical crops with different accent colors do not provide a useful creative choice. Keep the brand's palette, type roles, and wordmark discipline consistent across the options.

Local darkening, a clean brand field, or a restrained crop can help reading, but preserve the important hand, tool, and product. Do not clone missing parts or change a machine/product feature to make the composition fit. Label any illustrative composite when required to avoid a false documentary impression.

### Review a cover as a small static image

- Look first without reading: does one subject and one idea stand out?
- Reduce to a realistic thumbnail size: can the essential words and action still be understood? Remove optional labels or simplify the composition before shrinking everything.
- Check full-frame and destination-specific crops: the headline, action, and logo must survive their actual visible regions. Do not assume every platform uses the same square or vertical preview.
- Confirm palette hierarchy, logo clearance/minimum width, headline font, and any Vietnamese supporting-text treatment.
- Compare the options with the same review conditions; do not claim a direction will perform best without actual evidence.

When creating covers is in scope, hand over the requested final images and editable composition when practical, with source-frame provenance and any provisional brand-color choice. When only proposing directions, label them as concepts rather than finished artwork.

### Brand consistency review

Before presenting a cover or finished edit, check the result rather than only the settings:

- The correct font role is visible; Vietnamese body/caption text has the 105% horizontal treatment exactly once, with complete diacritics and no accidental double stretching.
- Logo geometry, clear space, size, and supplied variant are intact wherever the logo appears; uniform motion does not introduce a temporary clearance violation.
- Text uses a legible palette treatment, orange is absent from running captions/body, and Accent-tier colors do not dominate a designed field.
- Color tiers and orange emphasis stay restrained; the two ambiguous source codes are treated as documented provisional choices, not claimed as confirmed.
- Material and product color remain honest; natural worker actions and useful detail carry the story.
- Halftone, geometry, and motion support information without hiding action, creating moire, or introducing unverified technical claims.

## 6. Reporting

State what was actually delivered, the project or file format, relevant duration and aspect ratio, and how it was checked. Distinguish a plan, editable draft, preview render, and approved final. Explain any material limitation honestly: missing footage, unconfirmed voice-over, unavailable font, unsupported editor effect, uncertain color accuracy, or inability to open the draft. A written skill records instructions and preferences; it does not itself train a model's underlying weights.


# Motion Graphics, Voice-over and Music Production (Remotion)

Use this guide when the user asks for a motion-graphic template, overlay or explainer sequence that will be placed in CapCut, together with its voice-over script and background music. It records working practice from the SFDC (shop floor data collection) and Automatic Frame Alignment films, November 2026. Pixel sizes, timings and layouts are proposed starting points, not brand rules; official font roles, palette and logo rules in the brand guide take precedence.

## 1. Deliverable pattern (what the user actually asked for, in order)

1. A 60 s motion template for CapCut: 4K UHD 3840x2160, 60 fps, H.264 (`--crf=15`, `yuv420p`).
2. Either a **full-screen** layout, or a layout with an **empty 9:16 glass frame** on the left
   (X 80-1340) for real footage, with motion on the right. Ask which. The user switched from
   framed to full-screen for the opener, the ending and the frame-alignment video.
3. A matching **ElevenLabs v4 voice script**, then background-music prompt, then retiming to the real voice.
4. Variants of one story: 60 s, 20 s (buyer/technical cut) and a 10-15 s overview opener plus an 8 s ending.
5. A shoot brief for the footage (Vietnamese, as a Claude Docs doc).

Always: stills sheet, then a 1080p draft (`--scale=0.5`), then 4K only after the user says so.
Send the draft file to the user, not just a path. 4K overwrites the earlier file of the same name.

## 2. Content and honesty rules

- **Never invent numbers.** Every figure comes from the user or their files. Flag unverified ones
  in the reply (3.06 min/bundle, 99.8% FPY, 99.99% registration, 3-4 h, 1 min 40 s per frame).
  A "bar chart" or drift curve with no axis values is acceptable only if labelled illustrative.
- **Qualify claims that depend on scope.** "Under 1 h" is true for a 14-frame job, so the video says
  "on a 14-frame job". Recompute from the user's Excel when a claim looks borderline
  (14 frames x 1:40 = 23:20; whole session about 54:25; 16 frames is about 1 h).
- **Soften absolutes for buyers**: "Fewer delays and mistakes", not "No delays".
- **NDA**: booking codes only as `A**** PO 34***` (and `B****`, `C****`). No client or brand names.
- **Blur third-party machine brands** in photos (HJD logos on press columns). ffmpeg `boxblur`
  needs `luma_radius<25` and `chroma_radius<25`; blur the box, overlay it back.
- Real people and real factory photos help ("add human elements"): hands-on SOP illustrations in
  the middle scenes, 2-3 real floor photos behind the closing line.
- Use the official logo from `INKAVA-LOGO.pdf`: rasterize (qlmanage, 5000 px), crop, convert to white
  with alpha via `lut` + `alphamerge`. Never retype the wordmark.

## 3. Buyer-facing structure

- Hook in the first 5 s: say what the system does for the viewer, then go specific.
- Opener = the buyer's question as the headline ("What SFDC does for your order"), three benefit tiles
  (leaner tracked process / know what is on press / fewer delays and mistakes), hand-off line
  ("Here's how it works") into the detailed section. No metrics in the opener; metrics live in the detail.
- Ending after the last proof (QC) = recap of the four figures, then logo + the one-line promise.
- 20 s cut: 5 s benefit, four 3-3.5 s proof points (one number each), 1.5 s logo.

## 4. Two visual identities (do not mix)

| | SFDC | Frame alignment |
|---|---|---|
| Palette | navy `#0B132B`, cyan `#00F0FF`, green `#34C759`, red `#FF3B30` | brand guide: Night Blue `#1E2B4E`, Off-White `#F8F4E9`, Orange `#F37032` (small), Sky `#CFDDF0`, Light Green `#BEDEA4` |
| Fonts | Inter Display + JetBrains Mono (from the user's brief) | Garet Medium (headlines), Garet Regular (body) per brand guide |
| Source | user brief | brand-guidelines.md |

Type scale: the brief's px values were written for 1080p. On 4K use 1.6x (SFDC) or larger. Full-screen
layouts need a bigger scale and a content box below the header and above the progress rule.

## 5. Specific design corrections the user made

- Camera registration marks: **both** cameras show a cross (+), not a cross and a bar.
- Oval press top view: frames are drawn as real screen frames (aluminium edge, blue mesh, two registration
  crosses) and laid out on the two straight runs, following the supplied top-view drawing. Frame
  count varies with the artwork: 8, 12, 14, 16. Animate the change; align 14 one by one.
- Empty areas look broken: if a headline sits at the top and the lower half is blank for the first
  seconds, start it centred and lift it when the next layer arrives.
- Per-frame time and total time are separate claims: session "3-4 h to under 1 h"; per frame
  "15-20 min to 1 min 40 s". Show both. Remove stale derived numbers (52:05 contradicted 1:40/frame).
- Keep supporting claims honest on screen: the opener uses "Prevents..." style wording.

## 6. Voice-over (ElevenLabs)

- Eleven **v4**: audio tags in square brackets, free text emotions (`[warm, confident]`,
  `[soft, gentle, quietly confident]`), pauses as `[brief pause]` / `[long pause]`. **No SSML `<break>`** (that was v2/v3).
- One tag per sentence at most. Tags change delivery only; never rewrite the words.
- "Natural, not pushy": avoid `[emphatic]`/`[proud]` on closing lines; the user asked for gentler endings.
  Use `[calm, warm, conversational]` and an ellipsis instead.
- Spell numbers for TTS ("ninety-nine point eight percent"), initialisms with dots ("E.T.D.").
- Pace estimate 2.75 words/s (about 150 wpm) including pauses; budget roughly 55 words per 20 s.
- Settings that worked for the user: Stability 50, Similarity 75; raise Stability to about 60 if too expressive.
- Poka-yoke is mis-transcribed by Whisper ("poker yoke", "pocket gate") and INKAVA as "in cover";
  that is a transcription artefact; add a Pronunciation Dictionary entry if TTS says "Incava".
- The user generates the audio; after that, **transcribe with word timings and retime the scenes**.
  A local `whisper-cli` with a base-size model is enough for timing; the tiny model is too weak.
- Voice text is written scene by scene so each fact lands when its graphic appears (counter finishing,
  lock turning green, ripple starting). Re-derive per-scene start times from the script before building.

## 7. Music

- User reference: "In Your Arms" (Trevor Kowalski, Epidemic Sound): instrumental, no vocals,
  quiet intro, long build, sustained plateau, gentle resolve. Measured with ffmpeg RMS per 2 s.
  Cannot judge instruments by ear, so say so; tempo estimate about 130 (half-time feel about 65 BPM).
- Prompt template: genre + instruments + BPM + tone, then a **time-coded structure matching the
  video's sections** (intro, build, tension at the poka-yoke lock, restrained climax at QC, calm resolve
  on the logo), then negatives: no vocals, no risers, no whooshes, no SFX, leave mid frequencies free for narration.
- No sound effects anywhere (user: "no whoosh"); the video render has no audio track.
- Don't put artist or track names in the generation prompt. Check licence for commercial use
  (Epidemic, Artlist; CapCut library only if marked commercial).
- Mix: music about -18 to -22 dB under voice or automatic ducking, 1 s fade in, 2 s fade out ending exactly at video end.
- Before writing a music prompt, check whether the supplied video already has a music bed
  (measure RMS in the gaps between sentences; below -60 dBFS means none).

## 8. Remotion and render engineering

- Project: Remotion 4 + React; `src/theme.ts` holds constants, `src/scenes/*.tsx` one file per scene.
  Composition ids per deliverable (one composition per deliverable and length, e.g. a 60 s film, a 20 s cut, a full-screen opener and an ending).
- Easing `cubic-bezier(0.16, 1, 0.3, 1)`, 400 ms transitions (24 frames at 60 fps). Counters use
  fixed-width digits so they do not jitter. Counters should end exactly on the claimed number.
- **macOS: headless Chrome hangs when the display is asleep** (`CVDisplayLinkCreateWithCGDisplay failed`,
  symptom "Waiting for root component to load" delayRender timeout). Fix: a wrapper script that runs
  `chrome-headless-shell --disable-gpu-vsync --disable-frame-rate-limit "$@"` and
  `Config.setBrowserExecutable(path.resolve(process.cwd(), 'chrome-wrapper.sh'))`. Confirmed with a minimal composition.
- Reusing a project: copy `node_modules`, `package.json`, `remotion.config.ts`, `tsconfig.json`, `chrome-wrapper.sh`
  (rewrite its absolute path), then fonts and logo into `public/`.
- Font loading: `FontFace` + `staticFile` with `delayRender`; Inter and Garet from `~/Library/Fonts`, JetBrains Mono via `@remotion/google-fonts`.
- Speed: render stills with `--scale=0.5` in parallel (`&` + `wait`), tile with ffmpeg `hstack/vstack` into one sheet.
- Safe shell: avoid `rm -rf $VAR/*` (blocked); write stills into a new directory. bash 3.2 rejects some
  constructs, so keep commands simple or put them in a script file.
- Final check: `ffprobe` for codec, 3840x2160, 60 fps, `yuv420p`, frame count; pull one frame from the finished MP4 and look at it.

## 9. Collaboration / process

- The user writes in Vietnamese; reply in Vietnamese, keep file names and code in English.
- The user prefers a short list of what changed and why, tables for timelines, and a clear
  "need confirmation" line for facts. Do not ask permission for obvious next steps; do ask before 4K.
- Leader/worker setups (one agent directs and reviews, another executes credit-heavy work through a task queue in the project folder with a git commit per task) are the user's choice; keep one writer per file and verify the diff before accepting.
- Shoot brief (Claude Docs, Vietnamese): overview table, shooting rules (static tripod camera, moving machines only),
  shot list table with timecodes tied to voice lines, B-roll, checklist, delivery naming
  `INKAVA_SFDC_<shot>_T<take>`, and a checklist of figures to confirm with the factory.
- When reusing an edited export as footage, note that burned-in subtitles come with it; ask for or use the clean clips.
