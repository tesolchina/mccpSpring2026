# Writing Feedback — QIN Weiyi (秦偉一)

## Feedback on QIN Weiyi's First Draft: Introduction and Literature Review

**Student:** QIN Weiyi (秦偉一)
**Topic:** Online Convex Optimization with Time-Varying Constraints (Double-Q Algorithm)
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** literature/WYQ*/firstDraft_template.md
**Your reflection:** literature/WYQ*/reflection_template.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

**Note:** Your writing samples are located in `literature/WYQ*/` rather than the expected `writing/writingSampleCollection/` folder. Please also copy them to the correct location for the final submission.

**Model papers analyzed:** COCO_Insights.md, COLDQ_Insights.md (your own analyses)

---

## Overall Assessment

This is one of the strongest drafts in the class. Your Introduction and Literature Review demonstrate the hallmarks of mature academic writing: (1) a clear and complete move structure with explicit labels; (2) dense, accurate citations throughout — nearly every claim is supported by references; (3) precise mathematical notation where needed; and (4) a well-constructed argument that progresses from general OCO territory to specific research gaps. The fact that you have also prepared detailed model paper analyses (COCO_Insights.md, COLDQ_Insights.md) shows deep engagement with the literature. The main areas for improvement are relatively minor: (1) some passages are very notation-heavy, which may reduce accessibility for readers from neighboring fields; (2) the transition between Move 2 and Move 3 could be smoother; and (3) a few claims about practical networking applications are mentioned but not developed.

**Estimated current level:** Excellent (9–10 range) — The structure, citation density, analytical depth, and mathematical rigor are all strong. This draft is close to publication quality for the Introduction/Literature Review sections.

---

## Part 1: Introduction Feedback

### What Works Well

- **Move 1 is well-structured and comprehensive.** You establish OCO as "a vital framework for sequential decision-making under uncertainty" and immediately ground it with foundational references (Shalev-Shwartz, Hazan, Orabona). The progression from standard OCO to constrained OCO (COCO) is logical and well-motivated.
- **The practical motivation is compelling.** "Many practical networking applications only require constraints to be satisfied cumulatively over time" — this bridges the gap between theory and practice effectively.
- **Citation density is exemplary.** Your Introduction alone contains 30+ citations, each precisely placed. This is the standard for a top-tier venue submission.
- **The two-metric framework is clearly explained.** The distinction between "soft violation" (allowing compensated violations) and "hard violation" (prohibiting any compensated violation) is a key conceptual contribution of the literature, and you explain it clearly.
- **Move labels are explicit.** You mark Move 1, Move 2, Move 3, and Move 4 — this is exactly the structural awareness the course teaches.

### Issue 1: Notation Density May Reduce Accessibility

Your Introduction introduces substantial mathematical notation: $\mathcal{O}(\sqrt{T})$, $\mathcal{O}(\log{T})$, $\mathcal{O}(T^{1-v})$, $\mathcal{O}(T^v)$, etc. While this precision is appropriate for an optimization theory audience, consider adding one plain-language sentence after each key result to help readers from related fields:

**Your sentence:** "The seminal OCO work achieved $\mathcal{O}(\sqrt{T})$ regret for a sequence of $T$ arbitrary convex loss functions."

**More accessible version:** "The seminal OCO work achieved $\mathcal{O}(\sqrt{T})$ regret for a sequence of $T$ arbitrary convex loss functions — meaning the average per-round performance gap shrinks to zero as the time horizon grows, at a rate inversely proportional to $\sqrt{T}$."

This is optional but would broaden your readership.

### Issue 2: Practical Applications Could Be Developed

You mention "many practical networking applications" and cite several papers, but don't develop what these applications are. One concrete example would strengthen the motivation:

**Suggestion:** "For instance, in wireless resource allocation [citation], the channel allocation constraint need not hold at every time slot; it suffices to ensure total allocated capacity remains within the budget over the scheduling horizon. Similarly, in online ad auction systems [citation], budget constraints are inherently cumulative."

### Issue 3: Move 3 Transition Could Be Smoother

The transition from Move 2's detailed analysis of existing bounds to Move 3 ("Another line of work bridges the two COCO worlds") is slightly abrupt. Consider adding a transitional sentence that explicitly frames the gap:

**Suggestion:** "The sharp contrast between the two COCO worlds — $\mathcal{O}(1)$ violation for fixed constraints versus $\mathcal{O}(T^{3/4})$ for arbitrary time-varying constraints — raises a natural question: can we design algorithms that achieve the best of both worlds, adapting to the actual level of constraint variation?"

---

## Part 2: Literature Review Feedback

### What Works Well

- **The literature review is embedded in the Introduction** (common in theory papers) and executed well. You trace the development from early COCO works through fixed constraints, time-varying constraints, and unified analysis.
- **Critical analysis is present.** You don't just cite papers — you compare their bounds: "improving to $\mathcal{O}(\max\{T^{1/2}, T^v\})$ soft violation under Slater's condition" — this shows exactly how the field has progressed.
- **Move 4 is strong and specific.** The conclusion explicitly positions your Double-Q algorithm: "bridges the best-known hard violations in the two COCO worlds, outperforming state-of-the-art algorithms." The reference to Table 1 for comparison is a good practice.

### Issue 4: Consider Adding a Comparison Table Description

You reference "Table~\ref{tab:1}" but the table itself is not in the submitted draft. For the course assignment, consider including the table or describing its contents textually so readers can see the comparison without the table.

### Issue 5: The "Two Worlds" Framing Could Be Made More Vivid

Your key insight — that fixed-constraint COCO and time-varying COCO have been studied as separate problems — is the central gap. Consider making this framing more vivid at the start of Move 2:

**Suggestion:** "The COCO literature has bifurcated into two largely independent worlds. In the first world — fixed constraints — algorithms achieve remarkably tight $\mathcal{O}(1)$ hard violation bounds. In the second world — time-varying constraints — even the best algorithms suffer $\mathcal{O}(T^{3/4})$ violation. This bifurcation is not just a gap in the literature; it reflects a fundamental algorithmic challenge: how to design a single algorithm that adapts its constraint satisfaction strategy to the actual level of constraint variation, without knowing this variation in advance."

---

## Part 3: Reflection and Process Feedback

### What Works Well

Your reflection demonstrates sophisticated metacognitive awareness:

- **"I follow a problem–limitation–opportunity structure"** — this maps directly to the Move 1 → Move 2 → Move 3 pattern, showing you have internalized the rhetorical structure
- **"AI is helpful for language polishing but requires careful checking for technical accuracy"** — critical insight for mathematics-heavy writing where AI often makes notation errors
- **Clear specific goals:** "gap identification, synthesis of related work, and high-level academic expression" — these are exactly the right areas

### Issue 6: Your Draft Already Shows Strong Gap Identification

Your reflection mentions gap identification as a goal to develop, but your draft already demonstrates strong gap identification (the "two COCO worlds" framing). This suggests your self-assessment may be overly modest. Your real growth area may be more about narrative flow — making the dense mathematical argument read as a compelling story rather than a sequence of results.

---

## Part 4: Model Paper Analyses

You have prepared detailed analyses of two model papers (COCO_Insights.md, COLDQ_Insights.md). This level of preparation is exceptional and shows deep engagement with the literature. These analyses will serve you well when writing the full paper.

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🟡 Medium | Add plain-language interpretations after key mathematical results | Broadens accessibility |
| 🟡 Medium | Develop one concrete practical application example | Strengthens real-world motivation |
| 🟡 Medium | Smooth the Move 2 → Move 3 transition | Improves narrative flow |
| 🟡 Medium | Copy files to `writing/writingSampleCollection/` for final submission | Meets submission requirements |
| 🟢 Lower | Include or describe Table 1 content textually | Makes comparison self-contained |
| 🟢 Lower | Make "two worlds" framing more vivid at the start of Move 2 | Enhances storytelling |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Consider adding accessibility touches (plain-language interpretations, concrete examples)
3. Smooth transitions between moves
4. Copy your draft to `writing/writingSampleCollection/` folder
5. Submit by **15 March 2026** via Moodle forum and Turnitin
