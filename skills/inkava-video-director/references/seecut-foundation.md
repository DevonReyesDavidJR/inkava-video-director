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
