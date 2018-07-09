---
interact_link: notebooks/Chapter_13/03_Sums_of_Simple_Random_Samples.ipynb
title: '13.3 Sums of Simple Random Samples'
permalink: 'chapters/chapter-13/03-sums-of-simple-random-samples'
previouschapter:
  url: chapters/chapter-13/02-sums-of-iid-samples
  title: '13.2 Sums of IID Samples'
nextchapter:
  url: chapters/chapter-13/04-finite-population-correction
  title: '13.4 Finite Population Correction'
---

## Sums of Simple Random Samples


When the random variables that are being added are not independent, finding the variance of the sum does involve finding covariances. As before, let $X_1, X_2, \ldots X_n$ be random variables with sum

$$
S_n = \sum_{i=1}^n X_i
$$

The variance of the sum is

$$
Var(S_n) ~ = ~ \sum_{i=1}^n Var(X_i) + \mathop{\sum \sum}_{1 \le i \ne j \le n} Cov(X_i, X_j)
$$

Before we apply this formula, let's start out by finding a simple covariance.

### Indicators
Let $A$ and $B$ be two events. Let $I_A$ be the indicator of $A$ and let $I_B$ be the indicator of  $B$. This is going to be one of the rare instances where we use an expected product to find a covariance. That's because we know that products of indicators are themselves indicators.

$$
Cov(I_A, I_B) = E(I_AI_B) - E(I_A)E(I_B) = P(AB) - P(A)P(B)
$$

You can see that the covariance is 0 if $A$ and $B$ are independent, consistent with the more general result of the previous section. When $A$ and $B$ are not independent, covariance helps us understand the nature of the dependence. For example, if $Cov(I_A, I_B)$ is positive, then

$$
P(AB) > P(A)P(B) ~~~ \implies ~~~ P(A)P(B \mid A) > P(A)P(B)
~~~ \implies ~~~ P(B \mid A) > P(B)
$$

That is, given that $A$ has occurred, the chance of $B$ is higher than it is overall. This is called *positive association* or *positive dependence* of $A$ and $B$.

### Variance of the Hypergeometric
Suppose you have a population of $N$ elements of which $G$ are good. Let $X$ be the number of good elements in simple random sample of $n$ elements drawn from the population. Remember that simple random samples are drawn without replacement.

We know that
$$
X = \sum_{j=1}^n I_j
$$

where $I_j$ is the indicator that draw $j$ yields a good element. 

By symmetry, we know that $E(I_j) = \frac{G}{N}$ for each $j$. That is why

$$
E(X) ~ = ~ n \frac{G}{N} ~ = ~ np ~~~~ \text{where } p = \frac{G}{N}
$$

That's the same formula as for the binomial.

We also know that $Var(I_j) = \frac{G}{N} \cdot \frac{B}{N}$ where $B = N-G$ is the number of bad elements in the population.

Also by symmetry, $Cov(I_j, I_k)$ is the same for each pair $j, k$ where $j \ne k$. The example above tells us how to calculate this common value.

$$
Cov(I_j, I_k) = \frac{G}{N} \cdot \frac{G-1}{N-1} - \frac{G}{N} \cdot \frac{G}{N}
$$

Therefore
$$
\begin{align*}
Var(X) &= \sum_{j=1}^n Var(I_j) + \mathop{\sum \sum}_{1 \le j \ne k \le n} Cov(I_j, I_k) \\ \\
&= n \frac{G}{N} \cdot \frac{B}{N} ~ + ~ n(n-1) \Big{(} \frac{G}{N} \cdot \frac{G-1}{N-1} - \frac{G}{N} \cdot \frac{G}{N} \Big{)} \\ \\
&= n \frac{G}{N} \cdot \frac{B}{N} ~ + ~ n(n-1) \frac{G}{N} \Big{(} \frac{G-1}{N-1} - \frac{G}{N} \Big{)} \\ \\
&= n \frac{G}{N} \cdot \frac{B}{N} ~ - ~ n(n-1) \frac{G}{N} \cdot \frac{N-G}{N(N-1)} \\ \\
&= n \frac{G}{N} \cdot \frac{B}{N} \cdot \Big{(} 1 - \frac{n-1}{N-1} \Big{)} \\ \\
&= n \frac{G}{N} \cdot \frac{B}{N} \cdot \Big{(} \frac{N-n}{N-1} \Big{)} \\ \\
&= npq \cdot \frac{N-n}{N-1}
\end{align*}
$$

where $p = \frac{G}{N}$ and $q = 1-p$. 

Notice that the formula is the same as the formula for the variance of the binomial, apart from the factor of $\frac{N-n}{N-1}$.

We can generalize this result to the case where the population isn't binary.

### Variance of a Simple Random Sample Sum
Suppose we have a population of $N$ numbers which need not be only zeros and ones. Suppose the population has mean $\mu$ and standard deviation $\sigma$. Draw a simple random sample of size $n$ from the population. For $j$ in the range 1 through $n$, let $X_j$ be the $j$th value drawn.

Let $S_n = X_1 + X_2 + \cdots + X_n$. Then $E(S_n) = n\mu$, and 

$$
Var(S_n) ~ = ~ \sum_{i=1}^n Var(X_i) + \mathop{\sum \sum}_{1 \le i \ne j \le n} Cov(X_i, X_j) ~ = ~ n\sigma^2 + n(n-1)Cov(X_1, X_2)
$$
by symmetry.

How can we find $Cov(X_1, X_2)$? It's not a good idea to try and multiply the two variables, as they are dependent and their distributions might be unpleasant. The expected product will be hard to find.

What we can use is the observation that the equation we derived above for $Var(S_n)$ is valid for any sample size. In particular, it is valid in the case when we take a census, that is, when we sample all the elements of the population. In that case $n = N$ and the equation is
$$
Var(S_N) = N\sigma^2 + N(N-1)Cov(X_1, X_2)
$$

Why is helpful? To answer this, think about the variability in $S_N$. We have sampled the entire population without replacement. Therefore $S_N$ is just the total of the entire population. There is no sampling variability in $S_N$, because there is only one possible sample of size $N$.

That means $Var(S_N) = 0$. We can use this to solve for $Cov(X_1, X_2)$.

$$
0 = N\sigma^2 + N(N-1)Cov(X_1, X_2) ~~~~~ \implies ~~~~~
Cov(X_1, X_2) = -\frac{\sigma^2}{N-1}
$$

Now plug this into the formula for $Var(S_n)$ for any smaller sample size $n$.

$$
Var(S_n) ~ = ~ n\sigma^2 - n(n-1)\frac{\sigma^2}{N-1} ~ = ~
n\sigma^2 \Big{(} 1 - \frac{n-1}{N-1} \Big{)} ~ = ~
n\sigma^2 \frac{N-n}{N-1}
$$

Recall that the variance of the sample sum is $n\sigma^2$ when the sample is drawn with replacement. When the sample is drawn without replacement, the formula is the same apart from the factor of $\frac{N-n}{N-1}$. 

That is exactly what we saw in the special case of the binary population. In the final section of this chapter we will investigate this relation between sampling with and without replacement.
