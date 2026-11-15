# Contributing

Thank you for helping improve UI Redesign Pro. This is a text-based skill, so a contribution is a change to instructions, not code. Small, evidence-backed changes are preferred.

## What makes a good change
- **A real failure.** Describe a screen or brief where the skill produced a poor or contradictory result, and what the output should have been.
- **One rule, one place.** Do not duplicate a rule in two sections. If two rules collide, fix the precedence (A3) instead of adding an exception.
- **Measurable wording.** Prefer a number, a count or a test ("at least 3:1", "at most 5 problems") to an adjective ("modern", "clean").
- **Honest sourcing.** Cite only sources you opened. Mark heuristics as heuristics.

## Workflow
1. Open an issue using the bug or feature template.
2. Fork, branch, and edit `ui-redesign-pro/SKILL.md` or a file in `references/`.
3. Run `python3 scripts/validate.py` (the same check runs in CI).
4. Add a line to `CHANGELOG.md` under "Unreleased" and pick the bump: MAJOR (the Commitment in A4 or the output structure changes), MINOR (new step or rule), PATCH (wording, fixes).
5. Open a pull request using the template.

## Conventions
- Keep the one-voice rule (A2): quieter, clearer, more exact wins.
- Do not add personal information, client names or private URLs.
- Persian text: keep numerals Latin, put Latin terms in parentheses after the Persian equivalent.
