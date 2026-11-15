#!/usr/bin/env python3
"""Self-test with synthetic data in a temp folder. Verifies the scripts run; produces no result."""
import csv, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CRIT = ["hierarchy", "usability", "accessibility", "visual_craft", "distinctiveness", "fidelity"]

with tempfile.TemporaryDirectory() as d:
    d = Path(d)
    for s in ["s1", "s2", "s3"]:
        (d / "runs" / s / "A").mkdir(parents=True); (d / "runs" / s / "B").mkdir(parents=True)
    subprocess.run([sys.executable, HERE / "blind.py", d / "runs", "--seed", "1", "--out", d], check=True)
    key = list(csv.DictReader(open(d / "blind-key.csv", encoding="utf-8")))
    assert len(key) == 6 and {r["condition"] for r in key} == {"A", "B"}
    rows = list(csv.DictReader(open(d / "rating-sheet.csv", encoding="utf-8")))
    for r in rows:
        if r["label"].startswith("overall_pick"):
            r["hierarchy"] = "X"
        else:
            for c in CRIT:
                r[c] = "3"
    with open(d / "ratings-r1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    with open(d / "metrics.csv", "w", encoding="utf-8") as f:
        f.write("screen,condition,contrast_failures,target_size_violations,steps_to_main_task,competing_emphasis_levels,notes\ns1,A,2,1,5,3,\ns1,B,0,0,4,1,\n")
    out = subprocess.run([sys.executable, HERE / "aggregate.py", d / "blind-key.csv", d / "ratings-r1.csv", "--metrics", d / "metrics.csv"],
                         capture_output=True, text=True, check=True).stdout
    assert "raters: 1, screens: 3" in out, out
print("selftest OK (synthetic data, not a result)")
