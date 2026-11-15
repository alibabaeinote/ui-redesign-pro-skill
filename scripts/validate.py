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

# Step numbering: steps 0..13 each appear exactly once as a heading.
steps = re.findall(r"^## Step (\d+)\.", text, re.M)
if sorted(map(int, steps)) != list(range(0, 14)):
    errors.append(f"step headings are {steps}, expected 0 to 13 once each")

# Personal-data guard.
for pat in [r"this user's own", r"@gmail\.com", r"alibabaei\.art"]:
    if re.search(pat, text):
        errors.append(f"SKILL.md contains a personal-data pattern: {pat}")

if errors:
    print("FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK: frontmatter, references, step numbering, personal-data guard")
