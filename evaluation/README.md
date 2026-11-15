# Evaluation kit

Runs the protocol in `docs/evaluation-protocol.md`: same screens, plain prompt (A) versus this skill (B), blind-rated, with measured items. Nothing here is a result. Results are published only after a real run.

## Steps
1. **Pick 5 screens** you may publish (form, list, dashboard, checkout or booking, onboarding). For each, copy `briefs/_template.md` to `briefs/<screen>.md` and fill it.
2. **Generate outputs.** Same model, same input, same output target. Condition A uses `prompts/condition-a.md`; condition B uses `prompts/condition-b.md`. No manual edits. Save to `runs/<screen>/A/` and `runs/<screen>/B/` (images or exported frames).
3. **Measure** each output with `metrics-template.csv` (contrast failures, target-size violations, steps to main task, competing emphasis levels). Computed values only.
4. **Blind it:** `python3 scripts/blind.py runs/ --seed 7`. It creates `rating-sheet.csv` (labels X or Y, random per screen) and a private `blind-key.csv`. Give raters only the sheet and the images renamed by label.
5. **Rate:** 3 or more designers, `rater-instructions.md`, one filled copy of the sheet each (`ratings-<name>.csv`).
6. **Aggregate:** `python3 scripts/aggregate.py blind-key.csv ratings-*.csv --metrics metrics.csv`.
7. **Publish** scores, raw outputs, instructions, and the limits (sample size, raters, model version).

Self-test of the scripts: `python3 scripts/selftest.py` (uses synthetic data in a temp folder; not a result).
