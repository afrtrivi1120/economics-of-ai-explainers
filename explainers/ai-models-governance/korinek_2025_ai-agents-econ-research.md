# AI Agents for Economic Research

**Authors:** Anton Korinek
**Year:** 2025
**Venue:** NBER Working Paper 34202
**PDF:** [papers/pdfs/korinek_2025_ai-agents-econ-research.pdf](../../papers/pdfs/korinek_2025_ai-agents-econ-research.pdf)
**Source:** https://www.nber.org/papers/w34202

## 1. Full citation

Korinek, Anton. 2025. "AI Agents for Economic Research." NBER Working Paper 34202, September 2025. National Bureau of Economic Research. Online resources: https://www.GenAIforEcon.org

## 2. Research question

How can economists — including those with no programming background — incorporate AI agents (autonomous LLM-based systems that plan, use tools, and execute multi-step tasks) into every stage of the research workflow, from literature review to data cleaning, econometric coding, and results synthesis? The paper combines a conceptual framework with a practical guide containing working code.

## 3. Method

This is not an empirical paper but a **methodological and technical guide** for researchers. Korinek:

- **Documents** the evolution of generative AI across three paradigms: traditional chatbots (System 1-style LLMs), reasoning models (System 2, released September 2024), and agentic chatbots (December 2024) (p. 4).
- **Compares** offerings from the leading labs (OpenAI, Anthropic, Google DeepMind, xAI, Alibaba, Moonshot) using LMSYS, GPQA, and SWE-Bench V benchmarks (Tables 2 and 3, pp. 9, 11).
- **Demonstrates** with runnable examples: Beveridge curve plots in ChatGPT o3 (pp. 12–14), Deep Research-style literature reviews, "vibe coding" an OLS tool with Claude Code (pp. 28–30), and building custom Python agents using the FRED API and the LangGraph framework (pp. 32–42).
- **Key assumption:** agents are assistants — not substitutes — for the researcher; they require close human supervision (p. 6).

## 4. Key findings

- **Agents already complete meaningful multi-step tasks.** Kwa et al. (2025) show that agents can autonomously perform tasks that take a human ~50 minutes, and the duration of tasks they can handle **has doubled every seven months since 2019**; at the current pace, they could handle full-day tasks by late 2026 (p. 22).
- **The reasoning frontier saturated quickly.** GPT-5 reaches 89.4% and Grok-4 88.9% on GPQA (PhD-level questions); when the benchmark was published in November 2023 the best model scored only 39%, and domain PhD students score ~65% (p. 11). In July 2025 two models won gold medals at the International Mathematical Olympiad (p. 11).
- **Access to the frontier is becoming a function of ability to pay.** Lab premium subscriptions cost ~$200/month (a 10× increase from the prior year); a power user with all subscriptions would spend ~$1,000/month, and Sam Altman has mentioned a PhD-level system at $20,000/year (p. 16).
- **Competitive open-source alternatives exist.** Kimi-K2 (Moonshot, July 2025) delivers near-frontier performance at **15 cents per million input tokens vs. $15 for Claude — a 100× difference** (p. 18). DeepSeek and Alibaba Qwen also offer open-weights models useful for researchers with limited budgets.
- **"Vibe coding" democratizes technical implementation.** Korinek shows that with ~300 lines of Python (largely generated from natural language) one can build a multi-agent Deep Research system in LangGraph; the full report in his example cost ~1 cent in tokens and 15 Tavily searches (p. 43).
- **Documented limitations:** hallucinations, "pseudo-data" generated when the agent cannot access the real source (p. 15), fragility to minor prompt changes, vulnerability to prompt injection, and still-weak economic reasoning ("they sometimes misapply theoretical frameworks and reproduce common misconceptions present in their training data") (p. 6).

## 5. Policy implications

- **Closing the computational gap.** For economics departments, central banks, and research centers — particularly those without large technical teams — agents offer a concrete path to overcome gaps in programming skills: vibe coding allows building functional econometric tools without dedicated technical staff (p. 5). Junior researchers can now "achieve what previously required entire teams" (p. 47).
- **Anti-dependence strategy and data sovereignty.** Korinek recommends **maintaining flexibility across providers rather than committing to a single ecosystem** (p. 6). For institutions handling sensitive data (central bank market information, government microdata, administrative records), locally deployed open-weights models (gpt-oss, Llama, Qwen) are the "gold standard" for security and allow compliance with data non-transfer requirements (p. 19).
- **Cost and unequal access.** The $200/month premium price and the possibility of $20,000/year fees for PhD-level systems is a **warning signal for public research budgets**. Institutional API agreements (pay-per-use) or the use of Kimi-K2 / Qwen / DeepSeek may be more viable strategies than multiple individual subscriptions (p. 19).
- **Local MCP infrastructure.** Public institutions — statistical agencies, central banks, research centers, universities — could publish **MCP (Model Context Protocol) servers** that expose their databases to agents in a standardized way, analogous to the role FRED plays in the US (p. 44). This would increase the visibility and use of national data in automated research workflows.
- **Researcher training.** The paper suggests economists should "embrace these tools now, not just to increase productivity but to understand their capabilities and limitations" (p. 47). Doctoral and master's programs should include AI agents in their methodological curriculum.

## 6. Debates and caveats

- **Democratizing optimism vs. concentration.** Korinek presents an internal tension: although vibe coding democratizes access, the GPQA/SWE-Bench benchmarks show that advanced capabilities remain concentrated in well-funded labs (p. 11), and "power users who best know how to deploy agents may benefit far more" (p. 5). This reading is consistent with the author's parallel work with Vipra — see `korinek-vipra_2025_concentrating-intelligence` — which emphasizes the risk of structural concentration in the AI industry.
- **Actual capability vs. announced capability.** The paper explicitly documents overconfidence: OpenAI's Deep Research system claimed that "AI agents are rapidly transforming how economists do research" — Korinek himself is not sure they improve causal inference (p. 26). This is relevant in relation to empirical studies like `brynjolfsson-li-raymond_2025_genai-at-work` that measure real productivity gains in more limited tasks.
- **Economic reasoning vs. synthesis.** Korinek is clear: agents are "superb assistants but not yet independent researchers" (p. 47). This qualifies more expansive views on the automation of scientific research such as those discussed in `agrawal-gans-goldfarb_2025_research-agenda-tai` and `agrawal-gans-goldfarb_2025_bicycles-for-the-mind`.
- **Novel risks:** Korinek cites Gans (2025) on the manipulation of LLM reviewers through prompt injection (p. 47), suggesting that the mass integration of agents into academic workflows opens previously unknown gaming vectors.

## 7. Related readings

- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — the other side of the coin: why the AI frontier tends to concentrate in a few labs.
- [agrawal-gans-goldfarb_2025_bicycles-for-the-mind](../firms-market-structure/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.md) — AI as a "bicycle for the mind" of the researcher, complementary to Korinek's "agents as assistants" framing.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — research agenda for transformative AI.
- [brynjolfsson-li-raymond_2025_genai-at-work](../labor-productivity/brynjolfsson-li-raymond_2025_genai-at-work.md) — empirical evidence on real productivity gains from generative AI in the workplace.
