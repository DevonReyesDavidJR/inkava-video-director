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
