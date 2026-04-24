# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Repository of **plain-language explainers for academic papers on the Economics of AI**, aimed at a Colombian policy/research audience (CEPE). Each paper in `inputs/economists_map.md` eventually gets: (1) a downloaded PDF, (2) a structured metadata record, (3) a Spanish/English explainer, and (4) a commit + push to GitHub.

## Repository Layout

```
inputs/economists_map.md           Canonical source list of authors + papers (do not edit)
papers/pdfs/{slug}.pdf              Downloaded full-text PDFs, one per paper
papers/metadata/{slug}.json         Bibliographic + source metadata (see schema below)
explainers/{subarea}/{slug}.md      Explainer markdown, filed by sub-area tag
scripts/download_papers.py          Bulk PDF downloader (NBER / SSRN / SF Fed / direct URLs)
.claude/agents/                     Custom subagents (see "Agents" section)
```

Sub-areas mirror the tags used in `inputs/economists_map.md`:
`labor-productivity` [L], `firms-market-structure` [F], `education` [E], `inequality-welfare` [I], `ai-models-governance` [M].

## Slug Convention

`{firstauthor-lastname}_{year}_{short-title}` — lowercase, hyphenated, ASCII only.
Example: `acemoglu_2024_simple-macro-ai`, `brynjolfsson-li-raymond_2025_genai-at-work`.

The slug is the shared key across `papers/pdfs/`, `papers/metadata/`, and `explainers/*/`. Never rename a slug once it has an explainer checked in.

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
  "abstract": "...",
  "download_status": "ok | failed | manual",
  "download_date": "YYYY-MM-DD"
}
```

## Common Commands

```bash
# Download all papers in inputs/economists_map.md (idempotent — skips existing PDFs)
python scripts/download_papers.py

# Download a single paper by slug
python scripts/download_papers.py --slug acemoglu_2024_simple-macro-ai

# Validate that every metadata record has a matching PDF and explainer (or known gap)
python scripts/check_coverage.py
```

## Agents

Invoke these via the `Agent` tool with the matching `subagent_type`. All three live in `.claude/agents/`.

- **paper-downloader** — resolves a paper reference to a direct PDF URL (NBER, SSRN, SF Fed, repec, author pages) and writes the PDF + metadata JSON. Validates `%PDF` magic bytes; never saves HTML/captcha pages with a `.pdf` extension. Must NOT fabricate URLs.
- **paper-explainer** — reads a downloaded PDF and produces `explainers/{subarea}/{slug}.md` using the explainer template (see "Explainer Template" below). Must cite specific page numbers for quantitative claims and never invent numbers.
- **github-publisher** — stages, commits, and pushes changes. Groups commits by paper (one commit per paper: PDF + metadata + explainer). Never force-pushes. Never bypasses hooks.

## Explainer Template

Every `explainers/*/{slug}.md` has this structure (bilingual: Spanish headers with English sub-content acceptable, or vice versa — match the audience):

1. **Cita / Citation** — full bibliographic reference + link to PDF.
2. **Pregunta / Question** — 1–2 sentences: what does the paper ask?
3. **Método / Method** — data, identification strategy, key assumptions.
4. **Hallazgos principales / Key findings** — 3–6 bullets with quantitative results and page citations `(p. N)`.
5. **Para política pública / Policy implications** — Colombia-relevant takeaways.
6. **Debates y caveats** — where this paper disagrees with others in the field (e.g., Acemoglu's conservative TFP estimate vs. Aghion's optimistic one).
7. **Lecturas relacionadas** — cross-links to other explainers in this repo by slug.

## Content Rules

- **Never fabricate numbers, quotes, or citations.** If a quantitative claim is not on the cited page, drop it.
- **Flag divergence explicitly** — the field has genuine disagreement on AI's macro impact (e.g., Acemoglu ≈0.66% TFP gain/10yr vs. Aghion ≈0.8–1.3pp/yr). Explainers should foreground this, not paper over it.
- **Respect the source list.** `inputs/economists_map.md` is the canonical scope. New papers go in only if they are cited by an author already in the map, or the user explicitly adds them.
- **PDFs are binary artifacts.** They belong in `papers/pdfs/` and should be committed (not gitignored) — this repo is a reference corpus, not a codebase. If the corpus grows past ~100 MB, revisit with Git LFS before adding more.

## Governance Boundary

This repo is a personal/CEPE research corpus, not the CEPE Bayesian decision pipeline (that lives in a separate project). Do not copy CEPE protocol documents, proposal data, or committee-facing memos into this repo.
