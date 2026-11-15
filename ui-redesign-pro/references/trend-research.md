# Live Trend Research — How and What to Search

Training data goes stale; design trends move in months, not years. Before finalizing a direction, run 1-3 targeted searches (via WebSearch) rather than relying on memory alone. This is the step most likely to be skipped under time pressure — don't skip it, it's the difference between a design that looks like "now" and one that looks like "generic AI output from two years ago."

## Sources

- **Awwwards, Dribbble, Behance** — the core three. Awwwards skews toward full sites with production polish and motion; Dribbble skews toward shots/concepts (often more experimental, sometimes never shipped — treat as mood/direction, not a literal spec); Behance skews toward full case studies with process explanation.
- **Muzli** (muz.li, also the "Muzli" browser extension/newsletter by Marko Sabotin) — a curated daily aggregator that pulls from many of the above plus product launches, AI tools, illustration, and branding in one feed. Useful specifically because it's pre-filtered by editors for what's fresh *today* rather than a raw firehose — good as a first stop to sense the current overall mood before drilling into Awwwards/Dribbble for specifics. Query it via `"muzli [topic]"` or `site:muz.li [keyword]`; like the other sources, pull it through WebSearch since there's no dedicated browsing tool for it.
- **Minimal Gallery** (minimal.gallery) — hand-picked, tag-organized gallery of clean, functional, real production websites (portfolios, SaaS, e-commerce, agencies), running since 2013. Reach for this specifically when the direction calls for restraint — quiet typography, generous whitespace, minimal color — rather than the more experimental/maximalist work that dominates Awwwards and Dribbble. Query via `"minimal.gallery [industry/tag]"` or `site:minimal.gallery [keyword]`; its own tag taxonomy (SaaS, portfolio, agency, e-commerce, editorial, etc.) is also worth browsing directly for a given industry.
- **Godly, SiteInspire, CSS Awards, Land-book** — narrower galleries, useful when Awwwards/Dribbble results feel too generic or oversaturated for a query.
- **The FWA** (thefwa.com) — one of the oldest curated "most innovative sites" lists (since the early 2000s), still a reliable pull for boundary-pushing, experimental work — skews further toward the experimental end than Awwwards.
- **Curated.design and Maxibestof.one** — smaller independent galleries of creative web UI, worth a look when the bigger three feel oversampled by everyone else (i.e. when you specifically want to avoid the most obvious/overused references).
- **Designspiration** (designspiration.com) — a Pinterest-style board of inspiring images across graphic design, illustration, and UI rather than a curated "best of" list; more useful for open-ended mood/direction exploration than for precise UI reference.
- **Bookmarks.design** — a large, tag-organized archive of both inspiration sites and design tools; useful as a jumping-off point when you're not sure which specific gallery fits the project, or when hunting for a tool (not just inspiration).

### Landing-page-specific galleries

When the deliverable is specifically a marketing/landing page (not a full site or app), these narrower, purpose-built galleries are often more efficient than the general ones above: **Lapa Ninja** (lapa.ninja), **One Page Love** (onepagelove.com, for single-page sites specifically), and **Landing Folio** (landingfolio.com, categorized by industry/section type — pricing, hero, testimonials — which is handy when you need reference for one specific section rather than a whole page).

If a `design-inspiration` MCP connector is available in the current session (tools like `browse_awwwards`, `browse_dribbble`, `browse_behance`, `browse_godly`, `browse_landbook`, `browse_css_awards`, `browse_siteinspire`, `search_inspiration`), prefer those over raw WebSearch for these specific sources — they return structured, curated results directly rather than requiring you to parse search-result snippets. Sources without a dedicated tool there (Muzli, Minimal Gallery, The FWA, Curated.design, Designspiration, Lapa Ninja, One Page Love, Landing Folio, etc.) still go through WebSearch.

## Query patterns that work

- `"[product type] UI design 2026 Awwwards"` — e.g. "fintech dashboard UI design 2026 Awwwards"
- `"[product type] landing page inspiration Dribbble"`
- `"[industry] website design trends [current year]"`
- `"muzli [topic]"` — e.g. "muzli SaaS onboarding" — for a fast, pre-curated pulse on what's current
- `"minimal.gallery [industry]"` — e.g. "minimal.gallery agency portfolio" — when the direction calls for a clean, restrained aesthetic specifically
- `"best [component type] design examples"` — e.g. "best pricing page design examples", "best onboarding flow design examples"
- `site:dribbble.com [keyword]`, `site:awwwards.com [keyword]`, or `site:muz.li [keyword]` to bias results toward curated design galleries rather than generic blog listicles
- `"[competitor or well-known product] design system"` if the user references a comparable product's aesthetic

## What to extract from the results

Don't just note "it looked cool" — pull out specific, reusable decisions:

1. **Layout motif**: is everything using bento grids now? Asymmetric hero splits? Full-bleed imagery with overlaid text?
2. **Palette approach**: monochrome + accent? Duotone? Specific colors recurring across multiple examples (a real signal, not one designer's taste)?
3. **Type pairing**: serif/sans combos, unusually large display type, variable font usage?
4. **Signature detail**: a recurring small touch (custom cursor, scroll-triggered reveal, grain texture, specific corner-radius language) that several current examples share.
5. **What's clearly dated**: if search results and your own knowledge agree something (e.g. skeuomorphism, flat-flat minimalism, a specific gradient style) reads as "2019" or "2022" now, note it explicitly as something to avoid.

## Calibrate to context, not just what's trendy

"Current trend" isn't automatically "correct for this project." A children's education app and an enterprise fintech dashboard shouldn't chase the same Dribbble trends. Use research to know the current *vocabulary* (what's technically possible and stylistically fresh right now), then apply judgment about what fits the product's actual audience and purpose. A trend search that turns up five neon-cyberpunk portfolio sites doesn't mean the user's B2B SaaS tool should go neon-cyberpunk.
