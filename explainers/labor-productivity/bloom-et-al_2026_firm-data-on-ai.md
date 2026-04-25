# Firm Data on AI

**Authors:** Ivan Yotzov, Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Steven J. Davis, Kevin M. Foster, Aaron Jalca, Brent H. Meyer, Paul Mizen, Michael A. Navarrete, Pawel Smietanka, Gregory Thwaites, Ben Zhe Wang
**Year:** 2026 (February, revised March)
**Venue:** NBER Working Paper No. 34836
**PDF:** [papers/pdfs/bloom-et-al_2026_firm-data-on-ai.pdf](../../papers/pdfs/bloom-et-al_2026_firm-data-on-ai.pdf)
**Source:** https://www.nber.org/papers/w34836

## 1. Full citation

Yotzov, I., Barrero, J. M., Bloom, N., Bunn, P., Davis, S. J., Foster, K. M., Jalca, A., Meyer, B. H., Mizen, P., Navarrete, M. A., Smietanka, P., Thwaites, G., & Wang, B. Z. (2026). *Firm Data on AI*. NBER Working Paper No. 34836. National Bureau of Economic Research.

## 2. Research question

How widespread is AI use among firms, and what effects — realized and expected — does it have on productivity, employment, and output? The paper builds a comparable dataset across four advanced economies (U.S., U.K., Germany, and Australia) by asking executives directly about what is happening "in their own firm" (PDF p. 2-3).

## 3. Method

- **Data**: Parallel surveys of nearly 6,000 senior executives (CEOs, CFOs, financial managers) in four countries, fielded between November 2025 and January 2026, with backing from central banks (Atlanta Fed, Bank of England, Bundesbank) and Macquarie University (PDF p. 1, 3, 6-8). For the U.S., roughly 3,000 workers were also surveyed via the Survey of Working Arrangements and Attitudes (SWAA) (PDF p. 17).
- **Design**: Identical questionnaire across countries, with five impact categories (from "large positive impact, >+5%" to "large negative impact, <-5%") on employment and productivity (sales/employee), both retrospective (past 3 years) and prospective (next 3 years) (PDF p. 13-15).
- **Identification**: Simple aggregation of forecasts from those with the "best line of sight" into their own firm. This is not a causal model; the core assumption is that executives are well-informed and motivated to respond honestly (PDF p. 2-3, 7).
- **Coverage**: Samples are nationally representative thanks to central bank sponsorship, which mitigates the "impostor" problem common in paid online panels (up to 80% according to Chandler and Paolacci 2017) (PDF p. 7).

## 4. Key findings

- **Broad adoption**: 69% of firms actively use AI (average across the four countries), and 75% expect to use it in the next three years (PDF p. 3, 12). The most common uses are text generation with LLMs, visual content creation, and data processing with machine learning.
- **Executive use paradox**: More than two-thirds of executives use AI in a typical week, but the average is only 1.5 hours/week — 41% report "up to 1 hour" and only 7% more than 5 hours (PDF p. 3, 12). Executive use rose roughly 50% (from 0.9 to 1.4 hrs/week) in less than a year (PDF p. 13).
- **Small realized impact**: More than 90% of firms report no impact on employment over the past 3 years, and 89% report no impact on productivity (sales/employee) (PDF p. 13, 15). The aggregate quantitative impact is essentially zero for employment and +0.29% cumulative for productivity (PDF p. 14, 16).
- **Much larger expectations**: Executives forecast that AI will raise productivity 1.4% and output 0.8%, and reduce employment 0.7% over the next 3 years (PDF p. 3, 17). In the U.S., the expected productivity boost reaches 2.3% (PDF p. 16).
- **Employer-worker gap**: U.S. workers expect AI to *increase* their firm's employment by 0.5% over 3 years, while U.S. executives expect a reduction of 1.2% (PDF p. 17-18). Workers are more optimistic about employment and less so about productivity.
- **Heterogeneity**: Younger, larger, more productive firms with younger managers and higher wages adopt AI more (PDF p. 3, 13). Information/communications sectors expect the largest productivity jump (+2.8%); accommodation/food and wholesale/retail expect the largest employment cuts (-1.8% to -2%) (PDF p. 15-16).

## 5. Policy implications (Colombia / Latin America)

- **Blueprint for a Colombian firm-level AI survey**: This paper is the methodological reference for collecting comparable, representative data. DANE, Banco de la República, or Confecámaras could replicate the questionnaire (five-category impact questions, retrospective + prospective, same technology options) to produce a series comparable with the U.S./EU. The critical lesson: central bank or government sponsorship raises response rates among senior executives, which is difficult to achieve with private panels.
- **Calibrating local expectations**: If firms in frontier economies report roughly zero realized impact over 3 years, expectations of immediate productivity leaps from AI in Colombian firms — where adoption will lag — should be tempered. Industrial policy (MinTIC, iNNpulsa) should measure adoption before subsidizing outcomes.
- **Employer-worker gap as political risk**: The 1.7 percentage-point divergence between what executives expect (-0.7% employment) and what workers expect (+0.5% employment) signals a public communication risk. In Colombia, where informality amplifies anxiety about automation, this gap may be even wider. Reskilling programs (SENA) should be designed with the awareness that employment reductions come mainly from "fewer new hires" (roughly 2/3 of the effect, PDF p. 14-15) rather than layoffs — a nuanced but crucial message for young workers.
- **Priority sectors**: Information/communications, professional services, and administrative services stand to gain the most in productivity; retail trade and food services face the largest expected employment losses. Regional planning (productive vocation strategies) can use this mapping as a starting point.

## 6. Debates and caveats

- **Macro optimism vs. pessimism**: The expected +1.4% productivity gain over 3 years (≈0.47%/year) falls in the middle range of the debate. It is more optimistic than Acemoglu's ceiling of 0.66% over 10 years — see `acemoglu_2024_simple-macro-ai` — but far more conservative than the 0.8-1.3pp/year of Aghion-Bunel (`aghion-bunel_2024_ai-and-growth`) or the 1.5pp/year of Briggs-Kodnani (PDF p. 5).
- **Executive optimism bias**: Forecasts are subjective and executives may overestimate the future impact of technology in which they have already invested. The paper itself notes that employment expectations have grown *more* negative between February 2025 and January 2026 (-0.8% to -1.4%), a sign of active revision (PDF p. 15).
- **No general equilibrium**: The survey does not capture employment at new firms, nor the equilibrium effects of higher real incomes (PDF p. 4). The -0.7% employment figure is partial and likely overstates the net aggregate effect.
- **Extensive vs. intensive margin**: Only whether the firm uses AI is measured, not how intensively, which limits causal interpretation (PDF p. 12).
- **Contrast with experimental evidence**: Task-level studies (Brynjolfsson et al. 2025 on call centers) report gains much larger than the firm-level estimates here — see `brynjolfsson-li-raymond_2025_genai-at-work`. The discrepancy suggests that task-level gains do not translate 1:1 into firm-level productivity.

## 7. Related readings

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — the conservative macro ceiling (~0.66% TFP over 10 years) against which to benchmark the 1.4% in 3 years expected by executives.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — the optimistic view of AI-driven growth, substantially higher than these firm-level forecasts.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — experimental evidence of large task-level gains, a complement to the firm-level averages here.
- [deming-bick-blandin_2024_rapid-adoption-genai](../labor-productivity/deming-bick-blandin_2024_rapid-adoption-genai.md) — individual-level adoption of generative AI in the U.S., the worker-side counterpart to the 1.5 hr/week executive figure.
- [stantcheva-et-al_2024_open-ended-survey](../inequality-welfare/stantcheva-et-al_2024_open-ended-survey.md) — how households perceive AI, useful for contextualizing the employer-worker gap documented here.
