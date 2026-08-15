#!/usr/bin/env python3
"""Portable prompt checks for wechat-cover-design.

Reads UTF-8 prompt text from stdin and returns 0 only when every selected check passes.
"""

from __future__ import annotations

import argparse
import re
import sys


def check_no_placeholders(text: str) -> tuple[bool, str]:
    found = re.findall(r"\{[^{}]*\}", text)
    if found:
        return False, f"unresolved placeholders: {', '.join(found[:5])}"
    return True, "no unresolved placeholders"


def check_negative(text: str) -> tuple[bool, str]:
    ok = bool(re.search(r"negative\s+prompt\s*:", text, re.I)) or bool(
        re.search(r"\bavoid\s*:", text, re.I)
    )
    return ok, "contains a negative/avoid section" if ok else "missing Negative prompt or Avoid section"


def check_ratio(text: str) -> tuple[bool, str]:
    ok = bool(re.search(r"21\s*:\s*9|2\.3[3-5]\s*:\s*1|\b\d+\s*x\s*\d+\b", text, re.I))
    return ok, "contains a ratio or explicit dimensions" if ok else "missing ratio or dimensions"


def check_length(text: str) -> tuple[bool, str]:
    count = len(text)
    ok = 300 <= count <= 8000
    return ok, f"length {count} characters" if ok else f"length {count} outside 300–8000 characters"


def check_text_strategy(text: str) -> tuple[bool, str]:
    patterns = [
        r"exact(?:ly)?\s+(?:render|display|text)",
        r"(?:render|display)\b.{0,50}\bexact(?:ly)?\b",
        r"small\s+(?:labels?|text|captions?)",
        r"post[- ]?process|overlay|quiet zone|quiet area|后期|小字",
    ]
    ok = any(re.search(pattern, text, re.I) for pattern in patterns)
    return ok, "contains a text-rendering strategy" if ok else "missing a text-rendering strategy"


def check_prompt_only_title(text: str) -> tuple[bool, str]:
    left_field = re.search(r"left(?:-side)?\s+(?:title|text|type)\s+(?:field|zone|area|block)", text, re.I)
    verbatim_title = re.search(r"(?:render|display|title)\s+.{0,50}(?:exact|verbatim)", text, re.I)
    subtitle = re.search(r"\bsubtitle\b", text, re.I)
    labels = re.search(r"\bsmall\s+labels?\b", text, re.I)
    if left_field and verbatim_title and subtitle and labels:
        return True, "contains an explicit left title field plus title, subtitle, and small-label instructions"
    return False, "prompt-only delivery needs an explicit left title field plus title, subtitle, and small-label instructions"


def check_content_alignment(text: str) -> tuple[bool, str]:
    """Require a minimal, inspectable record tying the prompt to the article."""
    required_fields = [
        "Article thesis",
        "Reader takeaway",
        "Content class",
        "Theme rationale",
        "Visual metaphor",
        "Element provenance",
        "Forbidden substitutions",
    ]
    missing = [field for field in required_fields if not re.search(rf"(?im)^\s*{re.escape(field)}\s*:", text)]
    if missing:
        return False, "missing Alignment Record fields: " + ", ".join(missing)

    provenance_match = re.search(
        r"(?ims)^\s*Element provenance\s*:\s*(.+?)(?=^\s*(?:Forbidden substitutions|English image prompt|Negative prompt)\s*:|\Z)",
        text,
    )
    if not provenance_match or len(provenance_match.group(1).strip()) < 25:
        return False, "Element provenance is empty or too vague"

    forbidden_match = re.search(
        r"(?ims)^\s*Forbidden substitutions\s*:\s*(.+?)(?=^\s*(?:English image prompt|Negative prompt)\s*:|\Z)",
        text,
    )
    if not forbidden_match or len(forbidden_match.group(1).strip()) < 10:
        return False, "Forbidden substitutions is empty or too vague"
    return True, "contains a complete Alignment Record"


def run(text: str, args: argparse.Namespace) -> int:
    checks = []
    if args.all or args.no_placeholders:
        checks.append(check_no_placeholders)
    if args.all or args.has_negative:
        checks.append(check_negative)
    if args.all or args.has_ratio:
        checks.append(check_ratio)
    if args.all or args.length:
        checks.append(check_length)
    if args.all or args.text_strategy:
        checks.append(check_text_strategy)
    if args.all or args.content_alignment:
        checks.append(check_content_alignment)
    if args.prompt_only:
        checks.extend(
            [
                check_no_placeholders,
                check_negative,
                check_ratio,
                check_length,
                check_text_strategy,
                check_content_alignment,
                check_prompt_only_title,
            ]
        )

    failed = False
    for check in checks:
        ok, message = check(text)
        print(("PASS" if ok else "FAIL") + ": " + message)
        failed = failed or not ok
    if args.all:
        print("\n" + ("All checks passed." if not failed else "One or more checks failed."))
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a wechat-cover-design prompt from stdin.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true")
    group.add_argument("--no-placeholders", dest="no_placeholders", action="store_true")
    group.add_argument("--has-negative", dest="has_negative", action="store_true")
    group.add_argument("--has-ratio", dest="has_ratio", action="store_true")
    group.add_argument("--length", action="store_true")
    group.add_argument("--text-strategy", dest="text_strategy", action="store_true")
    group.add_argument("--content-alignment", dest="content_alignment", action="store_true")
    group.add_argument("--prompt-only", dest="prompt_only", action="store_true")
    args = parser.parse_args()
    return run(sys.stdin.read(), args)


if __name__ == "__main__":
    raise SystemExit(main())
