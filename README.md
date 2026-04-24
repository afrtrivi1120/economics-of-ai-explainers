# AI Papers Explainers

A reference corpus of **plain-language explainers for academic papers on the Economics of AI**, aimed at a Colombian policy/research audience (CEPE).

Each paper in the corpus has:
1. A downloaded PDF — `papers/pdfs/{slug}.pdf`
2. A metadata record — `papers/metadata/{slug}.json`
3. A bilingual (Spanish/English) explainer — `explainers/{subarea}/{slug}.md`

## Sub-areas

| Tag | Folder | Scope |
|-----|--------|-------|
| [L] | `labor-productivity`       | Labor markets and productivity |
| [F] | `firms-market-structure`   | Firm behavior, adoption, market structure |
| [E] | `education`                | AI in education and human capital |
| [I] | `inequality-welfare`       | Inequality, welfare, distribution |
| [M] | `ai-models-governance`     | Economics of AI models, scaling, governance |

## Source list

The canonical scope of the corpus lives in [`inputs/economists_map.md`](inputs/economists_map.md) — a curated map of leading US and European economists working on AI, organized by sub-area. New papers enter the corpus only when authored by (or co-authored with) someone in that map.

## How it works

Three subagents live in [`.claude/agents/`](.claude/agents/):

- **`paper-downloader`** — resolves paper references to direct PDF URLs (NBER, SSRN, SF Fed, RePEc, author pages), downloads, validates `%PDF` magic bytes, and writes metadata JSON.
- **`paper-explainer`** — reads a downloaded PDF and writes a structured bilingual explainer with page-cited quantitative claims.
- **`github-publisher`** — groups one commit per paper (PDF + metadata + explainer), never force-pushes, never bypasses hooks.

Full operating rules and file conventions are in [`CLAUDE.md`](CLAUDE.md).

## Usage

```bash
# Download / refresh PDFs from the curated list
python scripts/download_papers.py

# Single paper
python scripts/download_papers.py --slug acemoglu_2024_simple-macro-ai
```

Current corpus: **24 papers, ~20 MB of open-access PDFs** — see `scripts/papers.csv` for the seed list.
