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
