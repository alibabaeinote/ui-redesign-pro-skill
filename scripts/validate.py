#!/usr/bin/env python3
"""Validate the skill package. Exit code 1 on any failure."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "ui-redesign-pro"
errors = []

skill = SKILL_DIR / "SKILL.md"
text = skill.read_text(encoding="utf-8")

m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("SKILL.md: missing frontmatter")
    front = ""
else:
    front = m.group(1)

name = re.search(r'^name:\s*"?([^"\n]+)"?\s*$', front, re.M)
desc = re.search(r'^description:\s*"(.*)"\s*$', front, re.M)
if not name:
    errors.append("frontmatter: name missing")
elif name.group(1).strip() != SKILL_DIR.name:
    errors.append(f"frontmatter: name '{name.group(1)}' != folder '{SKILL_DIR.name}'")
if not desc:
    errors.append("frontmatter: description missing")
else:
    d = desc.group(1)
    if len(d) > 1024:
        errors.append(f"description is {len(d)} chars (max 1024)")
    if "<" in d or ">" in d:
        errors.append("description contains angle brackets")

# Every referenced file must exist, and every reference file must be referenced.
referenced = set(re.findall(r"`references/([\w\-]+\.md)`", text))
existing = {p.name for p in (SKILL_DIR / "references").glob("*.md")}
for r in sorted(referenced - existing):
    errors.append(f"referenced but missing: references/{r}")
for r in sorted(existing - referenced):
    errors.append(f"present but never referenced: references/{r}")

# Structure: five stages, each once, in order, with the expected sub-sections.
stages = re.findall(r"^# Stage (\d+)\.", text, re.M)
if list(map(int, stages)) != [1, 2, 3, 4, 5]:
    errors.append(f"stage headings are {stages}, expected 1 to 5 once each, in order")
expected_subs = ["1.1", "1.2", "1.3", "3.1", "3.2"] + [f"4.{i}" for i in range(1, 10)] + ["5.1", "5.2"]
subs = re.findall(r"^## (\d\.\d) ", text, re.M)
if subs != expected_subs:
    errors.append(f"sub-sections are {subs}, expected {expected_subs}")
if re.search(r"^## Step \d+\.", text, re.M):
    errors.append("old 'Step N' headings still present")
# Personal-data guard.
for pat in [r"this user's own", r"@gmail\.com", r"alibabaei\.art"]:
    if re.search(pat, text):
        errors.append(f"SKILL.md contains a personal-data pattern: {pat}")

if errors:
    print("FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK: frontmatter, references, five-stage structure, personal-data guard")
