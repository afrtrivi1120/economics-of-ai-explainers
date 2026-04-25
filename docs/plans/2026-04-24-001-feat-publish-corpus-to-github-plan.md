---
title: Publish Economics-of-AI Explainers Corpus to GitHub
type: feat
status: active
date: 2026-04-24
---

# Publish Economics-of-AI Explainers Corpus to GitHub

## Overview

Take the local corpus (24 downloaded PDFs + matching metadata, no explainers yet, single initialization commit) from a working tree to a published, navigable GitHub repository. Three things must happen together:

1. **Write the missing explainers** (24 papers, currently `explainers/*/` is empty across all 5 subareas).
2. **Rebuild `README.md`** so it actually serves as the front page: aim of the repo + a navigable index of papers grouped by author, each link pointing at the explainer (not just the PDF).
3. **Create the GitHub repo** under the `afrtrivi1120` account, commit in coherent batches (one commit per paper bundle, per `CLAUDE.md` and the `github-publisher` agent), and push.

The `paper-explainer` and `github-publisher` subagents already exist and define the contract for steps 1 and 3 — this plan uses them, it does not reinvent them.

## Problem Frame

Today the repo is invisible to anyone outside this machine, and even locally a reader landing on `README.md` cannot reach a single explainer (none exist). Authors in `inputs/economists_map.md` are listed but not cross-linked to the papers we have actually downloaded. The intended audience cannot use it in this state.

This is a publication task, not a re-architecture. The slug convention, metadata schema, sub-area taxonomy, and explainer template are all already fixed in `CLAUDE.md` and `.claude/agents/paper-explainer.md` — the plan must respect them, not relitigate them.

## Requirements Trace

- **R1.** A GitHub repository exists under `afrtrivi1120/<repo-name>` (final name to be confirmed in Open Questions) and contains the full corpus.
- **R2.** `README.md` opens with a clear statement of the repo's aim (Economics-of-AI explainers for a Colombian / Latin American policy audience).
- **R3.** `README.md` contains an author-organized index of every paper currently in `papers/metadata/`, with each entry linking to its explainer (and secondarily to the PDF).
- **R4.** Every paper in `papers/metadata/*.json` has a corresponding `explainers/{subarea}/{slug}.md` that follows the template in `.claude/agents/paper-explainer.md` (bilingual headers, page-cited quantitative claims, debates/caveats section, cross-links).
- **R5.** Commits are grouped per paper (PDF + metadata + explainer in one commit) where possible, per the `github-publisher` contract; the README/index lands as its own commit after all explainers are in.
- **R6.** Push succeeds without `--force`, without `--no-verify`, and without committing files outside the existing scope (no secrets, no `.claude/settings.local.json`, no `*.pdf.tmp`).

## Scope Boundaries

- Not adding new papers to the corpus. The 24 papers in `papers/metadata/` and `papers/pdfs/` are the publication scope.
- Not editing `inputs/economists_map.md` (per `CLAUDE.md` and the `paper-explainer` agent rules).
- Not changing the slug convention, metadata schema, sub-area taxonomy, or explainer template.
- Not setting up CI, GitHub Pages, issue templates, or a Jekyll/MkDocs site. Plain Markdown rendered by GitHub is the deliverable.
- Not migrating to Git LFS. Current PDF footprint is ~20 MB, well under the ~100 MB threshold flagged in `CLAUDE.md`.

### Deferred to Separate Tasks

- **Coverage check script extension**: `scripts/check_coverage.py` is referenced in `CLAUDE.md` but does not exist in `scripts/`. Creating it is out of scope here; track separately.
- **Adding new papers** beyond the 24 currently downloaded.
- **GitHub Pages or static site generation**: deferred until the plain-Markdown corpus is in a steady state.

## Context & Research

### Relevant Code and Patterns

- `CLAUDE.md` — authoritative on slug convention, metadata schema, sub-area folders, content rules, and the no-fabrication rule.
- `.claude/agents/paper-explainer.md` — exact required structure of each explainer (sections 1–7, page citations, length 600–1200 words, cross-link rules).
- `.claude/agents/github-publisher.md` — the commit/push contract (one commit per paper bundle, no force-push, no hook bypass, asks before first push to a new remote).
- `.claude/agents/paper-downloader.md` — not invoked by this plan; PDFs and metadata are already in place.
- `inputs/economists_map.md` — canonical author list with sub-area tags `[L, F, E, I, M]`; used as the source of truth for the README's author index.
- `papers/metadata/*.json` — 24 records, each carries `authors`, `title`, `year`, `venue`, `subareas`, `source_url`, `pdf_path`. Drives both the README index and explainer front-matter.
- `README.md` — current version describes the project but predates any explainers; will be rewritten in Unit 3.

### Institutional Learnings

- The corpus is intentionally bilingual (Spanish-leaning headers, English-acceptable body) — explainers must reflect the policy-audience tone, not generic academic prose.
- The field has genuine quantitative disagreement (Acemoglu's ~0.66% TFP/10yr vs. Aghion's ~0.8–1.3 pp/yr). `CLAUDE.md` and the explainer template both require this divergence to be foregrounded, not papered over. Explainers in `labor-productivity/` and `ai-models-governance/` will most often need this section to do real work.

### External References

- None required for this plan; all conventions are repo-internal.

## Key Technical Decisions

- **Use the `paper-explainer` subagent for each explainer**, one paper at a time. Rationale: the subagent already encodes the template, page-citation discipline, no-fabrication rule, and cross-link checks. Re-implementing that logic inline would duplicate it and risk drift.
- **Group explainer generation in dependency-ordered batches by sub-area**, starting with the papers most heavily cited by others in the corpus (Acemoglu, Aghion, Brynjolfsson-Li-Raymond). Rationale: later explainers' "Lecturas relacionadas" sections cross-link by slug — earlier explainers must already exist for the cross-links to be real.
- **Author index in README is generated from `papers/metadata/*.json`**, not hand-written from `inputs/economists_map.md`. Rationale: the metadata is what we actually have; the economists_map is a wishlist that exceeds the corpus. An author-grouped index built from metadata cannot drift out of sync with the actual files. Group by **first author** (alphabetical by surname); list co-authored papers under the first author and add a "Co-authored with: …" suffix.
- **Repo name**: pending confirmation in Open Questions, but default to `economics-of-ai-explainers` (matches the README phrasing and is more descriptive than the local directory name `ai_papers_explainers`).
- **Visibility**: public. Rationale: the corpus is built from open-access PDFs and is intended as a Colombian / Latin American policy reference. No private/internal data is in the tree. Confirm with user before `gh repo create` since this is a one-way decision in practice.
- **Commit grouping**: one commit per explainer + its (already-tracked) PDF and metadata when possible. Since the PDF and metadata are already in the prior `645adae` initialization commit, in practice each new commit will be `explainers/{subarea}/{slug}.md` alone. Bundle in groups of ~5 explainers per commit only if per-explainer commits become noisy; default to per-paper commits.
- **README rewrite lands as the final commit before push**, after all explainers exist, so every link in the index resolves.

## Open Questions

### Resolved During Planning

- **Are the explainers already written?** No — `explainers/*/` is empty across all 5 subareas. They must be written as part of this plan.
- **Does a remote exist?** No — `git remote -v` is empty. `gh repo create` is required.
- **Is `gh` authenticated?** Yes — `afrtrivi1120` account, scopes include `repo`. No auth work needed.
- **Are PDFs too large to commit directly?** No — 20 MB total. Stays well under the 100 MB threshold in `CLAUDE.md`.
- **Should the README index group by author or by sub-area?** By author, per the user's explicit request ("links to papers by authors"). Sub-area browsing is already served by the `explainers/{subarea}/` folder structure.

### Deferred to Implementation

- **Final repository name** (`economics-of-ai-explainers` vs. `ai-papers-explainers` vs. user's preference) — confirm with user before `gh repo create`.
- **Repository description string** for `gh repo create --description` — draft from README opening sentence, confirm with user.
- **Whether to bundle explainers into multi-paper commits** if 24 commits feels noisy in `git log` — decide during execution; default is per-paper.
- **Exact ordering of explainers within an author's section** in the README (chronological vs. by sub-area) — pick during README writing; chronological is the safer default.

## Implementation Units

- [ ] **Unit 1: Confirm repo name, description, and visibility; create the GitHub repo**

**Goal:** Have an empty (or `--source`-tracked) GitHub repository ready to push to, with the right name, description, and visibility settings. No commits pushed yet.

**Requirements:** R1, R6

**Dependencies:** None.

**Files:**
- No file changes in this unit. This is a `gh` CLI operation plus a `git remote add` (or `gh repo create --source .` which does both).

**Approach:**
- Ask user to confirm: repo name (default `economics-of-ai-explainers`), one-line description, and that public visibility is acceptable.
- Run `gh repo create afrtrivi1120/<name> --public --description "<desc>" --source=. --remote=origin` from the working tree. This creates the remote and wires `origin` in one step without pushing.
- Verify `git remote -v` shows `origin` pointing at the new repo.

**Patterns to follow:**
- `.claude/agents/github-publisher.md` — agent's contract says ask user before first push to a new remote. Same caution applies to `gh repo create`: confirm name and visibility first.

**Test scenarios:**
- Happy path: `gh repo view afrtrivi1120/<name>` returns metadata after creation; `git remote -v` shows `origin` URL matching.
- Error path: name collision with an existing repo on the account (`afrtrivi1120/causal-inference-papers-explainer` exists; the chosen name must not collide). On collision, surface to user and re-confirm.

**Verification:**
- Remote `origin` exists and points at `https://github.com/afrtrivi1120/<repo-name>.git`.
- `gh repo view` shows the repo with the agreed description and visibility.
- No commits pushed yet — the working tree's `645adae` initialization commit is still the only commit, locally.

---

- [ ] **Unit 2: Write all 24 explainers via the `paper-explainer` subagent, in dependency order**

**Goal:** Every paper in `papers/metadata/` has a `explainers/{subarea}/{slug}.md` that follows the template, cites pages for quantitative claims, includes the debates/caveats section, and cross-links to other explainers in the corpus by slug.

**Requirements:** R4

**Dependencies:** None for the first explainer; later explainers depend on earlier ones for the "Lecturas relacionadas" cross-links to be real.

**Files:**
- Create: `explainers/labor-productivity/{slug}.md` for slugs whose first subarea tag is `L`:
  - `acemoglu_2024_simple-macro-ai`, `acemoglu-restrepo_2018_ai-automation-work`, `aghion-bunel_2024_ai-and-growth`, `aghion-jones-jones_2017_ai-economic-growth`, `albanesi-et-al_2025_new-tech-jobs-europe`, `autor_2022_labor-market-impacts-tech`, `autor_2024_rebuild-middle-class`, `brynjolfsson-li-raymond_2025_genai-at-work`, `deming-bick-blandin_2024_rapid-adoption-genai`, `frey-osborne_2024_genai-reappraisal`, `johnson_2024_ricardo-thompson-ai`, `restrepo_2024_automation-rent-dissipation`, `trajtenberg_2018_ai-next-gpt`.
- Create: `explainers/firms-market-structure/{slug}.md` for slugs whose first subarea tag is `F`:
  - `agrawal-gans-goldfarb_2025_bicycles-for-the-mind`, `akcigit-et-al_2025_attention-money-universities`, `bloom-et-al_2026_firm-data-on-ai`, `cockburn-henderson-stern_2018_ai-impact-innovation`, `gans_2025_genius-on-demand`.
- Create: `explainers/ai-models-governance/{slug}.md` for slugs whose first subarea tag is `M`:
  - `agrawal-gans-goldfarb_2025_research-agenda-tai`, `jones_2026_ai-economic-future`, `korinek_2025_ai-agents-econ-research`, `korinek-vipra_2025_concentrating-intelligence`, `yuchtman-et-al_2023_exporting-surveillance-state`.
- Create: `explainers/inequality-welfare/{slug}.md` for slugs whose first subarea tag is `I`:
  - `stantcheva-et-al_2024_open-ended-survey`.
- Create: `explainers/education/{slug}.md` — none in current metadata; folder stays empty for now.
- Test: not applicable (no executable code; quality is asserted by reviewer pass over each explainer against the template — see Test scenarios below).

*Note on routing*: subarea is the **first** tag in `metadata.subareas`, per the `paper-explainer` agent rule. The 24 routings above were derived by reading every metadata JSON; verify at execution time and reroute if any metadata has been corrected.

**Approach:**
- **Wave 1 — anchor papers** (write first; later cross-links point at them): `acemoglu_2024_simple-macro-ai`, `aghion-bunel_2024_ai-and-growth`, `aghion-jones-jones_2017_ai-economic-growth`, `brynjolfsson-li-raymond_2025_genai-at-work`, `acemoglu-restrepo_2018_ai-automation-work`, `autor_2024_rebuild-middle-class`, `korinek-vipra_2025_concentrating-intelligence`. These are the most-cited-by-others-in-the-corpus pieces; doing them first means later explainers can include real cross-links rather than placeholder ones.
- **Wave 2 — remaining `[L]` and `[F]` papers**: everything else in `labor-productivity/` and `firms-market-structure/`.
- **Wave 3 — remaining `[M]` and `[I]` papers**: `ai-models-governance/` and `inequality-welfare/`.
- For each paper, invoke the `paper-explainer` subagent with the slug. The agent reads the PDF + metadata and writes the file. Do not hand-author explainers in this plan — defer to the agent so the no-fabrication and page-citation rules are enforced consistently.
- After each wave, do a quick scan: every explainer file exists, every "Lecturas relacionadas" link points at a slug whose explainer file is now on disk.

**Patterns to follow:**
- `.claude/agents/paper-explainer.md` — exact section structure, page-citation rule, length 600–1200 words, no fabricated numbers, debates/caveats required not optional.
- The "Note on conflicts and caveats" paragraph at the end of `inputs/economists_map.md` is the canonical framing of the divergence in the field; explainers can echo its tone.

**Test scenarios:**
- Happy path: pick 3 random explainers from each wave; verify (a) all 7 sections present, (b) every quantitative claim has a `(p. N)` citation, (c) "Debates y caveats" actually names another paper or framework rather than restating the abstract, (d) "Lecturas relacionadas" links resolve to real files.
- Edge case: a paper with no other paper in the corpus to disagree with (e.g., `stantcheva-et-al_2024_open-ended-survey` is the only `[I]`-first paper). Its "Debates y caveats" should reach across subareas (e.g., to Brynjolfsson on measurement) rather than be empty.
- Error path: PDF text extraction fails or pages are unreadable — `paper-explainer` should drop the unverifiable claim, not fabricate. Spot-check by reading the explainer and confirming numerical claims trace to an actual page in the PDF.

**Verification:**
- `find explainers -name '*.md' | wc -l` returns at least 24.
- Every slug in `papers/metadata/` has a matching explainer file under the expected subarea folder.
- A 5-explainer spot-check (one per wave, plus the one orphan in `inequality-welfare/`) reads as a clear, page-cited, ~600–1200-word piece for a Colombian / Latin American policy audience.

---

- [ ] **Unit 3: Rewrite `README.md` as a navigable front page with author-grouped paper index**

**Goal:** A reader landing on the GitHub repo's main page understands the aim immediately and can reach any explainer in one click via an author-organized index.

**Requirements:** R2, R3

**Dependencies:** Unit 2. The README links to explainer files; those files must exist before the README is committed, or the index will ship with broken links.

**Files:**
- Modify: `README.md`

**Approach:**
- Keep the existing aim paragraph and sub-area table (they already work).
- Replace the bottom half ("How it works", "Usage", "Current corpus") with two new sections:
  1. **"Papers by author / Papers por autor"** — author-grouped index, alphabetical by first author's surname. Under each author: bulleted list of `[Title](explainers/{subarea}/{slug}.md) — Year, Venue ([PDF](papers/pdfs/{slug}.pdf))`. For multi-author papers, list under the first author and append `(con {co-authors})` / `(with {co-authors})`.
  2. **"How it works / Cómo funciona"** — keep a slimmed version of the current agents/usage description, but move it below the index (it's reference, not what most readers come for).
- Generate the author index from `papers/metadata/*.json` (read the files, group by `authors[0]`, sort, render). This is a manual generation step in this plan — no script — but the reader of this plan can do it deterministically by inspecting the metadata folder.
- Add a "Last updated" footer with the date and corpus size (e.g., "Corpus: 24 papers, ~20 MB of open-access PDFs, last updated 2026-04-24").

**Patterns to follow:**
- Current `README.md` heading style and bilingual phrasing ("Sub-areas", "Source list").
- The way `inputs/economists_map.md` formats author entries (name, affiliation, sub-area tag) — the README index can be lighter (no affiliations) but should keep sub-area tags so a reader knows which subfolder an explainer lives in.

**Test scenarios:**
- Happy path: render the README in a Markdown previewer; every explainer link resolves to a file on disk; every PDF link resolves to a file on disk.
- Edge case: an author with multiple papers in the corpus (e.g., Acemoglu has at least two: `acemoglu_2024_simple-macro-ai` and `acemoglu-restrepo_2018_ai-automation-work`) appears once with both papers nested underneath, not twice.
- Edge case: a paper with multiple first-author candidates (e.g., `agrawal-gans-goldfarb_2025_*`) — pick the first author from `authors[0]` in metadata and stay consistent across the index.
- Integration: after `git add README.md && git commit`, `gh repo view --web` (post-push) shows the README rendered correctly with working internal links.

**Verification:**
- Every paper in `papers/metadata/*.json` appears exactly once in the author index.
- Every link in the index is a relative path that resolves on disk.
- Aim paragraph is in the first 5 lines of the file.

---

- [ ] **Unit 4: Commit the new explainers and the rewritten README via the `github-publisher` subagent**

**Goal:** All new files (24 explainers + revised README) are committed in coherent, reviewable batches, with no force-push, no hook bypass, and no out-of-scope files staged.

**Requirements:** R5, R6

**Dependencies:** Units 2 and 3 (files must exist).

**Files:**
- Stage: `explainers/labor-productivity/*.md`, `explainers/firms-market-structure/*.md`, `explainers/ai-models-governance/*.md`, `explainers/inequality-welfare/*.md`, `README.md`.
- Do not stage: `.claude/settings.local.json`, `.DS_Store`, anything matching `*.pdf.tmp` or `*.partial`.

**Approach:**
- Invoke the `github-publisher` subagent. Per its description, it groups one commit per paper (PDF + metadata + explainer). Since the PDF + metadata are already in `645adae`, in practice each commit will be a single explainer file. That is acceptable; alternatively, the agent may bundle 4–6 explainers per commit if it judges per-paper commits too noisy for a 24-paper batch.
- The README rewrite ships as its own final commit (`docs: add author-organized paper index and refresh front page`) after all explainers are committed, so the index never references a file that does not yet exist on `main`.
- Do not amend or rewrite `645adae`. New work is new commits.

**Patterns to follow:**
- `.claude/agents/github-publisher.md` — never force-push, never bypass hooks, never commit secrets, ask before first push to a new remote.
- Current commit message style from `git log`: imperative, capitalized (e.g., "Initialize Economics-of-AI paper explainers repository"). Match it.

**Test scenarios:**
- Happy path: `git status` is clean after the agent finishes; `git log --oneline` shows ~24 explainer commits + 1 README commit on top of `645adae`.
- Edge case: `git status -uall` (avoided per Bash tool guidance — use `git status` only) before staging shows no surprise files (e.g., a stray `.DS_Store` slipping in). The `github-publisher` agent must add files explicitly by path, not via `git add -A`.
- Error path: a pre-commit hook fails. Per `github-publisher` rules and the global `Bash` instructions, do NOT use `--no-verify`; fix the underlying issue and re-stage as a new commit.

**Verification:**
- `git status` is clean.
- `git log --oneline` shows commits attributed to the user (`Andres Rivera`), not to a bot identity.
- No file under `.claude/settings.local.json`, no `.env`, no `*.pdf.tmp` is in the staged tree.

---

- [ ] **Unit 5: Push to `origin/main`, verify the rendered repo, and hand off**

**Goal:** The corpus is live on GitHub at the chosen URL, the README renders correctly with working internal links, and the user has the URL.

**Requirements:** R1, R6

**Dependencies:** Units 1 and 4.

**Files:**
- No file changes.

**Approach:**
- Per the `github-publisher` agent's rule: ask the user before the first push to a new remote. Confirm the user is ready, then `git push -u origin main`.
- After push, run `gh repo view --web afrtrivi1120/<name>` (or report the URL to the user without auto-opening if they prefer headless). Spot-check that:
  - The README renders with the author index visible.
  - At least 3 explainer links from different subareas resolve when clicked through GitHub's web UI.
  - The PDFs are accessible and download cleanly through the GitHub web UI.

**Patterns to follow:**
- `.claude/agents/github-publisher.md` — confirm before first push; never `--force`.

**Test scenarios:**
- Happy path: `git push -u origin main` succeeds, `gh repo view` shows the README rendered, internal links work, PDFs downloadable.
- Edge case: push is rejected because the remote was created with an initial README/branch from `gh repo create`. Resolve by `git pull --rebase origin main` (NOT a force-push) and re-push, or by recreating the remote with `--source=. --push=false` and no initial files. The `gh repo create --source=.` form used in Unit 1 should avoid this; if it does not, fall back to plain `gh repo create` followed by `git remote add` + `git push`.
- Error path: push fails for auth reasons (token expired). Re-run `gh auth status`, refresh, retry. Do not force-push, do not skip hooks.

**Verification:**
- `git push` exit code 0, `git log` shows `origin/main` matches local `main`.
- The repo URL renders in a browser with a navigable index.
- The user has been given the public URL.

## System-Wide Impact

- **Interaction graph:** This plan touches three existing subagents (`paper-explainer`, `github-publisher`, and `paper-downloader` indirectly via the metadata it produced). It changes none of them. It does not touch the separate Bayesian decision pipeline that lives in a different repo, per `CLAUDE.md`'s governance boundary.
- **Error propagation:** A bad explainer (fabricated number, broken cross-link) propagates into the README index because the index links to it. Mitigation: write all explainers and validate cross-links before the README rewrite, then validate every README link before committing the README.
- **State lifecycle risks:** Explainer files added in waves; if execution is interrupted between waves, partially-written explainers must not be committed. Mitigation: commit only complete explainers; treat the working tree between waves as in-progress local state.
- **API surface parity:** The metadata schema and slug convention in `CLAUDE.md` are the public "API" of this corpus. Nothing in this plan changes them.
- **Integration coverage:** GitHub's Markdown renderer interprets relative paths slightly differently from local Markdown previewers. Spot-checking via `gh repo view --web` after push (Unit 5) is the integration test that matters.
- **Unchanged invariants:** `inputs/economists_map.md` is read-only here. `papers/pdfs/*.pdf` and `papers/metadata/*.json` are not modified — only consumed. The slug convention and explainer template are unchanged.

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Explainer agent fabricates a number not in the PDF | Spot-check at least 3 explainers per wave by opening the PDF to the cited page; the agent's prompt already enforces no-fabrication, this is a verification step, not a redesign. |
| Cross-links in "Lecturas relacionadas" point at slugs whose explainer doesn't exist yet | Strict wave ordering (anchor papers first); after each wave, scan that wave's "Lecturas relacionadas" links and confirm targets exist on disk. |
| README index drifts out of sync with the metadata folder over time | Generate the index from `papers/metadata/*.json` and mention in the README that it is regenerated when papers are added. (Automating that regeneration is a deferred follow-up, not in scope.) |
| GitHub repo name collision on the `afrtrivi1120` account | Confirm the chosen name with `gh repo view` before `gh repo create`; user already has `causal-inference-papers-explainer`, so name discipline matters. |
| Push rejected because `gh repo create` initialized the remote with content | Use `gh repo create --source=. --push=false` form; if that still creates conflicting remote content, `git pull --rebase` and re-push (no force). |
| Pre-commit hook fails partway through Unit 4 | Fix the underlying issue and create a new commit; never use `--no-verify`. Per global `Bash` instructions, this is non-negotiable. |
| `.DS_Store` or `.claude/settings.local.json` accidentally staged | Stage explicitly by path, never `git add -A`. `.gitignore` already excludes `settings.local.json` and `.DS_Store`; double-check `git status` before each commit. |

## Documentation / Operational Notes

- After push, the GitHub repo URL becomes the canonical link to share with policy colleagues. Consider adding it to the user's notes / `CLAUDE.md` follow-up so future sessions know where the corpus lives.
- No CI, no GitHub Actions, no Pages site in this plan. Plain Markdown rendered by GitHub is the deliverable.
- The 20 MB PDF footprint leaves ample room (~80 MB) before the `CLAUDE.md` LFS-revisit threshold; nothing to do operationally here.

## Sources & References

- Project conventions: `CLAUDE.md` (slug, schema, sub-areas, content rules, governance boundary)
- Subagents: `.claude/agents/paper-explainer.md`, `.claude/agents/github-publisher.md`, `.claude/agents/paper-downloader.md`
- Source list: `inputs/economists_map.md` (author taxonomy and divergence framing)
- Metadata: `papers/metadata/*.json` (24 records — drives both explainer routing and README index)
- Current front page: `README.md` (to be revised in Unit 3)
- Single existing commit: `645adae Initialize Economics-of-AI paper explainers repository`
