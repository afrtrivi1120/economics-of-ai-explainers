# The Impact of Artificial Intelligence on Innovation

**Authors:** Iain M. Cockburn, Rebecca Henderson, Scott Stern
**Year:** 2018
**Venue:** NBER Working Paper No. 24449
**PDF:** [papers/pdfs/cockburn-henderson-stern_2018_ai-impact-innovation.pdf](../../papers/pdfs/cockburn-henderson-stern_2018_ai-impact-innovation.pdf)
**Source:** https://www.nber.org/papers/w24449

## 1. Full citation

Cockburn, Iain M., Rebecca Henderson, and Scott Stern (2018). "The Impact of Artificial Intelligence on Innovation." NBER Working Paper No. 24449, March 2018.

## 2. Research question

Is deep learning merely a new productive technology, or is it more fundamentally an "invention of a method of inventing" (IMI) and simultaneously a general-purpose technology (GPT) that reorganizes the R&D process itself? And what public policies are needed to ensure this shift promotes competition and welfare rather than concentration?

## 3. Method

- **Conceptual framework:** The authors combine two traditions — (i) the "general-purpose technologies" framework of Bresnahan and Trajtenberg (1995) and David (1990), and (ii) the "invention of a method of inventing" concept from Griliches (1957) on hybrid corn (PDF p. 6). They construct a 2×2 matrix (GPT × IMI) that places industrial robotics, autonomous vehicles, static algorithmic tools (e.g. fMRI), and deep learning in distinct quadrants, with deep learning as the only case that is both "GPT + IMI" (PDF p. 14).
- **Bibliometric data:** They assemble two original datasets — (a) 95,840 AI publications classified in Web of Science (1955–2015) by keywords across three fields: symbolic systems (12.5%), learning (61.4%), and robotics (21.6%) (PDF p. 17); and (b) 13,615 unique AI patents from the USPTO (1990–2014), distributed more evenly: 28% learning, 29% symbolic, 40% robotics (PDF p. 18).
- **Empirical strategy:** Descriptive analysis of time trends and geographic/sectoral composition. The authors look for evidence of a shift toward applied research in the learning subfield from 2009 onward.
- **Key assumptions:** Keywords reasonably capture actual AI activity; the tripartite division (symbolic / robotics / learning) reflects distinct technological trajectories, not just labels.

## 4. Key findings

- **Deep learning is the only technology in the "GPT + IMI" quadrant** of the proposed taxonomy — industrial robots are neither IMI nor GPT, autonomous vehicles are GPT but not IMI, and static algorithmic tools like fMRI are IMI but not GPT (PDF p. 14).
- **There is a clear empirical shift toward applied learning-based research from 2009 onward.** Applied learning publications *more than doubled in seven years* and now account for "just under 50% of all AI publications" (PDF p. 21). By the end of 2015, "nearly 2/3 of all publications in AI were in fields beyond computer science" (PDF p. 21).
- **The takeoff is global, not American.** The "striking upward swing in AI application papers that begins in 2009 turns out to be overwhelmingly driven by publications ex US," with the United States in "catch up" mode toward the end of the sample (PDF p. 21). Before 2000 the U.S. had a comparable share; then it "falls significantly behind, only catching up again around 2013" (PDF p. 20).
- **Academia–industry asymmetry:** 85.5% of publications come from academic institutions, but only 7% of patents; 91% of patents are held by private entities (PDF pp. 17, 19). This suggests a division of labor in which academia produces open knowledge and firms capture the applied value.
- **Applications expand into substantive fields:** between the 2004–2006 and 2013–2015 cohorts, there are large relative increases in learning-related publications in medicine, radiology, and economics (PDF p. 21).
- **Concentration risk from data:** algorithms are largely public, but "the data pools that are essential to generate predictions may be public or private" (PDF p. 15). Firms with early data access can erect entry barriers "independent of traditional economies of scale or demand-side network effects" (PDF p. 15).

## 5. Policy implications

- **Data access as industrial policy.** The paper argues that "policies which encourage transparency and sharing of core datasets across both public and private actors may be critical tools for stimulating research productivity and innovation-oriented competition" (PDF p. 2 / abstract). This implies that opening administrative microdata — properly anonymized — is a competition policy, not merely a transparency measure. Without access to representative public data, domestic actors (universities, startups) in non-frontier economies are structurally locked out relative to global incumbents.
- **Catch-up mode as opportunity.** The fact that the post-2009 takeoff was led by countries other than the United States (PDF p. 21) suggests that the window for building national capacity in applied deep learning has not closed. Non-frontier economies can replicate the Canadian strategy (mentioned on p. 20) of investing counter-cyclically in neural networks when the field was not yet fashionable.
- **Applied focus, not foundational.** Since the algorithmic frontier is public but costly to push, it makes more sense for emerging markets to specialize in applications — precision agriculture, medical diagnostics, hydrology, environmental monitoring — where locally generated datasets are difficult for outsiders to replicate.
- **Intellectual property and "consumer data":** the authors explicitly raise the question "Should the data about e.g. my shopping and travel behavior belong to me or to the search engine or ride sharing company that I use?" (PDF p. 25). This connects directly to broader policy debates over data ownership and digital sovereignty.
- **Risk of data "balkanization"** within each applied sector (PDF p. 15) that reduces spillovers — a reason for policymakers to design public-private data consortia before competitive dynamics close them off.

## 6. Debates and caveats

- **Exploratory essay, not causal estimation.** The authors themselves caution that "the purpose of this exploratory essay has not been to provide a systematic account or prediction" (PDF p. 27). There are no identified regressions; the figures are descriptive.
- **Macro optimism vs. Acemoglu's skepticism.** Cockburn, Henderson, and Stern speculate that the diffusion of deep learning as an IMI will generate "economic growth that can eclipse any near-term impact of AI on jobs, organizations, and productivity" (PDF p. 14). This optimism is notably higher than Acemoglu's conservative estimate (~0.66% cumulative TFP gain over 10 years) in `acemoglu_2024_simple-macro-ai`, and aligns more closely with `aghion-bunel_2024_ai-and-growth` and with the "next GPT" thesis in `trajtenberg_2018_ai-next-gpt`.
- **No magnitudes are claimed.** The paper does not quantify the elasticity of R&D productivity to deep learning adoption, nor the diffusion timeline. Later work such as `agrawal-gans-goldfarb_2025_bicycles-for-the-mind` and `gans_2025_genius-on-demand` revisit the question with more firm-level data.
- **USPTO data biased toward the United States.** Only U.S. patents are used, which understates Chinese and Indian activity in applied deep learning (especially post-2015).
- **IMI classification by keyword.** The tripartite keyword classification is admittedly imperfect — the authors acknowledge that "key elements of research activity in artificial intelligence may not be observable using these traditional innovation metrics" (PDF p. 3).

## 7. Related readings

- [trajtenberg_2018_ai-next-gpt](../ai-models-governance/trajtenberg_2018_ai-next-gpt.md) — The companion thesis: AI as the next GPT, with emphasis on complementary policies.
- [agrawal-gans-goldfarb_2025_bicycles-for-the-mind](../firms-market-structure/agrawal-gans-goldfarb_2025_bicycles-for-the-mind.md) — Extends the line of argument: generative AI as a general-purpose cognitive tool for firms.
- [agrawal-gans-goldfarb_2025_research-agenda-tai](../firms-market-structure/agrawal-gans-goldfarb_2025_research-agenda-tai.md) — Research agenda for transformative AI that extends the GPT/IMI framework.
- [aghion-bunel_2024_ai-and-growth](../labor-productivity/aghion-bunel_2024_ai-and-growth.md) — Quantifies the growth effect that this paper only conjectures.
- [korinek-vipra_2025_concentrating-intelligence](../ai-models-governance/korinek-vipra_2025_concentrating-intelligence.md) — Deepens the concentration risk from data control that this paper anticipates.
