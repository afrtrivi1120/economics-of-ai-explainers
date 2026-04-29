# Economics of AI — Paper Explainers

A reference corpus of **plain-language explainers for academic papers on the Economics of AI**.

Each paper in the corpus has three artifacts:

1. The downloaded full-text PDF — `papers/pdfs/{slug}.pdf`
2. A bibliographic metadata record — `papers/metadata/{slug}.json`
3. An explainer — `explainers/{subarea}/{slug}.md`

Every explainer follows a fixed 7-section template (full citation, research question, method, key findings, policy implications, debates and caveats, related readings) and **cites a page number for every quantitative claim**. The aim of an explainer is to dissect a paper into clear, accessible language for a non-specialist policy audience — strip the academic apparatus, keep the substance. Where the literature genuinely disagrees — most notably on the macroeconomic impact of AI — the divergence is foregrounded, not papered over.

## Sub-areas

| Tag | Folder | Scope |
|-----|--------|-------|
| `[L]` | [`explainers/labor-productivity/`](explainers/labor-productivity/) | Labor markets and productivity |
| `[F]` | [`explainers/firms-market-structure/`](explainers/firms-market-structure/) | Firm behavior, adoption, market structure |
| `[E]` | [`explainers/education/`](explainers/education/) | AI in education and human capital |
| `[I]` | [`explainers/inequality-welfare/`](explainers/inequality-welfare/) | Inequality, welfare, distribution |
| `[M]` | [`explainers/ai-models-governance/`](explainers/ai-models-governance/) | Economics of AI models, scaling, governance |

A paper's home folder is its **first** sub-area tag in the metadata (e.g., `[L, I, M]` → `labor-productivity/`).

## Papers by author

Listed alphabetically by first author's surname. Every entry links to the explainer (clickable) and the underlying PDF. Co-authors are noted in parentheses.

### Acemoglu, Daron — MIT
- **[Artificial Intelligence, Automation and Work](explainers/labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md)** `[L,I]` — 2018, NBER WP 24196 (with Pascual Restrepo) · [PDF](papers/pdfs/acemoglu-restrepo_2018_ai-automation-work.pdf)
- **[The Simple Macroeconomics of AI](explainers/labor-productivity/acemoglu_2024_simple-macro-ai.md)** `[L,I,M]` — 2024, NBER WP 32487 · [PDF](papers/pdfs/acemoglu_2024_simple-macro-ai.pdf)
- **[Learning from Ricardo and Thompson: Machinery and Labor in the Early Industrial Revolution, and in the Age of AI](explainers/labor-productivity/johnson_2024_ricardo-thompson-ai.md)** `[L,I,M]` — 2024, NBER WP 32416 (with Simon Johnson) · [PDF](papers/pdfs/johnson_2024_ricardo-thompson-ai.pdf)
- **[Automation and Rent Dissipation](explainers/labor-productivity/restrepo_2024_automation-rent-dissipation.md)** `[L,I]` — 2024, NBER WP 32536 (with Pascual Restrepo) · [PDF](papers/pdfs/restrepo_2024_automation-rent-dissipation.pdf)
- **[AI, Human Cognition and Knowledge Collapse](explainers/ai-models-governance/acemoglu-kong-ozdaglar_2026_knowledge-collapse.md)** `[M,I]` — 2026, NBER WP 34910 (with Dingwen Kong, Asuman Ozdaglar) · [PDF](papers/pdfs/acemoglu-kong-ozdaglar_2026_knowledge-collapse.pdf)

### Aghion, Philippe — Collège de France / LSE / INSEAD
- **[Artificial Intelligence and Economic Growth](explainers/ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md)** `[M]` — 2017, NBER WP 23928 (with Benjamin Jones, Charles I. Jones) · [PDF](papers/pdfs/aghion-jones-jones_2017_ai-economic-growth.pdf)
- **[AI and Growth: Where Do We Stand?](explainers/labor-productivity/aghion-bunel_2024_ai-and-growth.md)** `[L,M]` — 2024, SF Fed Working Paper (with Simon Bunel) · [PDF](papers/pdfs/aghion-bunel_2024_ai-and-growth.pdf)

### Agrawal, Ajay K. — University of Toronto, Rotman
- **[The Economics of Bicycles for the Mind](explainers/firms-market-structure/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.md)** `[F,M]` — 2025, NBER WP 34034 (with Joshua S. Gans, Avi Goldfarb) · [PDF](papers/pdfs/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.pdf)
- **[Genius on Demand: The Value of Transformative AI](explainers/firms-market-structure/gans_2025_genius-on-demand.md)** `[F,M]` — 2025, NBER WP 34316 (with Joshua S. Gans, Avi Goldfarb) · [PDF](papers/pdfs/gans_2025_genius-on-demand.pdf)
- **[AI in Science](explainers/ai-models-governance/agrawal-mchale-oettl_2026_ai-in-science.md)** `[M,F]` — 2026, NBER WP 34953 (with John McHale, Alexander Oettl) · [PDF](papers/pdfs/agrawal-mchale-oettl_2026_ai-in-science.pdf)

### Akcigit, Ufuk — University of Chicago
- **[Attention (And Money) Is All You Need: Why Universities Are Struggling to Keep AI Talent](explainers/firms-market-structure/akcigit-et-al_2025_attention-money-universities.md)** `[F,M]` — 2025, NBER WP 34964 (with Craig A. Chikis, Emin Dinlersoz, Nathan Goldschlag) · [PDF](papers/pdfs/akcigit-et-al_2025_attention-money-universities.pdf)

### Albanesi, Stefania — University of Pittsburgh / Miami Herbert / CEPR
- **[AI and Women's Employment in Europe](explainers/labor-productivity/albanesi-et-al_2025_new-tech-jobs-europe.md)** `[L,I]` — 2025, NBER WP 33451 (with António Dias da Silva, Juan F. Jimeno, Ana Lamo, Alena Wabitsch) · [PDF](papers/pdfs/albanesi-et-al_2025_new-tech-jobs-europe.pdf)

### Athey, Susan — Stanford GSB
- **[The Economics of Algorithmic Personalization: Evidence from an Educational Technology Platform](explainers/education/agrawal-athey-et-al_2026_algorithmic-personalization-edtech.md)** `[E,F]` — 2026, NBER WP 34950 (with Keshav Agrawal, Ayush Kanodia, Shanjukta Nath, Emil Palikot) · [PDF](papers/pdfs/agrawal-athey-et-al_2026_algorithmic-personalization-edtech.pdf)

### Autor, David — MIT
- **[The Labor Market Impacts of Technological Change](explainers/labor-productivity/autor_2022_labor-market-impacts-tech.md)** `[L,I]` — 2022, NBER WP 30074 · [PDF](papers/pdfs/autor_2022_labor-market-impacts-tech.pdf)
- **[Applying AI to Rebuild Middle Class Jobs](explainers/labor-productivity/autor_2024_rebuild-middle-class.md)** `[L,I]` — 2024, NBER WP 32140 · [PDF](papers/pdfs/autor_2024_rebuild-middle-class.pdf)

### Beraja, Martin — MIT
- **[Exporting the Surveillance State via Trade in AI](explainers/ai-models-governance/yuchtman-et-al_2023_exporting-surveillance-state.md)** `[M,I]` — 2023, NBER WP 31676 (with Andrew Kao, David Y. Yang, Noam Yuchtman) · [PDF](papers/pdfs/yuchtman-et-al_2023_exporting-surveillance-state.pdf)

### Brynjolfsson, Erik — Stanford
- **[A Research Agenda for the Economics of Transformative AI](explainers/firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md)** `[F,M]` — 2025, NBER WP 34256 (with Anton Korinek, Ajay K. Agrawal) · [PDF](papers/pdfs/agrawal-gans-goldfarb_2025_research-agenda-tai.pdf)
- **[Generative AI at Work](explainers/labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md)** `[L,F]` — 2025, QJE 2025 / NBER WP 31161 (with Danielle Li, Lindsey Raymond) · [PDF](papers/pdfs/brynjolfsson-li-raymond_2025_genai-at-work.pdf)

### Cockburn, Iain — Boston University Questrom
- **[The Impact of Artificial Intelligence on Innovation](explainers/ai-models-governance/cockburn-henderson-stern_2018_ai-impact-innovation.md)** `[M,F]` — 2018, NBER WP 24449 (with Rebecca Henderson, Scott Stern) · [PDF](papers/pdfs/cockburn-henderson-stern_2018_ai-impact-innovation.pdf)

### Cruces, Guillermo — Universidad de San Andrés / University of Nottingham
- **[Does Generative AI Narrow Education-Based Productivity Gaps? Evidence from a Randomized Experiment](explainers/inequality-welfare/cruces-et-al_2026_genai-education-productivity-gaps.md)** `[I,L]` — 2026, NBER WP 34851 (with Diego Fernández Meijide, Sebastian Galiani, Ramiro H. Gálvez, María Lombardi) · [PDF](papers/pdfs/cruces-et-al_2026_genai-education-productivity-gaps.pdf)

### Deming, David — Harvard
- **[The Rapid Adoption of Generative AI](explainers/labor-productivity/deming-bick-blandin_2024_rapid-adoption-genai.md)** `[L]` — 2024, NBER WP 32966 (with Alexander Bick, Adam Blandin) · [PDF](papers/pdfs/deming-bick-blandin_2024_rapid-adoption-genai.pdf)

### Frey, Carl Benedikt — Oxford
- **[Generative AI and the Future of Work: A Reappraisal](explainers/labor-productivity/frey-osborne_2024_genai-reappraisal.md)** `[L,I]` — 2024, Brown Journal of World Affairs (with Michael Osborne) · [PDF](papers/pdfs/frey-osborne_2024_genai-reappraisal.pdf)

### Jones, Charles I. — Stanford GSB
- **[A.I. and Our Economic Future](explainers/ai-models-governance/jones_2026_ai-economic-future.md)** `[M,L]` — 2026, Working Paper · [PDF](papers/pdfs/jones_2026_ai-economic-future.pdf)

### Korinek, Anton — University of Virginia
- **[Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence](explainers/ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md)** `[M]` — 2025, Economic Policy 2025 / NBER WP 33139 (with Jai Vipra) · [PDF](papers/pdfs/korinek-vipra_2025_concentrating-intelligence.pdf)
- **[AI Agents for Economic Research](explainers/ai-models-governance/korinek_2025_ai-agents-econ-research.md)** `[M]` — 2025, NBER WP 34202 · [PDF](papers/pdfs/korinek_2025_ai-agents-econ-research.pdf)

### Shen, Judy Hanwen — Anthropic
- **[How AI Impacts Skill Formation](explainers/labor-productivity/shen-tamkin_2026_ai-skill-formation.md)** `[L,E]` — 2026, arXiv:2601.20245 (with Alex Tamkin) · [PDF](papers/pdfs/shen-tamkin_2026_ai-skill-formation.pdf)

### Stantcheva, Stefanie — Harvard
- **[Understanding Economic Behavior Using Open-ended Survey Data](explainers/inequality-welfare/stantcheva-et-al_2024_open-ended-survey.md)** `[I,M]` — 2024, NBER WP 32421 (with Ingar Haaland, Christopher Roth, Johannes Wohlfart) · [PDF](papers/pdfs/stantcheva-et-al_2024_open-ended-survey.pdf)

### Trajtenberg, Manuel — Tel Aviv University
- **[AI as the Next GPT: A Political-Economy Perspective](explainers/ai-models-governance/trajtenberg_2018_ai-next-gpt.md)** `[M,L]` — 2018, NBER WP 24245 · [PDF](papers/pdfs/trajtenberg_2018_ai-next-gpt.pdf)

### Van Nieuwerburgh, Stijn — NYU Stern
- **[Financing the AI Buildout](explainers/ai-models-governance/van-nieuwerburgh_2026_financing-ai-buildout.md)** `[M,F]` — 2026, Working Paper · [PDF](papers/pdfs/van-nieuwerburgh_2026_financing-ai-buildout.pdf)

### Yotzov, Ivan — Bank of England
- **[Firm Data on AI](explainers/labor-productivity/bloom-et-al_2026_firm-data-on-ai.md)** `[L,F]` — 2026, NBER WP 34836 (with Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Steven J. Davis, et al.) · [PDF](papers/pdfs/bloom-et-al_2026_firm-data-on-ai.pdf)

## Source list

The canonical author scope of the corpus lives in [`inputs/economists_map.md`](inputs/economists_map.md) — a curated map of leading US and European economists working on AI, organized by sub-area. New papers enter the corpus only when authored by (or co-authored with) someone in that map.

## Maintaining the corpus

```bash
# Bulk download PDFs from the curated list (idempotent — skips existing files)
python scripts/download_papers.py

# Download a single paper by slug
python scripts/download_papers.py --slug acemoglu_2024_simple-macro-ai

# Validate that every metadata record has a matching PDF and explainer,
# explainer is in the correct subarea folder, and all cross-links resolve
python scripts/check_coverage.py
```

## A note on quantitative disagreement

Estimates of AI's macroeconomic impact diverge by **more than an order of magnitude** across this corpus:

- Acemoglu (2024): ~0.66% TFP gain over 10 years (~0.07 pp/yr) — the conservative end.
- Aghion–Bunel (2024): ~0.8–1.3 pp/yr via electricity-wave analogy — an order of magnitude higher.
- Brynjolfsson–Li–Raymond (2025): 14% average / 34% novice productivity at the firm level, with inequality compression.
- Korinek–Trammell, Jones (2026): transformative-AI scenarios that span much wider ranges still.

This is genuine empirical and theoretical disagreement, not a consensus that has yet to land. Every explainer's "Debates and caveats" section makes the divergence explicit rather than smoothing it over.

---

**Corpus:** 30 papers, ~30 MB of open-access PDFs · **Last updated:** 2026-04-29
