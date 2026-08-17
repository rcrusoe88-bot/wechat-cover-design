"""Run repository contract checks for the bundled structured-brief examples."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw

from cover_quality import TITLE_ZONE, audit_background


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(*args: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [PYTHON, *args],
        cwd=ROOT,
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
    )


def report(label: str, result: subprocess.CompletedProcess[str], expected: int) -> bool:
    ok = result.returncode == expected
    print(("PASS" if ok else "FAIL") + f": {label}")
    if not ok:
        print(result.stdout.strip())
        print(result.stderr.strip())
    return ok


def main() -> int:
    final_brief = ROOT / "evals" / "brief_final_valid.json"
    provisional_brief = ROOT / "evals" / "brief_provisional_rejected.json"
    final_data = json.loads(final_brief.read_text(encoding="utf-8"))

    bright_field = Image.new("RGB", (1584, 672), "#F6F4EA")
    dark_field = Image.new("RGB", (1584, 672), "#193F54")
    busy_field = Image.new("RGB", (1584, 672), "#F6F4EA")
    busy_draw = ImageDraw.Draw(busy_field)
    for x in range(TITLE_ZONE[0], TITLE_ZONE[2], 12):
        busy_draw.line((x, TITLE_ZONE[1], x, TITLE_ZONE[3]), fill="#183E56", width=4)
    intrusion_field = Image.new("RGB", (1584, 672), "#F6F4EA")
    intrusion_draw = ImageDraw.Draw(intrusion_field)
    intrusion_draw.line((TITLE_ZONE[0] + 16, 300, TITLE_ZONE[2] - 12, 300), fill="#183E56", width=5)
    intrusion_draw.ellipse((360, 245, 470, 355), outline="#183E56", width=5)

    checks = [
        report(
            "final structured brief is accepted",
            run("scripts/validate_brief.py", str(final_brief)),
            0,
        ),
        report(
            "final prompt package passes --all",
            run("scripts/validate_prompt.py", "--all", stdin=final_data["image_prompt"]),
            0,
        ),
        report(
            "provisional structured brief is rejected",
            run("scripts/validate_brief.py", str(provisional_brief)),
            1,
        ),
        report(
            "theme 10 accepts a quiet bright title field",
            subprocess.CompletedProcess([], 0 if not audit_background(bright_field, 10) else 1),
            0,
        ),
        report(
            "theme 12 accepts a quiet bright title field",
            subprocess.CompletedProcess([], 0 if not audit_background(bright_field, 12) else 1),
            0,
        ),
        report(
            "theme 10 rejects a dark low-contrast title field",
            subprocess.CompletedProcess([], 1 if audit_background(dark_field, 10) else 0),
            1,
        ),
        report(
            "quality gate rejects a busy title field",
            subprocess.CompletedProcess([], 1 if audit_background(busy_field, 12) else 0),
            1,
        ),
        report(
            "quality gate rejects a long chart or process mark in the title field",
            subprocess.CompletedProcess([], 1 if audit_background(intrusion_field, 9) else 0),
            1,
        ),
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
