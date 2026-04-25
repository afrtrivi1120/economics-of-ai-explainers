# AI and Growth: Where Do We Stand?

**Authors:** Philippe Aghion, Simon Bunel
**Year:** 2024 (June)
**Venue:** San Francisco Fed Working Paper
**PDF:** [papers/pdfs/aghion-bunel_2024_ai-and-growth.pdf](../../papers/pdfs/aghion-bunel_2024_ai-and-growth.pdf)
**Source:** https://www.frbsf.org/wp-content/uploads/AI-and-Growth-Aghion-Bunel.pdf

## 1. Full citation

Aghion, Philippe and Simon Bunel (2024). "AI and Growth: Where Do We Stand?" San Francisco Fed Working Paper, June 2024. Collège de France / INSEAD / LSE; Banque de France / ENS.

## 2. Research question

How much should artificial intelligence raise aggregate productivity growth over the next decade, and why do economists arrive at such different estimates? The authors compare two approaches — analogy with previous technological revolutions and Acemoglu's (2024) task-based model — to bound the plausible range (p. 1).

## 3. Method

- **Approach 1 — Historical parallel.** Compares the "AI cycle" with two earlier waves: the European industrial electrification of the 1920s and the ICT wave in the U.S. in the late 1990s and early 2000s. Uses labor productivity series from Bergeaud, Cette, and Lecat (2016) (p. 4).
- **Approach 2 — Task-based model (Acemoglu 2024).** Applies Hulten's formula: annual TFP gain ≈ ExpAI × ProfitableAI × LaborCostSavingsAI × LaborShareAI, where each term is re-estimated from the recent empirical literature (Eloundou et al. 2023; Gmyrek et al. 2023; Pizzinelli et al. 2023; Svanberg et al. 2024; Brynjolfsson et al. 2023; Noy & Zhang 2023; Peng et al. 2023) (pp. 5–11).
- **Key assumption 1:** AI has a productive impact only through task automation in goods and services; the automation of idea production is explicitly excluded (p. 1).
- **Key assumption 2:** the median of each parameter's interval is used as the baseline scenario.

## 4. Key findings

- **Historical approach (optimistic):** if AI replicates Europe's 1920s electricity wave, productivity would grow **+1.3 percentage points (pp) per year** from 2024; if it replicates the U.S. ICT wave (1996–2007), the increase would be **+0.8 pp/year** (p. 4). For reference, France's potential growth is currently estimated at 0.5% per year (p. 4).
- **Task-based approach (recalibrated):** plausible range of **[0.07 pp; 1.24 pp]** per year in TFP over 10 years; median estimate of **+0.68 pp/year** (p. 11).
- **Decomposition of the baseline scenario (p. 11):** ExpAI = 0.60; ProfitableAI = 0.50; LaborCostSavingsAI = 0.40; LaborShareAI = 0.57 → 0.60 × 0.50 × 0.40 × 0.57 × 10 = **0.68 pp per year**.
- **Historical-approach gains are transitory:** once the entire economy adopts AI, the effect on growth disappears (Figure 3, p. 5). Only the automation of idea production would generate a permanent effect (p. 12).
- **Supporting microeconomic evidence:** Brynjolfsson et al. (2023) reports +14% productivity in the first month, stabilizing at ~25% after three months, for customer-service agents using an AI assistant (p. 2); Noy & Zhang (2023) and Dell'Aqua et al. (2023) find gains of 25–40% for consultants and professionals (footnote 1, p. 2); Pôle Emploi (2023) finds that 72% of French employers using AI report a positive impact on performance (p. 2).
- **A lower bound, not an upper bound:** the authors note that 0.68 pp/year understates the effect if AI automates idea generation (Aghion, Jones & Jones 2018), but overstates it if concentration in the AI value chain (GAFAMs) blocks innovator entry (pp. 13–14).

## 5. Policy implications

- **Relevant magnitude for non-frontier economies.** In many developing and emerging-market economies where TFP growth is already constrained, a positive surprise of +0.68 pp/year — if achieved — would be transformative. But Figure 4 (p. 7), based on Gmyrek et al. (2023) and the ILO, shows that AI exposure in middle-income countries is substantially lower than in the U.S. or the U.K., with smaller shares of employment in high-exposure/high-complementarity categories. The conclusion: **the 1.3 pp/year ceiling applies to economies with advanced occupational structures; non-frontier economies would likely capture a fraction of that.**
- **The bottleneck is not the technology frontier but diffusion.** The parallel with electricity (a 30-year lag between invention and productivity gains, pp. 3–4) suggests that public policy should focus on business reorganization, complementary capital, and investment — not just on model access.
- **Competition policy.** Aghion and Bunel stress that concentration in upstream segments (data, compute) can neutralize productivity gains (pp. 13–14). For policymakers, this means AI policy is inseparable from digital competition policy: dependence on a few compute and model providers limits local capture of gains.
- **Education and reorganization.** Gains of 25–40% in cognitive tasks (customer service, coding, writing) point to productivity opportunities in urban service sectors, but they require AI-use training and process redesign. Vocational training systems and public education finance will need to adapt.

## 6. Debates and caveats

This note is **the most explicit counterweight** to Acemoglu's conservative estimate in this corpus. The authors reproduce Acemoglu's (2024) formula but, by re-reading the empirical literature, arrive at a median of **0.68 pp/year** — nearly ten times the **0.07 pp/year** Acemoglu reports using the same four terms (p. 6, p. 11). The key difference: Aghion-Bunel assume `ExpAI = 0.60` (following Pizzinelli et al., based on skills) rather than ~0.20 (Eloundou/Gmyrek, based on tasks), and `LaborCostSavingsAI = 0.40` rather than 0.27.

- Against [`acemoglu_2024_simple-macro-ai`](../labor-productivity/acemoglu_2024_simple-macro-ai.md): Acemoglu obtains ~0.66% total TFP over 10 years (≈0.07 pp/year); Aghion-Bunel more than triple the range using the same model and **also** offer a ceiling of 1.3 pp/year via historical analogy. The discrepancy is not about the model — it is about **reading the microeconomic evidence**.
- Against [`aghion-jones-jones_2017_ai-economic-growth`](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md): that paper provides the theoretical basis for the **permanent** effect via idea automation, which Aghion-Bunel acknowledge but **do not quantify** (p. 12). The 0.68 pp/year is by construction a lower bound.
- Against [`brynjolfsson-li-raymond_2025_genai-at-work`](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md): the authors cite this study as the anchor evidence for +25% productivity in customer service (p. 2, p. 10), but warn that extrapolating from a single firm to the aggregate is problematic.
- Against [`korinek-vipra_2025_concentrating-intelligence`](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md): both agree that concentration in the AI value chain can cancel out aggregate gains (pp. 13–14).
- **Major methodological caveat:** this note is not a new empirical paper; it is a recalibration of parameters drawn from the literature. Its value lies in **showing the sensitivity** of Acemoglu's result to defensible assumptions.
- **Historical caveat:** the electricity parallel assumes that today's economic structure allows for comparable reorganizations; it does not control for the possibility that AI, like post-2005 ICT, is a technology whose gains dissipate in entertainment (Rachel 2021, cited p. 13).

## 7. Related readings

- [`acemoglu_2024_simple-macro-ai`](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — The conservative estimate (≈0.07 pp/year) that Aghion-Bunel recast with the same formula and inflate by nearly 10x.
- [`aghion-jones-jones_2017_ai-economic-growth`](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md) — Theoretical framework for the "idea automation" channel that this note leaves unquantified.
- [`brynjolfsson-li-raymond_2025_genai-at-work`](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — Key microeconomic evidence (+14% month 1, +25% stabilized) anchoring the `LaborCostSavingsAI` parameter.
- [`acemoglu-restrepo_2018_ai-automation-work`](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — Task-based model that both approaches use as their theoretical backbone.
- [`autor_2024_rebuild-middle-class`](../labor-productivity/autor_2024_rebuild-middle-class.md) — Complementary view on how AI could rebuild middle-class tasks.
- [`korinek-vipra_2025_concentrating-intelligence`](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — Elaborates the upstream concentration risk that Aghion-Bunel flag as a potential brake.
