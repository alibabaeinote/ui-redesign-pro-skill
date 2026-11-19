---
name: "ui-redesign-pro"
description: "Designs new UI or redesigns screens (Persian RTL-native or LTR) in five stages: evaluate current visual usability, list serious problems, generate three strongly different solutions, combine the best and improve every level, then write a short management defense document."
---

# UI Redesign Pro (formerly Pixel Perfect UI / modern-ui-design)

Note: if the `references/` files named below are not available in this skill, apply the same rules from the text itself and say so once.

## How to use this skill

**Two modes, one method.**
- **New design:** nothing exists yet. Start from a brief.
- **Redesign:** screens already exist. Start from an evaluation. The Commitment (A4.1) applies: content meaning, purpose, business goal, audience and every function stay; visual style, layout, components, navigation and microcopy wording are redesigned.

**The five stages (the whole method, always in this order):**

| Stage | Name | What it produces |
|---|---|---|
| 1 | Evaluate the current visual usability | Locale record, change level, Content and Function Inventory, evaluation of the current screens |
| 2 | List the serious problems | Numbered problems P1 to Pn with evidence, severity and baseline metrics |
| 3 | Three better, strongly different solutions | Benchmark and playbook, then three versions, each mapped to the problems it solves |
| 4 | Choose and combine the best, improve every level | One combined version, refined on every level, every problem closed, built, checked |
| 5 | Brief defense document | The management report that defends the new version |

New design has no current screens: Stage 1 becomes the brief, Stage 2 becomes "brief and risks" (the user problem, constraints, the 3 biggest design risks), and the rest is unchanged.

**Parts:** A Principles, then Stages 1 to 5, H Persian layer (only in Persian RTL projects), I Appendix (tools, design-system file, starting palette, references).

Skip steps that are truly irrelevant (a single icon needs no trend search). Never skip the research, the final pass or the management report just to save time.

**Artifacts this skill produces, in order** (new design skips the evaluation items):
1. Locale record (1.1) and change level with interaction mode (1.2).
2. Content and Function Inventory and the evaluation (1.3).
3. Numbered problems P1 to Pn and baseline metrics (Stage 2).
4. Benchmark, screen-type playbook, then three versions (Stage 3).
5. The combined version, then the refined final with a component, navigation and copy change log (4.1 to 4.7).
6. `design-system.md` (4.6, Part I).
7. Spacing table (4.8), Parity Check, before and after metrics, review notes (4.9).
8. Management report (5.2).

---

# Part A. Principles

## A1. Why this skill exists

Default AI output has a dated look: purple-blue gradients, one font everywhere, identical rounded cards with shadows, emoji as icons, centered hero plus three cards. The fix is what a real designer does: look at current work, ground choices in tested systems, and decide type and color on purpose. The first layout that comes to mind is the most common one, so the method has two movements inside the five stages: **diverge** (Stage 3: three strongly different solutions) and **converge** (Stage 4: combine the best, then rework hard for usability). Never skip converge because diverge looked good.

## A2. One voice

Everything speaks as: **refined, hierarchical, gestalt-driven, pixel-perfect**. When two valid choices compete, pick the quieter, clearer, more exact one.

- **Refined:** few colors, weights and shapes. Contrast comes from scale and tone, not decoration. A detail stays only if it carries meaning or identity. **Quiet means fewer elements, never paler ones.** Tonal-on-tonal pastel (a tint on a tint, a thin pale icon on a pale panel) is a defect, not refinement: every card keeps one strong anchor (a dark or saturated value) that the eye can lock onto. Contrast floors (4.2 item 6) always beat the preference for quiet.
- **Hierarchical:** one focal point, one primary action, ordered secondary and tertiary levels. Visual weight matches importance.
- **Gestalt:** organize by proximity first (gaps inside a group smaller than gaps between groups), then similarity, common region (a container only where proximity fails), alignment, figure/ground, closure, simplicity.
- **Pixel-perfect:** every value comes from a scale, every size is proportionate to siblings and screen, and it is checked at real size.

## A3. Order of authority

The skeleton (screen organization, grouping, navigation model, component set) is free only in Stage 3 and in 4.1. From 4.2 the skeleton is fixed and later steps refine it, with one exception: 4.2 item 8 may swap or redesign individual components inside the skeleton.

**Precedence when rules collide:** (1) the user's brief and pinned constraints, (2) the Commitment and honesty (A4), (3) accessibility and ergonomic floors (4.2), (4) the later step over the earlier one, (5) the quieter, clearer, more exact option (A2).

## A4. Contract (redesign mode, and honesty in both modes)

1. **Commitment (redesign).**
   - **Locked, never changed:** the topic and the meaning of the content (facts, data fields, numbers, legal text, media meaning), the screen's purpose, the business goal, the audience, and every capability inside the UI (each function, state and action must still exist and work).
   - **Not carried over by default:** the original visual style. Nothing of its palette, typography, shape language, icon style, imagery or decoration is kept unless the brief names it (a brand guideline, "keep the colors", "keep the font"). A named item is a constraint; everything else gets a new, deliberate visual language.
   - **Improved on purpose:** layout, grid, hierarchy, motion, the wording of microcopy under 4.3 (labels, buttons, hints, errors, empty states; meaning unchanged), and the components and navigation themselves. Where usability, learnability or navigation gets better, redesign a component or replace it with a better best-practice one (for example a long dropdown with a searchable combobox, a chain of modals with a stepper, a hidden gesture with a visible control, an overloaded tab bar with grouped navigation). The function it serves stays, and it must not become harder to reach for frequent tasks. Record every replacement and every reworded string with the problem it fixes (P-number) and, for components, its best-practice source.
2. **No silent changes (redesign).** Before designing, build a **Content and Function Inventory** (every string, control, data field, state, action, icon meaning, link). After designing, run a **Parity Check** against it. The check covers content and functions, not components: a replaced component passes when every function it carried is still present and reachable. Anything added, removed or merged is listed and justified; the default is not to do it. Reworded strings are allowed only as microcopy under 4.3, each listed with before, after and the P-number it fixes. Valuable ideas that change scope go to an "Out-of-scope opportunities" list, never into the design. Technical necessities (a missing focus, error, empty or loading state) may be added as flagged state variants.
3. **Honesty (both modes).** Label claims as Fact (seen in the UI), Inference (reasoned) or Assumption (needs validation). Never claim testing or analytics you do not have. Estimates are labeled as estimates. Cite sources for research.
4. **Questions.** Ask at most one blocking question, once, before work starts, combining the locale, change level, output target and any real blocker. After work starts, do not ask: state the assumption in one line and proceed.
5. **Communication.** Reply in the user's language and follow their saved formatting preferences.

## A5. Working method

- Run the Locale Gate (1.1) first, then calibrate (1.2: Change Dial, interaction mode, output). Start with one sentence saying what you are about to do. Combine the Locale Gate, Change Dial and any real blocker into the single allowed question; otherwise proceed with stated assumptions.
- **Several screens:** design the system once, then apply it across all screens. Treat the set as one flow, with the same tokens, components and patterns.
- **User constraints** (keep brand colors, keep the font, target stack, deadline) override this skill's defaults, except the Commitment, no silent changes, honesty and the one-question limit in A4.
- Commit to one direction after exploration and explain it. Show several finalists only when the choice truly depends on the user's preference.

---

# Stage 1. Evaluate the current visual usability

Redesign: judge what exists, in numbers and facts, not taste. New design: this stage is the brief.

## 1.1 Locale Gate (first, before reading the screens for meaning)

Record the language and direction of the product as a Fact with evidence: script of the visible text, where the layout anchors, where navigation, back and primary actions sit, digit style, calendar (Jalali or Gregorian), any user statement.

- The **primary UI language** is decided by the interface chrome and the main content, not by a few embedded brand names. Mixed products: the primary language sets the mode; the secondary language is embedded content handled correctly.
- If evidence is genuinely split, fold the question into the single blocking question (A4.4); otherwise state the assumption.
- **Mode FA** (Persian, RTL-native): conceive, compose and judge as a Persian product from the first sketch. Part H is active in full.
- **Mode EN** (English or any LTR language): Part H stays dormant.
- Hard rule: never conceive an LTR design first and convert it afterwards. In Mode EN do not add RTL considerations the original does not contain.

## 1.2 Calibrate and choose the output

- **Change Dial (redesign), how far structure and components may change:** (1) Refine: keep the structure and upgrade components only where the evaluation shows a usability problem; (2) Restructure: also improve layout, grouping and navigation; (3) Rebuild: new composition, new component set and new navigation model wherever best practice supports it. At every level the content, purpose, business goal, audience and functions stay identical, and the visual style is newly designed unless the brief pins it (see A4). Take it from the user; otherwise recommend one with a reason inside the single allowed question; if no answer is possible, default to level 2 and say so.
- **Interaction mode:** static is fine for presentational screens. **Interactive is required** when there is input or validation; toggles, tabs, filters, sorting, search, selection, steppers or carousels; overlays; state transitions; scroll-linked behavior; multi-step flows; meaningful motion; or the user asks. When in doubt, choose interactive.
- **Output target:**
  - **Figma** (default for users who work in Figma, and always for redesign unless told otherwise): build in Figma using the Figma tools and the `figma-use` and `figma-generate-design` skills. If Figma tools fail, say so plainly and offer to retry; do not silently switch format.
  - **Interactive web UI:** one self-contained HTML or React artifact. For award-level marketing sites also consult `top-design`; for a theme across several artifacts, `theme-factory`.
  - **Static graphic:** `canvas-design`, `pdf` or `pptx`, passing the decided palette, type pairing and layout motif.
  - If unclear, infer from the wording and state the assumption (or fold it into the single question in A4.4).

## 1.3 Evaluate the current design (or frame the brief)

Write a few lines before anything else.

- **Redesign:** the user's main task on this screen; what must stay; the Content and Function Inventory; the evaluation of the current visual usability, through the lenses below (hierarchy and focal point, noise, weight inversions, contrast, inconsistent details, missing states). Be factual: compute contrast, count competing focal points. Turning the findings into numbered problems is Stage 2.
- **New design:** who uses it and when, the one task, the primary action, real content (or [placeholders], never lorem), constraints (platform, brand, script and direction), what should be clear in 3 seconds.
- **Both:** a state list (default or empty, loading, error, success, disabled, plus screen-specific ones). Design the default state first.
- **Understand the context** in a few lines: product and domain, platform and primary viewport, screen type (and its best practices and typical mistakes), 2 to 4 likely user segments, the task and its frequency, where the screen sits in the flow, probable business metrics and the design levers for each, constraints (brand, regulation, trust).
- Evaluation lenses: Nielsen heuristics, learnability and discoverability (recognition over recall, visible labels, consistent patterns, first-use guidance), navigation and information architecture (findability, depth, orientation: where am I, where can I go, how do I go back), component fitness (is each component the best-practice choice for its job), cognitive load (Hick, Miller, progressive disclosure), ergonomics (Fitts, thumb zones for the real reading hand, target sizes), accessibility, dark patterns in payment and consent flows, visual craft, component reuse. Also evaluate the copy (clarity, consistency, tone, error, empty and help text). Mode FA adds: Persian typography problems, digit inconsistency, broken embedded Latin, left-biased composition inherited from Latin conventions.

If the request cannot fill this, take the most reasonable assumption, state it in one line, and go on.

---

# Stage 2. List the serious problems

Turn the evaluation into a short, ranked, numbered list. This list is the contract for every later decision.

1. **Number every problem** (P1, P2, ...). Each gets: a one-line statement, a **measured evidence line** (a number, a count, a ratio, a step count), its effect on the user's task or the business, a **severity** (critical, major, minor) and a label of Fact, Inference or Assumption.
2. **What counts as serious:** anything that blocks or slows the main task, hides the primary action, breaks accessibility floors, confuses navigation or learnability, or damages trust in payment and consent flows. Cosmetic taste is not a problem unless it hurts one of these; label it "identity or brand choice" instead.
3. **Order by severity.** Group duplicates. Keep minor items on a short "also noticed" line.
4. **Screen-type failure modes.** Classify each screen (checkout, dashboard, form, list, onboarding, settings, detail, search, and so on) and check the 3 to 5 common failure modes of that type from established guidance. Stage 3 later completes the playbook with proven practices.
5. **Baseline metrics (redesign).** Capture the measurable items in a table now, so 4.9 can show before and after: competing emphasis levels, distinct sizes, weights and colors, primary-action prominence and reachability, target-size violations, contrast failures, elements and decisions per view, steps and taps for the main task.
6. **New design mode:** write "brief and risks" instead: the user problem, the constraints, the success criteria and the 3 biggest design risks.

The management report (5.2) and every decision in Stages 3 and 4 refer to these P-numbers. Numbers may skip in the final report, but never get reused.

---

# Stage 3. Three better, strongly different solutions

Research first, then diverge. Nothing here is the final design.

## 3.1 Benchmark current design (live, never from memory)

Two separate lookups:
- **Aesthetic trends:** newest work for this exact screen type on Awwwards, Dribbble, Behance, Muzli. See `references/trend-research.md`.
- **Functional patterns:** teardowns and case studies of shipped products for this flow, with 3 to 5 real products of the same category in the same market. Mode FA: prioritize products designed natively in Persian or Arabic; treat translated Latin references only as sources of principles. See `references/pattern-libraries.md`.

Rules:
- Use only sources you can actually open. If one needs a login, a paid plan or is blocked, say so in one line and switch to web search for teardowns and write-ups. Do not retry a blocked source.
- A pattern counts as a trend only if it appears in at least 3 credible examples and serves the user's task. Fewer means label it "single example, not a trend".
- Extract principles and moves, not layouts. Never clone a shot or brand; never reproduce a known brand's identity or characters.
- Deliver a short benchmark: per source its recency, 2 to 3 repeating patterns, and which you adopt, adapt or reject and why. Never present memory as a fresh benchmark.
- **Screen-type playbook.** For each screen type classified in Stage 2, write 5 to 8 proven practices (and extend its 3 to 5 failure modes), from the benchmark and established guidance, and apply them unless the original's content makes them impossible. Examples: checkout cuts fields, shows the total and trust cues early, and keeps the primary action reachable; a dashboard leads with the one key number, supports comparison and drill-down, and avoids chart junk; a form uses a single column, inline validation and clear error recovery; a list supports scanning with one consistent row anatomy. Feed the playbook into the decisions table of the management report (5.2).
- Define one **signature idea**: a single product-specific visual or interaction concept (a type treatment, shape language, motion motif), justified by user value and kept systematic so it scales.

## 3.2 Diverge: three versions, freely

Produce three better versions that differ **strongly in structure**: they must differ on at least 3 of these 5 axes: organization and grouping, navigation or flow model, component set, primary interaction, information density. Three recolors or restyles of one skeleton count as one version. At Change Dial level 1, directions may be narrower variations of the refinement strategy.

- Leave common patterns behind (card grids, tab bars, hero plus three cards, stacked forms). Do not treat any design system's component set as a boundary here.
- Each version gets a one-line concept (for example search-first, timeline, one dominant action), a hypothesis for why it could serve the user, and a **problem map**: which of P1 to Pn it solves and how. Every version must address every critical and major problem.
- Keep content and core functions identical across versions and draw the default state in all three. Use real content from the original, never lorem.
- Give each a type and color direction (read `references/typography-color.md` first), at enough fidelity to judge structure, hierarchy and feel.
- Build them quickly on an Explorations page or side by side. Score each against: problems closed (of P1 to Pn), fit to users and tasks, hierarchy clarity, ergonomics, distinctiveness, typographic fit for the script, buildability, risk.

---

# Stage 4. Choose and combine the best, improve every level

Pick the strongest ideas, merge them into one design, raise every level, close every problem, then build and verify. From 4.2 the skeleton is fixed (A3).

## 4.1 Combine the best of the three (the main deliverable)

The goal is to harvest, not to crown one winner. For each version list its 1 to 2 best ideas and its weaknesses. Compose **one combined version** that keeps the strongest ideas of all three and drops their weaknesses.

- Start from the version that closes the most problems and best fits the user's main task as the skeleton, then bring in the strongest parts of the others.
- Name each borrowed idea's origin (for example "price block from A, progress rail from C").
- Check the seams: one voice, one focal point, one primary action, no leftover joints, and that the combination still closes every critical and major problem.
- Decide and explain in 2 to 3 sentences, and record why alternatives were rejected. Show finalists only when the choice truly depends on the user's preference and the criteria cannot settle it.
- The combined version must visibly draw on all three. Picking one version and borrowing a detail does not satisfy this step. Only the combined version is developed to full fidelity.

## 4.2 Converge: refine the combined version for usability

In this order, and write down what changed:

1. **Simplify.** Remove decoration, redundant labels, extra borders, dividers and shadows, duplicate actions. Test: remove it; if nothing gets worse, it stays removed.
2. **Clarify attention.** One focal point, one primary action. Run the squint test and the 3-second test.
3. **Re-weigh.** Visual weight must match importance. Fix inversions (decoration louder than the primary action, secondary text as heavy as headings).
4. **Recognizable components.** Buttons look like buttons, inputs like inputs; default, selected, disabled and focus states are distinct. Unclear icons get labels.
5. **Legibility and scanning.** Readable sizes and line-height, short lines (about 45 to 75 characters), aligned edges, grouping by space, key data (numbers, status, dates, prices) prominent.
6. **Contrast, computed for text AND shapes** with the tool in Part I, on every pair including surfaces. Primary text and key actions 7:1 or more; secondary text at least 4.5:1; icons, control borders, focus rings and the fill of anything the user must find (play button, avatar, badge, bookmark) at least 3:1 against what is directly behind them. Surface steps (card on page, panel on card, chip on card): either a fill step of at least 1.25:1 or a 1px border; any tonal-on-tonal pair under 1.15:1 counts as invisible and must be fixed, not defended as subtle. Decorative hairlines may be lighter but must not carry meaning and stay visible (at least 1.3:1 to their surface). Never rely on color alone. Sample the colors from the rendered screenshot, not only from the token values.
7. **Ergonomics.** Targets at least 44x44pt (iOS), 48x48dp (Android) or 24x24 CSS px (WCAG 2.2 AA floor), larger for primary actions; spacing between targets; one-hand reach; destructive actions separated and confirmed or undoable.
8. **Component and navigation upgrade (inside the fixed skeleton).** Swap or redesign components and local navigation paths without changing the skeleton chosen in 4.1. If you find a skeleton-level problem, go back to 4.1 once, fix it there, and continue. For each component and each navigation path ask: is this the best-practice choice for its job? Redesign or replace it when a numbered problem justifies it (usability, learnability, findability). Check that every function is still reachable, that frequent tasks take no more steps than before (count them), that labels are visible and first-use guidance exists where learnability was weak, and that navigation answers where am I, where can I go and how do I go back. Record each replacement as before, after, reason and source (for example Nielsen, WCAG, Material, HIG, Baymard); cite only sources you opened.

## 4.3 Raise every level

4.2 is the usability core. This step checks that nothing else was left behind. Walk each level, write one or two lines of what changed, and fix any level that is still at the original's quality.

| Level | What to raise | Where the rules live |
|---|---|---|
| Visual | Hierarchy, one focal point, simplicity, balance, signature idea | 4.2 items 1 to 5, A2, 4.8 |
| Usability and learnability | Fewer steps, clear paths, recognition over recall, first-use guidance, error recovery | 4.2 item 8 |
| Interaction | Every state, feedback, validation, motion with a purpose, reduced-motion | 4.2 item 4, 4.6 (Motion), 4.7 |
| Copy (microcopy) | See the rules below | below |
| Design system | Tokens, components, one family of icons and graphics | 4.5, 4.6 |
| Ergonomics | Targets, spacing between targets, reach, destructive actions | 4.2 item 7 |
| Accessibility | Contrast, focus, names, color not alone, text scaling | 4.2 item 6, 4.9 |
| Aesthetics | Type and color with intent, craft details, no "AI look" clichés | 4.6, 4.8, `references/trend-research.md` |

**Copy rules.** Improve the wording, never the meaning.
- Allowed when a string fails a numbered problem or is inconsistent: clearer and shorter labels, buttons that name the action (a verb), one term for one thing, helpful error, empty and hint text, a consistent voice.
- Never changed: facts, numbers, data values, names, legal or regulatory text, anything whose meaning could shift. If unsure, keep the original and list it under out-of-scope opportunities.
- Every changed or new string goes into the Parity Check with before, after, reason and P-number. New strings for added states (error, empty, loading) are flagged as new.
- Mode FA: natural Persian, not translation from English; follow Part H for digits, punctuation and embedded Latin.

## 4.4 Close the problems (traceability)

Write a closure table for every P: **P-number | fix (version or step that solves it) | evidence after (number or check) | status** (closed, partly closed, open with reason). A critical or major problem may not stay open without a stated reason and a next step. Any decision that matches no problem is labeled "identity or brand choice". Add anything new the redesign introduced and its mitigation (a regression is reported, not hidden).

## 4.5 Ground in an established system

After converging, harden spacing, states, touch targets and tokens with `references/design-systems.md` (Material 3, Apple HIG, shadcn/Radix, Carbon, Polaris, Primer, Atlassian, Fluent 2). This hardens the structure; it must not pull it back toward the template. Platform fit: HIG for iOS, Material 3 for Android, WCAG and responsive conventions for web; deviate only with a reason.

## 4.6 Type, color and the design system

Create a new design system for the redesign unless the user says to follow the current one (then treat its tokens as constraints and improve within them). Read `references/typography-color.md` first.

- **Tokens:** primitives, then semantic, then component tokens, named by role (color/text/primary, space/stack/md), DTCG-compatible so they export to Figma Variables, CSS custom properties, Tailwind and native tokens.
- **Color:** one dominant neutral, one supporting neutral, one confident accent (60-30-10), tonal scales (OKLCH is a good space to build them), semantic colors, surface layers, interactive states, light and dark themes with equal care. Verify every pair with the contrast tool. Never rely on color alone.
- **Type:** pair a distinctive display face with a restrained body face; define roles (display, headline, title, body, label, caption, numeric), a real scale (ratio about 1.2 to 1.33), line-height and weight per role, with properly licensed fonts and script coverage for every language in the product.
- **Spacing, shape, elevation:** one base unit (4 or 8) with a small named scale; micro, component, group and section tiers; radius tied to component size (nested radius equals outer radius minus padding); one coherent shadow recipe; a focus-ring spec.
- **Icons and graphics:** follow the rules below.

  **Choose one icon family, once, by criteria (never by taste):**
  1. Follow the brand guideline only if the brief names it (for example a stated Phosphor Bold). The original product's own icon style is not kept by default (A4.1). Otherwise choose from the list below.
  2. Credible, maintained sources: Phosphor, Lucide, Tabler, Material Symbols, SF Symbols (Apple platforms), Fluent System Icons, Carbon, Radix Icons, Iconoir, Streamline (use the Streamline connector when it is in the session, to search and download the real file instead of guessing names).
  3. Criteria: active maintenance (a release in the last 12 months), a license that allows commercial use (record it), several weights or styles (for example Regular, Bold, Fill) on one grid, and coverage of every meaning in the Content and Function Inventory inside that single family.
  4. Style fits the benchmark: look at which style (outline, fill, duotone) the 3 to 5 comparable products use and justify the choice in one line. Trendy is allowed only when the pattern passed the 3-example rule in 3.1; otherwise prefer plain and timeless. Simple, geometric and quiet beats decorative.
  5. Never mix families, never use emoji as icons, and never hand-draw an icon with SVG when a family has it. If a needed meaning is missing, draw it on the same grid, keyline, stroke and corner rules, and flag it as custom.

  **Pixel-perfect icon rules:**
  - Grid and live area: 24px base with about 2px padding (20px live area); 20px and 16px sizes use their own optical versions or the family's small set, never a scaled-down 24px icon.
  - Stroke: one weight across the product (1.5px or 2px at 24px; about 1.25 to 1.5px at 16px). Match icon weight to the text weight beside it: regular text with regular icons, bold text with bold icons. Caps and joins are the same everywhere and echo the typeface's terminals; corner radius echoes the component radius family.
  - Snap to the pixel grid: integer coordinates, and half-pixel offsets for odd stroke widths so lines are not blurry. Check at 1x, 2x and 3x.
  - Size and alignment: icon about 1.0 to 1.3 times the label size, centered on the text's visual mass (cap-height or x-height), not the line box; a 24px icon sits inside a separate 44px (or 48dp) touch target. In Persian, center on the glyph mass and mirror directional icons per the direction table in Part H.
  - Color and states: color comes only from semantic tokens (use currentColor in SVG, no hardcoded fills); the selected state uses the family's fill or bold variant, never a different family; icon-only controls carry an accessible name, and unclear icons get a visible label.
  - Delivery: SVG with a viewBox, optimized, named by role (icon/arrow/start), one sprite or component set, plus a license note in the handoff.

  **Graphics, illustration and imagery:**
  - One visual language per product: shape language tied to the radius tokens, a palette made only of existing color tokens and their tints (at most 3 to 4 hues per illustration), one stroke weight, one level of detail. Add dark-theme variants.
  - Prefer real product imagery, abstract geometric forms, or a restrained custom set over generic stock-vector people and stock clip-art. Gradients are subtle and built from token colors (OKLCH). 3D, glass, grain or other trend effects only if they passed the 3-example rule, serve the task, and have a flat fallback.
  - Photography: consistent crop, color treatment and subject distance; sources with clear licenses (own shoots, Unsplash, Pexels, or paid stock such as Shutterstock when the connector is available); record the license; never download or use photos of real public figures.
  - Format: SVG for line art and illustration, AVIF or WebP for photos, with sized variants and the correct alt text (empty alt for decorative graphics).
  - Every graphic has a job: orient, explain, delight, or confirm. If removing it changes nothing, remove it. Check it in grayscale and at small size so it never competes with the primary action.
  - Check every icon's and graphic's meaning against the original so nothing changes the content or function (Commitment, A4.1).
- **Motion:** purpose first (orient, confirm, guide). Duration tokens (about 100 to 150ms micro, 200 to 300ms standard, 300 to 500ms large), easing tokens, a reduced-motion alternative, directional motion following the reading flow.
- **Components:** for each, anatomy, variants, sizes, the full state matrix (default, hover, focus-visible, pressed, disabled, loading, error, success, selected, empty), content rules and responsive behavior.
- Persist everything in the design-system file (Part I).

## 4.7 Build

**All targets:** every value maps to a token or a component variant; no magic numbers. Layout is auto-layout, flex or grid logic with constraints, not pixel positions. Content survives stress: 2x longer strings, very short strings, large numbers, missing images, 0, 1 and many items, error and offline, skeletons that match the final layout, text scaling to 200%.

**Figma:**
- Order: foundations (Variables, text and effect styles), then components, then screens, then interactions; check each stage with a screenshot.
- Bind colors, text, spacing and radius to variables and styles; no detached instances; layers named in slash-separated form.
- Default frames show the resting state only: no focus ring, hover tint, selection outline or debug stroke may leak into the default variant (a focus-visible ring appears only in its own state frame).
- Measure through the Figma API, do not eyeball: use `use_figma` to read the absolute bounds (x, y, width, height) of every node in each screen and feed them to the geometry audit in 4.8 item 2.
- When the originals come from Figma, read them with get_design_context, get_metadata and get_screenshot; if they are images, place them as labeled reference frames.
- **Interactive builds:** use interactive components, variants and variables so the prototype behaves like the product: inputs and validation, toggles, tabs, filters, overlays, loading to success or error, sticky or collapsing bars, multi-step flows. Use proper triggers, conditional logic, Smart Animate with the motion tokens. Every behavior in the Inventory gets a working interaction or a documented simulation (state which data and outcomes are simulated). Document an **Interaction Map** (trigger, action, result, motion token) and walk every path in preview. If a needed interaction cannot be created, build what is possible, list what could not be wired and why, and offer a coded prototype as an optional extra in the delivery note.
- **File pages:** 1 Cover (name, version, locale mode, change level, interaction mode), 2 Original, 3 Audit, 4 Explorations, 5 Foundations, 6 Components, 7 Screens, 8 Flow and Prototype, 9 Handoff (includes the management report from 5.2), 10 QA.

**Web:** real CSS with tokens as custom properties, responsive by default, purposeful motion only, real copy, performance-aware images (AVIF or WebP, SVG).

**Static graphic:** hand off to `canvas-design`, `pdf` or `pptx` with the decided palette, type pairing and layout motif.

**Buildability:** note component-to-code hints, responsive rules, accessible markup (roles, labels, focus order), asset export specs, and anything costly to implement with a cheaper equivalent. List the next 5 to 10 likely screens or patterns the system must cover.

## 4.8 Pixel-perfect pass (measured, not asserted)

Run the applicable sections of `references/pixel-perfect-checklist.md`. If you cannot render or inspect, compute from the code or Figma values and label the result "computed, not rendered". In this order:

1. **Proportion and scale.** Repeated items share dimensions; control heights from one family (for example 40/48/56); adjacent type roles differ by a real ratio, never by 1 to 2px; icon size about 1.0 to 1.3 times label size; nested radius equals outer radius minus padding.
2. **Alignment and geometry: a numeric audit, zero tolerance.** Dump the absolute bounds of every node per screen (Figma: `use_figma`; web: getBoundingClientRect) and run these checks in code, listing each defect with node name and delta:
   - Every x, y, width and height is an integer and on the spacing scale; named exceptions only.
   - Edges that are meant to align (a column of rows, card insets, section titles, dividers) differ by exactly 0px; any 1 to 3px deviation is a defect.
   - No unintended overlap between sibling bounding boxes. Overlays (badge, bookmark, audio pill) are allowed only on the whitelist and must never cover the focal subject or placeholder glyph of the image beneath them.
   - Overlay controls on one container share one inset from the container edge (mirrored in RTL) and sit in corners or safe bands.
   - Icon and text in a row: vertical center delta at most 0.5px; multi-line rows share the first baseline. Left and right inner margins of a container are equal unless the asymmetry is intended and named.
   - Header, row and card edges meet the same outer margin (one value, for example 16 or 20).
   Fix and re-run until the defect list is empty.
3. **Spacing audit, always in the output.** Read real margin and padding values (Figma properties, or computed styles from the DOM) and deliver a compact table: edge margins, padding per container type, gaps inside groups, between groups, between sections. Run the scale check on every value and fix or name each exception. Same component type means identical padding everywhere; inner padding never exceeds the gap to a neighbour; left and right margins match. A static graphic with no spacing writes "not applicable".
4. **Micro-detail consistency.** Same stroke, radius, border width, shadow logic and icon grid.
5. **States and real content.** Every state from 1.3 is drawn or explicitly deferred. Test short and long names, big numbers, mixed-direction text, missing images.
6. **Noise and balance.** Grayscale and blur views: one focal point, balanced masses. Remove what fails.

An exception to any rule must be intentional and nameable.

## 4.8b Negative space, composition and the flawless gate

White space is designed, measured and reported like any other value.

- **Proximity ratio.** The gap between groups is at least 1.5 times the gap inside a group; the gap between sections is at least 2 times the gap between groups. Adjacent spacing levels differ by a visible step, never 4px versus 8px.
- **Margins and padding.** One outer screen margin. Card inner padding at least 16 and never smaller than the largest inner gap. Nothing touches its container edge (at least 12px).
- **Whitespace budget (heuristic, label it as such).** Measure the share of empty (background-colored) pixels inside the content region of each rendered screen and report it. About 35 to 55 percent reads calm for list and detail screens; under 30 reads cramped and over 65 reads sparse. Outside the range, justify or fix.
- **Elements per card.** At most 7 distinct elements per card or row; beyond that, group, demote to the detail screen, or remove.
- **Placeholders are designed states.** An empty photo or avatar gets its own treatment (initials or an illustration on a strong tonal anchor, glyph at least 3:1), drawn at the same quality as real content, never a pale box with a thin outline icon.
- **Aesthetic bar.** Put each key screen next to 2 or 3 benchmark references at the same scale, write the 3 sharpest gaps (hierarchy, contrast, rhythm, restraint), fix them, and repeat once.
- **Flawless gate (definition of done).** Do not deliver while any list is non-empty: contrast failures, alignment defects, unintended overlaps, off-scale spacing values, whitespace outside the range without a justification, leaked states in default frames. Report the final counts (all zero) in the Parity and metrics section.

## 4.9 Checks and review

1. **Parity Check (redesign):** original versus redesigned inventory; every row matches or is flagged. Components may differ; content meaning and functions may not. Reworded microcopy is listed per 4.3.
2. **Contrast and size:** computed ratios for every text and UI pair; target sizes and minimum font sizes. Latin floors: body not below 16px web or 17pt iOS, captions not below 12px or 11pt. Persian floors are in Part H. Check status colors and charts under color-vision-deficiency simulation.
3. **Render loop (at least 2 full passes).** Export every screen at 2x. Inspect the whole frame, then zoomed tiles (about a quarter of a screen each) of every card, header, control and overlay, the way a reviewer zooms in. Log defects D1 to Dn with location and cause (misalignment, clipping, overflow, uneven spacing, collision, low contrast, leaked state), fix them, re-render, and repeat until a complete pass finds zero. State the number of passes in the delivery note. Never deliver after a single pass. Mode FA adds: broken shaping, wrong text direction, font substitution, clipped dots, left-heavy weight, bidi errors.
4. **Binding check:** no hardcoded fills, strokes, radii, spacing or text properties outside variables and styles.
5. **Interaction check (when interactive):** every path in the Interaction Map runs in preview.
6. **Token-swap test:** change brand hue, base font, radius scale and spacing unit, and test light and dark; the design must stay coherent.
7. **Before and after metrics (redesign):** the same table captured in Stage 2, measured again, plus a task-time estimate by the Keystroke-Level Model (labeled as an estimate). Report regressions honestly with a justification.
8. **Independent review:** a fresh reviewer (a sub-agent if available) that has not seen the working process gets only the Inventory, the brief, screenshots of before and after, the Interaction Map if any, and a rubric (parity, hierarchy, usability, ergonomics, accessibility, visual craft, system rigor, buildability, plus Persian typography and RTL composition in Mode FA). If none is available, do a clearly separated adversarial critique and say it is self-review. Fix every valid finding; note rejected ones with a reason.
9. **Hypotheses and score:** for each key change state the expected effect, metric and validation method (A/B test, 5-user test, analytics event), as hypotheses, not results. Score 1 to 5 on distinctiveness, hierarchy, usability, ergonomics, accessibility, system rigor, buildability and scalability; anything below 4 gets another iteration.

---

# Stage 5. Brief defense document

The last thing produced, always. It defends the new version to the people who decide.

## 5.1 Deliver

Deliver in this order, as separate frames:
1. The three explored versions (brief), each with its problem map.
2. The **combined best-of-three version** alone, labeled with which idea came from which version, before any refinement.
3. The refined final of that combined design, in key viewport states. Combined and refined are never merged into one frame.

Also include: the benchmark (with unreachable sources named), the spacing table, what refinement removed, re-weighted and strengthened, and what the pixel pass adjusted. For redesign add the Parity Check, metrics table, out-of-scope opportunities and a short change log (before, after, reason, expected impact). If the user asks for one quick version, skip exploration and say so.

The chat reply stays short: locale decision, change level, interaction mode, what was made, the link, the 3 to 5 most important decisions, and what needs validation. Depth lives in the file.

## 5.2 Management report (always last, after all output)

After 5.1, write one plain-text document for presenting the result to managers. It is **simple, exact, short, technical and defensible**. Its focus: (1) what is wrong today, found by the audit, and (2) why each new decision was made. Everything else is kept to the minimum.

**Format and delivery:** plain text or markdown, one page (about 350 to 500 words), simple everyday wording (explain a technical term once in a few words), in the user's language and saved formatting preferences (Mode FA: Persian RTL rules from Part H, the user's saved numeral and term-formatting rules). Save it as a separate file, copy it to the Figma Handoff page when the target is Figma, and give it in the chat after the short reply. No decoration.

**Fixed structure, four sections in this order:**

1. **Audit: current problems (largest section).** At most 5 problems, ordered by severity, keeping the P-numbers from Stage 2 (numbers may skip). One line each: the problem, the measured evidence (a number, a count, a ratio, a step count), and what it costs the user or the business. Example shape: P1. Three elements compete for attention, so the primary action is found late (3 emphasis levels at equal weight; primary button is 14% of the screen width). Mark each as Fact, Inference or Assumption.
2. **Benchmark.** 3 to 5 comparable products (or sources), one line each: what they do on this flow, and whether we adopted, adapted or rejected it. State clearly if a source could not be opened or a pattern was a single example.
3. **Decisions and reasons (second largest section).** Component, navigation and copy replacements always appear here, each with the problem it fixes and, for components, its best-practice source. A table of at most 7 rows: Problem it solves (P-number) | Decision | Reason (principle, number or benchmark) | Trade-off. Icon and graphic choices are listed too, in one line each: the chosen family or style, the reason (benchmark, license, coverage) and the trade-off. Every decision must point to a problem; a decision with no problem is labeled "identity or brand choice" and not presented as a usability gain.
4. **Checks.** What was verified and the result, in one short list: content and function parity, contrast, target sizes, before and after numbers (contrast failures, steps to the main task, task-time estimate labeled as an estimate), independent review result. Then one line for what is still an assumption and the cheapest test to confirm it (for example a 5-user test with a success threshold). Show any regression and why it is acceptable.

End with one line: the decision requested from the managers.

**New design mode:** there is no audit, so section 1 becomes "Brief and risks" (the user problem, the constraints, and the 3 biggest design risks), and section 4 lists the checks without before and after numbers.

**Rules:** no hype and no superlatives; no claims of tested results you do not have; no invented numbers (every number is computed or labeled as an estimate); never cite a source you did not open; out-of-scope ideas are listed as proposals, never as delivered changes; effort is stated as low, medium or high with a reason, never invented hours.

---

# Part H. Persian layer (active only in Mode FA)

The product is Persian. Think, compose and judge in Persian from the first decision; never start from an LTR layout and flip it.

## H1. Native RTL composition
- The eye enters at the right edge and travels right to left, top to bottom. Decide the focal point, heaviest mass, start of every list, row, form, table and step sequence, navigation and tab order, progress direction, drawer and sheet origin and swipe gestures from that flow and from Persian platform conventions.
- Directional icons (arrows, chevrons, back, send, list indents, progress, undo and redo) follow their meaning in the Persian reading flow. Universal symbols (media controls, clocks, checkmarks, phone, lock, logos, numbers, code) keep their form. Record this in a short direction-semantics table.
- Embedded Latin: isolate LTR runs (brand names, emails, URLs, phone numbers, codes, English terms). Inputs for phone, email, URL and card numbers keep LTR entry. Use Persian punctuation forms and check that parentheses and quotes land on the correct side.
- Numerals: choose Persian or Latin digits once, per the original or the user's stated rule, and apply them everywhere; prefer tabular figures. Dates follow Jalali if the original does.
- Preserve ZWNJ (half-space) in compound words; avoid justified text; no letter-spacing on connected script.
- Check left-right balance: images, avatars, badges and FABs must create a deliberate balance, not a leftover left-heavy weight.

## H2. Persian typography
- Pick fonts with complete Persian shaping, optical consistency with their Latin glyphs, a real weight range and clear licensing. Candidates to verify in Figma and by license: Vazirmatn, Estedad, Peyda, IRANSansX, Yekan Bakh, Shabnam, Noto Sans Arabic, IBM Plex Sans Arabic, Readex Pro, Almarai, Tajawal, Cairo. Test with real strings including digits, mixed Latin and long words.
- Never copy Latin sizes. Heuristics, to be confirmed by rendering: body about +1 to +2px (8 to 15%) over a comparable Latin size; floors body 15 to 16px, secondary 13 to 14px, captions not below 12px and used sparingly.
- Line-height per role as a token (heuristics): body about 1.7 to 1.9, headings about 1.4 to 1.6, single-line labels not below 1.5 (protects dots from clipping, especially with truncation).
- Hierarchy comes mainly from size steps, color and spacing; weight is secondary. Avoid weights below 400 under 18px; check bold does not clog counters. No faux italic, no uppercase logic.
- Mixed lines: match x-height and visual weight rather than nominal size, align baselines, and keep digits and Latin brand names from looking oversized or too light.

## H3. Effect on spacing, size and proportion
- Spacing is measured from the text line box, not the font size; the same numeric padding looks larger vertically. Tune padding per component and center the glyph mass, not the line box, in buttons, chips, tabs, inputs and rows.
- Re-derive control, row and card heights from content, but preserve the original's information density rather than inflating it. Re-balance the grid where text wraps more.
- Test wrapping and truncation with real strings, 1.3x longer strings and large digits; define max lines and ellipsis behavior.
- Re-check hierarchy ratios (heading, body, caption) after sizing, and compare original and redesign at the same frame size for text mass, white space and left-right weight.
- **Figma:** set text direction to right-to-left and alignment to right on every Persian text layer (never by manual flipping); build auto-layout in Persian order; confirm the font is actually loaded, not substituted; define text styles per role with Persian line-heights. Dev notes: logical properties (inline-start and inline-end), the dir attribute, bidi isolation.

---

# Part I. Appendix

## I1. Contrast and scale check (Python, tested)

```python
def lum(h):
    h = h.lstrip('#')
    if len(h) == 3: h = ''.join(c*2 for c in h)
    r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r) + 0.7152*f(g) + 0.0722*f(b)

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def off_scale(vals, base=4):
    return [v for v in vals if v % base]
```

Sanity values: black on white is 21.0; #767676 on white is 4.54.

## I2. DOM spacing dump (web outputs)

Not yet run in a real browser, so verify its output once. In Figma, read the same values with get_design_context and get_variable_defs instead.

```js
[...document.querySelectorAll('[class]')].slice(0,300).map(e=>{const s=getComputedStyle(e);return {c:e.className.toString().slice(0,40),pad:s.padding,mar:s.margin,gap:s.gap}}).filter(x=>x.pad!=='0px'||x.gap!=='normal')
```

## I3. Design-system file (persists across sessions)

After 4.6, write `design-system.md` to the project folder: color tokens (with computed contrast per pair), type scale and families, spacing scale, radius, elevation, control heights, direction-semantics table (Mode FA) and the chosen concept. For later screens: read it first, inherit it, and write only what is genuinely new under a page-specific section. Never silently diverge; name any exception.

## I4. Verified starting palette

Neutral plus accent; contrast computed with the tool above. Adjust the accent per brand and recompute.

| Role | Light | Dark | Contrast on bg (light / dark) |
|---|---|---|---|
| bg | #FAFAF7 | #0F1115 | |
| text | #14161A | #F2F3F5 | 17.3 / 17.0 |
| text secondary | #4A4F57 | #A7ACB5 | 7.9 / 8.3 |
| text muted | #6B7078 | #8A8F99 | 4.8 / 5.8 |
| accent | #2F5BEA | #8CA8FF | 5.3 / 8.2 |
| on-accent text | #FFFFFF | #0F1115 | 5.5 / 8.2 (on accent) |
| control border | #8A8F98 | #6B717C | 3.1 / 3.9 |

Hairline dividers can be lighter than the control border because they carry no meaning.

## I5. Reference files

- `references/pixel-perfect-checklist.md`: final-pass checklist, 12 sections (proportion and scale, alignment, spacing, micro-details, typography, color and contrast, icons, states, content stress, motion, accessibility, handoff).
- `references/design-systems.md`: Material 3, Apple HIG, shadcn/Radix, domain systems and component references, with tokens and patterns.
- `references/typography-color.md`: type pairing, scales, color theory, WCAG contrast, 2025-2026 type and color trends including OKLCH.
- `references/trend-research.md`: aesthetic galleries, how to search them live, and the "AI look" clichés to avoid.
- `references/pattern-libraries.md`: UX-reasoning sources and pattern references; ignore entries that need a paid plan or login.
