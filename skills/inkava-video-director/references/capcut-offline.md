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
