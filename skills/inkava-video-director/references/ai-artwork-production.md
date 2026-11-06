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
