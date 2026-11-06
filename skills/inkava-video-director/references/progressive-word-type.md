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
