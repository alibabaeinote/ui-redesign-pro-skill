# Changelog

## 0.10.0 - 2026-11-15
- **Restructured the method into five stages** (was steps 0 to 13): 1 evaluate current visual usability, 2 list the serious problems, 3 three better and strongly different solutions, 4 choose and combine the best and improve every level, 5 brief defense document. All earlier rules were kept and moved under these stages; section numbers changed (for example old step 13 is now 5.2).
- New: Stage 2 owns the numbered problem list and baseline metrics; each of the three versions must carry a problem map and differ on at least 3 of 5 axes; new 4.3 (raise every level, including microcopy rules) and 4.4 (closure table for every P).
- Changed the Commitment: microcopy wording may be improved when it fixes a numbered problem, meaning unchanged; every changed string is listed.
- Validator now checks the five-stage structure.
- Added `evaluation/` kit (briefs, prompts, blinding and aggregation scripts, self-test in CI) and a first automated A/B run on 5 synthetic screens, metrics only, no human raters: `evaluation/RESULTS-v0.9.0.md`. That run tested the 0.9.0 step structure, not this one.

Format: [Semantic Versioning](https://semver.org). MAJOR = the Commitment (A4) or the output structure changes. MINOR = a new stage, step or rule. PATCH = wording or fixes.

## 0.9.0 - 2026-11-15
First public release candidate. Not yet validated on real projects; stays 0.x until it has been run on at least 3 real screens and the results are published.

- Pipeline: Locale Gate, audit with numbered problems (P1..Pn), live benchmark, three structural versions, best-of-three combination, refinement, pixel-perfect pass, checks, delivery.
- Commitment (A4.1): content, purpose, business goal, audience and functions are locked; original visual style is not carried over unless the brief names it; components and navigation may be replaced by best-practice ones.
- Step 13: one-page management report (audit, benchmark, decisions with reasons, checks).
- Persian (RTL-native) layer, activated only for Persian products.
- Icon and graphics rules (family selection by criteria, pixel-perfect icon rules).
- Added references/pixel-perfect-checklist.md (12 sections).
