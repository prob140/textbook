---
interact_link: notebooks/Chapter_21/00_The_Beta_and_the_Binomial.ipynb
title: 'Chapter 21: The Beta and the Binomial'
permalink: 'chapters/Chapter_21/00_The_Beta_and_the_Binomial'
previouschapter:
  url: chapters/Chapter_20/03_Independence_Revisited
  title: '20.3 Independence, Revisited'
nextchapter:
  url: chapters/Chapter_21/01_Updating_and_Prediction
  title: '21.1 Updating and Prediction'
redirect_from:
  - 'chapters/chapter-21/00-the-beta-and-the-binomial'
---

# The Beta and the Binomial

Connections between the beta and binomial families have acquired fundamental importance in machine learning. In the previous chapter, you began to see some of these connections. In this chapter we will generalize those observations.

The experiment that we will study has two stages.
- Pick a value of $p$ according to a beta distribution
- Toss a coin that lands heads with the chosen probability $p$

We will see how the posterior distribution of the chance of heads is affected by the prior and by the data. After observing the results of $n$ tosses, we will make predictions about the next toss. We will find the unconditional distribution of the number of heads in $n$ tosses of our random coin and examine the long run behavior of the proportion of heads.

In labs, you will apply this theory to study a model for clustering when the number of possible clusters is not known in advance.
