# Writing Feedback — YU Guofan (余国帆)

## Feedback on YU Guofan's Previous Writing: Introduction and Literature Review

**Student:** YU Guofan (余国帆)
**Topic:** LLM External Tool Calling Latency Issues: Protocol, Scheduling, and Server-Side Performance Analysis
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your writing:** writing/writingSampleCollection/previousWriting.md
**Your reflection:** writing/writingSampleCollection/previousWriting.md (reflection section)
**Reviewer comments:** writing/writingSampleCollection/comments.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

Your survey paper demonstrates strong technical knowledge of LLM tool-calling latency and a well-organized thematic structure (protocol, server-side, host-side). You have clearly invested considerable effort in identifying and categorizing the literature. However, both Prof. Chen and Prof. Yin flagged critical issues that closely align with what I see: (1) the writing reads as heavily AI-generated, lacking an authentic academic voice; (2) citations are concentrated in the first paragraph of the Introduction, leaving the rest unsupported; (3) the Literature Review sections lean toward surface-level description rather than critical analysis and synthesis. Your self-reflection shows excellent awareness of these issues — now the key is acting on that awareness in your revised draft.

**Estimated current level:** Satisfactory (6–7 range) — The topic coverage is comprehensive and the structure is clear, but the writing needs significant improvement in voice authenticity, citation integration, critical depth, and rhetorical moves to reach Excellent.

---

## Part 1: Introduction Feedback

### What Works Well

- Your opening paragraph effectively establishes the territory by identifying two fundamental limitations of LLMs (static knowledge, limited actionable capabilities) — this is a clear Move 1
- The tool-augmented LLM pipeline (4-step process) is explained clearly and gives readers a concrete mental model
- The three-perspective structure (protocol, server-side, host-side) provides a logical organizational framework
- You clearly identify latency as the critical bottleneck — a genuine and well-targeted research gap

### Issue 1: Citations Disappear After the First Paragraph

Both reviewers flagged this, and it is your most critical structural problem. Your Introduction has citations [1]–[4] in the first paragraph only. The remaining four paragraphs — which contain important claims about latency impact, deployment barriers, and the fragmented state of research — have zero citations.

**Your sentence (no citation):** "the latency introduced by external tool calling has become a major obstacle to their deployment in latency-sensitive applications such as conversational agents, interactive tutoring systems, and real-time decision-making tools."

This is a strong claim. Which papers demonstrate this? Which applications have reported latency as a barrier? Without citations, readers cannot verify the claim and may question whether this is your opinion or established fact.

**Action:** Every paragraph in the Introduction needs citations. Specifically:
- Paragraph 2 (pipeline description): cite the foundational tool-augmented LLM papers that establish this pipeline
- Paragraph 3 (latency as obstacle): cite specific studies that report latency issues in the applications you name
- Paragraph 4 (fragmented research): cite the specific papers/domains you are referring to as "fragmented"

### Issue 2: The Writing Reads as AI-Generated

Both Prof. Chen and Prof. Yin independently identified this issue. Phrases like "has revolutionized AI applications," "enabling human-like text generation, reasoning, and domain-specific problem-solving," and "the cumulative effect can severely degrade user experience" are typical of AI-polished text — they sound smooth but lack specificity and personal analytical voice.

**How to fix this:**
- Replace generic claims with specific, evidence-backed statements. Instead of "LLMs have revolutionized AI applications," write something like "Since the release of GPT-4 in 2023, tool-augmented LLMs have been deployed in production systems including [specific examples with citations]"
- Avoid superlatives and sweeping claims ("revolutionized," "major obstacle," "critical barrier") unless you back them with concrete evidence (performance numbers, deployment statistics, user studies)
- Write your first draft without AI assistance, then revise it yourself. Use AI only for grammar checking at the very end, if at all
- Read your sentences aloud — if they sound like marketing copy rather than a researcher explaining their work to a colleague, rewrite them

Your reflection shows you already understand this: "over-reliance on AI polishing can make the writing sound generic and machine-generated." This is an important insight — now put it into practice.

### Issue 3: Move 2 (Identifying the Niche) Is Underdeveloped

Your gap statement — "these efforts are often fragmented across different domains, lacking a unified framework to understand and mitigate latency holistically" — is the right idea but needs more substance.

**What's missing:**
- Which specific domains are fragmented? Name them with citations
- What have previous surveys covered, and what have they missed?
- Why is a unified framework important — what problems arise from the fragmented approach?

**Compare with a stronger Move 2 pattern:** "While individual studies have addressed protocol overhead [X], server-side execution delay [Y], and host-side scheduling [Z], no existing work provides a comprehensive analysis across all three dimensions. This fragmentation means that optimizing one stage may inadvertently worsen another — for example, aggressive caching on the server side may conflict with host-side batching strategies [citation]. A holistic framework is therefore needed to..."

### Issue 4: Move 3 (Occupying the Niche) Lists Sections Rather Than Stating Contributions

Your Move 3 reads like a table of contents ("Section II investigates...," "Section III focuses on...," "Section IV shifts the focus to..."). This is common in survey papers but is a missed opportunity.

**What a strong Move 3 should do:**
1. State the specific contributions or findings of your survey (not just what each section covers)
2. Explain what makes your analysis unique compared to existing surveys
3. Provide a preview of key insights

**Suggestion:** Instead of "Section II investigates the communication protocols," write something like: "We provide the first systematic comparison of MCP, Function Calling APIs, and RESTful interfaces for LLM tool interaction, revealing that [key finding about which protocol is more latency-efficient and why]."

---

## Part 2: Literature Review Feedback

### What Works Well

- The three-category organization (protocol, server-side, host-side) is logical and comprehensive
- You cover a wide range of recent works (MCP, RAG-MCP, Conveyor, Speculative Actions, etc.)
- The protocol comparison table concept is useful for readers

### Issue 5: Description Without Critical Analysis

This is the most common weakness across all three review sections. You summarize what each paper does but rarely evaluate how well it works, what its limitations are, or how it compares to alternatives.

**Your sentence (description only):** "RAG-MCP [20] addresses latency in the initial stage by dynamically retrieving relevant tools from an external index based on user queries, reducing prompt bloat."

**With critical analysis:** "RAG-MCP [20] addresses latency in the initial stage by dynamically retrieving relevant tools, reducing prompt tokens by over 50% and improving tool selection accuracy from 13.62% to 43.13%. However, the retrieval step itself introduces additional latency, and the approach assumes a well-curated tool index — a requirement that may not hold in rapidly evolving tool ecosystems. Compared to the 'Less-is-More' strategy [21], which achieves similar prompt reduction without a retrieval component, RAG-MCP trades simplicity for flexibility."

Notice how the revised version:
- Includes specific numbers (your paper already has these — use them!)
- Identifies a limitation (retrieval introduces its own latency)
- Compares with an alternative approach (Less-is-More)
- Makes a judgment (trades simplicity for flexibility)

### Issue 6: Section III Lacks Depth (Prof. Chen's Comment)

Prof. Chen noted that "Section III contains too many points and short descriptions; can be elaborated more with more details." This is a common survey writing pattern — trying to cover everything at the expense of depth.

**Action:** Select the 3–4 most important server-side techniques and analyze them in depth rather than listing 8–10 techniques briefly. For each selected technique:
- Explain the core mechanism in detail
- Report quantitative results
- Identify limitations and assumptions
- Compare with alternative approaches

### Issue 7: Missing Synthesis Across Sections

Your three sections (protocol, server-side, host-side) are treated independently, but real systems combine techniques from all three layers. Your survey would be much stronger with a synthesis section that discusses:
- How do protocol choices affect server-side optimization options?
- Can host-side and server-side optimizations conflict with each other?
- What combinations of techniques have been shown to work well together?

This kind of cross-cutting analysis is what separates a literature survey from a literature list.

---

## Part 3: Language and Style Feedback

### Issue 8: Typos and Inconsistencies

Both reviewers noted typographical errors. I found several:
- "optimizw" should be "optimize" (in the server-side section)
- "e-end" should be "end-to-end" (in the host-side section)
- Inconsistent capitalization of technical terms

**Action:** Do a careful manual proofread. Do not rely solely on AI for this — read each sentence carefully yourself.

### Issue 9: Reference Formatting

Prof. Yin noted inconsistent reference formatting and use of arXiv versions where published versions exist.

**Action:**
- Check every arXiv reference to see if a published version exists (conference proceedings or journal)
- Use a consistent citation format throughout (IEEE, ACM, or APA — pick one and stick with it)
- Ensure all references in the bibliography are cited in the text

---

## Part 4: Addressing Your Self-Identified Goals

Your reflection identifies five goals. Here is how to act on each:

1. **"Develop a more authentic academic voice"** — Write your first draft completely by yourself, without AI. Read published papers in your field and note how the authors express complex ideas. Imitate their sentence patterns (not their content).

2. **"Integrate citations more thoroughly"** — Set a rule: every factual claim needs a citation. Go through each paragraph and ask "how do I know this?" If the answer is "a paper told me," cite it. If the answer is "everyone knows this," still cite it.

3. **"Improve critical analysis and synthesis"** — For every paper you review, ask three questions: (a) What problem does it solve? (b) What assumptions does it make? (c) What doesn't it do? Write one sentence for each answer.

4. **"Elaborate with more depth"** — Choose quality over quantity. It is better to analyze 5 papers deeply than to mention 15 papers briefly.

5. **"Maintain consistent reference formatting"** — Use a reference manager (Zotero, Mendeley) to ensure consistency. Check every arXiv paper for a published version.

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Add citations throughout the Introduction (not just paragraph 1) | Addresses both reviewers' primary concern |
| 🔴 High | Rewrite without AI assistance to develop authentic voice | Addresses AI-generation concern |
| 🔴 High | Add critical analysis to Literature Review (limitations, comparisons) | Transforms description into argument |
| 🟡 Medium | Develop Move 2 with specific gap evidence | Strengthens the research motivation |
| 🟡 Medium | Rewrite Move 3 to state contributions, not just section titles | Signals your unique contribution |
| 🟡 Medium | Add cross-section synthesis | Elevates the survey from a list to an analysis |
| 🟢 Lower | Fix typos and reference formatting | Improves polish and credibility |
| 🟢 Lower | Add workflow figures (Prof. Chen's suggestion) | Improves visual clarity |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Write a new Introduction (1000–1500 words total including Literature Review) following the three-move structure
3. For the Literature Review, select your strongest sections and add critical analysis
4. Submit your revised draft by **15 March 2026** via both Moodle forum and Turnitin
5. Please add **tesolchina** as a collaborator on your GitHub repository so I can provide future feedback directly
