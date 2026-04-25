# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Repository of **plain-language English explainers for academic papers on the Economics of AI**. Each paper in `inputs/economists_map.md` eventually gets: (1) a downloaded PDF, (2) a structured metadata record, (3) an English explainer, and (4) a commit + push to GitHub.

## Repository Layout

```
inputs/economists_map.md           Canonical source list of authors + papers (do not edit)
papers/pdfs/{slug}.pdf              Downloaded full-text PDFs, one per paper
papers/metadata/{slug}.json         Bibliographic + source metadata (see schema below)
explainers/{subarea}/{slug}.md      Explainer markdown, filed by sub-area tag
scripts/download_papers.py          Bulk PDF downloader (NBER / SSRN / SF Fed / direct URLs)
scripts/check_coverage.py           Validates corpus invariants (slugs, routing, links, sections)
docs/solutions/                     Documented learnings from past work (best practices, bug fixes, workflow patterns), organized by category with YAML frontmatter (module, tags, problem_type)
docs/plans/                         Implementation plans for non-trivial work
.claude/agents/                     Custom subagents (see "Agents" section)
```

Sub-areas mirror the tags used in `inputs/economists_map.md`:
`labor-productivity` [L], `firms-market-structure` [F], `education` [E], `inequality-welfare` [I], `ai-models-governance` [M].

## Slug Convention

`{firstauthor-lastname}_{year}_{short-title}` — lowercase, hyphenated, ASCII only.
Example: `acemoglu_2024_simple-macro-ai`, `brynjolfsson-li-raymond_2025_genai-at-work`.

The slug is the shared key across `papers/pdfs/`, `papers/metadata/`, and `explainers/*/`. Never rename a slug once it has an explainer checked in.

### Documented slug exceptions

When a slug predates a metadata correction that changes `authors[0]`, the slug stays (per the no-rename rule). Currently exempt:

- `yuchtman-et-al_2023_exporting-surveillance-state` — `authors[0]` is Martin Beraja in the corrected metadata, but the slug still uses `yuchtman-et-al` from the original source-list framing. The README correctly indexes the paper under Beraja.

## Metadata Schema (`papers/metadata/{slug}.json`)

```json
{
  "slug": "...",
  "title": "...",
  "authors": ["Firstname Lastname", ...],
  "year": 2024,
  "venue": "NBER WP 32487 | AER | QJE | ...",
  "subareas": ["L", "I", "M"],
  "source_url": "https://www.nber.org/...",
  "pdf_url": "https://www.nber.org/system/files/working_papers/w32487/w32487.pdf",
  "pdf_path": "papers/pdfs/acemoglu_2024_simple-macro-ai.pdf",
  "download_status": "ok | failed | manual",
  "download_date": "YYYY-MM-DD"
}
```

`authors[0]` is the **first author of the actual PDF** (not the curator's preferred index name) and drives both subarea routing and README author grouping. When corpus-side conventions and PDF reality conflict, the PDF wins and the metadata is corrected to match.

## Common Commands

```bash
# Download all papers in inputs/economists_map.md (idempotent — skips existing PDFs)
python scripts/download_papers.py

# Download a single paper by slug
python scripts/download_papers.py --slug acemoglu_2024_simple-macro-ai

# Validate that every metadata record has a matching PDF and explainer,
# explainer is in the correct subarea folder, and cross-links resolve
python scripts/check_coverage.py
```

## Agents

Invoke these via the `Agent` tool with the matching `subagent_type`. All three live in `.claude/agents/`.

- **paper-downloader** — resolves a paper reference to a direct PDF URL (NBER, SSRN, SF Fed, repec, author pages) and writes the PDF + metadata JSON. Validates `%PDF` magic bytes; never saves HTML/captcha pages with a `.pdf` extension. Must NOT fabricate URLs.
- **paper-explainer** — reads a downloaded PDF and produces `explainers/{subarea}/{slug}.md` using the explainer template (see `.claude/agents/paper-explainer.md`). Must cite specific page numbers for quantitative claims and never invent numbers. Output is English-only.
- **github-publisher** — stages, commits, and pushes changes. Groups commits by paper (one commit per paper: PDF + metadata + explainer). Never force-pushes. Never bypasses hooks.

## Explainer Template (English only)

Every `explainers/*/{slug}.md` follows this structure:

1. **Full citation** — bibliographic reference + link to PDF.
2. **Research question** — 1–2 sentences: what does the paper ask?
3. **Method** — data, identification strategy, key assumptions.
4. **Key findings** — 3–6 bullets with quantitative results and page citations `(p. N)`.
5. **Policy implications** — concrete takeaways for AI, education, or labor policy.
6. **Debates and caveats** — where this paper disagrees with others in the corpus (e.g., Acemoglu's conservative TFP estimate vs. Aghion's optimistic one). Cite by slug.
7. **Related readings** — cross-links to other explainers in this repo by slug.

Length: ~600–1500 words. Tone: plain, accessible English for a non-specialist policy audience. The aim of an explainer is to dissect a paper into simple language — strip the academic apparatus, keep the substance.

## Content Rules

- **Never fabricate numbers, quotes, or citations.** If a quantitative claim is not on the cited page, drop it.
- **Flag divergence explicitly** — the field has genuine disagreement on AI's macro impact (e.g., Acemoglu ≈0.66% TFP gain/10yr vs. Aghion ≈0.8–1.3pp/yr). Explainers should foreground this, not paper over it.
- **Respect the source list.** `inputs/economists_map.md` is the canonical scope. New papers go in only if they are cited by an author already in the map, or the user explicitly adds them.
- **PDFs are binary artifacts.** They belong in `papers/pdfs/` and should be committed (not gitignored) — this repo is a reference corpus, not a codebase. If the corpus grows past ~100 MB, revisit with Git LFS before adding more.

## Governance Boundary

This repo is a personal research corpus, separate from any decision pipelines that may live in other projects. Do not import committee-facing memos, proposal data, or protocol PDFs from those projects here.
