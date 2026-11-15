#!/usr/bin/env python3
"""Sync SKILL.md from the account's cloud copy into this repo, one way (cloud -> repo).

Usage: sync_from_cloud.py CLOUD_SKILL_MD [--init]

Logic (deterministic, so a scheduled agent only has to run it and push):
  - Hash the cloud file (trailing whitespace normalized) and compare with .cloud-sync-hash,
    the hash of the cloud copy last seen.
  - Same hash: the cloud copy did not change since the last check. Do nothing, even if the
    repo differs (repo-side edits are owned by the repo).
  - Different hash: the user saved a new version in the account. Copy it over SKILL.md,
    run scripts/validate.py; if validation fails, restore the old file and exit 2.
  - --init: record the hash without copying (baseline).
Exit codes: 0 nothing to do or updated, 2 validation failed (repo untouched), 3 bad input.
"""
import hashlib, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "ui-redesign-pro" / "SKILL.md"
STATE = ROOT / ".cloud-sync-hash"

def norm(text: str) -> str:
    return text.rstrip() + "\n"

def digest(text: str) -> str:
    return hashlib.sha256(norm(text).encode("utf-8")).hexdigest()

def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    init = "--init" in sys.argv
    if len(args) != 1 or not Path(args[0]).is_file():
        print("usage: sync_from_cloud.py CLOUD_SKILL_MD [--init]")
        return 3
    cloud = Path(args[0]).read_text(encoding="utf-8")
    if not cloud.lstrip().startswith("---") or 'name: "ui-redesign-pro"' not in cloud:
        print("input does not look like the ui-redesign-pro SKILL.md; nothing done")
        return 3
    h = digest(cloud)
    last = STATE.read_text().strip() if STATE.exists() else ""
    if init:
        STATE.write_text(h + "\n")
        print(f"baseline recorded: {h[:12]}")
        return 0
    if h == last:
        print("no change in the cloud copy since the last check")
        return 0
    backup = TARGET.read_text(encoding="utf-8")
    TARGET.write_text(norm(cloud), encoding="utf-8")
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py")], capture_output=True, text=True)
    if r.returncode != 0:
        TARGET.write_text(backup, encoding="utf-8")
        print("validation failed; repo left untouched\n" + r.stdout + r.stderr)
        return 2
    STATE.write_text(h + "\n")
    changed = backup != TARGET.read_text(encoding="utf-8")
    print(f"updated {h[:12]}; SKILL.md {'changed' if changed else 'identical to repo (hash only)'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
