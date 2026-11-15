# Sales overview dashboard: redesign report

Mode EN (English, LTR, desktop 1280). Redesign, change level 2 (restructure). Static layout plus working range selector. Output: one self-contained HTML file, light and dark themes.

## 1. Audit: current problems
(Measured in a real browser at 1280 wide. Fact unless marked.)

- P1. No focal point. Four KPI cards have the same size and weight (24px bold each); Revenue, the main figure, gets no priority. Cost: the user scans four equals to find the answer. (Fact)
- P2. Text and chart contrast fails. 5 text pairs are under 4.5:1: grey labels and month names 2.85, green delta 3.43, red delta 3.96, tab links 3.59. Chart bars are 2.96 (need 3). Cost: small text is hard to read. (Fact)
- P3. The time-range control looks like plain links. 4 targets, 14px tall, no selected state. Cost: the user cannot see which period the numbers show, and the targets are hard to hit. (Fact)
- P4. Deltas depend on color alone, and the comparison window ("vs last period") appears on 1 of 4 cards. Cost: ambiguous meaning for color-blind users and for the other three cards. (Fact; the cost is an Inference)
- P5. The chart has no highlight and the month labels are spaced with non-breaking spaces, so they do not sit under their bars. Top-products rows show numbers only, with no sense of scale. Cost: slow comparison. (Fact)
- P6. The sidebar has no current-page marker and no icons. Cost: weak orientation. (Fact)

## 2. Benchmark
Opened: saasui.design (KPI card patterns), Stripe Apps chart-layout docs, 925studios Stripe dashboard teardown. Not opened: Awwwards, Dribbble, Behance, Muzli (no search results were opened from them, so no trend claim is made from them). Only 2 searches were used.
- Stripe dashboard: a few headline numbers, with the previous period shown beside the value. Adapted.
- Stripe chart guidance: headline value above the chart, same-height charts in a row, 2/3 plus 1/3 split. Adopted.
- saasui.design: separate arrow direction from good-or-bad color; state the comparison window. Adopted (arrow plus color; window kept on the hero card).
- Same source: sparklines and drill-down cards. Rejected: no data, and it would add scope.

## 3. Decisions and reasons
| Problem | Decision | Reason | Trade-off |
|---|---|---|---|
| P1 | Revenue becomes a 44px hero; the other 3 are 28px, in one strip with hairline dividers (no cards) | Hierarchy by scale (Stripe pattern); proximity instead of boxes | Less equal treatment of metrics |
| P2 | New palette, all text at least 5.4:1 in both themes; bars 3.06:1 | WCAG 2.2 AA (1.4.3, 1.4.11) | Muted bars look softer |
| P3 | Segmented radio group, 32px segments, visible selected state, arrow-key support (replaces links) | Recognition over recall (Nielsen); target size | Default "30 days" is an assumption |
| P4 | Arrow icon plus color plus sign; hidden "Up/Down" text for screen readers | Never color alone | None |
| P5 | Highest bar and top product in accent, others muted; labels centered under bars; proportional bars in the list | Focal point and comparison | Accent shows "highest" only |
| P6 | Icons, current-page state, Settings pinned at the bottom | Orientation | Icons add 5 graphics |
| Icons (choice) | Phosphor Bold, MIT license, inline SVG | Covers all 7 meanings; bold weight matches 600 text | Identity choice |

Typeface: Inter Text plus Inter Display (one family, two optical sizes), embedded subset. Identity choice; a more distinctive display face would be a later option.

## 4. Checks
- Parity: all strings, 4 KPIs, 6 bars, 4 products, 5 nav items and 4 ranges are present. Differences: true minus sign (−1.4%) instead of a hyphen; hidden screen-reader text; a selected state added to the range control.
- Contrast: 0 failures (before: 5 text pairs plus bars). Targets under 24px: 0 (before: 4). Text sizes: 6 (before 6). Weights: 3 (before 2).
- Task steps: unchanged (1 click to change range). No time-estimate claim is made.
- Render: no external requests, no horizontal scroll at 1024, 820 and 640 wide; dark theme checked.
- Review: self-review only (no fresh reviewer). Findings: the range control changes only its selection, because the source has no data for other ranges; the chart has no values or axis because the source has none; the accent bar is also marked by a bold month label.
- Assumption to test: the "30 days" default and the readability of an unlabeled chart. Cheapest test: a 5-user test with a threshold of 4 of 5 stating the latest month's rank correctly.
- Out of scope, proposals only: chart values or axis, previous-period comparison on all cards, sparklines, KPI drill-down.

Decision requested: approve this direction so engineering can bind real data to the range selector and chart.
