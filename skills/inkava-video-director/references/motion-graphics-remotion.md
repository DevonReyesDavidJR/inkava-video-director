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
