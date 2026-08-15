"""Run repository contract checks for the bundled structured-brief examples."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


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
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
