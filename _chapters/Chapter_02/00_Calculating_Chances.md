---
interact_link: notebooks/Chapter_02/00_Calculating_Chances.ipynb
title: 'Chapter 2: Calculating Chances'
permalink: 'chapters/chapter-02/00-calculating-chances'
previouschapter:
  url: chapters/chapter-01/05-an-exponential-approximation
  title: '1.5 An Exponential Approximation'
nextchapter:
  url: chapters/chapter-02/01-addition
  title: '2.1 Addition'
---

# Calculating Chances

Once you start working with probabilities, you quickly realize that the assumption of all possible outcomes being equally likely isn't always reasonable. For example, if you think a coin is biased then you won't want to assume that it lands heads with the same chance as tails. 

To deal with settings in which some outcomes have a higher chance than others, a more general theory is needed. In the 1930's, the Russian mathematician [Andrey Kolmogorov](https://en.wikipedia.org/wiki/Andrey_Kolmogorov) (1903-1987) formulated some ground rules, known as *axioms*, that covered a rich array of settings and became the foundation of modern probability theory.

The axioms start out with an outcome space $\Omega$. We will assume $\Omega$ to be finite for now. Probability is a function $P$ defined on events, which as you know are subsets of $\Omega$. The first two axioms just set the scale of measurement: they define probabilites to be numbers between 0 and 1.

- Probabilities are non-negative: for each event $A$, $P(A) \ge 0$.
- The probability of the whole space is 1: $P(\Omega ) = 1$.

The third and final axiom is the key to probability being a "measure" of an event. We will study it after we have developed some relevant terminology.
