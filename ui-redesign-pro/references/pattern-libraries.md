# Real-App Pattern Libraries — Working Reference

These differ from Awwwards/Dribbble in an important way: Awwwards/Dribbble show *aesthetics* (often single static shots, sometimes concept work that never shipped). Pattern libraries show *how shipped, real products actually solved a specific interaction* — captured as real screenshots or screen recordings from production apps. For anything that's actually a flow (not just a screen) — onboarding, signup, paywall, empty state, settings, checkout, search, notifications — these are the more useful reference, because they show sequences and edge-case states, not just a pretty hero shot.

## The main sources

- **Mobbin** (mobbin.com) — the largest library of real mobile and web app screens, organized by app, by flow (onboarding, paywall, search, empty state, etc.), and by UI element. The gold standard for "how does [well-known app] handle X" questions.
- **Page Flows** (pageflows.com) — screen-recorded videos of full user flows (not just static screens) — useful when the sequencing/transitions matter as much as any individual screen.
- **Screenlane** (screenlane.com) — similar screenshot library to Mobbin, mobile and web, organized by pattern.
- **Pttrns** (pttrns.com) — mobile UI patterns organized strictly by screen type (login, onboarding, search, checkout, etc.); narrower and simpler than Mobbin, good for a fast look at one specific screen type across many apps.
- **TheAppFuel** (theappfuel.com) and **Appshots.design** — archives of categorized screenshots from known products, similar niche to Mobbin/Screenlane; worth checking either if the other doesn't have good coverage for a specific app or pattern.
- **UI Garage** (uigarage.net) and **CollectUI** (collectui.com) — daily-updated feeds of individual UI screens/components. Closer to Dribbble in format (single curated shots) but sourced more from real or near-real product UI than concept work, so they sit between the aesthetic galleries and the pure pattern libraries.
- **Lapa Ninja, One Page Love, Landing Folio, Land-book** — skew toward marketing/landing pages specifically rather than in-app product flows; use these instead of Mobbin when the deliverable is a marketing site, not an app. (See `references/trend-research.md` for more on these.)
- **Growth.Design** and **Built For Mars** (builtformars.com) — case-study/teardown format (illustrated or written breakdowns of *why* a product made a specific UX decision, sometimes with explicit critique of what doesn't work) — useful when you need the reasoning behind a pattern, not just a picture of it. Built For Mars in particular is worth reaching for when the user wants to understand *why* a flow converts well, not just what it looks like.

## Access limitations — be upfront about this

Mobbin, Page Flows, and Screenlane are commercial products and most of their content sits behind a signup/login wall or a paywall for full search and browsing. There's no MCP connector for any of them in this environment, so in practice:

- `WebSearch` for `"mobbin [pattern name]"` or `"site:mobbin.com [pattern]"` will often surface indexed preview pages, blog posts referencing specific examples, or Mobbin's own public trend write-ups — use whatever surfaces.
- If a fetch hits a login wall or paywall, don't try to work around it (no scraping workarounds, no credential prompts) — treat it the same as any other inaccessible page: note it, and fall back to what search results did surface, plus general knowledge of how major apps (which is extensively documented on the open web via reviews, teardown blog posts, and UX case studies) handle the pattern in question.
- Tell the user plainly if a specific requested source turned out to be inaccessible, rather than presenting a best-guess reconstruction as if it came directly from the library.

## What to extract when a source is accessible

- The specific sequence of steps/screens for a flow (e.g. a paywall: value prop screen → plan comparison → payment → confirmation, vs. a shorter single-screen paywall).
- Which elements recur across multiple examples of the same pattern from different apps (a strong signal it's converged on for a reason — e.g. most onboarding flows now show progress via dots/bar, most empty states pair an illustration with one clear CTA).
- Edge-case states that are easy to forget when designing from scratch: empty states, loading states, error states, zero-results search, permission-request screens.

## When to reach for these vs. Awwwards/Dribbble

- Building a specific app flow or product screen (onboarding, settings, dashboard, checkout) → pattern libraries first, aesthetic galleries second.
- Building a marketing/landing page, portfolio, or poster → aesthetic galleries (Awwwards/Dribbble/Behance) and `references/trend-research.md`; pattern libraries are less relevant here.
- Both matter for a full product (e.g. a SaaS app with both a marketing site and an in-app dashboard) — research each part with the source suited to it.
