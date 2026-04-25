# Generative AI at Work

**Authors:** Erik Brynjolfsson, Danielle Li, Lindsey R. Raymond
**Year:** 2023 (revised Nov 2023; QJE 2025)
**Venue:** QJE 2025 / NBER Working Paper No. 31161
**PDF:** [papers/pdfs/brynjolfsson-li-raymond_2025_genai-at-work.pdf](../../papers/pdfs/brynjolfsson-li-raymond_2025_genai-at-work.pdf)
**Source:** https://www.nber.org/papers/w31161

## 1. Full citation

Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). *Generative AI at Work*. NBER Working Paper No. 31161 (forthcoming, *Quarterly Journal of Economics*, 2025). National Bureau of Economic Research.

## 2. Research question

What is the causal effect of deploying a generative-AI conversational assistant on the productivity, work quality, and job experience of customer-service agents? And, crucially, how are those gains distributed across workers with different skill and experience levels? (p. 2-3)

## 3. Method

- **Data.** Administrative records at the chat and agent-month level for 5,179 customer-service agents at a Fortune 500 business-process software firm — primarily offshore outsourced — during the staggered rollout of a GPT-based assistant (p. 2; PDF p. 3, p. 12).
- **Identification strategy.** Difference-in-differences with year-month, agent, and agent-tenure fixed effects; standard errors clustered at the agent level (eq. 1, p. 13). As a robust check for treatment heterogeneity and dynamics, the authors use the interaction-weighted event-study estimator of Sun and Abraham (2021), with additional checks via Callaway–Sant'Anna, Borusyak et al., and de Chaisemartin–D'Haultfœuille (p. 13–14).
- **Main outcome variable.** Resolutions per hour (RPH); also average handle time (AHT), chats per hour (CPH), resolution rate (RR), and net promoter score (NPS) (p. 12).
- **Key assumptions.** Parallel trends, no anticipatory behavior, and comparable dynamic treatment profiles across cohorts (p. 13). The AI suggests text in real time, but the agent decides whether to use it (p. 2).

## 4. Key findings

- Access to the assistant raises average productivity (RPH) by **14%** — 0.30 additional chats per hour over a baseline of 2.6 (Table 3, Col. 2; p. 14) — with a **9%** drop in average handle time (3.8 minutes off a base of ~40 min; p. 14) and a **1.3 percentage-point** increase in resolution rate (off a base of 82%, significant at 10%; p. 14-15).
- Effects are strongly **heterogeneous by skill**: agents in the bottom quintile of the pre-AI skill index gain **34%** in RPH (0.29 log points), while those in the top quintile show no gain and exhibit small declines in resolution rate and customer satisfaction (p. 15-16).
- **By tenure**, agents with less than one month at the firm improve **46%** in RPH (0.38 log points) relative to untreated workers of the same tenure; those with more than one year show no effect (p. 16). A treated agent with 2 months of experience performs like an untreated agent with more than 6 months, evidence of an accelerated descent of the experience curve (p. 16-17).
- The assistant **improves the work experience**: customer sentiment rises by 0.18 points — roughly half a standard deviation (Table 4, Col. 1; p. 25) — requests to speak with a supervisor fall ~25% (off a base of 6 p.p.; p. 26), and turnover among new agents drops ~10 p.p., a **40%** reduction off a base of 25% (p. 26).
- Evidence of **persistent learning**: during system outages, agents with prior exposure continue to perform above their own baseline, suggesting internalization of good practices rather than mere dependence (p. 18, 20). Text analysis shows **convergence**: the communicative similarity between low- and high-skill agents rises from 0.55 to 0.61 (p. 23).

## 5. Policy implications

- **Compression of the productivity distribution.** Unlike earlier waves of IT — which tended to complement higher-skilled workers — generative AI appears to **narrow the gap between novice and experienced workers** (p. 15-16, 23). In many developing economies, where outsourced services and contact centers are a significant source of formal employment for young workers, this suggests that AI can **shorten training curves** and allow workers with fewer years of education to reach performance levels previously reserved for experienced staff.
- **Training policy.** Vocational training systems and employability programs can integrate generative assistants as active pedagogical tools, not merely as course content. The evidence of learning during outages (p. 20) implies that early exposure leaves residual human capital.
- **Distributional risk on the jobs side**, not just wages. The authors note that their data do not observe aggregate labor demand: if demand for customer service is inelastic, higher productivity could translate into **fewer positions** (p. 3, p. 27). For economies with large outsourced services sectors, this calls for active monitoring of sectoral employment and proactive transition policies.
- **"Training data" compensation.** The paper raises the point that top-performing workers are not compensated for the tacit practices the AI extracts from their chats (p. 3-4, p. 27). This opens a concrete debate for labor regulation: ownership or licensing of data generated within employment relationships? An open question for labor ministries and competition authorities.
- **Worker well-being.** The drop in turnover and improvement in customer treatment (p. 25-26) are results that receive little attention in public debate about AI, but are relevant for workforce formalization and mental health in high-emotional-pressure sectors.

## 6. Debates and caveats

- **Compatibility with Acemoglu's macro ceiling.** Acemoglu (2024) estimates TFP gains on the order of 0.66% accumulated over 10 years from AI-exposed tasks with ~14% average micro improvement (`acemoglu_2024_simple-macro-ai`). The 14% average from Brynjolfsson-Li-Raymond is **exactly the order of magnitude** Acemoglu uses as a reasonable bound; in that sense, this paper **does not contradict** Acemoglu's conservative view.
- **Tension with Aghion-Bunel.** Aghion and Bunel (2024) report gains of 0.8–1.3 percentage points per year in TFP growth in the optimistic scenario (`aghion-bunel_2024_ai-and-growth`), an order of magnitude higher. If AI generally compresses the low-productivity tail as seen here, aggregate gains could be larger than what extrapolating the average would suggest.
- **Inverted skill-bias relative to Acemoglu-Restrepo.** Acemoglu and Restrepo (2018) model automation as biased against low-skill workers (`acemoglu-restrepo_2018_ai-automation-work`). Here the direction is reversed: generative AI **levels up** less-skilled workers (p. 15-16), supporting Autor's (2024) hypothesis that AI may rebuild the middle class (`autor_2024_rebuild-middle-class`).
- **Internal caveats.** (i) A single firm in a relatively stable sector; the authors caution that effects may not generalize to environments with changing products (p. 27-28). (ii) They do not observe wages, aggregate demand, or changes in hiring composition (p. 3). (iii) Turnover results are less robust because agent fixed effects cannot be included (p. 26). (iv) The small negative effects on top performers (p. 16) are consistent with AI "distracting" or homogenizing those workers.
- **Power concentration.** The fact that a single OpenAI model captures the tacit knowledge of thousands of workers (p. 3-4) reinforces Korinek and Vipra's concern about concentration (`korinek-vipra_2025_concentrating-intelligence`).

## 7. Related readings

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — the conservative macro ceiling with which the 14% in this paper is arithmetically compatible.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — a more optimistic view of aggregate growth via AI.
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — the hypothesis that AI can rebuild the middle class; this paper supplies consistent micro-level evidence.
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — theoretical framework on tasks and automation against which the compression pattern observed here should be contrasted.
- [aghion-jones-jones_2017_ai-economic-growth](../ai-models-governance/aghion-jones-jones_2017_ai-economic-growth.md) — theoretical foundations on AI and growth.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — who captures the rents from tacit knowledge aggregated by LLMs.
