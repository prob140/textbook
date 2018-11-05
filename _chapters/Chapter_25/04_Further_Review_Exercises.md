---
interact_link: notebooks/Chapter_25/04_Further_Review_Exercises.ipynb
title: '25.4 Further Review Exercises'
permalink: 'chapters/Chapter_25/04_Further_Review_Exercises'
previouschapter:
  url: chapters/Chapter_25/03_Multivariate_Normal_Regression
  title: '25.3 Regression and the Multivariate Normal'
nextchapter:
  url: 
  title: ''
redirect_from:
  - 'chapters/chapter-25/04-further-review-exercises'
---

## Further Review Exercises

Many of these exercises require the material of Chapter 19 onwards, which of course relies on the material of the previous chapters. However, some of them can be solved using earlier material alone. 

According to students and alumni, some of the exercises have appeared as questions in "quant" interviews.

**1.**
A coin lands heads with probability $p$. Let $X$ be the number of tosses till the first head appears and let $Y$ be the number of tails before the first head.

(a) Find the moment generating function of $X$.

(b) Use the answer to (a) to find $E(X)$. Note that by now you have found $E(X)$ in several ways: by the tail sum formula, by conditioning on the first toss, by the pgf, and now by the mgf.

(c) Use the answer to (a) to find the moment generating function of $Y$.

**2.**
Let $X_1, X_2, \ldots, X_n$ be i.i.d. Poisson $(\mu)$ random variables. Find the maximum likelihood estimate of $\mu$.

**3.**
Let $X_1, X_2, \ldots, X_n$ be i.i.d. uniform on $(0, \theta)$. 

(a) Find the MLE of $\theta$. [Don't leap into a calculation. Sketch a graph of the function you are trying to maximize, and be careful about its domain.]

(b) Is the MLE unbiased? If not, use the MLE to construct an unbiased estimate of $\theta$.

**4.** $X$ and $Y$ are i.i.d. with moment generating function $M(t) = e^{t + t^2}$, $-\infty < t < \infty$. What is the distribution of $(X-Y)^2$?

**5.**
*Capture-recapture* methods are sometimes used to estimate population sizes. A standard image is that a pond contains $N$ fish for some fixed but unknown $N$, and that $G$ of the $N$ fish have been captured, tagged, and returned alive to the pond. 

In the recapture phase, assume that a simple random sample of $n$ fish is drawn from the $N$ fish in the pond (you might have to use some imagination to believe this assumption). We can observe $X$, the random number of tagged fish in the sample. 

The goal is to use the observation to estimate $N$.

(a) For large $n$, the sample proportion $X/n$ is likely to be close to a constant. Identify the constant and hence construct an estimate of $N$ based on $X$. Later in this exercise you will see how your estimate is related to the MLE of $N$.

(b) For $N \ge n$, find the likelihood $lik(N)$. You can assume $n > G$. 

(c) To maximize this likelihood function, adapt the method you used to find the mode of the binomial and Poisson distributions. Find the likelihood ratio $\frac{lik(N+1)}{lik(N)}$ and show that it is a decreasing function of $N$. [Go back and look at how we showed the corresponding fact for binomial odds ratios.]

(d) Now find the MLE of $N$. How does it compare with your estimate in (a)?

**6.** 
Show that if $r > 1$ and $s > 1$ then the mode of the beta $(r, s)$ distribution is $(r-1)/(r+s-2)$. Remember to ignore multiplicative constants and take the log before maximizing. 

**7.** 
Suppose that $X$ has the beta $(r, s)$ distribution, and that given $X=p$, the conditional distribution of $H$ is binomial $(10, p)$. Find

(a) the conditional distribution of $X$ given $H = 7$

(b) $E(X \mid H = 7)$

(c) the MAP estimate of $X$ given $H = 7$ 

(d) $P(H = 7)$

(e) $E(H)$

**8.**
The chance of heads of a random coin is picked according to the beta $(r, s)$ distribution. The coin is tossed repeatedly.

(a) What is the chance that the first three tosses are heads and the next three tosses are tails?

(b) Given that the first three tosses are heads and the next three tosses are tails, what is the chance that the seventh toss is a head?

(c) Given that three out of the first six tosses are heads, what is the chance that the seventh toss is a head? Compare with the answer to (b).

**9.**
Person A creates a coin by picking its chance of heads uniformly on $(0, 1)$. In three tosses of that coin, Person A gets two heads.

Independently of Person A, Person B creates a coin by picking its chance of heads uniformly on $(0, 1)$. In three tosses of that coin, Person B gets one head.

(a) Given the data, what is the distribution of the chance of heads of Person A's coin?

(b) Given the data, what is the distribution of the chance of heads of Person B's coin?

(c) Given the data, what is the probability that Person A's coin has a higher chance of heads than Person B's coin?

**10: Markov and Chebyshev Bounds on the Poisson-Binomial Upper Tail.** 
For $j \ge 1$ let $I_j$ be independent indicators such that $P(I_j = 1) = p_j$. Let $X = I_1 + I_2 + \ldots + I_n$. Then $X$ is the number of successes in $n$ independent trials that are not necessarily identically distributed.

We say that $X$ has the Poisson-binomial distribution with parameters $p_1, p_2, \ldots, p_n$. The binomial is the special case when all the $p_j$'s are equal.

You saw in lab that the number of occupied tables in a Chinese Restaurant process had a Poisson-Binomial distribution. These distributions arise in statistical learning theory, the theory of randomized algorithms, and other areas.

Let $E(X) = \mu$. For $c > 0$, you are going to find an upper bound on $P(X \ge (1+c)\mu)$. That's the chance that $X$ exceeds its mean by some percent. 

In the special case of the binomial, $\mu = np$ and so $P(X \ge (1+c)\mu)$ can be rewritten as $P(\frac{X}{n} - p \ge cp)$. That's the chance that the sample proportion exceeds $p$ by some percent.

(a) Find $\mu = E(X)$ and $\sigma^2 = Var(X)$ in terms of $p_1, p_2, \ldots, p_n$.

(b) Find Markov's bound on $P(X \ge (1+c)\mu)$.

(c) Find Chebyshev's bound on $P(X \ge (1+c)\mu)$ in terms of $\mu$ and $\sigma$.

(d) If all the $p_j$'s are equal to $p$, what is the value of the bound in (c)?

**11: Chernoff Bound on Poisson-Binomial Upper Tail.**
This exercise continues the previous one and uses the same notation.

(a) Show that the mgf of $I_j$ is given by $M_{I_j}(t) = 1 + p_j(e^t - 1)$ for all $t$.

(b) Use (a) to derive an expression for $M_X(t)$, the mgf of $X$ evaluated at $t$.

(c) An useful exponential bound is that $e^x \ge 1 + x$ for all $x$. You don't have to show it but please look at the [graphs](http://prob140.org/resources/exponential_approximations/). Use the fact to show that $M_X(t) \le \exp\big{(}\mu(e^t -1)\big{)}$ for all $t$. Notice that the right hand side is the mgf of a Poisson random variable that has the same mean as $X$.

(d) Use Chernoff's method and the bound in (c) to show that 

$$
P\big{(}X \ge (1+c)\mu\big{)} 
~ \le ~ 
\Big{(} \frac{\exp(c)}{ (1+c)^{1+c}} \Big{)}^\mu
$$

Remember that $\mu = np$ when all the $p_j$'s are equal. If $g(c) = \exp(c)/(1+c)^{1+c}$ is small then the bound above will decrease exponentially as $n$ gets large. That is the focus of the next exercise.

**12: Simplified Chernoff Bounds on Poisson-Binomial Upper Tail.** This exercise continues the previous one and uses the same notation.

The bound in the previous exercise is a bit complicated. Often, simpler versions are used because they are good enough even though they are weaker.

(a) It is not hard to show that $\log(1+c) \ge \frac{2c}{2+c}$ for $c > 0$. You don't have to show it but please look at the [graphs](http://prob140.org/resources/exponential_approximations/).
Use the fact to show that $c - (1+c)\log(1+c) \le -\frac{c^2}{2+c}$ for $c > 0$. 

(b) Show that if $X$ has a Poisson-binomial distribution with mean $\mu$ then

$$
P\big{(} X \ge (1+c)\mu\big{)} ~ \le ~ \exp\big{(}-\frac{c^2}{2+c}\mu\big{)}, ~~~~ c > 0
$$

(c) A simpler but weaker version of the bound in (b) is also often used. Show that

$$
P\big{(} X \ge (1+c)\mu\big{)} ~ \le ~ \exp\big{(}-\frac{c^2}{3}\mu\big{)}, ~~~~ c \in (0, 1)
$$
