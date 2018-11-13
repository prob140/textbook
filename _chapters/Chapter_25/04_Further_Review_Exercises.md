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

**13.** 
A positive random variable $V$ has expectation $\mu$ and variance $\sigma^2$. 

(a) For each $v > 0$, the conditional distribution of $X$ given $V=v$ is Poisson $(v)$. Find $E(X)$ and $Var(X)$ in terms of $\mu$ and $\sigma$.

(b) For each $v > 0$, the conditional distribution of $X$ given $V=v$ is gamma $(v, \lambda)$ for some fixed $\lambda$. Find $E(X)$ and $Var(X)$ in terms of $\mu$ and $\sigma$.

**14.**
Let $X_1, X_2, \ldots, X_n$ be i.i.d. with expectation $\mu$ and variance $\sigma^2$. Let $S = \sum_{i=1}^n X_i$.

(a) Find the least squares predictor of $S$ based on $X_1$, and find the mean squared error (MSE) of the predictor.

(b) Find the least squares predictor of $X_1$ based on $S$, and find the MSE of the predictor. Is the predictor a linear function of $S$? If so, it must also be the best among all linear predictors based on $S$, which is commonly known as the regression predictor. 

**15.** 
A $p$-coin is tossed repeatedly. Let $W_{H}$ be the number of tosses till the first head appears, and $W_{HH}$ the number of tosses till two consecutive heads appear.

(a) Describe a random variable $X$ that  depends only on the tosses after $W_H$ and satisfies $W_{HH} = W_H + X$.

(b) Use Part (a) to find $E(W_{HH})$ and $Var(W_{HH})$.

**16.** 
Let $N$ be a non-negative integer valued random variable,
and let $X, X_1, X_2, \ldots $ be i.i.d. and independent of $N$. As before, define
the *random sum* $S$ by

$$
\begin{align*}
S ~~&=~~0~~ \mbox{if}~N=0 \\
&=~~ X_1 + X_2 + \cdots + X_n ~~ \mbox{if}~N = n > 0 
\end{align*}
$$

(a) Let $M$ be our usual notation for moment generating functions.
By conditioning on $N$, show that

$$
M_S(t) ~~=~~ M_N\big{(}\log M_X(t) \big{)}
$$

assuming that all the quantities above are well defined. 
[The identity $(e^a)^n = e^{an}$ might be handy.]

(b) Let $N$ have the geometric $(p)$ distribution on $\{1, 2, 3, \ldots \}$. Find the mgf of $N$. This doesn't use Part (a).

(c) Let $X_1, X_2, \ldots $ be i.i.d. exponential $(\lambda)$ variables and let $N$ be geometric as in Part (b). Use the results of Parts (a) and (b) to identify the distribution of $S$.

**17.**
Let $\mathbf{X}$ be a $p \times 1$ random vector and suppose we are trying to predict a random variable $Y$ by a linear function of $\mathbf{X}$. In an earlier [section](http://prob140.org/textbook/chapters/Chapter_25/02_Best_Linear_Predictor) we identified the least squares linear predictor by restricting our search to linear functions of $X$ that are unbiased for $Y$. Show that this was a legitimate move. 

Specifically, let $\hat{Y}_1 = \mathbf{c}^T \mathbf{X} + d$ be a biased predictor so that $E(\hat{Y}_1) \ne \mu_Y$. Find a non-zero constant $k$ such that $\hat{Y}_2 = \hat{Y}_1 + k$ is unbiased, and show that $MSE(\hat{Y}_1) \ge MSE(\hat{Y}_2)$. This will show that the least squares linear predictor has to be unbiased.
