---
interact_link: notebooks/Chapter_25/05_Further_Review_Exercises.ipynb
title: '25.5 Further Review Exercises'
permalink: 'chapters/Chapter_25/05_Further_Review_Exercises'
previouschapter:
  url: chapters/Chapter_25/04_Multiple_Regression
  title: '25.4 Multiple Regression'
nextchapter:
  url: 
  title: ''
redirect_from:
  - 'chapters/chapter-25/05-further-review-exercises'
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
*Capture-recapture* methods are sometimes used to estimate population sizes. A standard image is that a pond contains $N$ fish for some fixed but unknown $N$, and that $G$ of the $N$ fish have been captured, tagged, and returned alive to the pond. You can assume that $G/N$ isn't close to 0.

In the recapture phase, assume that a simple random sample of $n$ fish is drawn from the $N$ fish in the pond (you might have to use some imagination to believe this assumption). We can observe $X$, the random number of tagged fish in the sample. 

The goal is to use the observation to estimate $N$.

(a) For large $n$, the sample proportion $X/n$ is likely to be close to a constant. Identify the constant and hence construct an estimate of $N$ based on $X$.

Later in this exercise you will see how your estimate is related to the MLE of $N$.

(b) For $N \ge n$, find the likelihood $lik(N)$. You can assume $n > G$. 

(c) Find the likelihood ratio $R(N) = \frac{lik(N)}{lik(N-1)}$ for $N > n$. Simplify the answer as much as you can.

(d) Find the maximum likelihood estimate of $N$ by comparing the likelihood ratios and 1. How does the MLE compare with your estimate in (a)?

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
A random vector $\mathbf{Y} = [Y_1 ~~ Y_2 ~~ \cdots ~~ Y_n]^T$ has mean vector $\boldsymbol{\mu}$ and covariance matrix $\sigma^2 \mathbf{I}_n$ where $\sigma > 0$ is a number and $\mathbf{I}_n$ is the $n \times n$ identity matrix. 

(a) Pick one option and explain: $Y_1$ and $Y_2$ are

$~~~~~ (i) ~ \text{independent.} ~~~~~~~~ (ii) ~ \text{uncorrelated but might not be independent.} ~~~~~~~~ (iii) ~ \text{not uncorrelated.}$

(b) Pick one option and explain: $Var(Y_1)$ and $Var(Y_2)$ are

$~~~~~ (i) ~ \text{equal.} ~~~~~~~~ (ii) ~ \text{possibly equal, but might not be.} ~~~~~~~~ (iii) ~ \text{not equal.} $

(c) For $m \le n$ let $\mathbf{A}$ be an $m \times n$ matrix of real numbers, and let $\mathbf{b}$ be an $m \times 1$ vector of real numbers. Let $\mathbf{V} = \mathbf{AY} + \mathbf{b}$. Find the mean vector $\boldsymbol{\mu}\_\mathbf{V}$ and covariance matrix $\boldsymbol{\Sigma}\_\mathbf{V}$ of $\mathbf{V}$.

(d) Let $\mathbf{c}$ be an $m \times 1$ vector of real numbers and let $W = \mathbf{c}^T\mathbf{V}$ for $\mathbf{V}$ defined in Part (c). In terms of $\mathbf{c}$, $\boldsymbol{\mu}\_\mathbf{V}$ and $\boldsymbol{\Sigma}\_\mathbf{V}$, find $E(W)$ and $Var(W)$.

**18.** 
Let $[X_1 ~~ X_2 ~~ X_3]^T$ be multivariate normal with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$ given by

$$
\boldsymbol{\mu} ~ = ~
\begin{bmatrix}
\mu \\
\mu \\
\mu
\end{bmatrix}
~~~~~~~~~~~
\boldsymbol{\Sigma} ~ = ~ 
\begin{bmatrix}
\sigma_1^2 & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_2^2 & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_3^2
\end{bmatrix}
$$

Find $P\big{(} (X_1 + X_2)/2 < X_3 + 1 \big{)}$.

**19.**
Let $X$ be standard normal. Construct a random variable $Y$ as follows:

- Toss a fair coin.
- If the coin lands heads, let $Y = X$.
- If the coin lands tails, let $Y = -X$.

(a) Find the cdf of $Y$. 

(b) Find $E(XY)$ by conditioning on the result of the toss.

(c) Are $X$ and $Y$ uncorrelated? 

(d) Are $X$ and $Y$ independent?

(e) Is the joint distribution of $X$ and $Y$ bivariate normal?

**20.**
Let $X$ and $Y$ be standard bivariate normal with correlation $\rho$. Find $E(\max(X, Y))$. The easiest way is to use the fact that for any two numbers $a$ and $b$, $\max(a, b) = (a + b + \vert a - b \vert)/2$. Check the fact first, and then use it.

**21.**
Suppose that $X$ is normal $(\mu_X, \sigma_X^2$), $Y$ is normal $(\mu_Y, \sigma_Y^2)$, and the two random variables are independent. Let $S = X+Y$.

(a) Find the conditional distribution of $X$ given $S=s$.

(b) Find the least squares predictor of $X$ based on $S$ and provide its mean squared error.

(c) Find the least squares linear predictor of $X$ based on $S$ and provide its mean squared error.

**22.**
Let $\mathbf{X}$ be a $p \times 1$ random vector and suppose we are trying to predict a random variable $Y$ by a linear function of $\mathbf{X}$. A [section](http://prob140.org/textbook/chapters/Chapter_25/02_Best_Linear_Predictor) of the textbook identifies the least squares linear predictor by restricting the search to linear functions $h(\mathbf{X})$ for which $E(h(\mathbf{X})) = \mu_Y$. Show that this is a legitimate move. 

Specifically, let $\hat{Y}_1 = \mathbf{c}^T \mathbf{X} + d$ be a linear predictor such that $E(\hat{Y}_1) \ne \mu_Y$. Find a non-zero constant $k$ such that $\hat{Y}_2 = \hat{Y}_1 + k$ satisfies $E(\hat{Y}_2) = \mu_Y$. Then show that $MSE(\hat{Y}_1) \ge MSE(\hat{Y}_2)$. This will show that the least squares linear predictor has to have the same mean as $Y$.

**23.**
Let $U_1, U_2, U_3, \ldots $ be i.i.d. uniform on $(0, 1)$. For $n \ge 1$, let $S_n = \sum_{i=1}^n U_i$. 

Let $f_{S_n}$ be the density of $S_n$. The formula for $f_{S_n}$ is piecewise polynomial on the possible values $(0, n)$. In this problem we will just focus on the density on the interval $(0, 1)$ and discover a nice consequence.

(a) For $0 < x < 1$, find $f_{S_2}(x)$. 

(b) Use Part (a) and the convolution formula to find $f_{S_3}(x)$ for $0 < x < 1$.

(c) Guess a formula for $f_{S_n}(x)$ for $0 < x < 1$ and prove it by induction.

(d) Find $P(S_n < 1)$.

(e) Let $N = \min\{n: S_n > 1\}$. Use Part (d) to find $E(N)$.


**24: Normal Sample Mean and Sample Variance, Part 1.**
Let $X_1, X_2, \ldots, X_n$ be i.i.d. with mean $\mu$ and variance $\sigma^2$. Let

$$
\bar{X} ~ = ~ \frac{1}{n} \sum_{i=1}^n X_i
$$

denote the sample mean and 

$$
S^2 ~=~ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

denote the sample variance as defined earlier in the course.

(a) For $1 \le i \le n$ let $D_i = X_i - \bar{X}$. Find $Cov(D_i, \bar{X})$.

(b) Now assume in addition that $X_1, X_2, \ldots, X_n$ are i.i.d. normal $(\mu, \sigma^2)$. What is the joint distribution of $\bar{X}, D_1, D_2, \ldots, D_{n-1}$? Explain why $D_n$ isn't on the list.

(c) True or false (justify your answer): The sample mean and sample variance of an i.i.d. normal sample are independent of each other.

**25: Normal Sample Mean and Sample Variance, Part 2**

(a) Let $R$ have the chi-squared distribution with $n$ degrees of freedom. What is the mgf of $R$?

(b)
For $R$ as in Part (a), suppose
$R = V + W$ where $V$ and $W$ are independent and $V$ has the chi-squared 
distribution with $m < n$ degrees of freedom. Can you identify the distribution of $W$? Justify your answer.

(c) Let $X_1, X_2, \ldots , X_n$ be any sequence of random variables and let $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$. Let $\alpha$ be
any constant. Prove the *sum of squares decomposition*

$$
\sum_{i=1}^n (X_i - \alpha)^2 ~=~ \sum_{i=1}^n (X_i - \bar{X})^2 ~+~ n(\bar{X} - \alpha)^2
$$

(d) Now let $X_1, X_2, \ldots , X_n$ be i.i.d. normal with mean $\mu$ and variance $\sigma^2 > 0$. Let $S^2$ be the "sample variance" defined by 

$$
S^2 ~=~ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

Find a constant $c$ such that $cS^2$ has a chi-squared distribution. Provide the degrees of freedom.

[Use Parts (b) and (c) as well as the result of the previous exercise.]

**26.**
The heights of a population of mother-daughter pairs have the bivariate normal distribution with equal means of 67 inches, equal SDs of 2 inches, and correlation 0.5.

(a) Of the mothers on the 90th percentile of heights, what proportion have daughters who are taller than the 90th percentile?

(b) In what proportion of mother-daughter pairs are both women taller than average?
