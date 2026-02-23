# Slide Plan: LLMs for Serendipity Evaluation

**Total Slides:** 9
**Design Style:** Simple, Easy to Understand, Pastel Palette (per `feedback.md`)

---

## Slide 1: Title Slide
*   **Type:** Title
*   **Content:**
    *   **Title:** Evaluating the Unexpected
    *   **Subtitle:** Exploring the Potential of LLMs for Serendipity Evaluation in Recommender Systems
    *   **Presenter:** [Your Name]
    *   **Context:** Paper Review
*   **Visuals:** Clean typography on a soft pastel background.
*   **Notes:** Start with the "Hook" immediately.

## Slide 2: The "Happy Accident" Problem
*   **Type:** Content / Visual
*   **Content:**
    *   **Heading:** What is Serendipity?
    *   **Definition:** Finding something valuable *by accident*.
    *   **The Conflict:** Recommender Systems want **Accuracy** (Predictable) vs. Users love **Serendipity** (Surprising).
*   **Visual Element:** A simple CSS diagram showing a straight line (Accuracy) vs. a winding, blooming path (Serendipity). Use pastel colors.
*   **Rubric Tag:** `Content: Accessibility`

## Slide 3: Why LLMs? (Methodology)
*   **Type:** Content
*   **Content:**
    *   **Heading:** Replacing the Human Evaluator
    *   **Old Way:** User Studies (Slow, Expensive).
    *   **New Way:** LLMs (GPT-4) as "User Simulators".
    *   **Key Idea:** Can an LLM "feel" surprised like a human?
*   **Visual Element:** Icon comparison: 👤 vs. 🤖.
*   **Rubric Tag:** `Content: Accuracy`

## Slide 4: Experimental Setup
*   **Type:** Content / Chart
*   **Content:**
    *   **Heading:** How They Tested It
    *   **Datasets:** MovieLens (Movies), Yelp (Restaurants), Amazon (Books).
    *   **Models:** GPT-3.5, GPT-4, LLaMA2.
    *   **Metric:** Correlation with Human Ratings.
*   **Visual Element:** A simple flowchart or table showing: Data -> LLM -> Serendipity Score.
*   **Rubric Tag:** `Visual Aids: Clarity`

## Slide 5: Key Findings (RQ1 & RQ2)
*   **Type:** Data / Chart
*   **Content:**
    *   **Heading:** Do LLMs Match Humans?
    *   **Finding 1:** GPT-4 is the best predictor (High Correlation).
    *   **Finding 2:** Open-source models (LLaMA) struggle.
    *   **Finding 3:** Explanation-augmented prompts help slightly.
*   **Visual Element:** **Bar Chart** comparing correlation scores of GPT-4 vs. LLaMA vs. Humans. (Pastel bars: Blue for GPT-4, Green for Human, Red for LLaMA).
*   **Rubric Tag:** `Content: Key Findings`

## Slide 6: Key Findings (RQ3 - Multi-LLM)
*   **Type:** Data / Chart
*   **Content:**
    *   **Heading:** Two Heads Are Better Than One?
    *   **Approach:** Using multiple LLMs to debate the score.
    *   **Result:** Improves accuracy and reduces bias.
*   **Visual Element:** **Line Chart** or **Grouped Bar Chart** showing performance improvement with Multi-LLM vs Single LLM.
*   **Rubric Tag:** `Visual Aids: Data`

## Slide 7: Significance & Limitations
*   **Type:** Content / List
*   **Content:**
    *   **Heading:** Why This Matters
    *   **Significance:** We can evaluate serendipity *at scale* without thousands of dollars for user studies.
    *   **Limitation:** LLMs still have "hallucinations" and bias.
*   **Visual Element:** Balance Scale icon (Pros vs. Cons).
*   **Rubric Tag:** `Content: Significance`

## Slide 8: Impact on My Research
*   **Type:** Content / Personal
*   **Content:**
    *   **Heading:** My Takeaway
    *   **Connection:** [Insert connection to your specific research area].
    *   **Application:** Using LLMs for preliminary evaluation before human testing.
*   **Visual Element:** Simple arrow pointing from "Paper" to "My Work".
*   **Rubric Tag:** `Content: Reflection`

## Slide 9: Closing & Q&A
*   **Type:** Title / Closing
*   **Content:**
    *   **Heading:** Thank You!
    *   **Subtext:** Questions?
    *   **Contact:** [Your Email/Info]
*   **Visuals:** Simple, welcoming.
*   **Notes:** Reiterate the main takeaway in one sentence.

## Technical Specs (Updated per `feedback.md`)
*   **Layout:** Flexbox column, centered.
*   **Padding:** `5vh 10vw`.
*   **Fonts:** `clamp()` based sizes. Sans-serif (e.g., Arial, Helvetica, system-ui).
*   **Colors (Pastel Palette):**
    *   **Background:** `#FDFBF7` (Off-white/Cream) or `#F0F4F8` (Very pale blue-grey)
    *   **Primary Accent (Blue):** `#AEC6CF` (Pastel Blue) - for headers/highlights
    *   **Secondary Accent (Green):** `#77DD77` (Pastel Green) - for positive data/charts
    *   **Tertiary Accent (Red):** `#FF6961` (Pastel Red) - for negative data/charts
    *   **Text:** `#333333` (Dark Gray) - for contrast
*   **Charts:** CSS-only simple bar charts using `linear-gradient` or flexbox divs with width %.
*   **Navigation:** Keyboard arrow keys + Click zones.
*   **Rubric Tags:** Small pill badges in top-right corner.
