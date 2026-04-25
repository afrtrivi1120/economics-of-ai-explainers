# The Economics of Bicycles for the Mind

**Authors:** Ajay K. Agrawal, Joshua S. Gans, Avi Goldfarb
**Year:** 2025
**Venue:** NBER Working Paper No. 34034 (July 2025)
**PDF:** [papers/pdfs/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.pdf](../../papers/pdfs/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.pdf)
**Source:** https://www.nber.org/papers/w34034

## 1. Full citation

Agrawal, A. K., Gans, J. S., & Goldfarb, A. (2025). *The Economics of Bicycles for the Mind*. NBER Working Paper No. 34034. National Bureau of Economic Research.

## 2. Research question

How should we formally model computers and AI as "cognitive tools" — bicycles for the mind, in Steve Jobs's metaphor — and what does that framework imply for productivity, inequality, automation, and organizational design? The paper builds a unifying model that explains why computers appear to have increased inequality while generative AI, at least so far, appears to reduce it within adopting firms (p. 2).

## 3. Method

- **Theoretical model**, not empirical. There are no primary data; the paper synthesizes the existing empirical literature on computers and AI.
- An agent performs **iterative task improvement**. In each period, with probability γ ("opportunity judgment") the agent identifies an improvement opportunity; when implementing it, the agent exerts effort *e* with cost *c(e)* and probability of success *p(se)*, where *s* is implementation skill (p. 5–6).
- A cognitive tool, parameterized by θ, **substitutes for implementation effort** and **complements opportunity judgment** (the capacity to see what to improve). "Payoff judgment" α — knowing what action to take given a diagnosis — is only complementary under specific conditions (p. 13, Definition 1).
- Key assumptions: *p(·)* is concave (diminishing returns to effort), *c(·)* is convex, and the tool reduces the ratio of marginal benefit to marginal cost of effort (equation 5, p. 7).
- Extensions: wage inequality with heterogeneous skills (section 4), automation vs. human-tool collaboration (section 5), and team production with judgment specialists (section 6).

## 4. Key findings

- **Cognitive tools reduce human effort but increase net output** (Proposition 1, p. 14). The worker does less but produces more — the essence of the "bicycle for the mind."
- **Inequality follows a U-shape** with respect to tool quality θ (Proposition 3, p. 18). Initially, tools favor low-skill workers ("inverse skill bias," the θ/s term), reducing wage variance; eventually, the amplification of judgment (γ₀, α) reverses the pattern and inequality rises again (p. 19).
- **This reconciles two literatures**: the evidence that computers increased inequality (Autor et al. 2006; Acemoglu-Restrepo 2018) reflects the long amplification phase; the evidence that generative AI reduces it within the firm (Brynjolfsson et al. 2025; Cui et al. 2025; Dell'Acqua et al. 2023) corresponds to the initial inverse skill bias phase (p. 21).
- **Full automation faces three multiplicative "penalties"** relative to human-tool collaboration: an opportunity-identification penalty (ρ_γ < 1), a dynamic-adjustment penalty (Φ(ρ_γ) < 1), and a payoff-judgment penalty (ρ_α < 1) (Proposition 4, p. 25).
- **The tool-improvement paradox**: as cognitive tools improve, full automation becomes *harder* to justify, not easier (p. 26). This explains why complete automation of complex tasks (medical diagnosis, strategic planning) has remained elusive even as AI advances (p. 26).
- **In teams**, better tools shift control over implementation away from the implementation-skill specialist and toward the judgment specialist — but a "communication tax" complicates optimal assignment (Proposition 5, p. 28; section 6.3, p. 29).

## 5. Policy implications (Colombia / Latin America)

- **Bet on the complement, not the substitute.** The framework predicts that generative AI, in its current phase, is closing productivity gaps within firms — which is an opportunity for Colombian workers without elite credentials (junior analysts, rural physicians, teachers, lawyers at small firms) to access tasks today reserved for experts. This reinforces the "let non-elites do expert tasks" framing from Autor.
- **Design authority, not just tool delivery.** The key result from the medical example (p. 11) — "AI should be prioritized for physicians who have the authority and knowledge to act" — implies that in Colombia, regulations on prescription, professional scope, and function delegation (Ley 100, MinSalud scope-of-practice rules) determine how much value AI generates. A world-class diagnostic AI creates no value if the technician operating it cannot prescribe.
- **Do not expect full automation.** For the Colombian public sector evaluating whether to replace workers with AI, the model warns: the rigidity of pre-specified judgment makes total automation costly wherever context varies (citizen services, administrative justice, health). The dominant path is hybrid.
- **Watch the inequality U-turn.** If Colombia adopts generative AI today and captures the inverse skill bias phase, it could reduce within-firm gaps — but the model predicts that with more mature tools, "opportunity judgment" (creativity, problem definition) will again command a premium, which requires parallel investment in higher-order education.

## 6. Debates and caveats

- **It is a model, not new evidence.** The magnitudes (how pronounced the U is, when the inflection point θ* occurs) depend on unobserved variances in skills vs. judgment (p. 18, equation 30). The paper does not quantify anything empirically.
- **Selective optimism about generative AI.** The authors rely on Brynjolfsson-Li-Raymond and Cui et al. to argue that AI reduces within-firm inequality — see [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md). But they acknowledge exceptions: Otis et al. (2023) on SMEs in Kenya shows that lower-performing firms do *not* benefit (p. 22). For Colombia/Latin America, this caveat is central: if there is a minimum human-capital floor required to capture value from AI, the inverse skill bias never materializes for the poorest workers.
- **Diverges from macro pessimism.** The framework treats AI primarily as a productive complement. This contrasts with Acemoglu's conservative estimate (~0.66% TFP over 10 years) — see [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — and sits closer to the optimistic view of Aghion-Bunel ([aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md)). The paper does not resolve the macro dispute; it only provides microfoundations on the agent side.
- **Teams and authority under-explored empirically.** The teams section (p. 26–29) is theoretically novel but untested; the results on "communication tax" and decision-rights assignment are hypotheses for future research.

## 7. Related readings

- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — the "let non-elites do expert tasks" thesis that this paper formalizes microeconomically.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — empirical evidence of inverse skill bias in call centers; the paradigm case the model aims to explain.
- [johnson_2024_ricardo-thompson-ai](../labor-productivity/johnson_2024_ricardo-thompson-ai.md) — the complementarity vs. substitution distinction that anchors section 5 on automation.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — research agenda by the same authors; this paper is one piece of that program.
- [gans_2025_genius-on-demand](../firms-market-structure/gans_2025_genius-on-demand.md) — Gans solo, on how AI democratizes access to expert "genius."
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — macro-pessimist counterpoint to the micro-optimism of this paper.
