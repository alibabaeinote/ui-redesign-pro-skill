# Signup screen redesign: management report

Setup: English, LTR (Mode EN), Change level 2 (Restructure), interactive, one self-contained HTML file. Contrast and sizes below are computed from the code; layout was rendered in Chrome at 1280 and 390, light and dark.

## 1. Audit: current problems
- P1. Text and borders are too faint. 8 text or border pairs fail (labels, subtitle and links #888 = 3.54:1; hint #aaa = 2.32:1; input border #ccc = 1.61:1; white button text = 4.03:1). Users read the form with effort and may not see where fields end. Fact.
- P2. Controls are small. Inputs are 32px high with 13px text, the button is 36px, and labels and hints are 11 to 12px. Misses on touch, and iOS zooms into 13px inputs. Fact.
- P3. The fast path is buried. "Continue with Google" is the last item, a small grey link under the button, after 7 controls. Fact. Likely lowers use of the one-click route (Inference).
- P4. Weak form components. Company size is a dropdown for 4 options (2 taps, options hidden). The password has no show option and its rule is a faint hint. Terms is a bare 12px checkbox. No error states exist. Fact.
- P5. No focal point. Title (22px) and button have almost equal weight to labels; a grey card floats on a grey page. 1 flat level of emphasis. Inference.

## 2. Benchmark
- UX Planet, "10 best practices for sign-up forms" (opened): adopted social login, password rules shown up front, show/hide password, inline validation, a descriptive button label.
- Formsort, "10 SaaS signup flows" (opened): all 10 require a password; free-tier products collect no card. Adopted: keep fields minimal. Rejected: breached-password check and email verification (new scope, listed below).
- Other search results (Mobbin-style libraries, Awwwards, saasui.design and similar) were only listed in search, not opened, so they are not claimed as evidence.
- Split-screen layout and a 14-segment trial motif were not verified as a trend. They are my decisions (Assumption).

## 3. Decisions and reasons
| Fixes | Decision | Reason | Trade-off |
|---|---|---|---|
| P3 | Google button first, then "or" divider | Faster route first; benchmark above | Weighs email path slightly lower |
| P4 | Company size: select becomes 4-option segmented control (1-10 stays preselected) | All options visible, 1 tap instead of 2 | Breaks if options grow past about 5 |
| P4 | Password: show/hide toggle, rule shown below with a check when met | UX Planet practices 5 and 6 | One added control |
| P4 | Inline errors on blur and submit; focus moves to first error | Error recovery; Nielsen heuristic 9 | Added error copy |
| P2 | 48px controls, 16px input text, 44px targets | Ergonomics; no iOS zoom | Form is taller (needs scroll under about 840px height) |
| P1 | Text at least 5.95:1, control borders at least 3.55:1 | WCAG 1.4.3 and 1.4.11 | None |
| P5 | Split layout: dark panel holds title and trial promise, form on warm paper | One focal point; green accent used only for primary action, selection and focus | Left panel carries no new information |
Identity choices (not usability gains): serif display title with system sans body (no webfonts, so zero external requests; the serif falls back by platform), deep green accent, warm neutrals, and a decorative 14-tick strip. Icons: Phosphor Bold (MIT, maintained, covers eye, eye-slash, check, warning, Google), one family, inline SVG, currentColor.

## 4. Checks
- Parity: every string, field and action is kept. Changed: Google moved to the top and became a button; the subtitle is split into two lines (same words); Terms and Privacy Policy became links (href="#").
- Added states (flagged): errors, valid-hint, loading, "Account created", password toggle.
- Contrast (computed): 0 failures in light and dark, versus 8 before.
- Targets: all at least 44px (before: 32px and 36px). Smallest text 14px (before 11px).
- Main task: 4 text fields, 1 checkbox, 1 click, same count as before (default size kept). Time estimate not computed.
- Review: self-review only, no independent reviewer. It caught and fixed a checkbox overlay that blocked clicks. Not done: colour-vision simulation, real-device test, webfont rendering.
- Out-of-scope proposals: breached-password check, email verification, workspace name, a real Google flow.
- Assumption to test: Google-first raises sign-up completion. Cheapest test: A/B on completion rate, or 5 users with an 80% success threshold.

Decision requested: approve this direction, including the added states, so it can go to build.
