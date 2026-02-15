# My First Draft

## Source Information

**Date written:** [2026-02-14]

**Context:** [This is a draft for the course assignment.]

**Status:** [Partial draft - includes Introduction and Literature Review sections.]

---

## Introduction

Serendipity-oriented recommender systems play a pivotal role in enhancing user satisfaction and engagement by mitigating the information cocoon and filter bubble issues prevalent in traditional systems. Despite growing recognition of its importance, explicitly modeling serendipity remains significantly challenging due to its inherently subjective and ambiguous nature. Existing algorithms often rely on objective metrics that linearly combine relevance, novelty, and unexpectedness, or directly employ Large Language Models (LLMs) to predict user serendipity. However, these approaches frequently fail to align with users' subjective perceptions, creating a discrepancy between algorithmic optimization and actual user experience. To address this gap, this study adopts a cognitive science perspective. We aim to simulate the serendipity perception process to develop a model that more accurately reflects subjective user experiences.



## Literature Review
Current research on serendipity in recommender systems primarily focuses on quantifying a serendipity score for candidate items to guide recommendations. The objective is to identify and recommend high-scoring items that are both unexpected and valuable to the user. Existing methodologies can be broadly categorized into two paradigms: objective metric-based approaches and Large Language Model (LLM)-based prediction methods.

The first category defines serendipity through objective metrics, typically constructed as a linear combination of factors such as relevance, novelty, unexpectedness, diversity, and unpopularity. For instance, Zhang et al. and Li et al. formulate the serendipity score by combining relevance (e.g., click-through rate) and unexpectedness. Specifically, Zhang et al. measure unexpectedness via category and content differences between candidates and user history, while Li et al. calculate it as the weighted distance between a candidate item and the clusters of user interests. Kotkov et al. extend this by integrating relevance (predicted ratings), diversity (dissimilarity within the candidate set and user history), and unpopularity. Similarly, Jiang et al. approach the problem by balancing long-term preferences against short-term demands to capture serendipitous moments.

The second category leverages the semantic capabilities of LLMs to directly predict serendipity scores. Fu et al. define serendipity as "unexpected but relevant," utilizing LLMs to output a probability of "Yes" for a serendipity query, which serves as the score. Kang et al. adopt a "pleasant surprise" definition, prompting LLMs to simulate the user's serendipity rating of a candidate item.

Despite these advancements, significant limitations persist. Objective metric-based approaches rely on heuristic definitions that frequently fail to align with the complex, subjective nature of user perception. While LLM-based methods offer a more semantic approach, they often treat serendipity prediction as a black-box classification task without explicitly modeling the underlying cognitive mechanisms that drive user perception.

In summary, while existing methods have made strides in estimating serendipity through heuristic combinations and semantic predictions, a critical gap remains in aligning computational models with human cognitive processes. This underscores the necessity for a cognitive science-grounded approach to model the user's perception of serendipity more accurately, setting the stage for the methodology proposed in this study.


## Notes

[Any additional notes about your draft, challenges you faced, questions you have, etc.]
