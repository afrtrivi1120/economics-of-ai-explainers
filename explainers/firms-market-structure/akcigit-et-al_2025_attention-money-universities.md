# Attention (And Money) Is All You Need: Why Universities Are Struggling to Keep AI Talent

**Authors:** Ufuk Akcigit, Craig A. Chikis, Emin Dinlersoz, Nathan Goldschlag
**Year:** 2026 (NBER WP, March)
**Venue:** NBER Working Paper No. 34964
**PDF:** [papers/pdfs/akcigit-et-al_2025_attention-money-universities.pdf](../../papers/pdfs/akcigit-et-al_2025_attention-money-universities.pdf)
**Source:** https://www.nber.org/papers/w34964

## 1. Full citation

Akcigit, Ufuk; Chikis, Craig A.; Dinlersoz, Emin; and Goldschlag, Nathan (2026). "Attention (And Money) Is All You Need: Why Universities Are Struggling to Keep AI Talent." NBER Working Paper No. 34964, National Bureau of Economic Research, Cambridge MA, March. JEL: I23, J45, L33, O31.

## 2. Research question

Who are AI researchers, how large is the wage gap between academia and industry, and how does the type of knowledge they produce change when they move from universities to large tech firms? The paper documents a structural reorganization of the supply side of frontier AI innovation in the United States.

## 3. Method

- **Data:** a novel dataset linking publication records from Microsoft Academic Graph (MAG) with administrative microdata from the U.S. Census Bureau (LEHD, Longitudinal Employer-Household Dynamics). The study follows 42,000 AI researchers over two decades (2001–2021) (p. 1, p. 4).
- **Identification:** combines (i) descriptive statistics on demographic composition, earnings, and transition rates; and (ii) a stacked difference-in-differences event study (Cengiz et al., 2019) comparing researchers who move from academia to industry against researchers who move within academia, controlling for person-cohort and field-cohort-age-time fixed effects (p. 14).
- **Key assumptions:** academic movers serve as a valid counterfactual (both groups reveal a willingness to change affiliation, which differences out common selection effects); classification as an "AI researcher" is based on the modal publication field in MAG (p. 5).
- **Acknowledged limitations:** LEHD does not capture 1099-MISC/NEC consulting income (understates moonlighting); top industrial compensation is understated because LEHD excludes unexercised stock options and capital gains (p. 11).

## 4. Key findings

- **Talent concentration in industry:** in 2019, 68% of AI researchers worked in industry, up from 48% in 2001 (p. 1). Industry's share of AI patents rose from 86% to 95%, and its share of papers from 27% to 32% (p. 6).
- **Fivefold wage gap at the top:** earnings of the top 1% in industry rose from US$595,000 in 2001 to US$1.94 million in 2021 (in 2015 dollars), while the academic top 1% barely moved from US$301,000 to US$392,000 (p. 2, p. 10). Average real academic salaries for AI researchers fell 22% between 2001 and 2021 (p. 11).
- **Acceleration after technological milestones:** migration accelerated after AlexNet (2012) and the "Attention Is All You Need" paper (2017). Annual transitions from academia to industry rose from 1.4% to 3.4% (a 55% increase) during the 2010s (p. 12). After 2017, transitions of junior researchers to incumbent firms (>1,000 employees, >20 years old) increased 46% (p. 12).
- **Shift in output type:** researchers who move to industry reduce their probability of publishing papers by 30 percentage points and produce 65% fewer papers per year, while their patent output increases 530% (6 p.p. more likely to patent) (p. 2, p. 16). The relative earnings premium is 63% compared to those who move within academia (p. 16).
- **Demographic composition:** the female share in academia rose from 16% to 29%, compared to only 19% to 23% in industry (p. 8). The proportion of U.S.-born researchers fell 5.5 p.p., offset almost entirely by increases from China (+3.8 p.p.) and India (+2.0 p.p.) (p. 1, p. 8).
- **Growing moonlighting:** the share of AI academics with a second job rose 16% (from 9.9% to 11.5%), and the fraction of their total income from secondary employment in industry rose from 6.3% (2001–2016) to 7.6% (2017–2021) (p. 16).

## 5. Policy implications

For universities in non-frontier economies, the findings are relevant even if the absolute dollar amounts do not apply: it is the gradient of the wage gap — not its level — that reorganizes the innovation ecosystem. Three takeaways for policymakers:

1. **Retaining AI faculty:** if in the U.S. the academic top 1% earns ~US$392K and the industrial top 1% ~US$1.9M (p. 10), the gap in many developing economies — where a full professor earns a fraction of that while global firms recruit remotely at multiples of local salaries — is structurally similar or worse. University talent policy cannot assume academic salaries will be competitive; it needs parallel instruments: paid sabbaticals in industry, joint appointments, flexible IP rights, and explicit tolerance for regulated moonlighting.
2. **Compute access as a substitute for salary:** the paper emphasizes that firms' advantage is not only money but infrastructure — massive datasets, GPUs, clusters (p. 3). A public policy on shared compute (along the lines of the U.S. National AI Research Resource) could be more effective at retaining researchers than pure salary increases, given fiscal constraints in many countries.
3. **Two-way brain drain:** in many emerging markets, AI talent flows to both global industry and universities in high-income countries. The authors show that in the U.S. foreign talent (China, India) is substituting for domestic talent in industry (p. 8); non-frontier economies can occupy similar niches if they invest in doctoral pipelines and offer competitive return conditions.
4. **Risk to open science:** if researchers who migrate publish 64% less and patent 530% more (p. 16), the frontier of AI becomes less legible to regulators and universities in emerging markets. This reinforces the role of public universities in independent evaluation, benchmarking, and auditing — functions the paper explicitly highlights (p. 17).

## 6. Debates and caveats

- **Market concentration:** the finding of Akcigit et al. (most talent flowing to incumbents with >1,000 employees, not to startups, p. 2) reinforces the thesis of Korinek and Vipra on AI concentration — see `korinek-vipra_2025_concentrating-intelligence`. The novelty here is showing that concentration operates through the scientific labor market, not only through capital or data.
- **Spillovers and growth:** Aghion and Bunel project that AI may add 0.8–1.3 p.p./year to TFP growth (see `aghion-bunel_2024_ai-and-growth`); Acemoglu estimates ~0.66% over 10 years (see `acemoglu_2024_simple-macro-ai`). Akcigit et al. do not take sides in that debate, but their evidence that migration reduces publications and increases patents suggests that open-knowledge spillovers weaken — which tempers optimistic forecasts: output may grow but diffusion is constrained.
- **Innovation policy:** the evidence complements but also tensions the view of Cockburn-Henderson-Stern (see `cockburn-henderson-stern_2018_ai-impact-innovation`) on AI as a general-purpose technology that "changes the method of discovery": if the discoverers migrate to proprietary environments, the GPT may materialize but its public character erodes.
- **Measurement caveat:** the authors do not characterize the optimal allocation of scientists between academia and industry (p. 17); they document magnitudes, not normative conclusions. A normative interpretation requires a structural model that does not yet exist.

## 7. Related readings

- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — market concentration in AI: here we see the talent channel.
- [cockburn-henderson-stern_2018_ai-impact-innovation](../ai-models-governance/cockburn-henderson-stern_2018_ai-impact-innovation.md) — AI as a GPT that reorganizes scientific discovery.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — research agenda for transformative AI.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — growth projections that assume knowledge diffusion which this paper shows is weakening.
