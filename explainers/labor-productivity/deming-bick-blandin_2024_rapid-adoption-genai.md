# The Rapid Adoption of Generative AI

**Authors:** Alexander Bick, Adam Blandin, David J. Deming
**Year:** 2024 (rev. February 2025)
**Venue:** NBER Working Paper No. 32966
**PDF:** [papers/pdfs/deming-bick-blandin_2024_rapid-adoption-genai.pdf](../../papers/pdfs/deming-bick-blandin_2024_rapid-adoption-genai.pdf)
**Source:** https://www.nber.org/papers/w32966

## 1. Full citation

Bick, Alexander; Blandin, Adam; Deming, David J. (2024). *The Rapid Adoption of Generative AI*. NBER Working Paper No. 32966. National Bureau of Economic Research, Cambridge, MA. Revised February 2025. JEL: J24, O33.

## 2. Research question

How fast and how deep is the real-world diffusion of generative AI among the U.S. working-age population, and how does its adoption trajectory compare to that of the personal computer and the internet? What does that adoption imply for aggregate productivity?

## 3. Method

- **Data.** Real-Time Population Survey (RPS), a nationally representative online survey of adults aged 18–64, fielded via Qualtrics, with waves in August and November 2024 (n = 5,014 + 5,329, total >10,000) (PDF p. 1, p. 5). Cross-validated with the Survey of Working Arrangements and Attitudes (SWAA, n = 4,698 in December 2024) (PDF p. 12).
- **Identification strategy.** Not causal: this is descriptive measurement. The paper replicates the exact questionnaire of the CPS Computer and Internet Use Supplement (CIU) from 1984–2009, enabling a direct comparison of the generative AI diffusion curve with the historical PC and internet curves using identical questions (PDF p. 7–9).
- **Productivity model.** Aggregate Cobb-Douglas production function with labor in wage-weighted efficiency units; self-reported time savings by users (s_i) are summed and converted to a labor productivity gain via ΔY/Y ≈ (1−α)·(Σs_iw̃_i / Σℓ_iw̃_i) (PDF p. 26–27).
- **Key assumptions.** (i) Perfect substitutability of labor across workers; (ii) time savings are reinvested in additional output rather than on-the-clock leisure; (iii) firms adjust expectations and capture the gains (PDF p. 27).

## 4. Key findings

- **Massive penetration within two years.** In August–November 2024, 39.4% of adults aged 18–64 report having used generative AI for work or outside of work; 26.5% of employed adults use it at work, and 9.0% use it every working day (PDF p. 10, Figure 2a).
- **Faster diffusion than the PC and internet.** Two years after ChatGPT, overall generative AI adoption exceeds that of the PC (≈20% at three years) and the internet over a comparable window; work adoption (27% in 2024) is similar to PC adoption in 1984 (25%), but non-work adoption (34% for AI vs. 5% for PC) is far faster (PDF p. 14, Figures 3 and 4b).
- **Dominant products.** ChatGPT (28.1% of all respondents), Gemini (16.6%), and embedded products such as Microsoft Copilot (14.1%) (PDF p. 12).
- **Heterogeneity by education, age, and gender.** Work adoption is ≈40% among those with a college or postgraduate degree vs. ≈18% among those without college education (PDF p. 15–16, Figure 5a). Adoption is 7.5 percentage points higher among men than women — the opposite of the PC in 1984, when women in administrative roles were the early majority (PDF p. 15).
- **Wage premium and use intensity.** Controlling for demographics, occupation, and industry, daily generative AI users earn 40% more than non-users (30% in hourly wages); weekly users earn 22% more (PDF p. 19).
- **Time saved and aggregate productivity.** Between 1 and 5 (specifically 1.4–5.4)% of total U.S. hours worked are assisted by generative AI; the average time saving among users is 5.4% of hours (≈2.2 hours/week on a 40-hour schedule), and 1.4% across all workers (PDF p. 25). This implies a potential aggregate labor productivity gain of **1.1%** (using Acemoglu's exposure-adjusted labor share) or **1.9%** without adjustment (PDF p. 27).
- **Validation of predicted exposure.** The occupational exposure metric of Eloundou et al. (2024) correlates ρ = 0.67 with actual adoption by occupation, supporting the use of such measures in projections (PDF p. 20–21).

## 5. Policy implications

- **Policy cannot wait for firms to adopt formally.** The paper documents that individual adoption is well ahead of organizational adoption (only 5.4% of firms had formally adopted generative AI as of February 2024, per Bonney et al., cited at PDF p. 27). This means that regulating or training exclusively through formal firms leaves out the individual user — who is already rewriting their workflow with ChatGPT. Workforce programs should target individuals, not just firms.
- **Education gap in adoption.** Adoption is roughly twice as high among college-educated workers compared to those without a degree. In many developing and middle-income economies where tertiary enrollment coverage is limited, this points to a productivity gap concentrated in already-privileged segments, widening urban/rural and formal/informal divides.
- **Gender gap.** Unlike the PC (which entered through female-dominated administrative occupations), generative AI is being adopted first by men. Digital-inclusion programs should incorporate this early pattern and design outreach that reaches women workers specifically.
- **Low cost + no hardware required = inevitable diffusion.** The authors note that the speed of adoption is partly explained by near-zero costs and no need for technical expertise (PDF p. 14). In settings where mobile penetration exceeds fixed broadband, generative AI can spread even in limited-infrastructure environments — but it will also escape traditional fiscal and regulatory controls.
- **Most-benefited tasks: writing, administration, translation/summarization.** 39.5% of users rank generative AI first or second for writing; 25.6% for administrative tasks; 22.7% for translation and summarization (PDF p. 21, Figure 9). For public services involving document processing, citizen assistance, and multilingual contexts, the potential time savings are direct and replicable.

## 6. Debates and caveats

- **Aggregate productivity: optimists vs. pessimists.** The Bick-Blandin-Deming estimate (1.1% potential, based on *reported use*) is slightly above Acemoglu's 0.7% (PDF p. 28), which is based on *task-predicted exposure*. Both are orders of magnitude below the Aghion-Bunel projections (0.8–1.3 pp/year of growth). See `acemoglu_2024_simple-macro-ai` and `aghion-bunel_2024_ai-and-growth`. The authors clarify that their estimate is of *potential* productivity: "these gains may not appear in productivity statistics, at least not yet" (PDF p. 27), because much adoption is informal and unrecognized by firms.
- **Self-report bias.** Time savings (5.4% average) are self-reported; the authors do not validate against objective measures. This contrasts with the field experiment of Brynjolfsson, Li, and Raymond, which measures observed productivity in a call center (see `brynjolfsson-li-raymond_2025_genai-at-work`).
- **Selection in online panel.** The RPS is a commercial Qualtrics panel. The authors triangulate with SWAA and with a Pew postal survey (which includes non-internet users) and find similar figures (PDF p. 12), but bias toward early adopters cannot be fully ruled out.
- **Perfect labor substitutability.** The model assumes perfect substitutability across worker types; the authors acknowledge that with imperfect substitution — and given that intensive users tend to be the highest earners — the aggregate effect could be smaller (PDF p. 27, note 20). This connects to `acemoglu-restrepo_2018_ai-automation-work` on task-level displacement.
- **What does Humlum find?** The parallel survey by Humlum and Vestergaard in Denmark (cited at PDF p. 12, note 9) reports similar rates by age, gender, and education, but studies whether adoption translates into wage changes — a test the U.S. survey is not yet able to perform.

## 7. Related readings

- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — experimental evidence on productivity in a call center; complements the self-reported time savings documented here.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — the conservative counterpoint (0.7% potential vs. 1.1% in this paper).
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — the optimistic end of the macro-forecast distribution.
- [albanesi-et-al_2025_new-tech-jobs-europe](../labor-productivity/albanesi-et-al_2025_new-tech-jobs-europe.md) — employment effects of AI-related technologies in Europe.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — a framework for thinking about who gains and who does not from technological waves.
- [bloom-et-al_2026_firm-data-on-ai](../labor-productivity/bloom-et-al_2026_firm-data-on-ai.md) — firm-level adoption, which this paper documents as far behind individual adoption.
