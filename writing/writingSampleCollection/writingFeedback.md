# Writing Feedback — GOU Jiajie (苟嘉杰)

## Feedback on GOU Jiajie's Writing Samples: Introduction and Related Work

**Student:** GOU Jiajie (苟嘉杰)
**Topic:** IDDR-NGP — Efficient 3D Distractor Removal Using Implicit Neural Representations and 2D Detectors
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your samples:** writing/writingSampleCollection/IDDR-NGP.md (full paper), IDDR-NGP-reviews.md, IDDR-NGP-author-reflection.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

You are in a unique position in the class: you have submitted a complete, published (or near-published) paper with real peer review feedback and a detailed author reflection. This gives me an unusually rich view of both your writing strengths and weaknesses. Your writing demonstrates strong technical competence — the paper is well-structured, the experimental design is comprehensive, and you clearly understand the domain deeply. Your author reflection is exceptionally thoughtful, covering challenges from "clarifying the boundary between problem and contribution" to "balancing technical detail with readability." However, based on the reviewer feedback and the Introduction/Related Work sections, several areas need attention: (1) the Introduction could more clearly separate the problem definition from the contribution; (2) the Related Work is organized well but tends toward listing rather than critical analysis; and (3) some claims need stronger evidence or more careful qualification.

**Estimated current level:** Good to Excellent (8–9 range) — The technical depth, experimental rigor, and self-awareness are impressive. The writing improvements needed are refinements rather than structural overhauls.

---

## Part 1: Introduction Feedback

### What Works Well

- **Strong opening motivation:** You connect 3D distractor removal to real applications (robotics, autonomous driving)
- **Clear problem definition:** The distinction between 2D inpainting and 3D-aware distractor removal is effectively established
- **The contribution list is explicit:** You enumerate specific contributions (multi-resolution hash encoding, LPIPS+MVCL losses, dataset with annotations)
- **Good use of figures:** The teaser figure immediately communicates what your method does

### Issue 1: Problem-Contribution Boundary Needs Sharpening

Your author reflection identifies this as a key challenge: "The hardest part was explaining exactly what problem we address and what we do." The Introduction moves from general 3D applications → 2D vs 3D removal → existing limitations → your approach, but the transition from "what's the problem" to "what we do about it" could be sharper.

**Suggestion:** Add a clear transitional sentence before the contribution list: "To address the challenges of automated multi-type distractor detection and efficient 3D scene restoration, we propose IDDR-NGP, the first framework that combines implicit neural representations with off-the-shelf 2D detectors for unified distractor removal in 3D scenes. Specifically, our contributions include: ..."

### Issue 2: Qualify Claims More Carefully

Your Introduction states: "Training NeRF with contaminated images is an unexplored area, our work is the first that employs NeRF to restore both synthetic and realistic scenes with random distractors."

While this may be accurate, "first" claims are risky — reviewers often challenge them. Consider softening to: "To the best of our knowledge, this is the first work that employs NeRF to restore 3D scenes with multiple types of randomly distributed distractors."

### Issue 3: Connect to Broader Impact

The Introduction focuses on technical contributions but could briefly mention the broader impact. Why does removing distractors from 3D scenes matter beyond technical novelty? For example: "Accurate distractor removal enables cleaner 3D reconstructions for downstream applications such as autonomous navigation, augmented reality content creation, and cultural heritage digitization."

---

## Part 2: Related Work Feedback

### What Works Well

- **Good organizational structure:** NeRF → Fast NeRF → Object Detection → 3D Distractor Removal follows a logical progression
- **Effective niche identification:** The statement "training NeRF with contaminated images is an unexplored area" clearly positions your contribution
- **Appropriate breadth:** You cover the relevant subfields without excessive detail

### Issue 4: Related Work Tends Toward Listing

The Object Detection subsection is particularly list-like: "One-stage detectors, e.g., YOLOX, FCOS, DETR... Two-stage detectors, e.g., VFNet, CenterNet2... Anchor-based detectors, e.g., Scaled-YOLOv4..."

This reads as a catalog rather than a critical analysis. Why do you mention these specific detectors? How do they relate to your choice of YOLOv5 and FCOS?

**Stronger version:** "Our framework requires detectors that can identify diverse distractor types across varying scales and occlusion levels. We evaluate two representative approaches: YOLOv5 [citation], an anchor-based one-stage detector known for strong speed-accuracy tradeoffs in multi-class detection, and FCOS [citation], an anchor-free detector that avoids the hyperparameter sensitivity of anchor-based methods. This comparison reveals how detector design choices affect downstream 3D restoration quality (Section 4)."

### Issue 5: Add Critical Transitions Between Subsections

Your Related Work subsections are somewhat independent. Adding transition sentences that connect them would strengthen the narrative:

**Between NeRF and Fast NeRF:** "While NeRF achieves high-quality novel view synthesis, its slow training and rendering limit practical application to distractor removal, where iterative refinement is needed."

**Between Fast NeRF and Detection:** "Efficient NeRF variants like Instant-NGP make iterative 3D reconstruction feasible, but they assume clean training images. Identifying and masking contaminated regions requires integration with 2D detection methods."

### Issue 6: Address Reviewer Concerns About Positioning

Your reviewer feedback (which I have read) raises concerns about clarity of positioning relative to existing desnow/inpainting methods. In your revision, ensure the Related Work explicitly contrasts your approach with these methods:

**Suggestion:** Add a paragraph: "Our work differs from 2D inpainting methods [cite] in that we operate on multi-view 3D representations, leveraging cross-view consistency to fill regions that single-view methods must hallucinate. Unlike desnow-specific methods [cite], we handle multiple distractor types (snow, petals, confetti, etc.) within a unified framework."

---

## Part 3: Author Reflection Feedback

### What Works Well

Your author reflection is one of the most thoughtful I have read. Key strengths:

- **Precise problem awareness:** "If this is not stated clearly, the work can easily be misread as 'yet another desnow/derain method'" — this shows excellent understanding of how readers interpret papers
- **Structural awareness:** Your approach to limitations ("turning limitations into extendable research questions") is mature and publishable
- **Process transparency:** Describing your experiment-writing interplay ("experiments and writing progressed in parallel") shows a realistic understanding of the research process

### Issue 7: Apply Your Reflection Insights Systematically

You have identified most of your writing challenges yourself. The next step is to systematically address each one in your revision:
1. **Problem-contribution boundary:** Ensure the Introduction has a single, clear sentence that defines the problem before listing contributions
2. **Technical detail balance:** For each method subsection, ask "does a reader from a neighboring field need this detail?"
3. **Related Work scope:** Keep it focused on the threads directly relevant to your contribution

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🟡 Medium | Sharpen problem-contribution boundary in Introduction | Prevents misreading of scope |
| 🟡 Medium | Replace listing with critical analysis in Related Work (especially detection subsection) | Elevates from catalog to argument |
| 🟡 Medium | Add transition sentences between Related Work subsections | Creates narrative flow |
| 🟡 Medium | Qualify "first" claims more carefully | Prevents reviewer pushback |
| 🟢 Lower | Add broader impact statement | Motivates research beyond technical novelty |
| 🟢 Lower | Address reviewer positioning concerns explicitly | Strengthens revision |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. For the course assignment: Write a revised Introduction and Literature Review (1000–1500 words) addressing the issues above
3. **Important:** The course assignment requires writing a new Introduction and Literature Review following the rhetorical moves framework — not just revising the existing paper. Use the feedback above to guide your new draft.
4. Submit by **15 March 2026** via Moodle forum and Turnitin
