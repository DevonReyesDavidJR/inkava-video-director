# INKAVA Integration Modifications

Upstream: YeJe-cpu/SeeCut, revision b05d7ed27404a064060e0d370402f562b0c0c02e, inspected and adapted 6 November 2026. The original LICENSE and NOTICE accompany this copy. Required Notice: Copyright (c) 2026 YeJe-cpu (https://github.com/YeJe-cpu).

- Renamed the original skill entry to UPSTREAM_SKILL.md to retain one discoverable primary INKAVA skill. Added a precedence notice to that document and the original governing reference.
- Added an INKAVA geometry profile, protected action intervals, and word-instance timing so repeated words are evaluated independently. Face metadata is required only for the configured face-protection path, rather than every footage wrapper. Kept collision, annotation, applicable face protection and opt-in spring checks.
- Replaced unrestricted permission-bypass flags in agent calls with sandboxed calls with the session-scoped proceed-in-sandbox policy. Actual media-ingestion capability still requires verification.
- Added English INKAVA check and comparison prompts and routed the review helper to them. Original prompts remain for provenance. Added genuine tie support to the comparison schema and verdict mapping. The service returns JSON as text, with required fields and verdict types validated locally, rather than requiring its response-schema tool. An empty or incomplete check list cannot pass; retries are bounded to two attempts. Permission-denied review calls stop without being treated as valid output or retried as transient content failures.
- Added the separately obtained Apache 2.0 license text for the bundled HyperFrames-derived helpers and the Caveat font's OFL text. These assets retain their own terms and are not INKAVA brand defaults.

The original technical references are retained in their source language. The primary integration guide, direction and user-facing operating instructions are English. This package does not include source example videos, demo frames, runtime accounts, model weights, or the external JianYing draft engine.
