---
interact_link: notebooks/Chapter_13/00_Variance_Via_Covariance.ipynb
title: 'Chapter 13: Variance Via Covariance'
permalink: 'chapters/Chapter_13/00_Variance_Via_Covariance'
previouschapter:
  url: chapters/Chapter_12/04_Heavy_Tails
  title: '12.4 Heavy Tails'
nextchapter:
  url: chapters/Chapter_13/01_Properties_of_Covariance
  title: '13.1 Properties of Covariance'
redirect_from:
  - 'chapters/chapter-13/00-variance-via-covariance'
---

# Variance Via Covariance

In this chapter we return to random sampling and study the variability in the sum of a random sample. It is worth taking some time to understand how sample sums behave, because many interesting random variables like counts of successes can be written as sums. Binomial and hypergeometric random variables are such sums. Also, the mean of a random sample is a straightforward function of the sample sum. 

Let $X$ be a random variable. We will use some familiar shorthand:

- $\mu_X = E(X)$
- $\sigma_X = SD(X)$

Let $D_X = X - \mu_X$ denote the deviation of $X$ from its mean. Then

$$
Var(X) = \sigma_X^2 = E(D_X^2)
$$

### Variance of a Sum
Let $X$ and $Y$ be two random variables on the same space, and let $S = X+Y$. Then $E(S) = \mu_X + \mu_Y$, and the deviation of $S$ is the sum of the deviations of $X$ and $Y$:

$$
D_S ~ = ~ S - \mu_S ~ = ~ X + Y - (\mu_X + \mu_Y) ~ = ~ D_X + D_Y
$$

This gives us some insight into the variance of the sum $S$.

$$
\begin{align*}
Var(S) &= E(D_S^2) \\
&= E[(D_X + D_Y)^2] \\
&= E(D_X^2) + E(D_Y^2) + 2E(D_XD_Y) \\
&= Var(X) + Var(Y) + 2E(D_XD_Y)
\end{align*}
$$

The first thing to note is that while the expectation of a sum is the sum of the expectations, the calculation above shows that the variance of a sum is in general **not** the sum of the variances. There's an extra term. 

To calculate the variance of a sum, we have to understand that extra term. 

### Covariance
The *covariance of $X$ and $Y$*, denoted $Cov(X, Y)$, is the expected product of the deviations of $X$ and $Y$:

$$
Cov(X, Y) ~ = ~ E(D_XD_Y) ~=~ E[(X - \mu_X)(Y - \mu_Y)]
$$

In this chapter we will learn how to utilize covariance to find variances of sums. The fundamental calculation is the one we did above; here is the result again, using the language of covariance.

$$
Var(X+Y) ~ = ~ Var(X) + Var(Y) + 2Cov(X, Y)
$$
