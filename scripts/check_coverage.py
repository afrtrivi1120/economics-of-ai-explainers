#!/usr/bin/env python3
"""
Validate corpus invariants for the Economics-of-AI explainers repo.

Checks performed:
  1. Every paper in papers/metadata/ has a matching PDF in papers/pdfs/.
  2. Every paper in papers/metadata/ has a matching explainer at
     explainers/{subarea}/{slug}.md, where {subarea} is derived from
     metadata.subareas[0].
  3. Every explainer file has a matching metadata record (no orphans).
  4. Every PDF has matching metadata (no orphans).
  5. Every cross-link in every explainer (markdown links to .md files
     under explainers/) resolves to a file on disk.
  6. Every explainer contains the seven required template section
     headers in order.

Exit code: 0 if all checks pass, 1 otherwise. Prints a per-check summary
and a list of failures suitable for piping into a shell or CI step.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
METADATA_DIR = REPO_ROOT / "papers" / "metadata"
PDF_DIR = REPO_ROOT / "papers" / "pdfs"
EXPLAINERS_DIR = REPO_ROOT / "explainers"

SUBAREA_FOLDER = {
    "L": "labor-productivity",
    "F": "firms-market-structure",
    "E": "education",
    "I": "inequality-welfare",
    "M": "ai-models-governance",
}

REQUIRED_SECTIONS = [
    "## 1. Full citation",
    "## 2. Research question",
    "## 3. Method",
    "## 4. Key findings",
    "## 5. Policy implications",
    "## 6. Debates and caveats",
    "## 7. Related readings",
]

LINK_PATTERN = re.compile(r"\]\(([^)]+\.md)\)")


def load_metadata() -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted(METADATA_DIR.glob("*.json"))]


def expected_explainer_path(record: dict) -> Path:
    folder = SUBAREA_FOLDER[record["subareas"][0]]
    return EXPLAINERS_DIR / folder / f"{record['slug']}.md"


def check_pdf_present(records: list[dict]) -> list[str]:
    failures = []
    for r in records:
        pdf = PDF_DIR / f"{r['slug']}.pdf"
        if not pdf.exists():
            failures.append(f"missing PDF for {r['slug']}: expected {pdf.relative_to(REPO_ROOT)}")
    return failures


def check_explainer_present(records: list[dict]) -> list[str]:
    failures = []
    for r in records:
        path = expected_explainer_path(r)
        if not path.exists():
            failures.append(
                f"missing explainer for {r['slug']}: expected {path.relative_to(REPO_ROOT)} "
                f"(subareas={r['subareas']})"
            )
    return failures


def check_no_orphan_explainers(records: list[dict]) -> list[str]:
    expected = {expected_explainer_path(r).resolve() for r in records}
    actual = {p.resolve() for p in EXPLAINERS_DIR.rglob("*.md")}
    return [
        f"orphan explainer (no metadata): {p.relative_to(REPO_ROOT)}"
        for p in sorted(actual - expected)
    ]


def check_no_orphan_pdfs(records: list[dict]) -> list[str]:
    expected = {(PDF_DIR / f"{r['slug']}.pdf").resolve() for r in records}
    actual = {p.resolve() for p in PDF_DIR.glob("*.pdf")}
    return [
        f"orphan PDF (no metadata): {p.relative_to(REPO_ROOT)}"
        for p in sorted(actual - expected)
    ]


def check_cross_links() -> list[str]:
    failures = []
    for f in sorted(EXPLAINERS_DIR.rglob("*.md")):
        text = f.read_text()
        for match in LINK_PATTERN.finditer(text):
            link = match.group(1)
            if link.startswith(("http://", "https://")):
                continue
            target = (f.parent / link).resolve()
            if not target.exists():
                failures.append(
                    f"broken cross-link in {f.relative_to(REPO_ROOT)}: {link} -> "
                    f"{target.relative_to(REPO_ROOT) if REPO_ROOT in target.parents else target}"
                )
    return failures


def check_sections() -> list[str]:
    failures = []
    for f in sorted(EXPLAINERS_DIR.rglob("*.md")):
        text = f.read_text()
        last_pos = -1
        for header in REQUIRED_SECTIONS:
            pos = text.find(header)
            if pos == -1:
                failures.append(f"missing section in {f.relative_to(REPO_ROOT)}: '{header}'")
            elif pos < last_pos:
                failures.append(
                    f"out-of-order section in {f.relative_to(REPO_ROOT)}: "
                    f"'{header}' appears before earlier section"
                )
            else:
                last_pos = pos
    return failures


def main() -> int:
    if not METADATA_DIR.is_dir():
        print(f"ERROR: metadata directory missing: {METADATA_DIR}", file=sys.stderr)
        return 1

    records = load_metadata()
    print(f"Loaded {len(records)} metadata records.\n")

    checks = [
        ("PDF present for every metadata record", check_pdf_present(records)),
        ("Explainer present for every metadata record", check_explainer_present(records)),
        ("No orphan explainers (no matching metadata)", check_no_orphan_explainers(records)),
        ("No orphan PDFs (no matching metadata)", check_no_orphan_pdfs(records)),
        ("All cross-links resolve", check_cross_links()),
        ("All 7 required sections present and ordered", check_sections()),
    ]

    total_failures = 0
    for name, failures in checks:
        marker = "OK" if not failures else f"FAIL ({len(failures)})"
        print(f"[{marker}] {name}")
        for msg in failures:
            print(f"    - {msg}")
        total_failures += len(failures)

    print()
    if total_failures == 0:
        print("All checks passed.")
        return 0
    print(f"{total_failures} failure(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
