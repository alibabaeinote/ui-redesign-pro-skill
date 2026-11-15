#!/usr/bin/env python3
"""Create a blinded rating sheet and a private key from runs/<screen>/{A,B}/."""
import argparse, csv, random
from pathlib import Path

CRITERIA = ["hierarchy", "usability", "accessibility", "visual_craft", "distinctiveness", "fidelity"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", type=Path)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--out", type=Path, default=Path("."))
    a = ap.parse_args()
    rng = random.Random(a.seed)
    screens = sorted(p.name for p in a.runs.iterdir() if (p / "A").is_dir() and (p / "B").is_dir())
    if not screens:
        raise SystemExit("no screens with both A/ and B/ folders found")
    key, sheet = [], []
    for s in screens:
        order = ["A", "B"]
        rng.shuffle(order)
        for label, cond in zip(["X", "Y"], order):
            key.append({"screen": s, "label": label, "condition": cond})
            sheet.append({"screen": s, "label": label, **{c: "" for c in CRITERIA}, "weakness": ""})
        sheet.append({"screen": s, "label": "overall_pick(X/Y/tie)", **{c: "" for c in CRITERIA}, "weakness": ""})
    with open(a.out / "blind-key.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["screen", "label", "condition"]); w.writeheader(); w.writerows(key)
    with open(a.out / "rating-sheet.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["screen", "label", *CRITERIA, "weakness"]); w.writeheader(); w.writerows(sheet)
    print(f"{len(screens)} screens blinded. Keep blind-key.csv away from raters.")

if __name__ == "__main__":
    main()
