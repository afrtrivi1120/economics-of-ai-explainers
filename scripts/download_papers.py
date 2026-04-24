#!/usr/bin/env python3
"""Download Economics-of-AI paper PDFs from scripts/papers.csv.

Writes PDFs to papers/pdfs/{slug}.pdf and metadata to papers/metadata/{slug}.json.
Validates %PDF magic bytes; never saves HTML as .pdf. Idempotent — skips valid
existing downloads.

Usage:
    python scripts/download_papers.py                 # download all
    python scripts/download_papers.py --slug NAME     # single paper
    python scripts/download_papers.py --force         # re-download existing
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "scripts" / "papers.csv"
PDF_DIR = ROOT / "papers" / "pdfs"
META_DIR = ROOT / "papers" / "metadata"

USER_AGENT = (
    "Mozilla/5.0 (compatible; ai-papers-explainers/0.1; "
    "+contact andresrivera1120@gmail.com)"
)
RATE_LIMIT_SEC = 1.0  # polite delay between requests to the same host


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return f.read(4) == b"%PDF"
    except OSError:
        return False


def fetch(url: str, dest: Path, timeout: int = 60) -> tuple[bool, str]:
    """Download `url` to `dest`. Returns (ok, reason)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = resp.headers.get("Content-Type", "").lower()
            data = resp.read()
    except urllib.error.HTTPError as e:
        return False, f"http {e.code}"
    except urllib.error.URLError as e:
        return False, f"urlerror {e.reason}"
    except TimeoutError:
        return False, "timeout"
    except Exception as e:  # noqa: BLE001
        return False, f"error {type(e).__name__}: {e}"

    if not data.startswith(b"%PDF") and "pdf" not in ctype:
        return False, f"not-pdf (content-type={ctype or 'unknown'})"
    if not data.startswith(b"%PDF"):
        return False, "invalid-magic"

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return True, "ok"


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def process(row: dict[str, str], force: bool) -> dict[str, str]:
    slug = row["slug"]
    pdf_path = PDF_DIR / f"{slug}.pdf"
    meta_path = META_DIR / f"{slug}.json"

    status = "ok"
    reason = "cached"

    if force or not (pdf_path.exists() and is_pdf(pdf_path)):
        ok, reason = fetch(row["pdf_url"], pdf_path)
        status = "ok" if ok else "failed"
        time.sleep(RATE_LIMIT_SEC)
    else:
        reason = "exists"

    meta = {
        "slug": slug,
        "title": row["title"],
        "authors": [a.strip() for a in row["authors"].split(";") if a.strip()],
        "year": int(row["year"]) if row["year"].isdigit() else row["year"],
        "venue": row["venue"],
        "subareas": [s.strip() for s in row["subareas"].split(",") if s.strip()],
        "source_url": row["source_url"],
        "pdf_url": row["pdf_url"],
        "pdf_path": f"papers/pdfs/{slug}.pdf" if status == "ok" else None,
        "download_status": status if status == "ok" else "manual",
        "download_reason": reason,
        "download_date": date.today().isoformat(),
    }
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return {"slug": slug, "status": status, "reason": reason}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", help="Download only this slug")
    parser.add_argument("--force", action="store_true", help="Re-download existing PDFs")
    args = parser.parse_args()

    rows = load_rows()
    if args.slug:
        rows = [r for r in rows if r["slug"] == args.slug]
        if not rows:
            print(f"No row with slug={args.slug!r} in {CSV_PATH}", file=sys.stderr)
            return 2

    results = [process(r, force=args.force) for r in rows]

    ok = sum(1 for r in results if r["status"] == "ok")
    failed = [r for r in results if r["status"] != "ok"]
    print(f"\n--- Summary: {ok}/{len(results)} ok ---")
    for r in results:
        marker = "OK  " if r["status"] == "ok" else "FAIL"
        print(f"  [{marker}] {r['slug']} ({r['reason']})")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
