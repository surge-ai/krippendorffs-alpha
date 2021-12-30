# Krippendorff's Alpha
*by [Surge AI, the world's most powerful data labeling platform for NLP](https://www.surgehq.ai)*

This repo contains a walkthrough of how to calculate Krippendorff's Alpha for a sample dataset. Check out [kalpha.py](https://github.com/surge-ai/krippendorffs-alpha/blob/main/kalpha.py) for the code.

# Background

In machine learning and data labeling, it’s important to think about inter-annotator agreement: how well do the evaluators building your datasets agree with each other? [Cohen’s kappa statistic](https://www.surgehq.ai/blog/inter-rater-reliability-metrics-understanding-cohens-kappa) is a common way of measuring their agreement, but it suffers from several flaws: it can only be used for measuring two raters, and can only be used for categorical variables. 

One powerful alternative is known as [Krippendorff’s alpha](https://www.surgehq.ai/blog/inter-rater-reliability-metrics-an-introduction-to-krippendorffs-alpha), which generalizes interrater reliability to an arbitrary number of raters and a wide variety of data types. To learn more about it, read our tutorial on the Surge AI blog: [https://www.surgehq.ai/blog/inter-rater-reliability-metrics-an-introduction-to-krippendorffs-alpha](https://www.surgehq.ai/blog/inter-rater-reliability-metrics-an-introduction-to-krippendorffs-alpha)

# Contact

Interested in learning more about data labeling and inter-rater reliability? Check out our [blog](https://www.surgehq.ai/blog), or follow us on Twitter at [@HelloSurgeAI](https://www.twitter.com/@HelloSurgeAI)!
