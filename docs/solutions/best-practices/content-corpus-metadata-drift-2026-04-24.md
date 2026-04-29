---
title: Ship the invariant checker on day one for content corpora with multiple sources of truth
date: 2026-04-24
last_updated: 2026-04-29
category: docs/solutions/best-practices/
module: content-corpus-pipeline
problem_type: best_practice
component: development_workflow
severity: high
applies_when:
  - "A content corpus has slug + hand-written metadata + machine-extractable ground truth (PDF, image, asset) as three coexisting sources of truth"
  - "The curator's mental model of a paper / asset diverges from the published artifact (e.g., author order, classification tag)"
  - "Files are routed into subdirectories driven by metadata, making cross-links structural and breakable"
  - "A derived artifact (README index, site nav, registry) is built from the metadata and propagates errors silently"
  - "The corpus is publicly visible; attribution accuracy affects credibility on first careful read"
  - "The artifact triple has upstream sources (canonical source list, download manifest, schema doc) that the structural validator does not crawl"
related_components:
  - tooling
  - documentation
tags:
  - content-corpus
  - metadata-drift
  - invariant-checker
  - source-of-truth
  - cross-link-integrity
  - subarea-routing
  - pdf-extraction
  - check-coverage
  - co-update-checklist
  - upstream-drift
  - schema-drift
---

# Ship the invariant checker on day one for content corpora with multiple sources of truth

## Context

This repo is a corpus of 24 plain-language English explainers of academic papers on the Economics of AI ([afrtrivi1120/economics-of-ai-explainers](https://github.com/afrtrivi1120/economics-of-ai-explainers)). Each paper has three artifacts that share a `slug` as the primary key: the downloaded PDF, a hand-written metadata JSON, and the explainer markdown.

The corpus was published to a public GitHub repo without any automated invariant checker in place. A subsequent multi-reviewer review surfaced cascading drift across the metadata layer:

- **1 routing error** — `agrawal-gans-goldfarb_2025_research-agenda-tai.md` was filed in `explainers/ai-models-governance/` despite `metadata.subareas[0] = "F"` (which maps to `firms-market-structure/`).
- **6 author-attribution mismatches** — explainer headers (correctly extracted from PDF cover pages) credited different authors than the metadata recorded. E.g., metadata for `restrepo_2024_automation-rent-dissipation.json` listed solo Restrepo; the PDF and explainer correctly named both Acemoglu and Restrepo. Same shape for `johnson_2024` (PDF: Acemoglu + Johnson), `bloom-et-al_2026` (PDF lead: Yotzov, not Bloom), `gans_2025` (PDF: trio, not solo), and `agrawal-gans-goldfarb_2025_research-agenda-tai` (PDF: Brynjolfsson + Korinek + Agrawal, not Agrawal/Gans/Goldfarb).
- **1 wrong PDF/title pair** — `albanesi-et-al_2025_new-tech-jobs-europe.json` claimed the title "New Technologies and Jobs in Europe", but the downloaded PDF (NBER WP 33451) is actually "AI and Women's Employment in Europe" by the same author team.
- **Cross-link breakage** — moving the misrouted file fixed routing but broke 8 inbound cross-links from other explainers.
- **Internal-framing leak** — 7 references to a private organizational marker leaked into a committed plan document despite an explicit memory rule that public artifacts must drop that framing.
- **Bare-slug cross-link** — one cross-link used a directory-relative form `(slug.md)` instead of the canonical `(../subarea/slug.md)`, which would silently break if either file moved.

The post-publication cleanup ran for ~2 hours: 6 fix commits across 3 review rounds, plus the cost of the multi-reviewer LLM pass that surfaced the bugs. The corrective `scripts/check_coverage.py` invariant checker — written *after* the cleanup — is 172 lines of Python and would have flagged every one of the bugs above mechanically before the first push.

## Guidance

**Before publishing any content corpus, ship the invariant checker.**

The pattern applies whenever you have a frozen identifier (slug / primary key / filename stem), hand-authored metadata that references that identifier, and a machine-extractable artifact (PDF, image, compiled asset) whose content is independent ground truth. The checker is cheap; the post-publication cleanup is not.

**Step 1 — Name your sources of truth explicitly before writing any code.**

For this corpus:

| Dimension | Authoritative source | Tie-breaker rule |
|---|---|---|
| Slug | First commit (frozen) | Documented exception process in CLAUDE.md |
| Routing folder | `metadata.subareas[0]` | Metadata wins over file path |
| Author attribution | PDF cover page | PDF wins over metadata; metadata wins over README |
| Title | PDF title page | PDF wins over metadata; metadata wins over README |
| Cross-link form | `../{subarea}/{slug}.md` | Canonical form; bare slugs are an error |

**Step 2 — Designate one winner per dimension and encode it in the checker, not in prose.**

```python
SUBAREA_FOLDER = {
    "L": "labor-productivity", "F": "firms-market-structure",
    "E": "education", "I": "inequality-welfare", "M": "ai-models-governance",
}

def expected_explainer_path(record: dict) -> Path:
    # subareas[0] is canonical — not the folder the file actually landed in
    folder = SUBAREA_FOLDER[record["subareas"][0]]
    return EXPLAINERS_DIR / folder / f"{record['slug']}.md"
```

The checker's job is to hold every layer accountable to the layer above it. If the explainer file isn't where `metadata.subareas[0]` says it should be, the checker fails — regardless of who's "right."

**Step 3 — Make divergence loud, not silent.** The checker should print explicit pass/fail per invariant and exit nonzero on failure, so it can be wired into a `git commit` hook or CI step. A clean run that prints `(no broken cross-links found)` after every commit is worth more than a clean `git log`.

**Step 4 — Document slug exceptions explicitly.** When the slug captures the curator's original framing (e.g., `yuchtman-et-al_2023_*`) but a metadata correction later changes `authors[0]` (PDF cover page actually leads with Beraja), the slug stays per the no-rename rule — but the exception goes in `CLAUDE.md` so future contributors don't open a "fix" PR that renames the file and breaks every inbound cross-link. (See `CLAUDE.md` "Documented slug exceptions" section.)

**Step 5 — Audit the public-facing surface separately from the metadata.** Branding / framing / audience-positioning leaks (e.g., internal organizational markers that end up in a committed plan doc) are a different class of error — they don't fail any structural invariant — but a plain `grep -r "<internal-marker>" public-facing-paths/` step belongs in the same checker run.

**Step 6 — When you add new entries, co-update the upstream and schema files the checker can't see.** *(Added 2026-04-29 after a follow-up six-paper batch replayed adjacent drift.)*

`scripts/check_coverage.py` validates the artifact triple, subarea routing, and cross-link resolution. By construction it cannot detect drift in:

- **Upstream sources** — the canonical source list (`inputs/economists_map.md`) and the download manifest (`scripts/papers.csv`). The validator doesn't crawl them, so adding a paper to the artifact triple while leaving these stale leaves the corpus internally inconsistent and no longer regeneratable from inputs.
- **Schema doc** — fields written into every metadata record (e.g., `download_reason`) are invisible to a check that only verifies file presence and JSON parseability. If a field exists in 30/30 records but isn't in `CLAUDE.md`'s schema, that's silent drift.
- **Index doc** — `README.md` author groupings derived from `metadata.authors[0]` are textual conventions, not validated relations. Curatorial exceptions (e.g., a paper indexed under a senior co-author) need to be documented in `CLAUDE.md` so future contributors don't "fix" them.

Per-paper co-update checklist (one new paper = one new slug):

```
Artifact triple (caught by check_coverage.py):
  [ ] papers/pdfs/{slug}.pdf
  [ ] papers/metadata/{slug}.json   (matches schema in CLAUDE.md)
  [ ] explainers/{subarea}/{slug}.md  (subarea = metadata.subareas[0])

Upstream and indexing (NOT caught by the validator):
  [ ] inputs/economists_map.md      (bullet under existing author OR appendix entry)
  [ ] scripts/papers.csv             (one row so download_papers.py stays idempotent)
  [ ] README.md                      (author section under authors[0]; document any exception)
  [ ] CLAUDE.md                      (only if the addition introduces a new convention,
                                       schema field, or curatorial exception)

Post-batch sanity:
  [ ] python scripts/check_coverage.py        (must pass green)
  [ ] grep authors[0] across new metadata vs. README author sections
  [ ] wc -w explainers/{subarea}/{slug}.md     (verify within the documented band)
```

The checklist exists because the validator exists. They are complements: green validator + skipped checklist still produces silent drift in four files that a careful reader would notice but the machine wouldn't.

## Why This Matters

**Credibility damage is immediate and hard to repair.** A public corpus that attributes a paper to the wrong lead author fails on first careful read by exactly the audience it's trying to serve (in this case, policy researchers who recognize the literature). Six wrong attributions in a 24-paper corpus is a 25% error rate on the most basic field a reader checks.

**Silent drift compounds.** Each new explainer that cites a misattributed slug inherits the error. Cross-links that resolve to the wrong folder silently 404 in GitHub's renderer. A README that groups papers by `metadata.authors[0]` accumulates wrong groupings every time the metadata diverges from PDF reality.

**The arithmetic favors the checker.** Order-of-magnitude estimate from this incident:

- Cost of writing `scripts/check_coverage.py`: ~30 minutes, 172 lines.
- Cost of post-publication cleanup: 6 commits, 1 review pass with 5 specialist agents, ~2 hours of cycle time.

The ratio is roughly 4:1 against skipping the checker on a 24-item corpus. The ratio gets *worse* as the corpus grows — the cleanup cost scales with corpus size, the checker cost is essentially fixed.

**Compound-engineering principle in play:** each unit of engineering work should make subsequent units easier, not harder. A missing invariant checker is a negative-compound artifact — it silently allows drift to accumulate, so every subsequent paper added to the corpus increases the eventual remediation cost.

## When to Apply

Apply this pattern when **two or more** of the following are true:

- The project has a "single source of truth" claim but actually has multiple actual sources (slug + metadata + extractable-from-source is the canonical triad).
- The primary identifier is frozen after first use, making renames expensive.
- Metadata is hand-authored — human error rate is non-zero and not caught by a type system.
- The corpus is publicly visible and attribution / classification accuracy affects credibility.
- Cross-links exist between entries (broken links are invisible without a checker).
- A derived artifact (README, registry, nav, search index) is mechanically generated from the metadata.

Concrete project shapes where this applies directly: documentation sites with author front-matter, dataset catalogs with DOI/citation metadata, configuration registries where keys map to files, monorepos with auto-generated component registries, any DAM/CMS-like structure with structural folders and metadata files.

## Examples

**Real example — routing mismatch from this session.** The metadata for `agrawal-gans-goldfarb_2025_research-agenda-tai` had `subareas: ["F", "M"]`. First tag is `F` → expected folder is `firms-market-structure/`. The file landed in `ai-models-governance/`. The checker output that would have caught this:

```
[FAIL (1)] All cross-links resolve
    - broken cross-link in ../bicycles-for-the-mind.md:
      ../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md
      → file not at expected path
```

Cost without the checker: the file was committed and pushed; later moved (1 file rename); 7 inbound cross-links rewritten via `sed` across 6 explainers + the README; second pass to fix one link the move broke. About 30 minutes of cycle time.

**Real example — author attribution mismatch.** Metadata for `restrepo_2024_automation-rent-dissipation.json` originally:

```json
{ "authors": ["Pascual Restrepo"] }
```

PDF cover page (verified via `pdftotext`):
```
AUTOMATION AND RENT DISSIPATION:
IMPLICATIONS FOR WAGES, INEQUALITY, AND PRODUCTIVITY
Daron Acemoglu
Pascual Restrepo
```

Same shape repeated for `johnson_2024` (PDF: Acemoglu + Johnson, metadata: solo Johnson), `gans_2025` (PDF: Agrawal + Gans + Goldfarb, metadata: solo Gans), `bloom-et-al_2026` (PDF lead: Yotzov; metadata had Bloom first), `agrawal-gans-goldfarb_2025_research-agenda-tai` (PDF: Brynjolfsson + Korinek + Agrawal; metadata: Agrawal + Gans + Goldfarb), and a co-author name typo in `akcigit-et-al_2025` (metadata: "Bradley Chikis"; PDF: "Craig A. Chikis").

A script-level check that diffs `metadata.authors` against text extracted from PDF page 1 would have flagged all six in a single run. Cost without the check: 6 metadata edits, 1 README rebuild (the author groupings shifted significantly — Acemoglu group grew from 2 papers to 4, Yotzov became a brand-new author block, Bloom/Gans/Johnson/Restrepo standalone blocks dissolved), 2 commits.

**Real example — wrong PDF for the metadata title.** The metadata claimed "New Technologies and Jobs in Europe" (the *Economic Policy* paper) but the PDF actually downloaded was NBER WP 33451 "AI and Women's Employment in Europe" (the gender-extension companion by the same authors). The explainer correctly described the gender paper because it read the PDF; the metadata title and the PDF disagreed for ~24 hours after publishing.

A check that compares `metadata.title` against text extracted from PDF page 1 (with fuzzy matching for case / punctuation) would have surfaced this. Fix: 1 metadata edit (title + venue updated to match the PDF that's actually there).

**Real example — six-paper batch replays adjacent drift (2026-04-29).** A second batch added 6 new 2026 papers (corpus 24 → 30). The artifact triple was clean: 6 PDFs, 6 metadata JSON files, 6 explainers in correct subarea folders, README author sections updated, 7 commits pushed, `check_coverage.py` green. A `/ce:review` pass with 6 always-on reviewers surfaced 6 categories of drift the validator did NOT catch:

| Drift | Where | Why missed |
|---|---|---|
| `inputs/economists_map.md` not updated | Stale "canonical source list" | Validator doesn't reach upstream |
| `scripts/papers.csv` not updated | `download_papers.py` reads CSV not the source list | Validator doesn't reach pipeline input |
| README author grouping for Agrawal-Athey paper put it under Susan Athey but `authors[0] = Keshav Agrawal` | Curatorial exception not in CLAUDE.md | No author-vs-README check |
| `download_reason` field in 30/30 metadata records | Field never in CLAUDE.md schema | No JSON schema check |
| All 6 new explainers ran 1648-1825 words | CLAUDE.md said `~600-1500` | No word-count check |
| Two distinct first-author "Agrawals" share slug-prefix space | Convention not surfaced | No collision documentation |

Fix applied per Step 6: bullets added to `inputs/economists_map.md`, 6 rows appended to `scripts/papers.csv`, README-grouping exception documented in CLAUDE.md, schema in CLAUDE.md updated to include `download_reason`, word band widened to `~600-1800`, two-Agrawals disambiguation note added. `check_coverage.py` still passes — exactly the failure mode this learning is named for.

**The checker that shipped:** `scripts/check_coverage.py` — six invariants, ~172 lines, runs in under a second on the 30-paper corpus:

```
$ python scripts/check_coverage.py
Loaded 24 metadata records.

[OK] PDF present for every metadata record
[OK] Explainer present for every metadata record
[OK] No orphan explainers (no matching metadata)
[OK] No orphan PDFs (no matching metadata)
[OK] All cross-links resolve
[OK] All 7 required sections present and ordered

All checks passed.
```

The script is plain Python with no dependencies. It reads `papers/metadata/*.json`, derives the expected explainer path per the `SUBAREA_FOLDER` mapping, walks `explainers/` to find orphans, regexes every `]({path}.md)` cross-link, and asserts each explainer contains the seven required template section headers in order. It does *not* yet check author attribution against PDF text, JSON schema validity, README ↔ metadata index sync, word-count band, page-citation existence, or canonical cross-link form — those are the obvious next invariants to add. Until they exist, Step 6's per-paper checklist is the manual complement.

## Related

- `scripts/check_coverage.py` — the canonical implementation of the invariant-checker pattern in this repo.
- `CLAUDE.md` — see the "Documented slug exceptions" subsection (the slug-vs-`authors[0]` freeze rule is the codified output of one class of invariant violation), and the `authors[0]` clarification under Metadata Schema ("PDF wins, metadata reconciles down").
- `.claude/agents/paper-downloader.md` — the `%PDF` magic-byte check is a live example of an invariant check shipped *inside* an agent prompt rather than as a standalone script. Same pattern, different layer.
- `.claude/agents/paper-explainer.md` — the "cross-link by slug; verify file exists before linking" rule is another inline invariant check at write time.
- `docs/plans/2026-04-24-001-feat-publish-corpus-to-github-plan.md` — the planning doc that explicitly deferred `check_coverage.py` ("out of scope here; track separately") and identified the README-drift risk in passing without prescribing a fix. Adjacent historical context for *why* the checker was missing on day one.
