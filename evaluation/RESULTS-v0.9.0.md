# Evaluation results: v0.9.0 (automated metrics only)

> **Read this first.** This is a small, self-run check, not validation. Baseline screens were written by Claude (synthetic, see `inputs/`). Both conditions were run by Claude subagents (n=5 screens, 1 run each, no repetition). There were **no human raters**; no visual quality was judged. Metrics are automated and measure only contrast, target size, type sizes and text parity. Condition B subagents also self-reviewed and measured themselves during their runs, which the plain-prompt condition did not. Nothing here supports claiming the skill is "better" overall.

Condition A: plain prompt, no skill. Condition B: `ui-redesign-pro/SKILL.md` followed, HTML output, benchmark limited to 3 searches. Measured by `scripts/measure.py` in headless Chrome (1280px for s1-s3, 390px for s4-s5).

## Per screen (orig / A / B)

| Screen | Metric | orig | A | B |
|---|---|---|---|---|
| s1-signup | Contrast failures | 13 | 0 | 0 |
| s1-signup | Targets < 24px | 1 | 1 | 0 |
| s1-signup | Targets < 44px | 7 | 1 | 0 |
| s1-signup | Min font px | 11 | 13 | 14 |
| s1-signup | Distinct font sizes | 5 | 5 | 4 |
| s1-signup | Content parity % | 100.0 | 100.0 | 100.0 |
| s2-orders | Contrast failures | 17 | 0 | 1 |
| s2-orders | Targets < 24px | 5 | 0 | 0 |
| s2-orders | Targets < 44px | 9 | 15 | 23 |
| s2-orders | Min font px | 11 | 12 | 13 |
| s2-orders | Distinct font sizes | 5 | 5 | 6 |
| s2-orders | Content parity % | 100.0 | 97.6 | 97.6 |
| s3-dashboard | Contrast failures | 13 | 0 | 0 |
| s3-dashboard | Targets < 24px | 0 | 0 | 0 |
| s3-dashboard | Targets < 44px | 0 | 9 | 9 |
| s3-dashboard | Min font px | 11 | 11 | 12 |
| s3-dashboard | Distinct font sizes | 6 | 7 | 6 |
| s3-dashboard | Content parity % | 100.0 | 100.0 | 97.2 |
| s4-booking-fa | Contrast failures | 4 | 5 | 2 |
| s4-booking-fa | Targets < 24px | 0 | 0 | 0 |
| s4-booking-fa | Targets < 44px | 1 | 1 | 0 |
| s4-booking-fa | Min font px | 12 | 12 | 13 |
| s4-booking-fa | Distinct font sizes | 4 | 6 | 4 |
| s4-booking-fa | Content parity % | 100.0 | 100.0 | 100.0 |
| s5-onboarding-fa | Contrast failures | 2 | 0 | 0 |
| s5-onboarding-fa | Targets < 24px | 0 | 0 | 0 |
| s5-onboarding-fa | Targets < 44px | 2 | 0 | 3 |
| s5-onboarding-fa | Min font px | 12 | 14 | 15 |
| s5-onboarding-fa | Distinct font sizes | 4 | 4 | 4 |
| s5-onboarding-fa | Content parity % | 100.0 | 100.0 | 100.0 |

## Means across 5 screens

| Metric | orig | A | B |
|---|---|---|---|
| Contrast failures | 9.8 | 1.0 | 0.6 |
| Targets < 24px | 1.2 | 0.2 | 0.0 |
| Targets < 44px | 3.8 | 5.2 | 7.0 |
| Min font px | 11.4 | 12.4 | 13.4 |
| Distinct font sizes | 4.8 | 5.4 | 4.8 |
| Content parity % | 100.0 | 99.5 | 99.0 |

## Observations (not conclusions)

- Both A and B removed most contrast failures on the original screens. On s1 to s3 and s5 neither differs meaningfully from the other on this metric.
- s4 (Persian booking): A has 5 contrast failures against 4 in the original (unavailable-slot text at 2.0:1, which may count as disabled and be exempt under WCAG); B has 2. Small sample, one run.
- B was not better everywhere: on s2 it has 1 contrast failure ("Previous" 3.24:1) and 23 targets under 44px against 15 for A; on s5 it has 3 targets under 44px against 0 for A.
- On targets under 44px, B averaged more (7.0) than A (5.2) and the original (3.8), mostly on dense desktop tables (s2, s3), where small row actions were kept. The skill's own floor is 24px on web, which B met on every screen; 44px is the stricter touch target.
- Content parity: a few strings were not found verbatim (s2 "|" separator, s3 "-1.4%" likely re-typeset with a different minus sign). These are probably formatting differences; not hand-verified.
- Report length: B's `report.md` ran 713 to 808 words for the three English screens against a 350 to 500 word target in the skill. The s5 report could not be written by the subagent and was saved by the coordinator from its returned text (about 480 words in the original).
- Agents reported that benchmarks were thin (2 to 3 searches, no Persian-native teardown opened) and that no independent reviewer was used.

## Limits

- 5 screens, 1 run each, no variance estimate; no statistical test applied.
- Synthetic baselines authored by the same system that ran the conditions.
- Metrics ignore layout quality, hierarchy, usability, typography and Persian text handling. Those need blind human rating (`docs/evaluation-protocol.md`).
- Screenshots are in `out/`. Raw rows are in `out/measurements.csv`.

Version stays 0.9.0. Next step: blind human rating of these 15 outputs, and more screens.
