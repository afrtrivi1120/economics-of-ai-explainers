# Artificial Intelligence and Economic Growth

**Authors:** Philippe Aghion, Benjamin F. Jones, Charles I. Jones
**Year:** 2017
**Venue:** NBER Working Paper 23928 (later published as a chapter in *The Economics of Artificial Intelligence: An Agenda*, U. Chicago Press, 2019)
**PDF:** [papers/pdfs/aghion-jones-jones_2017_ai-economic-growth.pdf](../../papers/pdfs/aghion-jones-jones_2017_ai-economic-growth.pdf)
**Source:** https://www.nber.org/papers/w23928

## 1. Full citation

Aghion, Philippe, Benjamin F. Jones, and Charles I. Jones. 2017. "Artificial Intelligence and Economic Growth." NBER Working Paper No. 23928. National Bureau of Economic Research, Cambridge, MA.

## 2. Research question

How does artificial intelligence — understood as the latest phase of a 200-plus-year automation process — affect long-run economic growth, the distribution of income between capital and labor, and the possibility of technological "singularities"? The paper aims to build the theoretical scaffolding (not empirical evidence) needed to answer these questions (p. 1, p. 2).

## 3. Method

- **Model class:** Neoclassical and endogenous growth theory. Builds on Zeira (1998) and Acemoglu–Restrepo (2016), modeling AI as the automation of tasks (p. 3, p. 5).
- **Key assumptions:**
  - CES production of goods with an elasticity of substitution *less than one* (ρ < 0): tasks are complements, not substitutes (eq. 5, p. 7). This is the central mechanism that activates the "Baumol effect."
  - Each automated task uses one unit of capital; each non-automated task uses one unit of labor (eq. 2, p. 5; eq. 6, p. 7).
  - A fraction β_t of tasks are automated at time t; the authors treat β_t as exogenous (p. 9).
  - Standard neoclassical closure with a constant investment rate (p. 5, p. 8).
- **Analytical strategy:** Comparative statics and model simulations (Figures 1–3) without calibration to real data; the stated goal is to "shape a research agenda" (p. 2).

## 4. Key findings

- **The Baumol effect dominates.** When the elasticity of substitution across tasks is less than one, the economy ends up constrained not by what AI does well but by the essential tasks that improve slowly: "growth may be constrained not by what we do well but rather by what is essential and yet hard to improve" (Abstract, p. 1; restated p. 3, p. 29).
- **Balanced growth despite near-total automation.** In the Figure 1 simulation, with continuous automation (a fraction θ of non-automated tasks automated each year), GDP growth stabilizes at approximately 2% per year over 500 years, β_t → 1, and the capital share asymptotes to roughly 1/3 while labor retains roughly 2/3 of GDP (Figure 1, p. 12; text p. 11).
- **Automation is, counterintuitively, *labor-augmenting* and *capital-depleting*.** With ρ < 0, automating a task is equivalent to a combination of technical change that raises labor productivity and dilutes the return to capital (eq. 16, p. 10). This reverses the usual intuition that automation always favors capital.
- **Idea production and endogenous growth.** If AI automates the production of ideas (Section 3), the scarce factor (human researchers) limits acceleration when ρ < 0; but with Cobb-Douglas idea production, automating that process can permanently raise the growth rate (p. 18, eq. 25 p. 20).
- **Singularities are possible but fragile.** If AI automates *all* tasks (Example 1, p. 21–22), or if γ ≡ (σ/(1−α))·(β/(1−φ)) > 1 with Cobb-Douglas production (Example 3, eq. 36, p. 24), the model generates Type II growth explosions (infinite output in finite time). But the authors emphasize that these results depend on particular assumptions and are reversed by Baumol-type bottlenecks or "fishing-out" (p. 27, p. 28).
- **Three classes of bottleneck:** limits to full automation, search limits (ideas become progressively harder to find; φ ≤ 0), and natural laws (the second law of thermodynamics, physical constraints) (p. 27–29). Moore's Law is cited as a warning: computing power grew by 10^11 since World War II (p. 28, note 16) and GDP growth did not accelerate.

## 5. Policy implications

- **Do not expect an automatic AI shock on aggregate productivity.** The framework predicts that sectoral automation can coexist with stable aggregate growth rates, because essential but hard-to-improve sectors (care work, in-person education, infrastructure) absorb an ever-growing share of spending. Policymakers focused solely on adopting AI in manufacturing or financial services should expect modest macro effects unless bottlenecks in Baumol-intensive sectors (health, education, justice) are also addressed.
- **The binding constraint is human complementarity.** If scarce labor anchors growth, the policies with the highest return are those that raise labor productivity in non-automated tasks: teacher training, professionalizing care work, and skills certification. This aligns with Autor's argument about re-expanding middle-class employment (see `autor_2024_rebuild-middle-class`).
- **Capital vs. labor shares.** The model predicts that the capital share may rise transitionally but is bounded by the Baumol effect. For tax policy, this moderates alarmism about a "massive capital capture" while warning that the transitional dynamic can still increase concentration (Figure 2, p. 14).
- **Research and development.** If AI can automate part of the innovation process (p. 17), returns to domestic R&D investment rise: an AI that multiplies the productivity of each researcher makes maintaining national research capacity more valuable, not less.

## 6. Debates and caveats

- **Conservative vs. optimistic.** Aghion–Jones–Jones is theoretical and estimates no magnitudes; in later work, Aghion–Bunel quantify an impact of 0.8–1.3 percentage points per year on growth (see `aghion-bunel_2024_ai-and-growth`), while Acemoglu (2024) offers the most conservative estimate — roughly 0.66% TFP over 10 years (see `acemoglu_2024_simple-macro-ai`). This paper is the *theoretical plumbing* on which both camps build and dispute.
- **Critical assumption ρ < 0.** The entire "balanced growth despite automation" result hinges on tasks being gross complements (p. 9, p. 10). If ρ > 0 (substitutes), even without automation the model generates explosive growth (p. 19). The choice of ρ < 0 is defended as "the natural case," but it is an assumption, not a finding. Acemoglu–Restrepo (2018) work within a richer framework that endogenizes this elasticity (see `acemoglu-restrepo_2018_ai-automation-work`).
- **β is exogenous.** The authors explicitly acknowledge that treating the share of automated tasks as exogenous is a limitation and that endogenizing it "is an important direction for future research" (p. 9). Empirical evidence on real-world GenAI adoption (see `brynjolfsson-li-raymond_2025_genai-at-work`) suggests that β grows very unevenly across firms and workers.
- **No market structure.** The paper introduces firms in a later section, but the core growth argument ignores market power. Korinek–Vipra (2025) show that AI scaling laws generate strong concentration (see `korinek-vipra_2025_concentrating-intelligence`), a channel absent here.
- **Singularities as a rhetorical exercise.** The four "paths" to singularity (Section 4.1) are constructed to show the assumptions under which they *could* occur; the authors themselves list three classes of objections (automation limits, search limits, Baumol) that make them unlikely (p. 27–29).

## 7. Related readings

- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — the conservative empirical version of the task framework; estimates ~0.66% TFP over 10 years.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — Aghion revisits the same question with French data and obtains substantially higher figures (0.8–1.3 pp/yr).
- [acemoglu-restrepo_2018_ai-automation-work](../labor-productivity/acemoglu-restrepo_2018_ai-automation-work.md) — the sibling task framework, with endogenous automation and the creation of new tasks.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — field empirical evidence on β in a real firm (call center).
- [autor_2024_rebuild-middle-class](../labor-productivity/autor_2024_rebuild-middle-class.md) — complementary interpretation: if AI complements non-expert labor, it can re-expand the middle class.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — adds the market-structure channel that this paper omits.
