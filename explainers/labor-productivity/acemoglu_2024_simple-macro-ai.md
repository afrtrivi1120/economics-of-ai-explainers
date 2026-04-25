# The Simple Macroeconomics of AI

**Authors:** Daron Acemoglu
**Year:** 2024 (Economic Policy, 2025)
**Venue:** NBER Working Paper No. 32487
**PDF:** [papers/pdfs/acemoglu_2024_simple-macro-ai.pdf](../../papers/pdfs/acemoglu_2024_simple-macro-ai.pdf)
**Source:** https://www.nber.org/papers/w32487

## 1. Full citation

Acemoglu, Daron (2024). "The Simple Macroeconomics of AI." NBER Working Paper No. 32487, May 2024. Cambridge, MA: National Bureau of Economic Research. JEL E24, J24, O30, O33.

## 2. Research question

How large are the plausible macroeconomic effects of generative AI on total factor productivity (TFP), GDP, wages, and inequality in the United States over the next ten years? Acemoglu aims to discipline predictions — ranging from Goldman Sachs (7% of global GDP) to McKinsey (1.5–3.4 pp of annual growth) — using a micro-founded task-based framework (PDF p. 1).

## 3. Method

- **Conceptual framework:** task-based model from Acemoglu and Restrepo (2018, 2019, 2022). Final-good production requires a set of tasks that can be assigned to capital or labor according to comparative advantage (PDF p. 2).
- **Modeled channels:** automation (extensive margin) and task complementarity; the paper explicitly does NOT model automation deepening or transformative scientific effects (new materials discovery, biology) that Acemoglu considers unlikely within a 10-year horizon (PDF p. 3).
- **Quantitative identification (back-of-the-envelope):** a version of Hulten's theorem — aggregate effects on GDP and TFP are approximated by (share of tasks affected) × (average cost saving per task) (PDF p. 3).
- **Data:** task-exposure estimates from Eloundou et al. (2023); computer-vision feasibility from Svanberg et al. (2024); micro cost savings from the experiments of Noy & Zhang (2023) and Brynjolfsson, Li & Raymond (2023). Acemoglu aggregates to the occupational level, weighting by wage-bill share (PDF p. 4).
- **Key assumption:** AI's microeconomic effects operate through cost savings at the task level — if AI works through radically different channels (massive creation of new tasks, transformed science), the framework would underestimate its effects (PDF p. 5).

## 4. Key findings

- **Modest TFP gain:** ~20% of U.S. labor tasks are exposed to AI; applying a 27% cost saving (average of Noy-Zhang and Brynjolfsson et al.) and an overall weighted saving of 14.4%, TFP rises by at most **0.66% over 10 years** (~0.064% per year) (PDF p. 4).
- **Downward adjustment for hard tasks:** once a distinction is drawn between "easy-to-learn" and "hard-to-learn" tasks, the upper bound falls to **0.53% TFP and 0.90% GDP over 10 years** (PDF p. 5; PDF p. 33: the formula yields 0.0053).
- **GDP:** assuming the capital stock grows proportionally with TFP, GDP rises **0.93%–1.16%** over 10 years; using the full Acemoglu-Restrepo (2022) framework with endogenous investment response, the upper bound reaches **1.4%–1.56%** (PDF p. 4; Table 1, column 7, PDF p. 39).
- **Low wages without recovery:** even when AI raises the productivity of low-skill workers, **inequality does not fall**; Acemoglu finds it would negatively affect the real earnings of low-education women (especially native white women) and widen the capital-labor gap (PDF p. 6).
- **Capital-labor inequality:** capital's share of national income rises by ~**0.31 percentage points** as a result of AI deployment (PDF p. 40).
- **New "bad tasks":** quantifying deepfakes, digital manipulation, and cyberattacks, AI could appear to raise GDP by **2%** while reducing welfare by **−0.72%** in consumption-equivalent units (PDF p. 5; PDF p. 35: calculation 0.02 × 0.36 = 0.072% of GDP in damages).
- **Minimal wage growth:** even for the most-benefited group (less than high-school education), the wage increase is only **~1.3% over 10 years**; the standard deviation across groups rises slightly from 0.35 to 0.36 (PDF p. 38).

## 5. Policy implications (Colombia / Latin America)

- **Calibrate fiscal and productivity expectations.** Consultant-driven forecasts (McKinsey, Goldman) that underpin national AI plans and "digital transformation agendas" may be overstating aggregate gains by an order of magnitude. For Colombia, Acemoglu's framework suggests that no generative-AI productivity shock will, by itself, close GDP-per-capita gaps within a decade.
- **Do not expect automatic inequality reduction.** Acemoglu's theoretical result — AI can raise low-skill workers' productivity and still increase inequality — is directly relevant to the Colombian debate on AI in BPO, call centers, and education. Redistributive policy (capital taxes, training, new tasks for workers) must be designed separately; it will not emerge from the market.
- **Regulate "bad tasks."** The estimates on digital manipulation, disinformation, and cyberattacks justify explicitly including digital consumer protection, social-media regulation, and public cybersecurity in any national AI strategy — not as an ethical appendix but as a macroeconomic component (the damage can reach ~36% of monetized value).
- **Public investment should prioritize creating "new tasks for workers"** (education, health, AI-assisted personal care) over pure automation. This aligns with the "pro-worker AI" agenda that Acemoglu has developed with Johnson and Autor.
- **Be careful about counting AI revenue as welfare.** The paper's methodological warning (GDP ≠ welfare when manipulative tasks are present) has direct implications for how DANE and Planeación Nacional should measure the contribution of digital platforms.

## 6. Debates and caveats

This is one of the **most conservative estimates** in the field, and the divergence with the rest of the corpus is the most important quantitative debate in the economics of AI:

- **Aghion and Bunel (SF Fed, 2024)** estimate that AI could add **0.8 to 1.3 percentage points per year** to TFP growth in developed countries — a figure **12 to 20 times larger** than Acemoglu's (~0.064% per year). Aghion grounds this gap in an analogy with electrification and a Schumpeterian model in which AI acts as a general-purpose technology (GPT) and reorganizes production. See [`aghion-bunel_2024_ai-and-growth`](../labor-productivity/aghion-bunel_2024_ai-and-growth.md).
- **Aghion, Jones, and Jones (2017)** outline scenarios in which AI, by automating the production of ideas, can generate explosive growth if there are no binding bottlenecks. See [`aghion-jones-jones_2017_ai-economic-growth`](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md).
- **Brynjolfsson, Li, and Raymond (2025)** document productivity gains of **14% on average and 34% for novice workers** in a call center — far above the 27% average from Noy-Zhang/Brynjolfsson that Acemoglu uses — and with a compressing effect on inequality, the opposite of Acemoglu's theoretical result. See [`brynjolfsson-li-raymond_2025_genai-at-work`](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md).
- **Autor (2024)** argues that AI can *expand* the middle class by allowing non-elite workers to perform expert tasks — a more optimistic view of the distributional effect. See [`autor_2024_rebuild-middle-class`](../labor-productivity/autor_2024_rebuild-middle-class.md).
- **Korinek and Vipra (2025)** and the literature on transformative AI suggest that market concentration in the model layer can produce dynamics very different from Acemoglu's static task framework. See [`korinek-vipra_2025_concentrating-intelligence`](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md).

**Paper's own caveats:**
- Acemoglu acknowledges that the figures are "back-of-the-envelope" and highly speculative (PDF p. 5–6).
- The framework explicitly sets aside effects from scientific discovery (proteins, materials) and deep productive reorganization — categories that authors like Bresnahan or Korinek consider central.
- Hulten's theorem requires that savings occur at the task level with limited substitution; if AI induces massive reallocation across sectors, effects could be larger or smaller.

## 7. Related readings

- [`aghion-bunel_2024_ai-and-growth`](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — The optimistic counterpart (0.8–1.3 pp/year vs. Acemoglu's 0.064%/year).
- [`aghion-jones-jones_2017_ai-economic-growth`](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md) — Endogenous-growth theoretical framework with AI.
- [`brynjolfsson-li-raymond_2025_genai-at-work`](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — Experimental productivity evidence from a call center; a key input to Acemoglu's calculations.
- [`acemoglu-restrepo_2018_ai-automation-work`](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — Theoretical antecedent of the task framework used here.
- [`autor_2024_rebuild-middle-class`](../labor-productivity/autor_2024_rebuild-middle-class.md) — More optimistic view of distributional effects.
- [`korinek-vipra_2025_concentrating-intelligence`](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — Model-layer market structure as a constraint on Acemoglu's scenario.
