---
bibliography: references.bib
csl: ieee.csl
---

# LLM-Powered Cognitive Modeling for Serendipity-Aware Recommender Systems


## Introduction


In recent years, the explosive growth of digital content has led to the increasing prevalence of information overload [@bao2024large]. Therefore, the recommender system has become a key technology to screen and give priority to presenting the most valuable content to users [@burke2011recommender]. However, the traditional recommender system mainly uses the user's historical interaction and item attributes to maximize the prediction relevance; although this helps to improve short-term accuracy, it often aggravates the problem of filtering bubbles and information cocoon [@kunaver2017diversity]. To address these issues, the academic community and the industry have paid more and more attention to the recommender system oriented by serendipity [@ziarani2021serendipity]. Serendipity is usually defined as a pleasant surprise experience when discovering both relevant and unexpected content, so as to improve user satisfaction, participation and long-term retention [@chen2019serendipity].

Despite growing recognition of its importance, due to its inherent subjectivity and ambiguity, explicit modeling serendipity is still particularly challenging [@kotkov2016challenges]. The golden standard for obtaining real serendipity signals is user studies, but it is expensive, limited in scale, and difficult to update continuously [@binst2024evaluate]. In order to reduce the cost of annotation, existing methods usually adopt objective proxy metrics, such as linear weighting of relevance, novelty and unexpectedness [@DESR; @SNPR; @PURS], or directly use large language models (LLMs) to predict serendipity [@Japan; @fu2024art]. However, these methods are often difficult to align with the user's subjective experience: the user's perception of "serendipity" is not only affected by the attributes of the item, but also depends on individual characteristics, current situation and dynamic expectations, etc., which is difficult to capture based on item-level characteristics or static indicators [@kotkov2024dark]. This inconsistency creates a gap between the algorithm optimization objectives and real user experience, underscoring the need for a scalable and subjective modeling framework that can consider individual differences and situational variability.

To address these limitations, we propose the core research question: can we simulate the user's cognitive process to better approximate their subjective experience of serendipity? To this end, we adopt a cognitive science perspective and introduce the reward prediction error (RPE) theory [@schultz2016dopamine], which characterizes serendipity as a positive deviation between actual and predicted rewards. Building on this insight, we operationalize serendipity as a positive prediction error: the predicted reward corresponds to a user’s a priori expectations about recommended item, while the actual reward reflects the user’s realized perception and evaluation of the recommended item.  Methodologically, we leverage LLMs for expectation modeling by conditioning on user profiles and contextual information to simulate individualized expectation distributions. We then integrate user's traits and context to construct a personalized serendipity signal, which is incorporated into ranking and training objectives within our RPE-based serendipity modeling (RSM) framework. Empirically, on the Taobao Serendipity [@taobao] and MovieLens datasets [@seren2018], our RSM yields consistent and statistically significant improvements over strong baselines, achieving state-of-the-art performance.

The main contributions of this paper are as follows: 

- We formalize serendipity into positive prediction error within the cognitive science framework of RPE theory, which provides an explainable modeling paradigm for subjective serendipity.

- We propose a user expectation simulation and situational modeling method based on the Large Language Model to build a personalized serendipity signal, and bridge the gap between the algorithm optimization goal and the user's subjective experience while reducing the dependence on high-cost user studies.
  
- We have empirically verified the proposed method on the public and the real-world datasets, proving that it can better align with user perception and improve the recommended performance.

The structure of the rest of this paper is as follows: Section 2 reviews the relevant research; Section 3 details the proposed RSM framework and its implementation; Section 4 describes the experimental settings, results and related analysis; Section 5 summarizes the full text and looks forward to the future work direction.

## Literature Review

In recommender systems, serendipity refers to the pleasant surprise experience caused by items [@chen2019serendipity]. Accordingly, systems aim to present items with high serendipity scores from the candidate pool [@kotkov2016survey]. The current research primarily focuses on quantifying the serendipity score of candidate items to guide ranking, and its goal is to identify content that is both unexpected and valuable to users [@kaminskas2016diversity]. The existing methods can be broadly divided into two types of paradigms: objective metric-based approaches and LLMs-based prediction methods.

The first type of method defines serendipity through objective metrics, which is usually composed of a linear combination of factors such as relevance, novelty, unexpectedness, diversity and unpopularity. For example, Zhang et al. and Li et al. combine relevance (e.g., click-through rate) with unexpectedness to construct a serendipity score [@SNPR; @PURS]. Specifically, Zhang et al. measure the unexpectedness by the differences in category and content between candidates and user history [@SNPR], while Li et al. calculate it as the weighted distance between candidate items and user interest clusters [@PURS]. Kotkov et al. further integrate relevance (prediction score), diversity (dissimilarity within the candidate set and user history), and unpopularity [@kotkov2020does]. Similarly, Jiang et al. capture moments with serendipity by balancing long-term preferences and short-term needs [@DESR]. Although these heuristic objective metrics have good scalability and computational efficiency, they are often difficult to be consistent with the complex and subjective essence perceived by users.


The second type of method uses the semantic ability of the LLMs to directly predict serendipity scores. Fu et al. define serendipity as "unexpected but relevant," , and let LLMs output the probability of "Yes" for the serendipity query and use it as a score [@fu2024art]. Kang et al. use the definition of "pleasant surprise" to prompt LLM to simulate users' serendipity score for candidate items [@kang2025exploring]. Tokutake et al. do not give a clear definition of serendipity, but ask LLM to predict whether a candidate item would be serendipitous for the user [@Japan]. Although the LLM-based approach provides a more semantic approach, they often regard serendipity prediction as a black box classification task and do not explicitly model the underlying cognitive mechanism that drives user perception.

In summary, while the existing methods have made progress in estimating serendipity through heuristic combination and semantic prediction, there are still key gaps in aligning the computational model with the serendipity perception of real users. This highlights the necessity of methods based on cognitive science to more accurately model users' perception of serendipity, which also lays the foundation for the method proposed in this paper.


## Declaration of Generative AI Use
This work use Generative AI (GPT-5) to check grammer and spelling error, and polish writing.

## References