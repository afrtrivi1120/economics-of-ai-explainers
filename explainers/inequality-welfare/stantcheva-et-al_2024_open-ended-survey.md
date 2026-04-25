# Understanding Economic Behavior Using Open-ended Survey Data

**Authors:** Ingar K. Haaland, Christopher Roth, Stefanie Stantcheva, Johannes Wohlfart
**Year:** 2024 (revised December 2024)
**Venue:** NBER Working Paper No. 32421
**PDF:** [papers/pdfs/stantcheva-et-al_2024_open-ended-survey.pdf](../../papers/pdfs/stantcheva-et-al_2024_open-ended-survey.pdf)
**Source:** https://www.nber.org/papers/w32421

## 1. Full citation

Haaland, Ingar K., Christopher Roth, Stefanie Stantcheva, and Johannes Wohlfart. 2024. "Understanding Economic Behavior Using Open-ended Survey Data." NBER Working Paper No. 32421, May 2024 (revised December 2024). JEL C90, D83, D91.

## 2. Research question

How can economists use open-ended survey questions — combined with large language models (LLMs) — to uncover the motives, mental models, and narratives behind economic behaviors and expectations that traditional closed-ended questions fail to capture? The paper surveys an emerging literature and proposes a best-practices guide for collecting and analyzing qualitative data at scale.

## 3. Method

- **Type of work:** methodological review article covering publications in leading economics journals and working papers from NBER, CEPR, and CESifo since 1990 (PDF p. 2, Figure 1).
- **Data sources discussed:** single-item open-ended questions in written surveys, voice recordings, and AI-conducted qualitative interviews (PDF p. 3).
- **Analysis methods covered:**
  - Human coding with inductive vs. deductive schemes, codebooks, and inter-coder reliability (ICR) metrics such as Cohen's kappa and Krippendorff's alpha (PDF pp. 26–28).
  - LLM coding (GPT-4o, Claude 3 Opus) via API, evaluated against human benchmarks using F1-scores (PDF pp. 29–30).
  - Traditional methods: dictionaries, topic modeling, keyness analysis, ML classifiers (PDF p. 32).
- **Key assumptions:** (i) respondents can verbally articulate at least part of their reasoning (PDF p. 4, Ericsson-Simon vs. Nisbett-Wilson debate); (ii) frontier LLMs replicate human coding at acceptable quality when a subsample is validated (PDF p. 30); (iii) the richness of open-ended data justifies the additional cost relative to closed-ended questions.

## 4. Key findings

- **Explosive growth of the method:** studies using open-ended measures in leading economics journals rose from roughly 1–4 per year between 1990–2017 to approximately 37 in 2024 (PDF p. 2, Figure 1).
- **Documented thematic applications:** reasoning behind decisions (redistribution, non-participation in stock markets, gun ownership), narratives and mental models (causes of inflation), attention allocation, and associative memory (PDF pp. 5–6).
- **AI-conducted interviews match perceived human quality:** trained sociologists rate AI-conducted interviews as comparable to what a hypothetical skilled human interviewer would have achieved (PDF p. 23, citing Geiecke and Jaravel 2024). Respondents show similar selection rates as in standard surveys (PDF p. 24).
- **LLMs as scalable coders:** frontier models "provide very similar results to human coding in many cases" (PDF p. 29) and outperform dictionary-based methods, matching ML approaches without requiring additional training data (PDF p. 32).
- **Costs and privacy:** commercial APIs can be prohibitively expensive with large datasets; open-source LLMs such as Llama allow local execution with full replicability but demand computational resources and technical expertise (PDF p. 33).
- **Methodological risks:** "interpretive convergence" from excessive ICR iteration can suppress nuance (PDF p. 28); researcher degrees of freedom in codebook design threaten replicability and require pre-registration and detailed documentation (PDF pp. 34–35).

## 5. Policy implications

This is the only piece in the corpus whose contribution is methodological rather than substantive, which makes it especially valuable for survey design in a wide range of policy contexts:

- **Capturing informal-sector realities.** Standard closed-ended survey questions assume occupational and income categories built for formal labor markets. Open-ended questions analyzed with LLMs could reveal how informal workers conceptualize employment, risk, savings, and exposure to shocks — categories that are unlikely to appear in structured forms. This is particularly relevant where statistical agencies rely on labor force surveys designed around formal employment.
- **Surveys with low-literacy populations.** The authors explicitly note that AI-assisted interviews with follow-up probes improve data quality among "less literate or less educated" populations (PDF p. 23) — directly relevant for surveys in rural areas and communities where traditional written questionnaires perform poorly.
- **Measuring beliefs about AI and labor displacement.** Structured surveys on AI adoption (in the style of Bloom et al. or Bick-Blandin-Deming) can be complemented with open-ended questions to understand how workers perceive the threats and opportunities of AI, capturing local narratives that do not fit imported categories.
- **Redistributive policy design.** Stantcheva (cited in PDF p. 6) has used open-ended questions to map how citizens think about taxes and inflation. Applying this approach to policy debates on tax reform or pension reform could inform public communication and instrument design across many economies.
- **Accessible costs.** Using LLMs via API or open-source models dramatically lowers the barrier to entry for research centers with limited budgets, democratizing a methodology that previously required large teams of research assistants.

## 6. Debates and caveats

- **Validity of verbal reports.** The authors acknowledge the classic dispute between Ericsson-Simon (1980, 1993), who defend verbal reports as a window into reasoning, and Nisbett-Wilson (1977), who document unreliable introspection (PDF p. 4). This matters for any attempt to measure attitudes toward AI: what people *say* about technological displacement may not align with their revealed behavior — a concern that limits policy extrapolations.
- **Measurement vs. mechanism: contrast with Brynjolfsson.** [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) measures observed productivity (resolutions per hour) using administrative data. The open-ended questions in Stantcheva et al. open the "black box" of *why* — how agents think about the tool — but do not replace output measurement. Ideally the two methodologies are combined: administrative data for causal effects, open-ended data for mechanisms.
- **Application to the Acemoglu vs. Aghion debate.** The macro disagreement over the magnitude of AI's impact (see [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) with its ~0.66% TFP/10 years vs. [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) with 0.8–1.3 pp/year) rests in part on assumptions about which tasks are automatable. Stantcheva et al. offer an empirical path to ask workers and managers directly which parts of their jobs they believe AI can or cannot perform, complementing exposure exercises in the style of [frey-osborne_2024_genai-reappraisal](../labor-productivity/frey-osborne_2024_genai-reappraisal.md).
- **Algorithmic biases in LLM coding.** The authors warn of potential biases (Rozado 2024) and data privacy concerns (Dell 2024) (PDF p. 23), risks that are amplified in surveillance contexts documented by [yuchtman-et-al_2023_exporting-surveillance-state](../ai-models-governance/yuchtman-et-al_2023_exporting-surveillance-state.md).
- **Fragile replicability.** Researcher degrees of freedom and dependence on commercial models that may be discontinued (PDF p. 33) are a serious concern — especially when results inform public policy.

## 7. Related readings

- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — observed productivity measurement that would be complemented by open-ended questions on mechanisms.
- [korinek_2025_ai-agents-econ-research](../ai-models-governance/korinek_2025_ai-agents-econ-research.md) — use of LLMs in the economist's workflow, another dimension of the same methodological transformation.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — assumptions about automatable tasks that open-ended data could validate empirically.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — narratives about the middle class and work that are amenable to measurement with open-ended questions.
