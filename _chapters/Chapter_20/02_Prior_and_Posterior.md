---
interact_link: notebooks/Chapter_20/02_Prior_and_Posterior.ipynb
title: '20.2 Prior and Posterior'
previouschapter:
  url: chapters/Chapter_20/01_Maximum_Likelihood
  title: '20.1 Maximum Likelihood'
nextchapter:
  url: chapters/Chapter_20/03_Independence_Revisited
  title: '20.3 Independence, Revisited'
---

## Prior and Posterior ##

You are used to thinking of coin tosses as a sequence of i.i.d. Bernoulli $(p)$ variables for some fixed $p$. In an earlier section we showed that the sample proportion of successes $\hat{p}$ is the MLE of the fixed but unknown $p$.

Instead, suppose we think of $p$ as the result of a random draw from a distribution on the unit interval. That is, we assume the probability that the coin lands heads is a random variable $X$ with some density $f_X$ on $(0, 1)$. This is called the *prior* density of $X$.

The prior density reflects our opinion about the unknown parameter before we see the data. For example, if we have no idea what the chance of heads might be, we could use the uniform (0, 1) prior for $X$. If for some reason we happen to think that the chance of heads is somewhere around 70%, we might use a beta (7, 3) prior because then the prior expectation of the chance of heads would be $E(X) = 7/(7+3) = 0.7$. Or we could use some other beta $(r, s)$ prior such that $r/(r+s)$ is around 0.7 and the shape of the prior density reflects our opinion about how the chance of heads is distributed around 70%.

Now suppose you pick a value $p$ of $X$ according to the prior density $f_X$, and repeatedly toss a coin that has chance $p$ of landing heads. Then, given that $X = p$, the distribution of the number of heads in $n$ tosses is binomial $(n, p)$.

Before we go further, let's take a careful look at the phrase "given $X=p$". Because $X$ has a density, the chance that $X$ is equal to any specified value is 0, so we have to be clear about what we mean by "given $X=p$".

### Conditioning on a Continuous Variable ###
Let's take a moment for a general discussion about conditioning on a continuous variable. Our observations will parallel discussions in an earlier chapter where we found conditional densities.

Suppose $X$ is a random variable and $A$ is an event that depends on $X$.

If $X$ is a discrete random variable, then for any possible value $x$ of $X$ the quantity $P(A \mid X = x)$ has a clear definition by the division rule:

$$
P(A \mid X = x) ~ = ~ \frac{P(A, X = x)}{P(X = x)}
$$

When $X$ is continuous, the denominator is 0. In this case there is one main idea to keep in mind:

- $P(A \mid X \in dx)$ is essentially constant regardless of exactly where the infinitesimal interval $dx$ is placed relative to $x$. This constant value will be denoted $P(A \mid X = x)$.

So for continuous $X$, we will define
$$
P(A \mid X = x) ~ = ~ P(A \mid X \in dx) ~ \sim ~ \frac{P(A, X \in dx)}{P(X \in dx)} 
$$

We are assuming that the limit of the right hand side as $dx$ goes to 0 exists and doesn't depend exactly how $dx$ is defined: around $x$, or to the left of $x$, or to the right, and so on. This will be true under regularity conditions; you can just assume it works.

### Posterior Density ###
Let $X$ have possible values in the unit interval and probability density function $f_X$. Let $H$ be the number of heads in $n$ tosses of a coin that lands heads with probability $X$. That is, for each $x$ suppose the conditional distribution of $H$ given $X=p$ is binomial $(n, p)$.

Note the randomization: we are picking one value $p$ of $X$, and then tossing a $p$-coin $n$ times. We are not picking the coin afresh for each toss.

The *likelihood* of the data $H$ given the parameter is

$$
Lik(p) ~ = ~  {n \choose k} p^H (1-p)^{n-H}
$$

Given $H=k$, what is our opinion about $X$? The answer is expressed by the *posterior density of $X$ given* $H=k$. To find it, use Bayes' Rule:

$$
f_{X \vert H=k} (p)dp ~ \sim ~ \frac{P(X \in dp, H = k)}{P(H=k)}
~ \sim ~ \frac{f_X(p)dp \cdot P(H = k \mid X = p)}{P(H = k)}
$$

The denominator does not involve $p$. It is part of the constant that makes the posterior density integrate to 1. The posterior density is therefore *proportional* to the numerator:

$$
f_{X \vert H=k} (p) ~ \propto ~ f_X(p) \cdot P(H = k \mid X = p)
$$

As we saw in the discrete case earlier in the course, **the posterior is proportional to the prior times the likelihood**.

Sometimes, this observation is all that we need in order to identify the posterior distribution of $X$. Here is an example.

### Posterior Distribution Based on Uniform $(0, 1)$ Prior ###
Suppose we know nothing about the coin and therefore give $X$ the uniform (0, 1) prior. Then given $H = k$, the posterior density of $X$ is given by

$$
f_{X \vert H=k} (p) ~ \propto ~ 1 \cdot p^k(1-p)^{n-k}
$$

The factor of ${n \choose k}$ doesn't involve $p$ and has been swept into the constant of proportionality.

Keep in mind that the possible values of $X$ are in the unit interval. Can you recognize what the posterior density of $X$ must be?

That's right: it's the beta $(k+1, n-k+1)$ density. The functional form is determined by $p^k(1-p)^{n-k}$, where $n$ and $k$ are known from the data and $p$ is the value of the variable. 

Let's see what we can say about this beta density. 

Given the data, what do we expect $X$ to be? That's $E(X \mid H = k)$, that is, the expectation of the beta $(k+1, n-k+1)$ posterior density of $X$ given the data $H=k$. By beta density facts, we get

$$
E(X \mid H=k) ~ = ~ \frac{k+1}{n+2}
$$

which for large $n$ is pretty close to the observed proportion $k/n$ but is not exactly the same.

### MAP Estimation: The Posterior Mode ###
The posterior distribution of $X$ reflects our new opinion about $X$ given the data. If we insist that our estimate of the chance of heads has to be a number rather than a distribution, we could go with the posterior mean that we found above. Or we could use the answer to a different question:

Given the data, what is $X$ most likely to be? More precisely, what is the mode of the posterior distribution of $X$ given the data $H=k$?

That's the mode of the beta $(k+1, n-k+1)$ density. This is called the *maximum a posteriori* (MAP) estimate of the chance of heads.

The mode of the beta $(r, s)$ density is straightforward to find by calculus. When $r$ and $s$ are both greater than 1, the mode is $(r-1)/(r+s-2)$. 

So if $1 \le k \le n-1$ (that is, apart from the extreme cases $k = 0$ and $k = n$), the mode of the posterior distribution of $X$ given $H=k$ is 

$$
\frac{(k+1) - 1}{(n+2) - 2} ~ = ~ \frac{k}{n}
$$

which is the observed proportion of heads.

In the case $k = 0$, the posterior mode is 0, which is also the observed proportion of heads. In the case $k = n$, the posterior mode is 1, which again is the observed proportion of heads.

### MLE and MAP ###
We have just shown that if the chance of heads is chosen uniformly over the interval of possible values (0, 1), then the MAP estimate is the same as the MLE that we obtained assuming a fixed probability of heads.

Let's see why this makes sense. When the prior is uniform, the posterior density is given by

$$
f_{X \vert H=k} (p) ~ \propto ~ 1 \cdot p^k(1-p)^{n-k}
$$

The right hand side is just the likelihood of $k$ heads in $n$ tosses of a $p$-coin. Finding the mode of the posterior distribution is therefore equivalent to finding the $p$ that maximizes the likelihood. That's exactly what we did when we found the MLE of the chance of heads.

This equivalence relies on the fact that the uniform prior density is a constant. If we had used some other prior density on (0, 1), then the posterior mode might have been different from the proportion of heads. In the next chapter we will find the posterior density of $X$ starting with any beta prior. This is the basis of a popular model for clustering, which you will explore in labs. 

