# Feedback on Kang Li's First Draft: Introduction and Literature Review

**Student:** Kang Li  
**Topic:** Cognitive Science-Grounded Serendipity Modeling in Recommender Systems  
**Date:** 22 February 2026  
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** [`writing/writingSampleCollection/firstDraft.md`](../../writing/writingSampleCollection/firstDraft.md)  
**Your reflection:** [`writing/writingSampleCollection/reflection.md`](../../writing/writingSampleCollection/reflection.md)  
**Assessment rubric:** [`writing/assessment/writing_instructions_formatted.md`](../../writing/assessment/writing_instructions_formatted.md)

**Model papers analysed for this feedback:**
- **Model Paper 1** (your own RecSys 2025): [Full paper HTML](../../literature/LK*/paper1_3705328_3748167.html) | [Macro-level structural analysis](../../literature/LK*/KangPaper1_Insights.md) | [ACM link](https://dl.acm.org/doi/10.1145/3705328.3748167)
- **Model Paper 2** (Cai et al. SIGIR 2025): [Full paper HTML](../../literature/LK*/paper2_3726302_3729893.html) | [Macro-level structural analysis](../../literature/LK*/KangPaper2_Insights.md) | [ACM link](https://dl.acm.org/doi/10.1145/3726302.3729893)
- **Binst et al. (2025)** — "What Is Serendipity?": [arXiv full text](https://arxiv.org/html/2505.15440v1) | [arXiv abstract](https://arxiv.org/abs/2505.15440)

---

## Overall Assessment

Your draft demonstrates solid technical knowledge of serendipity in recommender systems and a clear sense of your research direction. You already have the core ingredients for a strong paper — a genuine research gap (misalignment between algorithmic metrics and subjective user experience) and a promising solution (cognitive science perspective). However, the current draft reads more like a technical summary than a well-structured academic argument. The key areas for improvement are: (1) building the Introduction into a full three-move argument with citations, (2) deepening the Literature Review with critical analysis rather than description, and (3) strengthening the connection between cognitive science and your proposed approach throughout.

**Estimated current level:** Satisfactory (6–7 range) — The gap identification is sound and writing is generally clear, but the draft needs significant structural and content development to reach Excellent.

---

## Part 1: Introduction Feedback

### What Works Well

- Your opening sentence effectively establishes the importance of serendipity-oriented recommender systems
- The gap identification (discrepancy between algorithmic optimization and actual user experience) is genuine and well-targeted
- The research direction (cognitive science perspective) is clearly stated

### Issue 1: Missing Title

Your draft has no title. A strong title signals your specific contribution and helps readers immediately understand your focus.

**Suggestion:** Consider something like:
- *"Modeling Serendipity Perception in Recommender Systems: A Cognitive Science Approach"*
- *"Beyond Objective Metrics: A Cognitive Science Framework for Serendipity in Recommender Systems"*

### Issue 2: No In-Text Citations or References

The entire draft contains zero citations. This is a critical gap — academic writing requires evidence-based claims. Every factual assertion needs support.

**Your sentence:** *"Serendipity-oriented recommender systems play a pivotal role in enhancing user satisfaction and engagement..."*

**What your own RecSys 2025 paper does** (see [KangPaper1_Insights.md](../../literature/LK*/KangPaper1_Insights.md), Move 1 section):

> "Serendipity plays a pivotal role in enhancing user satisfaction within recommender systems by mitigating the effects of the information cocoon and filter bubble issues from traditional recommendation methods."

This claim is supported by multiple citations in the [full paper](../../literature/LK*/paper1_3705328_3748167.html). Notice how even in the opening sentence, the published version connects serendipity to specific problems (information cocoon, filter bubble) — making the claim verifiable.

**What Binst et al. ([2025](https://arxiv.org/html/2505.15440v1)) does in their Introduction:**

> "Serendipity has been associated with numerous benefits in the context of recommender systems, e.g., increased user satisfaction (Pastukhov et al., 2022), stimulation of long-tail item consumption (Sá et al., 2022), support for users in achieving self-actualization (Graus et al., 2018; Sullivan et al., 2019; Knijnenburg et al., 2016), and mitigation of the overspecialization problem (Stitini et al., 2022)."

Notice how they attach a specific citation to each claimed benefit. This is the standard you should aim for.

**Action:** Add citations throughout. Key references you should consider:
- [Kotkov et al. (2016)](https://doi.org/10.1016/j.knosys.2016.08.014) — foundational survey on serendipity in RS
- Kotkov et al. (2024) — overview of serendipity definitions and operationalizations
- Ziarani & Ravanmehr (2021) — comprehensive survey of serendipity approaches
- De Gemmis et al. (2015) — beyond-accuracy metrics
- [Binst et al. (2025)](https://arxiv.org/abs/2505.15440) — conceptualizing experienced serendipity (fortuitous + refreshing + enriching)
- Your own [Kang et al. (2025) RecSys paper](https://dl.acm.org/doi/10.1145/3705328.3748167) — LLM-based serendipity evaluation

### Issue 3: Introduction Is a Single Paragraph — Needs Three CARS Moves

Your Introduction compresses everything into one paragraph (~130 words). The assignment requires three distinct moves, each deserving its own paragraph(s). The current structure jumps too quickly from territory to gap to solution.

**Move 1 — Establishing Territory (currently underdeveloped):**

Your opening assumes readers already understand serendipity in recommender systems. Many readers — even in CS — may not know why serendipity matters or how it differs from novelty/diversity. You need to:
- Define what serendipity means in the context of recommender systems
- Explain *why* it matters (user satisfaction, filter bubble mitigation, self-actualization)
- Summarize the current state of research with citations

**How [Binst et al. (2025)](https://arxiv.org/html/2505.15440v1) does Move 1:** They spend three paragraphs establishing territory — first explaining that content is increasingly recommended (not searched for), then introducing beyond-accuracy metrics, and finally defining serendipity with its associated benefits. Here is how they gradually narrow the focus:

> "Much of the content users encounter online is not actively searched for but recommended. Popular platforms like YouTube, Spotify, and Instagram all present users with automatically suggested content."

> "RecSys can also support users in exploring the item space, introducing them to new and unexpected content. In these cases, beyond-accuracy metrics become essential, serendipity in particular (De Gemmis et al., 2015; Ge et al., 2010; McNee et al., 2006)."

> "Serendipity, in the context of RecSys, captures the idea of desirable exploration within the item space (De Gemmis et al., 2015)."

This gradual narrowing guides readers who may not be specialists.

**How your own RecSys 2025 paper does Move 1** (see [KangPaper1_Insights.md](../../literature/LK*/KangPaper1_Insights.md), "Move 1: Establishing Territory"):

> The paper uses evaluative language ("pivotal role," "significant challenges," "inherently subjective") and establishes practical significance through filter bubbles and user satisfaction. This works because a RecSys conference audience already has context — but for this assignment's broader academic audience, you need more setup.

**Suggestion for Move 1 (2–3 paragraphs, ~200 words):**
- Paragraph 1: Why recommender systems matter; the problem of filter bubbles and homogeneous recommendations
- Paragraph 2: Serendipity as a solution — define the concept, cite its benefits, show growing research interest
- Paragraph 3: Current approaches to modeling serendipity (objective metrics, LLM-based) — this bridges to Move 2

**Move 2 — Establishing a Niche (partially present but underdeveloped):**

You mention that approaches "frequently fail to align with users' subjective perceptions." This is your gap, but it needs more development:
- *What specifically* fails to align? Give examples of where metrics disagree with users
- *Why* does this misalignment happen? (Because serendipity is inherently a cognitive/emotional experience that cannot be captured by item-level features alone)
- *What have others tried?* Acknowledge attempts to address this gap (user studies, qualitative approaches like Binst et al.'s grounded theory work)

**How [Binst et al. (2025)](https://arxiv.org/html/2505.15440v1) establishes their niche:**

> "Despite its potential advantages, the concept of serendipity remains conceptually ambiguous in the context of RecSys (Ziarani and Ravanmehr, 2021; Kotkov et al., 2024). This conceptual ambiguity led researchers to adopt diverse approaches to operationalize the concept, resulting in inconsistent metrics of serendipity, which complicate the synthesis of findings across studies."

> "While several have tried to address this research gap... none have focused their attention on understanding users' subjective experiences of serendipity with RecSys."

This is exactly the "conceptualization-operationalization gap" that your work also addresses. Reference this.

**How your RecSys paper does Move 2** (see [KangPaper1_Insights.md](../../literature/LK*/KangPaper1_Insights.md), "Move 2: Establishing Niche"):

> "The gold standard for user-centered evaluation involves carefully designed user studies that directly capture user feedback, which, however, are costly in practice. As a result, many researchers rely on predefined proxy metrics... Nonetheless, the gap between these indirect measurements and actual user perceptions introduces bias into serendipity research."

The gap is framed as a cost-accuracy tradeoff — specific and actionable. Your draft should similarly frame the gap in concrete terms rather than just saying approaches "fail to align."

**Move 3 — Occupying the Niche (present but needs expansion):**

Your final sentence states the research direction but is too brief. Move 3 should:
- Clearly state your research question or purpose
- Briefly outline your approach (cognitive science framework — which specific theories?)
- Preview what you achieve or find (even preliminary results)
- Indicate the structure of the paper

**How Cai et al. ([SIGIR 2025](../../literature/LK*/KangPaper2_Insights.md)) does Move 3:**

> "To this end, we introduce the **A**gentic **F**eedback **L**oop (AFL) modeling. AFL simultaneously constructs both a recommendation agent and a user agent, using textual communication to simulate the feedback loop."

They introduce their framework acronym, state specific quantitative contributions ("average improvement of 11.52%"), and enumerate numbered contributions — giving readers a concrete preview. See the full analysis in [KangPaper2_Insights.md](../../literature/LK*/KangPaper2_Insights.md), "Move 3: Occupying Niche" section.

**How your RecSys paper does Move 3** (from [KangPaper1_Insights.md](../../literature/LK*/KangPaper1_Insights.md)):

> "The emergence of large language models (LLMs) has revolutionized evaluation methodologies across human annotation tasks, showcasing remarkable potential in user simulation and automatic assessment. This breakthrough motivates our key research question: **Can LLMs effectively simulate human users for serendipity evaluation?**"

Notice the bold formatting for emphasis and the clear research question. Your draft should similarly state a crisp research question.

### Issue 4: Cognitive Science Perspective Not Explained

You mention "a cognitive science perspective" without explaining what this means. Readers need to understand:
- Which cognitive theories or frameworks inform your approach?
- How does cognitive science explain serendipity perception differently from current RS approaches?
- What specific cognitive processes are involved? (e.g., surprise detection, relevance evaluation, value assessment)

**Relevant research to draw on:**

- **Curiosity-driven models:** A recent paper ([arXiv:2504.06633](https://arxiv.org/abs/2504.06633), 2025) models user curiosity — epistemic curiosity (desire for knowledge) vs. perceptual curiosity (stimulated by sensory ambiguity) — as a driver of serendipity preference, connecting psychological constructs to computational models.

- **Binst et al.'s three-component framework** ([arXiv:2505.15440](https://arxiv.org/abs/2505.15440)): They define experienced serendipity as requiring three components — **fortuitous**, **refreshing**, and **enriching**. These implicitly map to cognitive processes:
  - *Fortuitous* relates to expectation violation
  - *Refreshing* relates to novelty detection
  - *Enriching* relates to value appraisal

  > "We conceptualize experienced serendipity as 'a user experience in which a user unintentionally encounters content that feels fortuitous, refreshing, and enriching'. We find that all three components — fortuitous, refreshing and enriching — are necessary and together are sufficient to classify a user's experience as serendipitous."

- **The RecSys vs. User serendipity distinction:** Kotkov et al. ([2024](https://doi.org/10.1016/j.knosys.2016.08.014)) distinguishes "RecSys serendipity" (system-side metric) from "user serendipity" (actual human perception) — this is fundamentally a cognitive science question.

---

## Part 2: Literature Review Feedback

### What Works Well

- Clear two-category organization (objective metrics vs. LLM-based)
- Specific author names mentioned (Zhang et al., Li et al., Kotkov et al., Fu et al.)
- The summary paragraph identifies genuine limitations
- Writing is generally clear and grammatically sound

### Issue 5: Limited Connection Between Introduction and Literature Review

The Introduction ends with "this study adopts a cognitive science perspective" but the LR never discusses cognitive science perspectives on serendipity. The LR only reviews computational approaches. This creates a disconnect.

**Suggestion:** Add a third category or thread in your LR that reviews cognitive/psychological perspectives on serendipity:
- How serendipity has been studied in cognitive science and information science — Makri & Blandford (2012) proposed a process model of serendipity through grounded theory
- The role of curiosity, surprise, and value in serendipitous experiences — see [arXiv:2504.06633](https://arxiv.org/abs/2504.06633)
- Attempts to bridge cognitive theories with computational models

### Issue 6: LR Move 1 (Thematic Overview) — Missing Context and Definitions

Your LR jumps straight into "quantifying a serendipity score" without first:
- Defining serendipity for the reader (the concept is contested — [Kotkov et al. (2016)](https://doi.org/10.1016/j.knosys.2016.08.014) identified at least 6 different definitions)
- Explaining why quantification is the dominant paradigm
- Setting up the scope of your review

**How [Binst et al. (2025)](https://arxiv.org/html/2505.15440v1) handles this:** Their Related Work section begins with a subsection "Conceptualizing Serendipity" that traces the evolution of the concept:

> "In 2012, Makri and Blandford described a process model of serendipity, where an individual makes a new connection due to a mix of unexpected circumstances triggering a moment of insight, which is subsequently exploited, leading to a valuable unanticipated outcome."

> "Smets (2022) contributes to the conceptualization of serendipity by positing it is a value that can be designed for. She distinguishes between three levels of serendipity: Intended serendipity (why design for it?), Afforded serendipity (how to stimulate it?), and Experienced serendipity (what characterizes the experience?)."

This gives readers a conceptual map before diving into specific approaches. Your LR should similarly start by mapping the conceptual landscape.

### Issue 7: LR Move 2 (Critical Analysis) — Descriptive Rather Than Critical

Your review of the first category (objective metrics) is largely descriptive: "Zhang et al. do X, Li et al. do Y, Kotkov et al. do Z." The [rubric](../../writing/assessment/writing_instructions_formatted.md) requires you to *critique* methodologies and findings, *show connections* between studies, and *synthesize* rather than list.

**Your current text:** *"Zhang et al. measure unexpectedness via category and content differences between candidates and user history, while Li et al. calculate it as the weighted distance between a candidate item and the clusters of user interests."*

**What this should become (with critical analysis):**
- *What assumption do both share?* Both treat unexpectedness as a measurable distance in item feature space — but this assumes items can be objectively compared, ignoring that the same item may be expected by one user and completely surprising to another depending on their background knowledge and cognitive state.
- *What's the limitation of this assumption?* These distance-based metrics cannot capture the subjective, context-dependent nature of surprise — what cognitive science calls "expectation violation" depends on the individual's mental model, not just their click history.
- *How do they relate to each other?* Show progression, contradiction, or complementarity between studies.

**A model for critical synthesis from your own RecSys 2025 paper** (see [KangPaper1_Insights.md](../../literature/LK*/KangPaper1_Insights.md), RQ2 section):

> "Notably, incorporating curiosity significantly improved performance, achieving a Pearson correlation coefficient of 17.83%. This is intuitive, as curiosity influences user perceptions of serendipity: more curious users are more inclined to explore items with lower relevance but higher unexpectedness."

This excerpt from your own paper shows exactly the kind of cognitive insight your LR should incorporate — connecting *user psychology* (curiosity) to *system behaviour* (metric performance).

### Issue 8: Second Category (LLM-Based) — Too Brief

The LLM-based category paragraph is only 3 sentences. Given that your own published work ([Kang et al., RecSys 2025](../../literature/LK*/paper1_3705328_3748167.html)) is a major contribution to this category, you have deep knowledge to draw on. This section should discuss:
- The promise of LLMs (semantic understanding, simulation of user perspectives)
- Specific approaches (Fu et al.'s "unexpected but relevant" definition, your own SerenEva framework)
- Limitations: LLMs as black boxes, the correlation ceiling with human judgments, domain-specific variations

From your own paper's findings (see [KangPaper1_Insights.md](../../literature/LK*/KangPaper1_Insights.md), RQ1 section):

> "In zero-shot settings, LLMs such as Qwen2.5-14B and GPT-4 surpass conventional metrics across both datasets by approximately 100% in Pearson correlation compared to the best proxy metric (SOG)."

This is powerful evidence that LLMs outperform traditional metrics — but the correlation with human judgment is still modest, leaving room for your cognitive science approach.

- The conceptual question: Are LLMs truly modeling user cognition, or just pattern-matching on training data?

### Issue 9: Missing Citations Throughout the LR

Like the Introduction, the LR mentions authors by name but lacks proper citation formatting. "Zhang et al." and "Li et al." need full citations with years and reference list entries. The current draft has no reference list at all.

### Issue 10: LR Move 3 (Research Gaps) — Present But Needs Sharpening

Your "significant limitations persist" paragraph identifies gaps but could be more precise:

**Your text:** *"Objective metric-based approaches rely on heuristic definitions that frequently fail to align with the complex, subjective nature of user perception."*

**Sharper version** (drawing on Binst et al.'s terminology): Something like — "While objective metric-based approaches provide computationally tractable solutions, they fundamentally operationalize serendipity as an *item property* (e.g., unexpectedness score) rather than as a *user experience*. This conflation means that a system might recommend items with high 'serendipity scores' that users perceive as merely random or irrelevant. [Binst et al. (2025)](https://arxiv.org/abs/2505.15440) identify this as the 'conceptualization-operationalization gap.' The core issue is that serendipity arises from a cognitive process — the interplay between expectation violation, curiosity arousal, and value recognition — that cannot be reduced to item-level features."

### Issue 11: LR Move 4 (Conclusion) — Needs Stronger Bridge to Your Study

Your concluding paragraph mentions "cognitive science-grounded approach" but doesn't explain what this entails. The LR conclusion should:
- Summarize the key insight from your review (both approaches treat serendipity computationally rather than cognitively)
- State how your study specifically addresses this (which cognitive models? what methodology?)
- Create anticipation for the methodology section

---

## Part 2B: Novelty Analysis — How Well Does Your Draft Communicate Novelty?

*(See also: [novelty.md](../../writing/novelty.md) — a course-wide reference on types of novelty and strategies for communicating them.)*

### Your Novelty Claim

Your draft's novelty is a **perspective novelty** — applying cognitive science to serendipity modeling in recommender systems. This is a legitimate and potentially powerful form of novelty (see [novelty.md, Type 3](../../writing/novelty.md)). However, the current draft does not communicate this novelty effectively.

### What the Draft Does Well

- You identify a genuine gap: existing approaches "frequently fail to align with users' subjective perceptions"
- You name a specific perspective (cognitive science) as your contribution
- The gap-to-solution structure is present in embryonic form

### What Needs Improvement

**Problem 1: The novelty claim is asserted, not demonstrated.**

You state that you will adopt "a cognitive science perspective" but never explain *what cognitive science reveals about serendipity that computational approaches miss*. Compare how other papers demonstrate their novelty:

- **Your RecSys 2025 paper** ([analysis](../../literature/LK*/KangPaper1_Insights.md)) demonstrates novelty through a concrete research question: "Can LLMs effectively simulate human users for serendipity evaluation?" — and names the framework (SerenEva). Your draft should similarly name your cognitive science framework and state what it enables.

- **Cai et al.** ([analysis](../../literature/LK*/KangPaper2_Insights.md)) demonstrates novelty by identifying exactly what existing work *overlooks*: "overlooking the critical role of the feedback loop between the user and the recommender." Your draft says existing approaches "fail to align" but doesn't explain *why* they fail — the cognitive mechanism explanation is missing.

- **Binst et al.** ([arXiv:2505.15440](https://arxiv.org/abs/2505.15440)) demonstrates novelty by using a different *method* (grounded theory) to study a familiar *topic* (serendipity), producing a new conceptualization (fortuitous + refreshing + enriching). Your draft should similarly state what new understanding cognitive science produces.

**Problem 2: No contribution enumeration.**

Every strong model paper enumerates its contributions. Your draft has none. You should add 2-3 specific contribution statements. For example:
1. We propose a cognitive framework that models serendipity perception as a three-stage process: expectation violation → curiosity arousal → value recognition
2. We demonstrate that incorporating cognitive features (e.g., curiosity) improves alignment with human serendipity judgments by X%
3. We provide a systematic comparison between cognitive-grounded and metric-based serendipity evaluation

**Problem 3: No name for the contribution.**

Successful papers name their contributions: SerenEva, AFL, CHASE-SQL, FedSum, COLDQ. Consider naming your framework — this forces you to define what it *is* precisely enough to deserve a name.

**Problem 4: No quantitative or qualitative evidence preview.**

Other papers preview their results in the Introduction:
- "average improvement of 11.52%" (Cai et al.)
- "Pearson correlation coefficient of over 20%" (Kang et al.)
- "73.01% execution accuracy" (CHASE-SQL)

Even if your results are preliminary, previewing them signals confidence and gives readers a reason to continue reading.

### How Other Model Papers Signal Novelty (Strategies You Should Adopt)

| Strategy | Example from Model Papers | How to Apply |
|----------|--------------------------|-------------|
| Gap-to-solution narrative | "The gap between indirect measurements and actual user perceptions introduces bias" → SerenEva (Kang et al.) | State the cognitive gap explicitly → name your cognitive framework |
| Research question | "Can LLMs effectively simulate human users?" (Kang et al.) | "Can cognitive science models predict users' subjective serendipity experiences more accurately than computational metrics?" |
| Contrastive positioning | "Existing research primarily focuses on optimizing either the recommendation agent or the user agent separately" (Cai et al.) | "Existing approaches treat serendipity as an item property; we model it as a cognitive process" |
| Contribution enumeration | Numbered contributions in Introduction (all model papers) | Add 2-3 bullet-point contributions after Move 3 |
| Naming the contribution | SerenEva, AFL, CHASE-SQL | Name your cognitive science framework |

### Recommended Revision for Novelty

In your Introduction Move 3, after stating the research direction, add something like:

> "Specifically, we draw on [cognitive theory X] to model serendipity perception as a multi-stage cognitive process involving [stage 1], [stage 2], and [stage 3]. We implement this in [framework name], which [does what specifically]. Our results show that [preview of key finding]."

This single paragraph would transform your novelty claim from *asserted* to *demonstrated*.

---

## Part 3: Addressing Your Self-Identified Challenges

Based on your [reflection](../../writing/writingSampleCollection/reflection.md), here are targeted suggestions for the challenges you identified:

### Challenge: "Logical flow and coherence"

**Strategy:** Use the "known → new" principle. Each sentence should begin with information already established and end with new information. Each paragraph should begin with a topic sentence that connects to the previous paragraph.

**Example:** Your LR currently jumps from defining objective metrics (paragraph 1) to LLM methods (paragraph 2) without a transition. Add a bridging sentence: *"While these metric-based approaches provide systematic frameworks for quantifying serendipity, they require pre-defined formulations that may not capture the full complexity of the concept. An alternative paradigm has emerged with the rise of large language models..."*

### Challenge: "Compelling research narrative"

**Strategy:** Think of your Intro+LR as telling a story with a central tension: *"Everyone agrees serendipity matters, but nobody can measure it properly because they're treating a cognitive experience as an engineering metric."* Every paragraph should advance this narrative.

### Challenge: "Balancing precision with brevity"

**Strategy:** For each study you cite, ask: "Does mentioning this specific detail advance my argument?" If it only adds technical detail without supporting your point, cut it. For example, the specific formula details (category differences, weighted distances) are less important than the underlying assumption they share (treating serendipity as item-level distance).

---

## Part 4: Concrete Next Steps (Priority Order)

1. **Add a title** that signals your cognitive science contribution
2. **Expand Move 1** of the Introduction: define serendipity, establish its importance with citations, introduce the evaluation challenge
3. **Develop Move 2**: articulate the conceptualization-operationalization gap with evidence
4. **Strengthen Move 3**: state your research question, preview your cognitive science framework, announce your contribution
5. **Restructure the LR** with three threads: (a) objective metric approaches, (b) LLM-based approaches, (c) cognitive/psychological perspectives on serendipity
6. **Transform descriptions into critical analysis**: for each approach, discuss not just *what* they do but *what assumptions they make* and *why those assumptions are problematic*
7. **Add all citations and build a reference list** — aim for 15–25 references for this length
8. **Write connecting transitions** between all major sections
9. **Ensure the cognitive science thread** runs throughout — this is your unique contribution and should be visible in every section

---

## Part 5: Key Resources to Incorporate

| Reference | Repo / Link | Why It Matters for Your Draft |
|-----------|------------|-------------------------------|
| Kang et al. (2025) — RecSys | [Paper HTML](../../literature/LK*/paper1_3705328_3748167.html) \| [Analysis](../../literature/LK*/KangPaper1_Insights.md) \| [ACM](https://dl.acm.org/doi/10.1145/3705328.3748167) | Your own work; LLM evaluation framework, SerenEva, curiosity as auxiliary data |
| Cai et al. (2025) — SIGIR | [Paper HTML](../../literature/LK*/paper2_3726302_3729893.html) \| [Analysis](../../literature/LK*/KangPaper2_Insights.md) \| [ACM](https://dl.acm.org/doi/10.1145/3726302.3729893) | Agentic feedback loops; model for Move 3 structure and contribution framing |
| Binst et al. (2025) — UMAP | [arXiv full text](https://arxiv.org/html/2505.15440v1) \| [arXiv abstract](https://arxiv.org/abs/2505.15440) | Defines experienced serendipity as fortuitous + refreshing + enriching; grounded theory approach; identifies conceptualization-operationalization gap |
| Curiosity-driven serendipity RS (2025) | [arXiv](https://arxiv.org/abs/2504.06633) | Models epistemic vs. perceptual curiosity as driver of serendipity preference |
| Kotkov et al. (2016) | [DOI](https://doi.org/10.1016/j.knosys.2016.08.014) | Foundational survey; defines serendipity components and reviews 6+ definitions |
| Makri & Blandford (2012) | [DOI](https://doi.org/10.1002/asi.22169) | Process model of serendipity from information science; grounded theory method |
| Comprehensive RS Survey (2024) | [arXiv](https://arxiv.org/abs/2407.13699) \| [GitHub](https://github.com/VectorInstitute/Recommender-Systems-Survey) | 500+ paper survey emphasizing diversity and serendipity for user experience |
| Ziarani & Ravanmehr (2021) | [DOI](https://doi.org/10.1007/s10462-021-09960-0) | Comprehensive survey of serendipity approaches and definitions |

---

## Part 6: Rubric-Based Assessment Summary

(Rubric details: [writing_instructions_formatted.md](../../writing/assessment/writing_instructions_formatted.md))

| Criterion | Current Level | Key Issue | Target for Final |
|-----------|--------------|-----------|-----------------|
| **Task Achievement** | Unsatisfactory–Satisfactory (5–6) | No citations, incomplete moves, limited critical evaluation | Excellent (9–10): Add citations, complete all moves, deepen critical analysis |
| **Organisation** | Satisfactory (6–7) | Single-paragraph intro, weak transitions, Intro-LR disconnect | Excellent (9–10): Three-move intro, strong transitions, narrative coherence |
| **Language Range** | Satisfactory–Excellent (7–8) | Writing is clear and technically accurate; some sentences could be more precise | Excellent (9–10): Maintain current quality, add hedging and evaluative language |

**Your writing quality is actually strong** — the language is clear, technically precise, and grammatically sound. The main improvements needed are structural (expanding the Introduction, deepening the LR) and scholarly (adding citations, building critical analysis). These are very achievable with revision.

---

*End of Feedback — Kang Li*
