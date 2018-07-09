---
interact_link: notebooks/Chapter_07/01_Poissonizing_the_Binomial.ipynb
title: '7.1 Poissonizing the Binomial'
permalink: 'chapters/Chapter_07/01_Poissonizing_the_Binomial'
previouschapter:
  url: chapters/Chapter_07/00_Poissonization
  title: 'Chapter 7: Poissonization'
nextchapter:
  url: chapters/Chapter_07/02_Poissonizing_the_Multinomial
  title: '7.2 Poissonizing the Multinomial'
redirect_from:
  - 'chapters/chapter-07/01-poissonizing-the-binomial'
---

## Poissonizing the Binomial

The families of distributions that data scientists tend to use most are those that arise out of natural assumptions about the randomness in the data. These distribution families also have mathematical properties that give rise to illuminating answers to questions about the data. The binomial and Poisson families are among these.

In this section we will study some more properties of the Poisson family, including another remarkable connection that it has with the binomial family.

### Sums of Independent Poisson Variables
Let $X$ have the Poisson ($\mu$) distribution, and let $Y$ independent of $X$ have the Poisson ($\lambda$) distribution. Then the sum $S = X+Y$ has the Poisson ($\mu + \lambda$) distribution.

To prove this, first notice that the possible values of $S$ are the non-negative integers.  For a non-negative integer $s$, find $P(S = s)$ by partitioning the event according to values of $X$, keeping in mind that both $X$ and $Y$ have to be non-negative because both are Poisson.

$$
\begin{align*}
P(S = s) &= \sum_{k=0}^s P(X=k, Y=s-k) \\
&= \sum_{k=0}^s e^{-\mu} \frac{\mu^k}{k!} \cdot e^{-\lambda} \frac{\lambda^{s-k}}{(s-k)!} \\
&= e^{-(\mu+\lambda)} \frac{1}{s!} \sum_{k=0}^s
\frac{s!}{k!(s-k)!} \mu^k \lambda^{s-k} \\
&= e^{-(\mu+\lambda)} \frac{(\mu+\lambda)^s}{s!}
\end{align*}
$$

by the binomial expansion of $(\mu+\lambda)^s$. This is the Poisson $(\mu + \lambda)$ probability formula for the value $s$.

One important application of this result is that if $X_1, X_2, \ldots , X_n$ are i.i.d. Poisson $(\mu)$ variables, then their sum $X_1 + X_2 + \ldots + X_n$ has the Poisson $(n\mu)$ distribution.


### Randomizing the Number of Bernoulli Trials
Suppose $N_H$ is the number of heads in 100 tosses of a coin, and $N_T$ the number of tails. Then $N_H$ and $N_T$ are far from independent. They are linear functions of each other because $N_T = 100 - N_H$. 

The same is true of any fixed number of tosses: if you know the number of heads, then you also know the number of tails. 

In any fixed number of Bernoulli trials, the number of successes and the number of failures are heavily dependent. If you know one, you know the other.

However, something remarkable happens when the *number of trials is itself random and has a Poisson distribution.* After we see what happens, we will be able to understand why it matters.

Let $N$ have the Poisson $(\mu)$ distribution, let $S$ be the number of successes in $N$ i.i.d. Bernoulli $(p)$ trials. More formally: 
- Given $N = 0$, define $S$ to be 0 with probability 1. Given that there are no trials, there are also no successes.
- For $n \ge 1$, let the conditional distribution of $S$ given $N = n$ be binomial $(n, p)$.

Then the joint distribution of $N$ and $S$ is given by:

$$
P(N=n, S=s) ~ = ~ e^{-\mu}\frac{\mu^n}{n!} \cdot 
\frac{n!}{s!(n-s)!} p^s(1-p)^{n-s}, ~~ 0 \le s \le n
$$

You should check that the formula is correct when $n=0$.

We can sum the terms in this joint distribution appropriately to get the marginal distribution of $S$.

### A Poisson Number of Successes
The possible values of $S$ are $0, 1, 2, \ldots $ with no upper limit because there is no upper limit on the possible values of $N$. For $s \ge 0$,

$$
\begin{align*}
P(S = s) &= \sum_{n=s}^\infty P(N=n, S=s) \\ \\
&= \sum_{n=s}^\infty e^{-\mu}\frac{\mu^n}{n!} \cdot 
\frac{n!}{s!(n-s)!} p^sq^{n-s} ~~~~ \text{where } q = 1-p \\ \\
&= e^{-\mu} \frac{\mu^sp^s}{s!} \sum_{n=s}^\infty
\frac{\mu^{n-s}q^{n-s}}{(n-s)!} \\ \\
&= e^{-\mu} \frac{(\mu p)^s}{s!} \sum_{n=s}^\infty
\frac{(\mu q)^{n-s}}{(n-s)!} \\ \\
&= e^{-\mu} \frac{(\mu p)^s}{s!} \sum_{j=0}^\infty
\frac{(\mu q)^j}{j!} \\ \\
&= e^{-\mu} \frac{(\mu p)^s}{s!} e^{\mu q} \\ \\
&= e^{-\mu p} \frac{(\mu p)^s}{s!} ~~ \text{because } \mu p+ \mu q = \mu
\end{align*}
$$

Thus the distribution of $S$ is Poisson with parameter $\mu p$.

Notice what we have just proved. If the number of trials $n$ is fixed, you know that the distribution of the number of successes is binomial $(n, p)$. But if the the number of trials is random with a Poisson $(\mu)$ distribution, then the distribution of the number of successes is Poisson $(\mu p)$. This is a major step in *Poissonizing* the binomial.

The best is yet to come, but let's take a moment to look at the result numerically. Suppose you run a Poisson $(12)$ number of i.i.d. Bernoulli $(1/3)$ trials. Then the number of trials is most likely to be somewhere around 12, but you can't say exactly what it will be because it's random. What we have shown is that the number of successes is Poisson with parameter $12 \times \frac{1}{3} = 4$.

The parameter 4 is not hard to understand intuitively. You're most likely to see around 12 trials, and about 1/3 of them are going to be successes, so you're most likely to see around 4 successes.

### Successes and Failures are Independent
Yes, you read that right. If you run a Poisson number of i.i.d. Bernoulli trials, then the number of successes and the number of failures are *independent*.

Randomizing parameters (in this case the number of trials) can have a drastic effect on the relations between random variables.

Let's prove our result, and then we will see a way in which it is used.

Suppose as before that we are running $N$ i.i.d. Bernoulli $(p)$ trials, where $N$ has the Poisson $(\mu)$ distribution. Also as before, let $S$ be the number of successes. 

Now let $F$ be the number of failures.
Then the distribution of $F$ is Poisson $(\mu q)$ where $q = 1-p$. This follows by redefining "success" as "failure" in our previous argument.

The joint distribution of $S$ and $F$ is

$$
\begin{align*} 
P(S = s, F = f) &= P(N = s+f, S = s) \\ \\
&= e^{-\mu} \frac{\mu^{s+f}}{(s+f)!} \frac{(s+f)!}{s!f!} p^s q^f \\ \\
&= \big{(} e^{-\mu p} \frac{ (\mu p)^s}{s!} \big{)} 
\big{(} e^{-\mu q} \frac{ (\mu q)^f}{f!} \big{)} \\ \\
&= P(S = s)P(F = f)
\end{align*}
$$

This shows that $S$ and $F$ are independent.

### Summary: Poissonization of the Binomial
Suppose you run $N$ i.i.d. Bernoulli $(p)$ trials, where $N$ has the Poisson $(\mu)$ distribution. Let $S$ be the number of successes and $F$ the number of failures, and let $q = 1-p$. Then:
- $S$ has the Poisson $(\mu p)$ distribution.
- $F$ has the Poisson $(\mu q)$ distribution.
- $S$ and $F$ are independent.

For example, suppose 90% of the individuals in a population are of Class A and 10% are of Class B. Suppose you choose a sample of $N$ people so that $N$ has the Poisson $(20)$ distribution and the choices are i.i.d. Then in your sample, the number of people of Class A has the Poisson $(18)$ distribution, the number in Class B has the Poisson $(2)$ distribution, and the counts in the two classes are independent.

Thus for example the chance that each class appears at least five times in your sample is

$$
\big{(} \sum_{i=5}^\infty e^{-{18}} \frac{18^i}{i!} \big{)}
\big{(} \sum_{j=5}^\infty e^{-{2}} \frac{2^j}{j!} \big{)}
~ = ~ 
\big{(}1 - \sum_{i=0}^4 e^{-{18}} \frac{18^i}{i!} \big{)}
\big{(}1- \sum_{j=0}^4 e^{-{2}} \frac{2^j}{j!} \big{)}
$$

Numerically, this is about 5%.


{:.input_area}
```python
(1 - stats.poisson.cdf(4, 18))*(1 - stats.poisson.cdf(4, 2))
```




{:.output_data_text}
```
0.052648585218160585
```



Already remarkable when there are two classes in the population, Poissonization really helps simplify calculations when there are three or more classes, as we will see in the next section.
