# AI and Women's Employment in Europe (companion to "New Technologies and Jobs in Europe")

**Authors:** Stefania Albanesi, António Dias da Silva, Juan F. Jimeno, Ana Lamo, Alena Wabitsch
**Year:** 2025
**Venue:** NBER Working Paper 33451 (February 2025); companion to Albanesi et al., *Economic Policy* (2024), "New Technologies and Jobs in Europe"
**PDF:** [papers/pdfs/albanesi-et-al_2025_new-tech-jobs-europe.pdf](../../papers/pdfs/albanesi-et-al_2025_new-tech-jobs-europe.pdf)
**Source:** https://www.nber.org/papers/w33451

> Note: the downloaded PDF (W33451, "AI and Women's Employment in Europe") is the gender-focused extension of the *Economic Policy* (2024) article "New Technologies and Jobs in Europe" referenced in `inputs/economists_map.md`. This explainer covers the findings of both, with emphasis on the downloaded paper.

## 1. Full citation

Albanesi, S., Dias da Silva, A., Jimeno, J. F., Lamo, A., and Wabitsch, A. (2025). *AI and Women's Employment in Europe*. NBER Working Paper No. 33451. Cambridge, MA: National Bureau of Economic Research. (Extension of Albanesi et al., 2024, *Economic Policy*, eiae058.)

## 2. Research question

Did the spread of AI-enabled technologies in Europe between 2011 and 2019 displace or increase employment, and what effect did it have specifically on women's share of employment? The study seeks an ex-post empirical test — not a projection — of the mass-displacement hypothesis (Frey-Osborne) and of skill-biased automation models (Acemoglu-Restrepo) in the European context.

## 3. Method

- **Data:** EU Labour Force Survey (EU-LFS) plus the United Kingdom, 16 countries, 2011–2019, ISCO-2008 3-digit occupations crossed with six aggregate sectors (p. 2–3).
- **AI exposure measures:** two indices built for the U.S. and mapped to ISCO through crosswalks (Hardy et al. 2018): the AI Occupational Impact score of Felten et al. (2019), based on skills, and the Webb (2020) index, based on textual overlap between AI patents and task descriptions (p. 2).
- **Strategy:** sector-occupation-country level regression of the percentage-point change in women's employment share between 2011 and 2019 on the AI-exposure percentile, with country and industry fixed effects, weighted by initial employment (p. 3, eq. 1).
- **Key assumptions:** the U.S.-built exposure measures transfer reasonably to the European occupational structure; the variation across cells captures the potential causal effect of AI diffusion and not merely pre-existing trends (a limitation implicitly acknowledged by the authors).

## 4. Key findings

- Moving 10 percentiles up the AI-exposure distribution is associated with a **2.2% increase in women's employment share** within the cell using the Webb measure and **2.9%** using Felten et al. (p. 4). These coefficients are roughly double those estimated for total employment in Albanesi et al. (2024) (p. 4).
- In countries with **larger relative gains in women's education**, the coefficient rises to **2.7% (Webb) and 3.4% (Felten et al.)** per 10 percentiles of exposure (p. 4, Fig. 2).
- The positive association is **stronger in countries with higher initial (2011) female labor-force participation**, suggesting that labor-market attachment protects against displacement effects (p. 5–6, Fig. 2 panels c–d).
- At the country level, **nearly all** 16 countries show positive coefficients for both measures; exceptions are Greece (negative under Webb) and Italy/Lithuania (close to zero) (p. 6, Fig. 3).
- The highest coefficients under Felten et al. correspond to the Netherlands, Portugal, and Estonia; under Webb to Austria, Belgium, and Luxembourg (p. 6).
- **Contrast with the U.S.:** Cortes-Pan (2019) and Cortés et al. (2024) find a **negative** correlation between automation exposure and women's employment in the U.S. 1980–2017; the European authors argue the difference stems from combining AI (not classical routine automation) with larger educational gains for women in Europe (p. 2, p. 7).

## 5. Policy implications

The European evidence is relevant for a broad set of policymakers. Three structural features of the European context make the findings transferable: (i) formal-sector labor-protection systems based on employment regulation rather than deregulation; (ii) gender gaps in participation narrowing through educational attainment; (iii) AI-exposed sectors (professional services, health, finance, public administration) concentrating formal female employment.

Operational implications:

- **Women's education amplifies the benefits of AI.** Technical and university training programs focused on women are not only gender policy — they are productivity and technology-absorption policy. The coefficient rises by roughly 50% in countries with greater female educational progress (p. 4). Vocational training systems and public education finance programs should account for this complementarity.
- **Labor-market attachment provides protection.** Policies that sustain women's participation — subsidized childcare, shared parental leave, measures to reduce barriers to formal employment — reduce the risk that AI diffusion ends up excluding women, as routine automation did in the U.S.
- **Do not mechanically replicate the U.S. displacement narrative.** The European pattern, grounded in stronger labor-market institutions, suggests positive net effects on formal female employment when human capital is available to complement the technology. Policymakers in non-frontier economies should weigh institutional context before importing U.S.-centric projections.
- **Caveat:** the effects are at the level of participation shares within occupations, not net job creation. The study does not address informal employment or sectors where women are concentrated outside the formal professional labor market.

## 6. Debates and caveats

- **Divergence from Frey-Osborne and from the U.S. automation literature.** The positive finding stands in direct contrast to the mass-displacement prediction of Frey-Osborne (see `frey-osborne_2024_genai-reappraisal`) and to the negative evidence of Cortes-Pan/Cortés et al. for the U.S. cited in the paper itself (p. 2, p. 7).
- **Moderate optimism vs. Acemoglu's macro pessimism.** While Acemoglu (2024) estimates TFP gains of ~0.66% over 10 years and warns about "the wrong kind of AI" (see `acemoglu_2024_simple-macro-ai` and `acemoglu-restrepo_2018_ai-automation-work`), Albanesi et al. find positive employment effects at the occupation level. A plausible reconciliation: heterogeneous effects by gender and education can coexist with modest aggregate gains.
- **Open question on generative AI.** The 2011–2019 period covers pre-ChatGPT predictive AI. Extrapolation to generative AI is uncertain; more recent studies (`brynjolfsson-li-raymond_2025_genai-at-work`, `deming-bick-blandin_2024_rapid-adoption-genai`) show different patterns of adoption and productivity compression.
- **Measurement limitations:** the Felten and Webb measures were built for the U.S. and disagree on which occupations they flag as exposed; the authors use them as proxies, but the coefficients differ in magnitude and country ranking (p. 6).
- **Weak causality.** There is no instrumental variation: the association is conditional on country and industry fixed effects, but could reflect pre-existing trends in the feminization of professional occupations independent of AI.

## 7. Related readings

- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — Task-based theoretical framework and displacement; predicts negative effects that the European paper does not find.
- [frey-osborne_2024_genai-reappraisal](../labor-productivity/frey-osborne_2024_genai-reappraisal.md) — "Automatability" estimates whose mass-displacement projections this study does not confirm ex-post.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Conservative macro TFP estimates that qualify the optimism of the European paper.
- [autor_2022_labor-market-impacts-tech](../labor-productivity/autor_2022_labor-market-impacts-tech.md) — General polarization framework with which the European pattern is in dialogue.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — Complementary microeconomic evidence on generative AI and less-experienced workers.
