# Exporting the Surveillance State via Trade in AI

**Authors:** Martin Beraja, Andrew Kao, David Y. Yang, Noam Yuchtman
**Year:** 2023
**Venue:** NBER Working Paper No. 31676
**PDF:** [papers/pdfs/yuchtman-et-al_2023_exporting-surveillance-state.pdf](../../papers/pdfs/yuchtman-et-al_2023_exporting-surveillance-state.pdf)
**Source:** https://www.nber.org/papers/w31676

## 1. Full citation

Beraja, Martin; Kao, Andrew; Yang, David Y.; Yuchtman, Noam. *Exporting the Surveillance State via Trade in AI.* NBER Working Paper No. 31676, September 2023.

## 2. Research question

Is China exporting, along with its facial-recognition AI technology, the institutions of the surveillance state? More specifically: who buys that technology, when do they buy it, and what happens to the political institutions of importing countries? The paper challenges the belief that trade integration necessarily diffuses liberal institutions (p. 1, p. 25).

## 3. Method

- **Data:** Construction of a novel database of 1,636 global facial-recognition AI trade deals between 2008 and 2021, drawn from the Carnegie Endowment report (Feldstein, 2019), web-scraping of 15,351 additional sources, NLP validation (Stanza/NER) and human verification, supplemented by the Capital IQ database (2,878 firms) (pp. 5–6). Covers 36 exporting and 136 importing countries.
- **Comparators:** Trade in 9 other frontier technologies (drones, robotics, genomics, etc.) from UN Comtrade (pp. 6–7), Polity IV data (regimes), NELDA (electoral quality), GDELT (protest events — 18.4 million events), World Bank, AidData, China Global Investment Tracker, and SIPRI.
- **Identification:** Linear probability models at the country-country-sector-year dyad level. The key strategy is a triple-difference (China × AI × autocratic regime), netting out trade in other frontier technologies to neutralize unobserved bilateral trade factors (p. 10, eq. 1; p. 14, eq. 2). For the protest-import effect, an event-study with leads/lags and country and year fixed effects is used (p. 17, eq. 3). For institutional erosion, a long-difference regression spanning 2005–07 vs. 2019–21 (p. 20, eq. 4).
- **Key assumptions:** That trade in other frontier technologies captures general bilateral confounders; and that the absence of pre-trends supports a causal interpretation of the protest shock on imports (p. 17).

## 4. Key findings

- **China dominates surveillance AI exports.** Between 2008 and 2021 China recorded 250 facial-recognition export deals (vs. 215 for the US), exporting to 83 countries (vs. 57 for the US) (pp. 6, 10). In "smart cities," China leads with 158 deals (vs. Germany, 124) (p. 6).
- **Comparative advantage specific to AI.** The China×AI interaction coefficient is **+47.4 pp** in the probability of dyadic trade, robust to controls for GDP, distance, language, shared border, and colonial ties (p. 10, Table 2). China shows no such dominance in the remaining frontier technologies (Figure 2, p. 13).
- **Autocratic bias in demand.** 44% of Chinese AI exports go to autocracies and weak democracies, versus only 24% of US exports (pp. 2–3). The triple-difference implies a **+22% increase in the probability** that an autocracy or weak democracy imports Chinese AI relative to other frontier technologies (p. 14, Table 3 Panel A). The bias does not appear in imports from the US (p. 15).
- **Imports spike in years of domestic protest.** In autocracies and weak democracies, a protest shock contemporaneously raises Chinese AI imports (coef. 0.073–0.097, significant at 5%) with no detectable pre-trends (p. 19, Table 4). The pattern is exclusive to AI — it does not appear in any of the other 14 frontier technologies (Figure 5, p. 22) — nor in mature democracies (Figure 4, p. 21).
- **Concomitant institutional erosion.** Importing Chinese AI during years of high unrest is associated with a significant decline in the NELDA electoral-quality index (coef. −0.556 to −0.704, p. 23, Table 5 Panel A). The same pattern does not appear in mature democracies importing the same technology.
- **Regime entrenchment.** Countries that import Chinese AI above the median during high unrest have only a **4.7% (1 in 21) probability** of transitioning to consolidated democracy, compared with **21.7% (5 in 23)** among low importers (p. 25).

## 5. Policy implications (Colombia / Latin America)

Latin America is an active target of Chinese AI deployment: the paper cites the case of Brazil, where Israel exported "Digital Intelligence" to the Federal Police in 2020 (p. 6), but the broader pattern — Huawei in Laos, Uganda, Zambia, Myanmar (pp. 1–2) — reflects a market that is also penetrating Latin American cities through "Safe City" and "Smart City" projects. For Colombia, the findings generate at least four concrete implications:

1. **Institutional due diligence for urban AI infrastructure contracts.** The paper shows that the risk lies not in the technology in the abstract but in the combination of technology × regime × political context: importing Chinese AI during an internal crisis correlates with electoral erosion (p. 23). Colombia should require rights-impact assessments before procuring municipal or police facial-recognition systems, especially in electoral or social-protest contexts.
2. **Transparency in subnational procurement.** Many purchases are made through B2B intermediaries (p. 5, note 10) and municipalities. Without a consolidated national registry of surveillance-AI contracts, the country loses legislative audit capacity.
3. **Regulation of cross-border externalities.** The authors propose modeling surveillance-AI regulation on existing regimes for dual-use goods or goods with global externalities (p. 26). Colombia, as an OECD member, could lead a Latin American regional agenda on AI export/import standards where rights risks are involved.
4. **This is not only a "China vs. US" debate.** The paper documents that when autocracies and weak democracies import AI *from the US* after protests, institutional erosion is also observed (p. 24). The problem is the technology in the hands of buyers with repressive motivations, not the geopolitical origin of the supplier.

## 6. Debates and caveats

- **Imperfect causality.** The authors are explicit: the association between Chinese AI imports in protest years and declining electoral quality is *not* interpreted as a direct causal effect of AI on institutions. It is more likely that both are co-outcomes of a deliberate regime effort to consolidate control (p. 22). This caution contrasts with more alarmist journalistic readings of "China exporting authoritarianism."
- **Small sample in the regime-change result.** The 4.7% vs. 21.7% statistic (p. 25) is based on 21 and 23 countries respectively — suggestive, not conclusive.
- **Supply vs. demand not disentangled.** The authors acknowledge they cannot directly test whether China subsidizes exports to autocracies as foreign policy, nor separate that from US firm self-bans (IBM, Microsoft, Google after 2018) (p. 16). The bias is robust to excluding the post-2018 period.
- **Tension with optimistic AI-and-growth narratives.** While `aghion-bunel_2024_ai-and-growth` and `acemoglu_2024_simple-macro-ai` debate the magnitude of AI productivity gains, this paper shows that global institutional costs may not be internalized by those macro models. A welfare accounting of AI should include externalities on political rights.
- **Complement to `korinek-vipra_2025_concentrating-intelligence`.** Korinek and Vipra focus on the concentration of *economic* power via AI; this paper documents the concentration of *political-coercive* power — two sides of the same governance problem.

## 7. Related readings

- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — Concentration of AI capabilities and power risks; a natural complement on governance.
- [jones_2026_ai-economic-future](../ai-models-governance/jones_2026_ai-economic-future.md) — Macro framework on the economic future of AI, where the political externalities documented here can be situated.
- [acemoglu_2024_simple-macro-ai](../labor-productivity/acemoglu_2024_simple-macro-ai.md) — Discusses "bad" uses of AI (including surveillance) that do not enter conventional TFP estimates.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — Research agenda on transformative AI that needs to incorporate the geopolitical dimension documented here.
