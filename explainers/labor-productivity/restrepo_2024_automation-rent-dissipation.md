# Automation and Rent Dissipation: Implications for Wages, Inequality, and Productivity

**Authors:** Daron Acemoglu, Pascual Restrepo
**Year:** 2024 (revised October 2025)
**Venue:** NBER Working Paper No. 32536
**PDF:** [papers/pdfs/restrepo_2024_automation-rent-dissipation.pdf](../../papers/pdfs/restrepo_2024_automation-rent-dissipation.pdf)
**Source:** https://www.nber.org/papers/w32536

## 1. Full citation

Acemoglu, Daron and Pascual Restrepo. 2024 (rev. 2025). "Automation and Rent Dissipation: Implications for Wages, Inequality, and Productivity." NBER Working Paper No. 32536. National Bureau of Economic Research. Available at https://www.nber.org/papers/w32536.

## 2. Research question

How do the effects of automation on wages, inequality, and productivity change when labor markets have rents — that is, when some jobs pay wages above a worker's outside option (due to unions, efficiency wages, regulation, or licensing)? The paper introduces a *rent dissipation* mechanism: automation selectively targets the tasks with the highest rents, amplifying wage losses and erasing a share of the expected productivity gains.

## 3. Method

- **Data:** BEA Integrated Industry-Level Production Accounts (49 industries), 1980 U.S. Census (500 demographic groups), O*NET (occupational routine content), CPS (wages by percentile, 1980–2016), three automation proxies: adjusted industrial robot penetration (Acemoglu and Restrepo, 2020), share of specialized software and dedicated machinery in value added (BLS) (PDF p. 23).
- **Identification strategy:** (i) group-level quantile regression (Chetverikov et al., 2016) of the log-wage change at each percentile on the group's task displacement (PDF p. 26); (ii) decomposition of the average wage change into a base-wage component (30th percentile) and a rent-dissipation component (additional drop above the 30th percentile) (PDF p. 29); (iii) direct measure of displacement from high-rent jobs using industry-occupation-level rent proxies (PDF p. 30).
- **Model:** Extension of the Acemoglu-Restrepo (2022) tasks framework. Jobs pay a wedge µ_gx ≥ 1 above the base wage, treated as rigid (efficiency wages, hiring, licensing, regulation) (PDF p. 6). General equilibrium with ripple effects across groups via two matrices: a *propagation matrix* and a *rent-impact matrix* (PDF p. 2).
- **Key assumptions:** Fixed wedges that do not adjust in equilibrium; λ = 0.5 (elasticity of substitution between tasks); π_i = 30%; µ_A/µ_i = 1.35 (PDF p. 23). Monopsony wedges generate similar implications (PDF p. 6, note 6).

## 4. Key findings

- Automation between 1980 and 2016 accounts for **52% of the increase in between-group wage inequality** in the U.S.; **42 pp** stem from the baseline labor-demand effect and **10 pp** (roughly one-fifth) come specifically from rent dissipation (PDF p. 3).
- Cost savings from automation raised TFP by approximately **3% cumulatively** between 1980 and 2016, but the inefficient targeting of high-rent tasks **offset between 60% and 90%** of that gain. Net aggregate TFP grew only **0.3–1.3%** and aggregate consumption grew only **0.45–1.95%** over the entire period (PDF p. 3).
- Groups in the lower-middle of the wage distribution lost **15%–20%** of their tasks to automation; groups with graduate degrees lost almost none (PDF p. 23).
- A 10 pp increase in task displacement is associated with a **24%** decline in a group's relative wages (without controls) or **20%** with full controls (PDF p. 24–25). That single measure explains **66%** of the variation in wage changes across demographic groups since 1980 (PDF p. 24).
- The within-group wage-change curve for exposed workers is **U-shaped**: drops of 25–30% per 10 pp of displacement at the 70th–90th percentiles (where high-rent jobs are concentrated), versus 16% at the 5th–40th percentiles (PDF p. 26).
- The estimated rent dissipation rate (µ_A/µ_g − 1) is **37%** without controls for compensating differentials and **28%** with controls (PDF p. 29). On average, automation displaced workers from jobs whose wages exceeded their outside option by **≈35%** (PDF p. 2).

## 5. Policy implications

- **Not all cost savings translate into social gains.** In economies with segmented labor markets — formal/informal, unionized/non-unionized, with binding licensing or minimum wages — automation can destroy rents that served a redistributive function without delivering the promised aggregate productivity gains. In many developing economies where formal employment concentrates rents alongside large informal sectors, the relevant metric for evaluating AI and robotization adoption must include reallocation costs, not just technical productivity.
- **Active labor market policy design:** workers displaced from high-rent jobs do not land in equivalent positions — they move down the distribution. This justifies robust unemployment insurance, targeted retraining through vocational training systems, and income protection during the transition, rather than subsidies for technology adoption per se.
- **Tax policy on automation:** the finding that rent dissipation erases 60–90% of TFP gains reinforces the argument made by Acemoglu (2024) and others for revisiting the asymmetric tax treatment that currently favors capital over labor (accelerated depreciation, investment deductions). In many emerging markets, where tax codes often privilege imported capital goods, the finding points toward recalibration.
- **Professional regulation and licensing:** since licensing-generated wedges are an identified source of rents, reforms to professional entry barriers should evaluate the equilibrium effect on automation incentives, not just the static competition effect.

## 6. Debates and caveats

- **Refinement of the Acemoglu-Restrepo (2022) framework.** The paper explicitly extends the prior tasks model (see `acemoglu-restrepo_2018_ai-automation-work`) by introducing wedges µ_gx ≥ 1. The key theoretical contribution: automation is not neutral with respect to which tasks it targets; it selects those where the wage exceeds the outside option, breaking the equivalence between private cost savings and social savings.
- **Tension with macro-optimistic views.** The authors estimate net aggregate TFP gains of only 0.3–1.3% over 36 years — an order of magnitude below the projections in `aghion-bunel_2024_ai-and-growth` (0.8–1.3 pp per year) and still below the conservative estimate in `acemoglu_2024_simple-macro-ai` (~0.66% over 10 years). The difference: here, targeting inefficiency acts as a "tax" on productivity gains that is absent in balanced-growth models such as `aghion-jones-jones_2017_ai-economic-growth`.
- **Dependence on fixed wedges.** The critical assumption is that µ_gx does not adjust in equilibrium. If unions renegotiate or regulations ease in response to automation, dissipation is mitigated. The authors discuss micro-foundations under which this does not occur (PDF p. 6, note 7), but the quantitative result is sensitive to this assumption.
- **Compatible with Autor's institutional reading.** The paper aligns with `autor_2024_rebuild-middle-class` in arguing that middle-class job loss is not only a skill supply-and-demand phenomenon but also an erosion of rents. It diverges from purely skill-biased explanations (Katz-Murphy, 1992), which the paper cites as insufficient (PDF p. 4).
- **Geographic limitation.** Wedges are calibrated with U.S. data (1980); mapping them to economies with different labor market institutions (informality, more binding minimum wages) requires recalibration before transferring the magnitudes.

## 7. Related readings

- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — The original tasks framework that this paper extends by incorporating rents.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Conservative macro estimate (~0.66% TFP/10 years) consistent with the skeptical reading here.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — More optimistic growth view that this paper implicitly challenges.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — Institutional and political reading of middle-class erosion, compatible with the rent mechanism.
- [autor_2022_labor-market-impacts-tech](../labor-productivity/autor_2022_labor-market-impacts-tech.md) — Complementary empirical evidence on polarization and technology-driven displacement.
