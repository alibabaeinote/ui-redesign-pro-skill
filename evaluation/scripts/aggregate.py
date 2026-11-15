#!/usr/bin/env python3
"""Aggregate blind ratings. Reports means, differences, wins/ties/losses. No p-values: n is too small."""
import argparse, csv, statistics as st
from collections import defaultdict
from pathlib import Path

CRITERIA = ["hierarchy", "usability", "accessibility", "visual_craft", "distinctiveness", "fidelity"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key", type=Path)
    ap.add_argument("ratings", type=Path, nargs="+")
    ap.add_argument("--metrics", type=Path)
    a = ap.parse_args()
    key = {(r["screen"], r["label"]): r["condition"] for r in csv.DictReader(open(a.key, encoding="utf-8"))}
    scores = defaultdict(list)          # (criterion, condition) -> values
    per_screen = defaultdict(lambda: defaultdict(list))  # screen -> condition -> overall means
    picks = {"A": 0, "B": 0, "tie": 0}
    for path in a.ratings:
        for r in csv.DictReader(open(path, encoding="utf-8")):
            lab = r["label"]
            if lab.startswith("overall_pick"):
                v = (r.get("hierarchy") or "").strip()  # pick is written in the first criterion cell
                cond = key.get((r["screen"], v))
                picks[cond if cond else "tie"] += 1
                continue
            cond = key[(r["screen"], lab)]
            vals = []
            for c in CRITERIA:
                if r[c].strip():
                    v = float(r[c]); scores[(c, cond)].append(v); vals.append(v)
            if vals:
                per_screen[r["screen"]][cond].append(st.mean(vals))
    n_raters = len(a.ratings)
    print(f"raters: {n_raters}, screens: {len(per_screen)}")
    print(f"{'criterion':16}{'A mean':>8}{'B mean':>8}{'B-A':>8}")
    for c in CRITERIA:
        ma = st.mean(scores[(c, 'A')]) if scores[(c, 'A')] else float('nan')
        mb = st.mean(scores[(c, 'B')]) if scores[(c, 'B')] else float('nan')
        print(f"{c:16}{ma:8.2f}{mb:8.2f}{mb-ma:8.2f}")
    w = l = t = 0
    for s, d in sorted(per_screen.items()):
        if d["A"] and d["B"]:
            diff = st.mean(d["B"]) - st.mean(d["A"])
            w, l, t = w + (diff > 0), l + (diff < 0), t + (diff == 0)
            print(f"  {s}: B-A = {diff:+.2f}")
    print(f"screens where B scored higher / lower / equal: {w} / {l} / {t}")
    print(f"overall picks (A / B / tie): {picks['A']} / {picks['B']} / {picks['tie']}")
    if a.metrics:
        rows = list(csv.DictReader(open(a.metrics, encoding="utf-8")))
        for col in ["contrast_failures", "target_size_violations", "steps_to_main_task", "competing_emphasis_levels"]:
            by = defaultdict(list)
            for r in rows:
                if r[col].strip():
                    by[r["condition"]].append(float(r[col]))
            print(f"{col}: A mean {st.mean(by['A']) if by['A'] else float('nan'):.2f}, B mean {st.mean(by['B']) if by['B'] else float('nan'):.2f}")
    print("Limits: small n, few raters, one model version. Do not report p-values or write 'proven'.")

if __name__ == "__main__":
    main()
