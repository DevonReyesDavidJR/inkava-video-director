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
