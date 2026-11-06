# INKAVA on the SeeCut Foundation

Integration version: 2.0.1. Completed 6 November 2026. Existing plugin identity: `inkava-video-director`. SeeCut upstream revision: `b05d7ed27404a064060e0d370402f562b0c0c02e`.

## What changed

SeeCut is now the bundled execution foundation for rendering, media-inspection calls, transcription orchestration, geometry checks, review and layered preparation. The accumulated INKAVA knowledge controls typography, complete subtitles, brand fonts and palette, original artwork, creative variation, B-roll, motivated effects and offline editing of the existing CapCut draft.

The integration contains 65 skill, helper, dependency and license files. The account plugin contains 69 files including its manifests and README. Its source was read back and the complete account archive was downloaded and compared with the expected files, including the binary supporting asset. The host regenerated compatibility keywords consistently with the portable manifest. Existing plugin identity, owner-private scope and default prompt were preserved.

## Source adaptations

- INKAVA remains the primary discoverable skill. The original SeeCut entry and technical references are retained beneath `upstream/seecut`, with an explicit integration precedence notice.
- An English integration guide and a `scripts/seecut.py` command wrapper connect the foundation to the existing INKAVA knowledge.
- The geometry profile permits intentional negative space and footage without a face. It retains collision and configured face checks, protects specified action regions, and evaluates repeated word instances independently.
- The review prompts use INKAVA criteria. They do not demand bounce, paper, a face, high graphic density, or automatic rejection of legitimate scanning footage.
- Comparison results support a genuine tie. Empty or malformed check lists cannot pass local validation. Permission-denied calls stop as unavailable rather than being accepted as a review.
- Runtime calls retain sandboxing and use a session-scoped proceed-in-sandbox policy. No global account permission rules were changed. Source inspection and installation do not establish native CapCut compatibility.

## Verification performed

| Check | Observed result |
|---|---|
| Dependency discovery | Node, FFmpeg/ffprobe, Antigravity CLI, HyperFrames, Playwright Core and faster-whisper available |
| Isolated runtime | Prepared under `~/.local/share/inkava-seecut`; Python and Node dependencies kept separate from global packages |
| Rendering | Synthetic one-second and five-second compositions produced 10 and 50 frames; distinct frame hashes and an inspected rendered frame confirmed output |
| Process profile | Clean composition with a footage wrapper and no face metadata passed |
| Repeated words | Two instances were independently detected at 0.20 and 0.60 seconds |
| Protected action | An intentionally obstructing text layer correctly failed |
| Comparison tie | A deterministic local response fixture preserved a tie in both orders; this was not an independent AI aesthetic comparison |
| Output validation | Empty check lists and malformed comparison output were rejected |
| Text-only service call | Returned OK |
| Media-content call | Returned the visible words and background; missed subtle movement in a one-second test, so this did not establish reliable temporal judgment |
| Complete AI review | Not validated: headless command permission was denied, and other attempts timed out. No failed or unavailable call was reported as a completed review |
| Packaging and installation | Skill validation passed; portable archives rebuilt; all local installed files matched the canonical skill; existing discovery symlink preserved |
| Actual CapCut edit | Not performed for this installation; no existing draft was opened or changed |

The account's Antigravity auto mode was unavailable. The supported sandbox policy was tried without altering global permission settings. Completing the automated review stage requires resolving the service's specific permission requirement and then checking a real valid media-review result. The integration is installed; an end-to-end production-quality review loop is not yet proven.

## Native draft and license boundaries

The source's layered-plan vocabulary targets JianYing. No separate JianYing engine was installed, and the integration does not create or register a replacement project automatically. The user's workflow remains direct edits to the existing CapCut draft while CapCut is closed, using a verified route for that actual version. A PNG text layer is not editable native text; a rendered external preview is not proof of a native export.

The bundled SeeCut material declares PolyForm Noncommercial 1.0.0. Its license, required copyright notice, third-party notices, modification record, Apache license and font OFL are included. Installation does not grant commercial rights. The upstream supporting font is not an INKAVA brand font. No example videos, source frames, model weights, runtime account credentials or API secrets are packaged.

## Primary sources

- [SeeCut overview](https://github.com/YeJe-cpu/SeeCut/blob/b05d7ed27404a064060e0d370402f562b0c0c02e/README.en.md)
- [SeeCut license](https://github.com/YeJe-cpu/SeeCut/blob/b05d7ed27404a064060e0d370402f562b0c0c02e/LICENSE)
- [Third-party notices](https://github.com/YeJe-cpu/SeeCut/blob/b05d7ed27404a064060e0d370402f562b0c0c02e/NOTICE)
- [JianYing integration scope](https://github.com/YeJe-cpu/SeeCut/blob/b05d7ed27404a064060e0d370402f562b0c0c02e/jianying/README.md)
- [Antigravity execution and permission settings](https://antigravity.google/docs/agent-settings)
