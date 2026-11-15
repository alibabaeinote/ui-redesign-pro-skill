# Pipeline

```mermaid
flowchart TD
  S0[0 Locale Gate] --> S1[1 Frame: inventory, audit P1..Pn, baseline]
  S1 --> S2[2 Calibrate: change level, interaction mode, output]
  S2 --> S3[3 Benchmark + screen-type playbook]
  S3 --> S4[4 Diverge: three structural versions]
  S4 --> S5[5 Combine best of three]
  S5 --> S6[6 Converge: usability, components, navigation]
  S6 --> S7[7 Ground in an established system]
  S7 --> S8[8 Type, color, icons, design system]
  S8 --> S9[9 Build]
  S9 --> S10[10 Pixel-perfect pass]
  S10 --> S11[11 Checks and review]
  S11 --> S12[12 Deliver]
  S12 --> S13[13 Management report]
  S6 -. skeleton-level problem .-> S5
```

## Authority
The skeleton (organization, grouping, navigation model, component set) is free in steps 4 and 5 and fixed from step 6, except that step 6.8 may swap individual components inside it.

Precedence when rules collide: (1) the user's brief and pinned constraints, (2) the Commitment and honesty (A4), (3) accessibility and ergonomic floors, (4) the later step over the earlier one, (5) the quieter, clearer, more exact option.

## Traceability
Every audit problem gets a number (P1..Pn) in step 1. Every decision in step 13 points to a P-number, or is labeled an identity or brand choice. This is what makes the final report defensible.
