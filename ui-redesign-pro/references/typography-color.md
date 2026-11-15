# Typography & Color — Working Reference

## Typography

**Pairing, not defaulting to one font.** Using a single sans everywhere (Inter for literally everything) is the fastest way to look generic. Instead:

- Pick a **display/headline face** with personality (a distinctive grotesk, a serif with character, a variable font with unusual proportions) for headlines and hero text.
- Pick a **restrained workhorse face** for body copy and UI — needs to be highly legible at small sizes, not distinctive. System stacks (`-apple-system`, `Segoe UI`, etc.) or well-tested web faces (Inter, Söhne, General Sans, Geist) are fine *here*, precisely because body text should get out of the way.
- Optionally add a **monospace accent** for numbers, code, timestamps, or metadata — it signals precision and is currently a strong trend in technical/SaaS products (see shadcn/ui-era products).
- Build a real **type scale** rather than guessing pixel values — a modular scale (ratio like 1.25 "major third" or 1.333 "perfect fourth") from a base size gives you sizes that feel intentional together. For web, prefer `clamp()` for fluid sizing between mobile and desktop rather than fixed breakpoint jumps.
- Tighten `line-height` as font-size increases (headlines can go to 1.0-1.1; body text wants 1.5-1.7) and add negative letter-spacing on very large display text (it looks loose otherwise).

## Color

**60-30-10 as a starting ratio**: ~60% dominant neutral (background/surface), ~30% secondary neutral or supporting tone (cards, secondary surfaces, text), ~10% accent (primary actions, links, focal highlights). This prevents the common failure mode of an accent color splashed everywhere, which reads as unfinished rather than bold.

**Semantic tokens over raw hex**: define `background`, `surface`, `surface-elevated`, `text-primary`, `text-secondary`, `border`, `accent`, `success`, `warning`, `danger` — then reference tokens in the design, not raw color values. This is what makes dark mode, and later edits, coherent instead of a hunt-and-replace exercise.

**Dark mode is not just inversion**: don't simply flip white↔black. Real dark-mode palettes desaturate and lighten accent colors slightly (a saturated accent that works on white can vibrate/glow uncomfortably on black), and use dark grays (not pure black) for elevated surfaces so depth via tone still works.

**WCAG AA contrast is a hard floor, not a suggestion**: 4.5:1 for body text, 3:1 for large text (24px+/19px+bold) and meaningful UI elements (icons, borders that convey information). Check this, don't eyeball it — low-contrast gray-on-white or pastel-on-white text is one of the most common "looks nice in the mockup, unusable in reality" mistakes.

## Current trends worth knowing (2025-2026, verify with live search per `trend-research.md` since this shifts fast)

- **OKLCH / perceptually uniform color spaces** are increasingly used over HSL/RGB for defining palettes and generating tonal ramps, because equal numeric steps look like equal *perceived* steps — reduces the "muddy midtones" problem HSL ramps often have.
- **Quiet, confident neutrals + one saturated accent** rather than multi-color gradients — the "gradient everything" aesthetic from 2022-23 has cooled; current premium product design favors near-monochrome with one deliberate pop of color.
- **Warm neutrals (off-white, warm gray) as an alternative to cold slate/blue-gray** — used to differentiate from the extremely common cool-gray SaaS look.
- **Grain/noise texture and subtle gradients as texture, not decoration** — used at low opacity to avoid flat, sterile surfaces, especially on marketing/hero sections.
- **Bento-grid layouts** (asymmetric grid of varied-size cards) for feature/summary sections — largely replaced the generic "3 equal cards in a row" pattern.
- **Restrained, physically-plausible motion** (spring easing, small scale/opacity transitions) over decorative animation — motion should confirm an action or guide attention, not perform.

## Things to actively avoid (the generic "AI-generated" look)

- Purple-to-blue gradient backgrounds as a default choice with no rationale.
- Inter (or any single font) used for headlines, body, and UI labels alike.
- Every card identical: same radius, same shadow, same padding, arranged in a uniform 3-column grid regardless of content.
- Generic emoji or line-icon-in-a-circle as the sole visual interest.
- Centered hero + centered subhead + centered button as the only layout considered for a landing page.
