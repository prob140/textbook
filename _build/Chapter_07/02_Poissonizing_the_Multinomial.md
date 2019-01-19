---
redirect_from:
  - "/chapter-07/02-poissonizing-the-multinomial"
interact_link: notebooks/Chapter_07/02_Poissonizing_the_Multinomial.ipynb
title: 'Poissonizing the Multinomial'
prev_page:
  url: /Chapter_07/01_Poissonizing_the_Binomial
  title: 'Poissonizing the Binomial'
next_page:
  url: /Chapter_08/00_Expectation
  title: 'Chapter 8: Expectation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## Poissonizing the Multinomial

Bernoulli trials come out in one of two ways. But many trials come out in multiple different ways, all of which we might want to track. A die can land six different ways. A jury member can have one of several different educational levels. In general, an individual might belong to one of several classes.

The *multinomial distribution* is an extension of the binomial to the case where each repeated trial has more than two possible outcomes. Let's look at it first in an example, and then we will define it in general.

A box contains 2 blue tickets, 5 green tickets, and 3 red tickets. Fifteen draws are made at random with replacement. To find the chance that there are 4 blue, 9 green, and 2 red tickets drawn, we could start by writing all possible sequences of 4 B's, 9 G's, and 2 R's. 

Each such sequence has chance $0.2^4 0.5^9 0.3^2$, so all we need for completing the probability calculation is the number of sequences we could write.
- There are $\binom{15}{4}$ ways of choosing places to write the B's.
- For each of these ways, there are $\binom{11}{9}$ ways of choosing 9 of the remaining 11 places to write the G's.
- The remaining 2 places get filled with R's.

So 

$$
\begin{align*}
P(\text{4 blue, 9 green, 2 red}) 
&= \binom{15}{4} \cdot \binom{11}{9} 0.2^4 0.5^9 0.3^2 \\ \\
&= \frac{15!}{4!11!} \cdot \frac{11!}{9!2!} 0.2^4 0.5^9 0.3^2 \\ \\
&= \frac{15!}{4!9!2!} 0.2^4 0.5^9 0.3^2
\end{align*}
$$

Notice how this simply extends the binomial probability formula by including a third category. 

Analogously, or formally by induction, you can extend the formula to any finite number of categories or classes.

### Multinomial Distribution
Fix a positive integer $n$. Suppose we are running $n$ i.i.d. trials where each trial can result in one of $k$ classes. For each $i = 1, 2, \ldots, k$, let the chance of getting Class $i$ on a single trial be $p_i$, so that $\sum_{i=1}^k p_i = 1$.

For each $i = 1, 2, \ldots , k$, let $N_i$ be the number of trials that result in Class $i$, so that $\sum_{i=1}^k N_i = n$.

Then the *joint* distribution of $N_1, N_2, \ldots , N_k$ is
given by

$$
P(N_1 = n_1, N_2 = n_2, \ldots , N_k = n_k)
~ = ~ \frac{n!}{n_1!n_2! \ldots n_k!}p_1^{n_1}p_2^{n_2} \cdots p_k^{n_k}
$$

where $n_i \ge 0$ for $1 \le i \le k$ and $\sum_{i=1}^k n_i = n$.

When there just two classes, then $k = 2$ and the formula reduces to the familiar binomial formula written as the joint distribution of the number of successes and the number of failures:

$$
P(N_1 = n_1, N_2 = n_2) = \frac{n!}{n_1!n_2!} p_1^{n_1}p_2^{n_2} ~~ \text{where } p_1+p_2=1 \text{ and }
n_1+n_2=n
$$

### Binomial Marginals
No matter how many classes there are, the marginal distribution of each $N_i$ is binomial $(n, p_i)$. You don't have to sum the joint distributions to work this out. $N_i$ is the number of Class $i$ individuals in the sample; each sampled individual is in Class $i$ with probability $p_i$; and there are $n$ independent draws. That's the binomial setting.

### Poissonization
If you replace the fixed number $n$ of trials by a Poisson $(\mu)$ random number of trials, then the multinomial gets Poissonized as follows:
- For each $i = 1, 2, \ldots , k$, the distribution of $N_i$ is Poisson $(\mu p_i)$.
- The counts $N_1, N_2, \ldots , N_k$ in the $k$ different categories are mutually independent.

We won't go through the proof which is a straightforward extension of the proof in the case $k=2$ given in an earlier section. Rather, we will look at why the result matters.

When the number of trials is fixed, $N_1, N_2, \ldots , N_k$ are all dependent on each other in complicated ways. But when you let the sample size be a Poisson random variable, then the independence of the counts $N_1, N_2, \ldots , N_k$ lets you quickly calculate the chance of any particular configuration of classes in the sample.

For example, suppose that in your population the distribution of classes is as follows:
- Class 1: 20%
- Class 2: 30%
- Class 3: 50%

Now suppose you draw $N$ independent times where $N$ has the Poisson $(20)$ distribution, then the chance that you will get at least 3 individuals in each class is about 71.27%.



{:.input_area}
```python
(1 - stats.poisson.cdf(2, 4))*(1-stats.poisson.cdf(2, 6))*(1-stats.poisson.cdf(2, 10))
```





{:.output .output_data_text}
```
0.71270362753222372
```



The number of factors in the answer is equal to the number of classes, unlike the inclusion-exclusion formula in which the amount of work increases much more with each additional class, as you have seen in exercises.

This helps data scientists tackle questions like, "How many times must I sample so that my chance of seeing at least one individual of each class exceeds a given threshold?" The answer depends on the distribution of classes in the population, of course, but allowing the sample size be a Poisson random variable can make calculations much more tractable. For applications, see for example the Abstract and References of this [paper](http://people.csail.mit.edu/jayadev/papers/psn_unv_cmp.pdf).

**Note.** If there are a large number of classes, then even with a fixed large sample size the sample counts in the different classes are almost independent. If you know some of the counts, the information doesn't have much effect on the distributions of the other counts. In such situations, you won't go very far wrong if you treat the counts as independent even though the sample size is fixed. 
