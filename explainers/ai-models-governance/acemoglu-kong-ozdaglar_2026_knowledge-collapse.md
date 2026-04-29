# AI, Human Cognition and Knowledge Collapse

**Authors:** Daron Acemoglu, Dingwen Kong, Asuman Ozdaglar
**Year:** 2026 (February 2026)
**Venue:** NBER Working Paper No. 34910
**PDF:** [papers/pdfs/acemoglu-kong-ozdaglar_2026_knowledge-collapse.pdf](../../papers/pdfs/acemoglu-kong-ozdaglar_2026_knowledge-collapse.pdf)
**Source:** https://www.nber.org/papers/w34910

## 1. Full citation

Acemoglu, D., Kong, D., & Ozdaglar, A. (2026). *AI, Human Cognition and Knowledge Collapse*. NBER Working Paper No. 34910. National Bureau of Economic Research.

## 2. Research question

Generative AI tools — and especially the next wave of *agentic* systems that can deliver context-specific decisions and recommendations on demand — promise to make every individual a better decision-maker. But human cognition is not just an individual phenomenon: each person's effort to understand a problem produces (a) private knowledge useful to herself and (b) a "thin" public signal that contributes to the community's stock of *general knowledge* on which everyone else builds. The paper asks: when an accurate AI substitute for context-specific learning effort becomes available, what happens to the dynamic accumulation of *general* knowledge? Does the convenience of agentic recommendations come at the cost of long-run collective understanding, and if so under what conditions, with what welfare consequences, and what regulation can mitigate the harm? (p. 2-4).

## 3. Method

This is a fully theoretical paper. The authors develop a tractable dynamic model with the following ingredients:

- **Agents and time.** Discrete time, a continuum of short-lived agents per period, partitioned into "islands" within which knowledge is shared (p. 6-7).
- **Two types of knowledge.** A *common state* θ_t that evolves as a random walk (general knowledge that is broadly applicable, like macro-financial fundamentals or basic medical mechanisms) and an *idiosyncratic state* θ_i,t (context-specific knowledge unique to each agent's task) (p. 7).
- **Production.** Successful action requires *both* general and context-specific knowledge — Δ_I = 0, Δ_X > 0 (Assumption 1) — i.e., context-specific knowledge alone produces no value, capturing strong complementarity (p. 7-8). Leontief production is a leading example.
- **Effort generates two signals.** Agent i's effort e_i,t produces a private signal about her idiosyncratic state with precision λ_I·e_i,t and a public signal about the common state with precision λ_G·e_i,t. The public signal is aggregated within the island, *uninternalized* by the individual (so it is a positive externality of effort) (p. 9-10).
- **Agentic AI.** Modeled as a context-specific information signal s^A with precision τ_A. Crucially, agentic AI does not directly produce general knowledge; it substitutes for the *private-learning* reason an agent would put in effort (p. 9-10).
- **Equilibrium.** Perfect Bayesian equilibrium with effort, predictions, and Kalman filtering. The dynamic system tracks how *public precision* X_t — the stock of general knowledge — evolves under different levels of agentic AI accuracy (p. 11-13).
- **Welfare.** Long-run average utility, evaluated in steady states; comparative statics on agentic precision τ_A, aggregation capacity I, and effort cost convexity α.
- **Extensions.** (i) AI also improves the aggregation of general knowledge; (ii) AI generates synthetic data that can substitute for human effort; (iii) effort can partially separate context-specific from general-knowledge production. The authors show their main qualitative results survive each extension under stated parameter restrictions (p. 29-32).

## 4. Key findings

- **Substitution vs. complementarity.** Public precision X_t (general knowledge) **complements** human effort: more general knowledge raises the marginal productivity of context-specific learning, encouraging more effort. Agentic AI precision τ_A **substitutes** for human effort: better recommendations crowd out the private incentive to learn (Observation 1, p. 13).
- **Static gains, dynamic harm.** A more accurate agentic AI *statically* helps each generation make better decisions. But because effort generates the public signal that builds general knowledge, lower effort tomorrow means a smaller stock of general knowledge — and eventually, in equilibrium, *less* useful AI recommendations and less effective decision-making (p. 4).
- **"Knowledge collapse" steady state.** When effort cost is sufficiently elastic (α-1 < 1/4), the dynamic system has *multiple* steady states: a high-knowledge equilibrium and a "knowledge-collapse" trap with zero general knowledge. As agentic AI accuracy rises, the basin of attraction of the collapse state expands. Beyond a critical threshold τ_A^c, the high-knowledge steady state vanishes entirely and the system collapses regardless of initial conditions (p. 4, Proposition 11).
- **Welfare is non-monotone in AI accuracy.** Long-run welfare U^+(τ_A) is initially *increasing* in agentic precision (better recommendations help) but eventually *decreasing*, with U^+ → 0 as τ_A → ∞ in the unique-steady-state regime (Proposition 10, p. 26). There is therefore an interior welfare-maximizing precision τ_A* — *less* than the maximum the technology can deliver.
- **Aggregation always helps.** Improving the community's ability to pool human-generated knowledge (larger I) shrinks the basin of attraction of the collapse state and raises welfare unambiguously (p. 4, 26-27). This is the bright side: invest in *human* knowledge sharing — Stack Overflow, Wikipedia, peer-reviewed literature — and resilience to AI substitution rises.
- **Scaling-law result.** As aggregation capacity I → ∞, the collapse threshold τ_A^c grows only *logarithmically* in I, and the welfare-maximizing precision τ_A^* / τ_A^c → 1/α (Proposition 12, p. 27). Even arbitrarily powerful aggregation does not let society approach the collapse boundary; the planner optimally stays bounded away from it.
- **Optimal information-design regulation.** Modeling regulation as Gaussian *garbling* (adding noise) of the agentic signal, the authors derive an optimal **two-phase policy** under multiple equilibria: a temporary moratorium phase (full suppression, κ_t = 0) to rebuild the stock of general knowledge, followed by a permanent cap at the welfare-maximizing precision τ_A^* (Proposition 13, p. 28-29). If general knowledge is initially abundant, only the cap is needed.
- **Synthetic data caveat.** When AI also generates synthetic data correlated with the common state, knowledge collapse can be *softened* — the zero steady state becomes a low-knowledge one rather than a true zero — provided synthetic data is not a perfect substitute for human-generated knowledge (Proposition 15, p. 31).

## 5. Policy implications

- **Information-design regulation has theoretical justification.** Most current AI policy debates focus on safety, content moderation, and IP. This paper provides a different rationale: *information capacity* of agentic AI should be capped (or temporarily suppressed) to preserve the externality of human learning effort that builds collective knowledge (p. 27-29).
- **Invest in human knowledge aggregation infrastructure.** Public goods that pool human-produced general knowledge — open-access scientific publishing, Wikipedia, Stack Overflow, public-sector data repositories — are *complements* to AI welfare, not redundant alternatives. Public investment in such infrastructure has higher social returns than its private benefit suggests (p. 27).
- **Two-phase regulation as a transition tool.** The optimal policy is not a permanent prohibition but a sequenced cap. This is unusually concrete actionable theory: regulators can imagine phasing in agentic AI subject to monitoring of collective-knowledge stocks (e.g., participation rates on Stack Overflow / Wikipedia in domains where AI is most substitutable) and adjusting suppression accordingly (p. 28-29).
- **Empirical motivation is already visible.** The authors cite del Río-Chanona et al. (2024) showing reduced engagement on Stack Overflow following ChatGPT availability and Lyu et al. (2025) showing reduced Wikipedia article generation in domains where ChatGPT is a good substitute (p. 2). Knowledge collapse is not purely hypothetical.
- **Subsidies for "explainability" and pedagogical AI.** Tools that *complement* rather than substitute for human learning — AI study modes, explanatory feedback, AI as a tutor — have value beyond their private benefit because they help maintain the human effort that sustains collective knowledge (p. 4-5).
- **Distinguish content-generation AI from agentic AI.** The model implies that AI which mostly aggregates existing general knowledge (e.g., a search engine over the existing internet) is welfare-improving and resilience-enhancing, while AI that *replaces* the act of context-specific learning is the source of collapse risk. Policy distinctions between these classes — analogous to distinguishing search from autonomous agents — would be useful (p. 27-29).

## 6. Debates and caveats

- **Theoretical only.** No empirical estimation. The authors are explicit that their analysis "is purely theoretical" (p. 33) and that the framework is intended to guide measurement of effects that should be evaluated empirically.
- **Acemoglu's continuity with his macro view.** This paper sharpens Acemoglu's earlier conservative position (`acemoglu_2024_simple-macro-ai`): even if AI raises within-task productivity, the dynamic externality on collective knowledge can dominate, dragging long-run welfare down. The paper offers a microfoundation for why aggregate AI gains may be smaller, or even negative, than micro experiments suggest.
- **Tension with AI-as-augmentation views.** Agrawal-McHale-Oettl (2026) (`agrawal-mchale-oettl_2026_ai-in-science`) argue AI augments human scientists rather than substituting for them, with judgment retained on humans. Acemoglu et al. emphasize the *substitution* margin and its dynamic externality. Whether AI complements or substitutes is a parameter (Δ_X vs. τ_A in the model) and the welfare answer depends on which dominates in practice.
- **Empirical resonance with shen-tamkin.** The Shen & Tamkin (2026) (`shen-tamkin_2026_ai-skill-formation`) experiment provides clean micro-evidence of the substitution mechanism: AI assistance reduces human effort in producing the very general skills the model takes as the source of collective knowledge. The two papers are theory-empirics counterparts.
- **Tension with optimistic CEO views.** Amodei, Altman, and Hassabis (cited by Agrawal-McHale-Oettl 2026) all argue AI will compress decades of human learning into months. Acemoglu et al.'s answer is that *aggregate* progress depends on human effort being *maintained*, not just on AI being accurate; AI compressing scientific progress is consistent with their model only if it also raises aggregation capacity I, not just precision τ_A.
- **Modeling choices.** Quasi-Leontief production (Δ_I = 0), atomistic agents who do not internalize their public-signal externality, and Gaussian information structure are all stylized. The extensions to imperfect separability and partial AI-driven aggregation suggest the qualitative results are robust, but quantitative magnitudes will depend on parameters that have not been calibrated.
- **Regulatory feasibility.** Garbling agentic AI signals is technically simple; politically difficult. The optimal two-phase policy assumes a regulator with a credible commitment mechanism, which may not exist for cross-border AI services.

## 7. Related readings

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — the conservative macro counterpart; this paper provides a theoretical mechanism for why micro-level gains may not aggregate.
- [shen-tamkin_2026_ai-skill-formation](../labor-productivity/shen-tamkin_2026_ai-skill-formation.md) — micro-level empirical evidence of the substitution mechanism the model formalizes.
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — task-based automation framework that this paper extends to information substitution.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — concentration of AI capability in a few firms; complements the externality argument here.
- [agrawal-mchale-oettl_2026_ai-in-science](../ai-models-governance/agrawal-mchale-oettl_2026_ai-in-science.md) — augmentation view of AI in scientific knowledge production; provides the optimistic counterpoint.
- [korinek_2025_ai-agents-econ-research](../ai-models-governance/korinek_2025_ai-agents-econ-research.md) — agentic AI applied to a specific knowledge domain (economics research).
- [johnson_2024_ricardo-thompson-ai](../labor-productivity/johnson_2024_ricardo-thompson-ai.md) — historical analogues of technologies that hurt workers in the short run; this paper extends the logic to long-run knowledge.
