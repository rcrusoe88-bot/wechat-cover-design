"""Run repository contract checks for the bundled structured-brief examples."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

from cover_quality import TITLE_ZONE, audit_background


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
REGISTERED_THEMES = {f"theme{index}" for index in range(1, 14)}


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
        print((result.stdout or "").strip())
        print((result.stderr or "").strip())
    return ok


def eval_dataset_contract() -> list[str]:
    """Reject stale or malformed trigger/theme datasets before publishing."""
    errors: list[str] = []
    triggers = json.loads((ROOT / "evals" / "trigger_eval.json").read_text(encoding="utf-8"))
    theme_matches = json.loads((ROOT / "evals" / "theme_match_eval.json").read_text(encoding="utf-8"))

    trigger_queries = [item.get("query") for item in triggers if isinstance(item, dict)]
    if len(trigger_queries) != len(triggers) or any(not isinstance(query, str) or not query.strip() for query in trigger_queries):
        errors.append("trigger_eval entries require non-empty query strings")
    if len(set(trigger_queries)) != len(trigger_queries):
        errors.append("trigger_eval contains duplicate queries")
    outcomes = {item.get("should_trigger") for item in triggers if isinstance(item, dict)}
    if outcomes != {True, False}:
        errors.append("trigger_eval must include both positive and negative cases")

    observed_themes: set[str] = set()
    for index, item in enumerate(theme_matches, 1):
        if not isinstance(item, dict) or not isinstance(item.get("article_type"), str):
            errors.append(f"theme_match_eval[{index}] requires article_type")
            continue
        expected = item.get("expected_theme")
        if expected not in REGISTERED_THEMES:
            errors.append(f"theme_match_eval[{index}] references unregistered theme: {expected}")
        else:
            observed_themes.add(expected)
    missing = REGISTERED_THEMES - observed_themes
    if missing:
        errors.append("theme_match_eval has no case for: " + ", ".join(sorted(missing)))
    return errors


def asset_contract() -> list[str]:
    """Keep distributable assets complete, licensed, and intentionally small."""
    errors: list[str] = []
    fonts_dir = ROOT / "assets" / "fonts"
    font_files = {path.name for path in fonts_dir.iterdir() if path.suffix.casefold() in {".ttf", ".otf"}}
    expected_fonts = {"Hanchan-Zhengkai-Big5.ttf", "PreTesto_it.ttf"}
    if font_files != expected_fonts:
        errors.append("bundled fonts must be exactly: " + ", ".join(sorted(expected_fonts)))
    for required in (fonts_dir / "NOTICE.md", fonts_dir / "OFL.txt", ROOT / "requirements.txt", ROOT / "agents" / "openai.yaml"):
        if not required.is_file():
            errors.append(f"missing distribution file: {required.relative_to(ROOT)}")

    titled_thumbs = list((ROOT / "assets" / "theme-previews" / "titled-thumbs").glob("theme*.jpg"))
    if len(titled_thumbs) != 13:
        errors.append(f"expected 13 titled gallery thumbnails, found {len(titled_thumbs)}")
    return errors


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

    invalid_prompt = """Cover plan:
Theme: [selected theme]
Alignment Record:
Article thesis: This deliberately vague record exists only to exercise validation behavior.
Reader takeaway: This text pads an invalid prompt.
Content class: mechanism
Theme rationale: This rationale is long enough but does not select a real theme.
Visual metaphor: An unspecified object represents an unspecified claim.
Element provenance: This sentence is long enough to satisfy a length-only implementation.
Forbidden substitutions: vague shortcut
English image prompt:
Create [focal scientific scene] at 100x100. Overlay something without reserving a left title field or requiring a text-free background.
Negative prompt:
watermark, logo, crowded composition
"""
    dataset_errors = eval_dataset_contract()
    asset_errors = asset_contract()
    preview_checks = []
    for theme_id in range(1, 14):
        preview_path = next((ROOT / "assets" / "theme-previews").glob(f"theme{theme_id}-*.png"))
        preview = Image.open(preview_path).convert("RGB")
        preview_checks.append(
            report(
                f"theme {theme_id} bundled preview passes the quality gate",
                subprocess.CompletedProcess([], 0 if not audit_background(preview, theme_id) else 1),
                0,
            )
        )
    with tempfile.TemporaryDirectory() as temp_dir:
        composed = run(
            "scripts/compose_cover.py",
            "--input",
            "assets/theme-previews/theme3-businessweek.png",
            "--output",
            str(Path(temp_dir) / "cover.png"),
            "--theme",
            "3",
        )
        subtitle_overflow = run(
            "scripts/compose_cover.py",
            "--input",
            "assets/theme-previews/theme3-businessweek.png",
            "--output",
            str(Path(temp_dir) / "overflow.png"),
            "--theme",
            "3",
            "--subtitle-line1",
            "这是一个未经语义换行而且会穿过标题安全区域进入右侧科学主体的超长副标题",
        )
        eyebrow_overflow = run(
            "scripts/compose_cover.py",
            "--input",
            "assets/theme-previews/theme3-businessweek.png",
            "--output",
            str(Path(temp_dir) / "eyebrow-overflow.png"),
            "--theme",
            "3",
            "--eyebrow",
            "THIS EYEBROW IS DELIBERATELY TOO LONG FOR THE FIXED LEFT TITLE FIELD AND MUST BE REJECTED",
        )

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
            "numeric reference markers are not mistaken for placeholders",
            run("scripts/validate_prompt.py", "--all", stdin=final_data["image_prompt"].replace("Article thesis:", "Article thesis: [1]", 1)),
            0,
        ),
        report(
            "invalid prompt package is rejected",
            run("scripts/validate_prompt.py", "--all", stdin=invalid_prompt),
            1,
        ),
        report("default deterministic title composition succeeds", composed, 0),
        report("subtitle overflow is rejected", subtitle_overflow, 1),
        report("eyebrow overflow is rejected", eyebrow_overflow, 1),
        report(
            "provisional structured brief is rejected",
            run("scripts/validate_brief.py", str(provisional_brief)),
            1,
        ),
        report(
            "theme 10 rejects a bright field for light typography",
            subprocess.CompletedProcess([], 0 if not audit_background(bright_field, 10) else 1),
            1,
        ),
        report(
            "theme 12 rejects a bright field for light typography",
            subprocess.CompletedProcess([], 0 if not audit_background(bright_field, 12) else 1),
            1,
        ),
        report(
            "theme 10 accepts a quiet dark title field",
            subprocess.CompletedProcess([], 0 if not audit_background(dark_field, 10) else 1),
            0,
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
        report(
            "trigger and theme evaluation datasets match the current registry",
            subprocess.CompletedProcess([], 0 if not dataset_errors else 1, stdout="\n".join(dataset_errors)),
            0,
        ),
        report(
            "distribution assets and licenses are complete",
            subprocess.CompletedProcess([], 0 if not asset_errors else 1, stdout="\n".join(asset_errors)),
            0,
        ),
        *preview_checks,
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
