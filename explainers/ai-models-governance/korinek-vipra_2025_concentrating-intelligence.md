# Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence

**Authors:** Anton Korinek, Jai Vipra
**Year:** 2024 (NBER WP, forthcoming *Economic Policy* 2025)
**Venue:** NBER Working Paper No. 33139
**PDF:** [papers/pdfs/korinek-vipra_2025_concentrating-intelligence.pdf](../../papers/pdfs/korinek-vipra_2025_concentrating-intelligence.pdf)
**Source:** https://www.nber.org/papers/w33139

## 1. Full citation

Korinek, Anton, and Jai Vipra. 2024. "Concentrating Intelligence: Scaling and Market Structure in Artificial Intelligence." NBER Working Paper No. 33139. National Bureau of Economic Research. Forthcoming, *Economic Policy* 2025.

## 2. Research question

Is the market structure for foundation models — particularly large language models (LLMs) — moving toward monopolistic concentration, and what competition-policy tools can regulators use to preserve a competitive landscape? The authors examine the technological features (cost scaling, scaling laws, vertical integration) that could "tip" the market toward one or a few dominant players.

## 3. Method

- **Approach:** descriptive institutional-economic analysis (not econometric). It combines:
  - Market data and benchmarks (LMSYS leaderboard, valuations, market shares as of end-2023/2024).
  - Cost-structure analysis of foundation models (pre-training, fine-tuning, inference).
  - Review of current regulatory frameworks (FTC, DoJ, CMA, EU AI Act, Digital Markets Act).
- **Key conceptual framework:** economies of scale and scope arising from high fixed costs + low variable costs; "scaling laws" (Kaplan et al. 2020; Hoffmann et al. 2022) predicting that performance grows with compute investment.
- **Assumptions:** capability advances will remain correlated with compute spending for another 3–5 years (p. 15); economic returns to AI will be sufficient to justify the investment.

## 4. Key findings

- **Explosive pre-training costs:** Epoch (2024) estimates that training Gemini Ultra in 2023 cost USD 130 million (PDF p. 13). Compute deployed in frontier models has grown 4.1× per year over the past 15 years (PDF p. 14), and compute spending 3.09× per year (PDF p. 14, n. 6).
- **Upstream concentration (chips):** Nvidia controlled approximately 92% of the GPU market according to Fernandez et al. (2023) (Figure 3, PDF p. 11), and a Wells Fargo report estimated 98% of the data-center GPU market in February 2024 (PDF p. 11).
- **Highly concentrated initial market shares:** at end-2023, OpenAI (via GPT-4) captured 39% of the generative AI market and Microsoft (also via GPT-4) 30% — together 69% (Figure 1, PDF p. 9). Google DeepMind came in a distant second with 7%.
- **But fierce competition at the frontier:** as of November 4, 2024, at least 16 labs had models comparable to the original GPT-4 (PDF p. 3), and the four leaders (OpenAI, Google DeepMind, xAI, Anthropic) are clustered within 54 LMSYS points — ChatGPT-4o has only a 55.3% probability of beating Gemini 1.5 Pro 002 and 57.7% against Claude 3.5 Sonnet (PDF p. 5). This suggests "Bertrand-style competition" with prices near variable cost (PDF p. 6).
- **Academic talent drained to industry:** Henshall (2024) reports that the share of AI Ph.D.s going to industry rose from 21% in 2004 to 73% in 2022 (PDF p. 17), raising the cost of the researcher pipeline and deepening incumbents' advantages.
- **Tipping risks and feedback loops:** the authors identify a new mechanism — the "intelligence feedback loop" — by which the leading lab uses its own internal models to accelerate the next version, which could in the limit produce an "intelligence explosion" (Good 1965) and self-reinforcing first-mover advantages (PDF p. 19).
- **Concerning vertical integration:** OpenAI already required exclusivity clauses from investors (including Nvidia) in its October 2024 funding round (PDF p. 10); Microsoft "absorbed" Inflection AI via a USD 650 million licensing deal that avoided antitrust review (PDF p. 10). Microsoft invested ~USD 14 billion in OpenAI (PDF p. 7); OpenAI was valued at USD 157 billion in October 2024 (Figure 2, PDF p. 9).

## 5. Policy implications

This paper is essential reading for policymakers because it frames AI as **critical infrastructure with a natural tendency toward global monopoly**, not as just another competitive market:

1. **Compute sovereignty limited by design:** most economies will not have the capacity to compete at the frontier of LLM training (training costs are projected in the billions of USD by 2027 according to Cottier et al. 2024, cited in bibliography PDF p. 27). National AI strategies in non-frontier economies must assume that they **will be consumers, not producers**, of frontier models, and focus on (a) negotiated access to APIs on non-discriminatory terms, (b) fine-tuning capacity using domestic data, and (c) local talent to evaluate and adapt models.
2. **Preventive competition policy:** competition authorities should incorporate lessons from the European DMA and the FTC/CMA analysis cited by the authors (PDF p. 11–12). Specifically: monitor "stealth" acquisitions like Microsoft–Inflection, exclusive cloud–LLM contracts, and early-access privileges that distort downstream markets.
3. **Data as a strategic asset:** the paper notes that 79% of U.S. news sites blocked OpenAI's crawlers (PDF p. 16). Governments could coordinate public data-sharing policies (health, education, anonymized judicial data) to reduce dependence on models trained only on dominant-language corpora and to strengthen their negotiating position vis-à-vis foreign providers.
4. **Risk of an "intelligence divide":** the authors warn that the EU faces an "intelligence divide" risk by lacking a frontier lab of its own (PDF p. 24). In many developing economies this risk is more severe: if global concentration consolidates, access, pricing, and terms of use for models will be determined by regulators in the U.S., EU, and China — leaving non-frontier economies with little structural leverage.

## 6. Debates and caveats

- **Optimists vs. pessimists on magnitude:** the authors explicitly cite Acemoglu's (2024) conservative estimate of a growth effect of **0.07% per year** over the next decade — under that scenario, they say, "the market concentration implications will be a footnote in economic history" (PDF p. 4). Korinek and Vipra lean closer to the optimist camp (Hatzius et al. 2023; JP Morgan 2024, which project that AI could underpin 7–10% of global GDP within a decade, PDF p. 4). Compare with `acemoglu_2024_simple-macro-ai` (conservative TFP estimate) and `aghion-bunel_2024_ai-and-growth` (~0.8–1.3pp/yr).
- **Is tipping inevitable?** The analysis stresses that as of November 2024 there was fierce competition, not monopoly. Joshua Gans (2024, cited PDF p. 19) argues that data feedback loops do not guarantee dominance if returns to additional data diminish quickly. The authors acknowledge this tension but bet that rising costs will eventually reduce the number of viable players.
- **Competition vs. safety:** the authors honestly flag an ethical trade-off: making the market more competitive (via open source) may clash with regulating AI safety (PDF p. 24). This contrasts with more maximalist pro-open-source views.
- **Empirical limitations:** the paper is descriptive and prospective, not causal. It estimates no elasticities, tests no hypotheses, and depends heavily on a November 2024 snapshot that is already aging quickly.

## 7. Related readings

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Conservative estimate of macro impact that, if borne out, makes concentration concerns a secondary issue.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — More optimistic view of AI-driven growth; raises the market prize and reinforces the urgency of competition policy.
- [aghion-jones-jones_2017_ai-economic-growth](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md) — Theoretical framework on bottlenecks and ideas becoming scarce — relevant to the "intelligence feedback loop."
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — Microeconomic evidence that LLMs do generate real productivity gains, justifying the investment that fuels concentration.
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — Task and automation framework that complements the question of who captures the rents.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — On how AI could redistribute market power in labor, dependent on the upstream market structure that Korinek-Vipra describe.
