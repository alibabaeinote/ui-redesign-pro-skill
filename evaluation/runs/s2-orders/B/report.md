# Orders screen redesign: management report

Mode EN (English, LTR, Fact: all visible text is English, nav on the left of a left-aligned layout). Redesign, change level 2 (restructure), desktop 1280, interactive. Output: one HTML file. Dark theme and responsive widths below 1280 were not built (deferred).

## 1. Audit: current problems
- P1. Status is hard to read. White text on the badge fills gives 2.78:1 (Paid), 2.16:1 (Pending), 4.23:1 (Refunded) at 11px; the minimum is 4.5:1. Cost: the one field staff scan for is the least legible. Fact (computed).
- P2. Row actions are tiny. View, Refund and Cancel are 12px blue links (4.03:1 on white), no padding, about 15px tall and 6px apart; the floor is 24px. Cost: mis-clicks, and Refund sits next to View with no confirmation. Fact (CSS) / Inference (tall estimate).
- P3. Filtering is slow and hidden. Status is a dropdown: 2 clicks to filter, options not visible. Fact.
- P4. No focal point. A saturated blue Export CSV button (rare task) is the loudest item; the grid has full cell borders on every cell (30 boxed cells); the total is left-aligned so amounts cannot be compared. Fact.
- P5. Weak orientation and low-contrast chrome. Nav has no current-page marker; input borders are 1.61:1; the pager text is 3.4:1. Fact (computed).

## 2. Benchmark
- Shopify Polaris index table: page redirected, could not be read. Not used as a source.
- uxdworld, "Best Practices for Providing Actions in Data Tables" (opened): a few labelled icon actions at the row end. Adopted.
- LogRocket, Pencil & Paper, saasui.design table guides: found by search, not opened, not cited.
- Right-aligned numbers, tinted status pills, horizontal rules only: established practice, not verified as a 3-example trend. Visual galleries not searched.
- Lucide checked on npm (v1.73.0, published 2026-11-14, ISC). Phosphor rejected: last release 2024-03-29.

## 3. Decisions and reasons
| Problem | Decision | Reason | Trade-off |
|---|---|---|---|
| P1 | Tinted pill, dark text plus icon (check, clock, undo) | 6.95, 6.74, 8.19:1; meaning no longer relies on color | Slightly wider badge |
| P2 | 32px View button; Refund/Cancel as quiet labelled actions; click opens inline "Confirm refund / Keep" (Esc cancels) | Target floor 24px met; WCAG 2.2; destructive action separated and undoable | One extra click for Refund/Cancel (an added state, flagged) |
| P3 | Status dropdown replaced by a segmented control, left of the date range | Options visible, 1 click instead of 2 (recognition over recall, Nielsen) | Takes toolbar width; fine at 4 options |
| P4 | Ledger table: horizontal rules only, right-aligned tabular totals, mono order #; Export CSV outlined and moved to the header; Pending rows get a 3px left marker | One focal area; scan and compare amounts; attention goes to pending items | Marker hue is color only, so the Pending text and icon remain |
| P5 | Left rail with icons and a current-page state; 3:1 control borders | Orientation; scalable for more sections | Rail uses 224px |
| Identity choice | Warm neutrals, ink and one blue accent (6.7:1), serif page title | Differentiate from cool-gray admin look | Serif needs a fallback stack |
| Icons | Lucide, one family, 2px at 24, shown at 18/14px | Maintained, free for commercial use, covers all meanings | Stroke is thinner at 14px |

Idea origins (three-version exploration): A ledger table (skeleton), B search-first toolbar (search, segments and date in one row), C queue triage (pending marker, per-row confirm).

## 4. Checks
- Parity: all columns, rows, actions, filters, Export CSV, nav items and paging text remain. Added and flagged: confirm step, disabled Previous, empty state, filtered count text.
- Contrast computed: 0 failures (original: 5 text, 1 border). Target sizes 32px or more (original about 15px).
- Rendered at 1280: no overflow, no external requests, spacing on a 4px scale.
- Estimate (KLM, not measured): status filter 2 clicks to 1.
- Review: self-review only. Search, filter, confirm and empty state were run in a browser.
- Assumption: staff prefer visible segments and a confirm step. Test: 5 users, pass if 4 refund without a mis-click. Fonts shown with fallbacks.

Decision requested: approve level 2 and the added refund confirmation.
