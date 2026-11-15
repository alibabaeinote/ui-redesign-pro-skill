# Established Design Systems — Working Reference

Use these as foundations to borrow from, not as rules to follow verbatim. Blend where it makes sense (e.g. Material 3 color tokens + shadcn/ui layout conventions is a common, effective combination for web apps).

## Material Design 3 (Google)

Best for: Android-adjacent products, data-dense apps, anything that benefits from a rigorously tested elevation/color system.

- **Dynamic color**: a full palette (primary, secondary, tertiary, error, neutral, neutral-variant) generated from tonal palettes at fixed lightness steps (0-100). Surfaces get subtle tinted tones rather than flat white/gray — this is what gives M3 apps their soft, cohesive look instead of stark black-on-white.
- **Elevation via tone, not just shadow**: higher elevation = slightly lighter/more tinted surface, in addition to (often instead of) heavier drop shadow. Keep shadows subtle.
- **Shape scale**: consistent corner radius tokens (none/extra-small/small/medium/large/extra-large/full) applied consistently by component role — buttons and chips get more rounding than cards and dialogs, not arbitrary per-element radii.
- **Type scale**: display/headline/title/body/label, each with large/medium/small variants — 15 total, all with defined size/line-height/weight/tracking. Don't freehand font sizes; pick from a scale.
- **State layers**: hover/focus/pressed are implemented as a semi-transparent overlay on the base color (8%/12%/... opacity), not a totally different color — keeps interactions feeling like the same object.

## Apple Human Interface Guidelines

Best for: iOS/macOS-adjacent products, anything premium/consumer-facing, situations where restraint and content-first hierarchy matter more than data density.

- **Clarity, deference, depth**: UI should recede in favor of content. Chrome is minimal; the content (photos, text, the product itself) is the star.
- **SF Pro / SF Rounded** as the reference typographic voice — but the transferable lesson is the discipline: one typeface, a handful of weights, generous type sizes for legibility (17pt body baseline on iOS), and real vertical rhythm.
- **Materials (blur/vibrancy)**: translucent, blurred layers used sparingly for navigation bars, sheets, and overlays to imply depth without heavy shadows — this is the "glassmorphism" effect done with restraint, not as wall-to-wall decoration.
- **Safe areas and generous touch targets**: minimum 44x44pt tap targets, real breathing room around interactive elements — this generalizes to web as "don't cram interactive elements."
- **Symbols**: a single consistent icon language (weight/scale matched to the adjacent text) rather than mixing icon sets.

## shadcn/ui + Radix Primitives (modern web/SaaS default)

Best for: web apps, dashboards, SaaS products — this is currently the dominant aesthetic for well-regarded product UI (Linear, Vercel, and most YC-adjacent startups converge here).

- **Composable primitives over monolithic components**: accessible, unstyled Radix primitives (Dialog, Popover, DropdownMenu, etc.) styled with Tailwind utility classes — the payoff is consistent focus states, keyboard nav, and ARIA behavior for free.
- **Neutral-first palette**: a desaturated gray/slate/zinc base (often defined in OKLCH now, not hex) carries 90% of the UI; a single accent color is used sparingly for primary actions and focus rings, not splashed everywhere.
- **Border-driven hierarchy over shadow-driven**: subtle 1px borders (often `border-border/50` style low-opacity tokens) separate sections more often than drop shadows do. Shadows are reserved for actual overlays (dropdowns, modals) floating above the page.
- **Radius tokens**: one `--radius` variable driving all corner rounding (buttons, inputs, cards) so the whole UI reads as one coherent system, not mismatched roundness per component.
- **Density and monospace accents**: tighter line-height and smaller base font sizes (14px body is common) than marketing sites, with monospace used deliberately for numbers/code/IDs to add technical credibility.

## Domain-specific systems (for enterprise / specialized products)

Worth knowing by name so you can borrow their conventions when the product fits their niche — each of these has already solved hard problems (dense data tables, complex forms, permissions UI) that are easy to get wrong from scratch.

- **IBM Carbon** — enterprise/data-dense products. Strong reference for complex forms, data tables, and a restrained, high-density type scale that stays legible at small sizes.
- **Shopify Polaris** — commerce/admin dashboards. Good reference for merchant-facing admin UI: clear content hierarchy in list/detail views, consistent empty-state and banner patterns.
- **GitHub Primer** — developer tools. Good reference for the "technical, monospace-accented, high information density but still calm" aesthetic that reads as credible to a technical audience.
- **Atlassian Design System** — B2B collaboration/PM tools. Good reference for notification, permissions, and multi-product-suite navigation patterns.
- **Microsoft Fluent 2** — cross-platform (web/desktop/mixed reality) enterprise products. Good reference for a system that has to stay coherent across very different device contexts.

## Component & pattern vocabulary references

Use these when you need to see how a *specific component type* (not a whole product) has been solved across many systems, or need the precise name for something before discussing or specifying it.

- **component.gallery** — the standout resource here: shows the same component (accordion, date picker, tag/chip, etc.) side by side as implemented across dozens of real, named design systems at once. The fastest way to survey the solution space for one specific component before picking an approach.
- **Adobe Spectrum** (spectrum.adobe.com/page/components) — Adobe's cross-product system; another well-documented reference alongside Carbon/Polaris/Primer, particularly relevant for creative-tool UI.
- **GOV.UK Design System** (design-system.service.gov.uk/components) — the UK government's system; unusually rigorous about explaining *when and why* to use each component, and a strong plain-language, high-accessibility baseline worth borrowing from even outside government contexts.
- **ui-patterns.com** — catalogs common interaction patterns independent of any one visual system, framed around the underlying UX problem each solves — useful for picking the right pattern before styling it.
- **uiguideline.com/components** — straightforward mobile/web component examples, good as a quick refresher on a component's standard anatomy.
- **Balsamiq's UI control guidelines** (balsamiq.com/learn/ui-control-guidelines) — a plain-language primer on basic control types and when to use each; a useful gut-check on fundamentals when something feels over-engineered.
- **Figma Community UI kits** (figma.com/community/category/ui-kits) — practical starting kits from well-known systems and independent designers, useful when the user wants an actual Figma file to work from rather than just a reference.
- **NameThatUI** — a labeled-screenshot reference/quiz for correctly naming UI elements ("stepper" vs. "segmented control" vs. "chip," etc.). Not an inspiration source — use it for precision when describing or specifying a design, so recommendations reference the correct, specific component name instead of vague description.

## When to blend

- Consumer mobile-first product → lean Apple HIG for restraint/depth, Material 3 type scale discipline.
- B2B SaaS dashboard → shadcn/ui conventions by default; borrow Material 3's tonal-surface idea if the product is data-dense and needs more visual layering than borders alone provide.
- Marketing/landing page → none of these directly (they're app systems) — instead lean on `references/trend-research.md` and typography/color choices; consult the `top-design` skill for motion-forward marketing sites.
