# Pixel-Perfect Checklist (final pass, step 10 and step 11)

Run the sections that apply. Each line is a pass or fail test. Label results "measured" or "computed, not rendered". Name every exception and say why it is intentional.

## 1. Proportion and scale
- [ ] Repeated items (cards, rows, chips) share identical width, height and padding.
- [ ] Control heights come from one family (for example 40 / 48 / 56); no one-off heights.
- [ ] Adjacent type roles differ by a real ratio (about 1.2 to 1.33), never by 1 to 2 px.
- [ ] Icon size is about 1.0 to 1.3 times the label size beside it.
- [ ] Nested radius = outer radius minus padding.
- [ ] Sizes are proportionate to the screen: primary action is the largest control, secondary is smaller.

## 2. Alignment and geometry
- [ ] Shared left/right (or start/end) guides for text, icons and controls.
- [ ] No 1 px offsets; every coordinate on the grid (4 or 8 base), with half-pixel offsets only for odd stroke widths.
- [ ] Optical corrections are deliberate (round shapes, play glyphs, text-to-icon centering) and recorded.
- [ ] Baselines align in mixed rows; text is centered on glyph mass, not the line box.

## 3. Spacing audit
- [ ] Table delivered: edge margins, padding per container type, gaps inside groups, between groups, between sections.
- [ ] Every value is on the scale (run off_scale from Part I); exceptions are named.
- [ ] Gap inside a group is smaller than the gap between groups (proximity).
- [ ] Same component type = identical padding everywhere.
- [ ] Inner padding never exceeds the gap to the neighbour; left and right margins match.

## 4. Micro-detail consistency
- [ ] One stroke width, one border width, one radius family, one shadow recipe.
- [ ] Dividers carry no meaning; meaning-bearing borders meet 3:1 contrast.
- [ ] Icons share grid, stroke, cap and join style; no mixed families.

## 5. Typography
- [ ] Fonts loaded and not substituted; script coverage confirmed with real strings.
- [ ] Roles defined (display, headline, title, body, label, caption, numeric) with size, line-height, weight.
- [ ] Line length about 45 to 75 characters; no widows or orphans in headings.
- [ ] Numerals consistent (one digit style), tabular where columns align.
- [ ] Persian (Mode FA): size and line-height floors from Part H, ZWNJ preserved, no letter-spacing, no justified text.

## 6. Color and contrast (computed)
- [ ] Every text and UI pair has a computed ratio (primary text 7:1 or more target, secondary at least 4.5:1, icons, control borders and focus rings at least 3:1).
- [ ] Color is never the only carrier of meaning; status colors pass color-vision-deficiency simulation.
- [ ] Light and dark themes both checked; accent follows 60-30-10.

## 7. Icons and graphics
- [ ] One family, one weight, license recorded, every meaning from the Inventory covered.
- [ ] 24 px base with live area; 20 and 16 px use optical versions, not scaled-down 24 px.
- [ ] Icon color from semantic tokens only; selected state uses the family's fill or bold variant.
- [ ] Checked at 1x, 2x, 3x for blurry lines.
- [ ] Illustrations use token colors only; alt text correct (empty for decorative).

## 8. States
- [ ] Default, hover, focus-visible, pressed, disabled, loading, error, success, selected, empty are drawn or explicitly deferred.
- [ ] Focus ring is visible, at least 3:1, and not clipped.
- [ ] Error states say what happened and how to recover.

## 9. Content stress
- [ ] Strings 2x longer and very short; 0, 1 and many items; large numbers.
- [ ] Missing image, slow network, offline; skeletons match the final layout.
- [ ] Text scaled to 200% without loss of content or function.
- [ ] Mixed-direction text and bidi isolation tested (Mode FA).

## 10. Motion
- [ ] Every animation has a purpose (orient, confirm, guide).
- [ ] Duration and easing come from tokens; reduced-motion alternative exists.
- [ ] Motion direction follows the reading flow.

## 11. Accessibility and ergonomics
- [ ] Targets at least 44 x 44 pt (iOS), 48 x 48 dp (Android) or 24 x 24 CSS px (WCAG 2.2 AA floor); primary actions larger.
- [ ] Spacing between targets; one-hand reach for frequent actions.
- [ ] Focus order matches reading order; icon-only controls have accessible names.
- [ ] Destructive actions are separated and confirmed or undoable.

## 12. Noise, balance and handoff
- [ ] Grayscale and blur views: one focal point, balanced masses.
- [ ] Squint test and 3-second test pass; primary action found first.
- [ ] No hardcoded fills, strokes, radii, spacing or text properties outside variables and styles.
- [ ] Handoff notes: component-to-code hints, responsive rules, export specs, license notes.
