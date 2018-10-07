---
interact_link: notebooks/Chapter_15/06_Review_Problems_Set_3.ipynb
title: '15.6 Review Problems: Set 3'
permalink: 'chapters/Chapter_15/06_Review_Problems_Set_3'
previouschapter:
  url: chapters/Chapter_15/05_Calculus_in_SymPy
  title: '15.5 Calculus in SymPy'
nextchapter:
  url: chapters/Chapter_16/00_Transformations
  title: 'Chapter 16: Transformations'
redirect_from:
  - 'chapters/chapter-15/06-review-problems-set-3'
---

## Review Problems: Set 3

These problems can be solved using the main ideas of Chapters 12 through 15. The Basics set will remind you of the fundamental concepts and some typical calculations. The rest are for you to further develop your problem solving skills and your fluency with the notation and ideas.

### The Basics

**1**. 
Let $X$ have the distribution given by

|$~~~~~~~~~~~~~~~~~~~~~~~~~x$|1|2|3|
|---:|---:|---:|---:|
|$P(X=x)$| 0.2 | 0.5 | 0.3 |

Find $E(X)$ and $SD(X)$.

**2.**
For random variables $X$ and $Y$, suppose

- $E(X) = 5$, $Var(X) = 2$
- $E(Y) = -3$, $Var(Y) = 7$

Let $W = 8X - 9Y + 10$.

(a) Find $E(W)$ and $Var(W)$ if $X$ and $Y$ are independent.

(b) Find $E(W)$ and $Var(W)$ if $Cov(X, Y) = -1.5$.

(c) If $Cov(X, Y) = -1.5$, find $Cov(X, W)$.

**3.**
Show that if $X$ and $Y$ are independent random variables then $Var(X + Y) = Var(X - Y)$.

**4.**
Show that if $X$ and $Y$ are i.i.d. then $X+Y$ and $X-Y$ are uncorrelated.

**5.**
Let $X$ have density given by 

$$
f(x) ~ = ~ 
\begin{cases}
c(1 - x^2), ~~ -1 < x < 1 \\
0 ~~~~~ \text{otherwise}
\end{cases}
$$

Find

(a) $c$

(b) the cdf of $X$

(c) $P(\vert X \vert > 0.5)$

(d) $E(X)$

(e) $SD(X)$

**6.** 
Measurements on the weight of an object are believed to be independent and
identically distributed. Each measurement has mean 12 grams and SD 1.1 gram. Approximately what is the chance that the average of 100 measurements is between 11.8 grams and 12.2 grams? 

**7.**
Find the expectation and SD of

(a) the number of times red faces appear in 12 rolls of a die that has two red faces and four green faces

(b) the number of face cards in a 5-card poker hand

(c) one random draw from the 10 digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9

**8.**
In each of Parts **a** and **b**, find $P(X > 4E(X))$ if you can. If you can't, then approximate it if you can, and if you can't approximate it, then provide the best upper and lower bounds that you can find.

(a) $X$ is a non-negative random variable

(b) $X$ has the exponential $(\lambda)$ distribution

**9.**
Let $A_n$ be the average of an i.i.d. random sample of size $n$ drawn from a population that has mean 100 and SD 2.

(a) What can you say about the value of $P(X \text{ is in the interval } 100 \pm 2)$ if $n = 4$?

(b) What can you say about the value of $P(X \text{ is in the interval } 100 \pm 0.2)$ if $n = 400$?

**10.**
Let $X$ have the exponential $(\lambda)$ distribution and let $c$ be a positive constant. Let $Y = cX$. Find the survival function of $Y$ and hence identify the distribution of $Y$.

### Additional Practice

**11.**
Let $p \in (0, 1)$ and let $X$ be the number of spots showing on a flattened die that shows its six faces according to the following chances:

- $P(X = 1) = P(X = 6)$
- $P(X = 2) = P(X = 3) = P(X = 4) = P(X = 5)$
- $P(X = 1 \text{ or } 6) = p$

Find $SD(X)$ and explain why it is an increasing function of $p$. Compare your answer with the answer you got for the mean absolute deviation in Review Set 2.

**12.**
A random variable $Y$ has expectation 20 and SD 2. Find the best upper and lower bounds you can on $P(15 < X < 30)$.

**13.** 
For $i = 1, 2, \ldots, n$, let $X_i$ have the exponential $(\lambda_i)$ distribution, and assume that $X_1, X_2, \ldots, X_n$ are independent.

Let $M = \min(X_1, X_2, \ldots, X_n)$. Find the distribution of $M$. Recognize it as one of the famous ones and provide its name and parameters.

**14.**
Let $X_1$ and $X_2$ be i.i.d. with mean $\mu$ and variance $\sigma^2$. Find a constant $c$ so that $P(\vert X_1 - X_2 \vert < c) \ge 0.99.$

**15.**
Throw $n$ balls into $m$ bins ($m \geq 3$). Each ball is thrown into a bin chosen uniformly at random, independent of all other balls.  For $i = 1, 2, 3$, let $X_i$ be the number of balls in Bin $i$. Find $Cov(X_1, X_2 + X_3)$ .

**16.**
A fair coin is tossed 300 times. Let $H_{100}$ be the number of heads in the first 100 tosses, and $H_{300}$ the total number of heads in all 300 tosses. Find $Cov(H_{100},H_{300})$. 

**17.**
A fair die is rolled $n$ times. Let $X$ be the number of ones and $Y$ be the number of twos. Find $Cov(X, Y)$ in the two ways indicated below.

(a) Express each of $X$ and $Y$ as the sum of indicators and use bilinearity.

(b) Recognize the distributions of $X$, $Y$, and $X+Y$, and use the formula for the variance of a sum.

**18.**
A random variable $X$ has expectation 10 and standard deviation 5.

(a) Find the best upper bound you can on $P(X\geq 20)$.

(b) Can $X$ be binomially distributed?

**19.**
Dibya is taking a 50-question multiple choice test that has 5 answer choices for each question. He gets 5 points for writing his name on the test, and he earns 2 points for each question he answers correctly. Dibya did not study for the test, so he decides to select an answer choice for each question uniformly at random independently of all other questions. Assuming that he correctly writes his name, find the expecation and variance of the number of points he gets on the test.

**20.**
Jason is taking a 50-question multiple choice test that has 4 answer choices for each question. He earns 2 points for each question he answers correctly. Jason studied for only half an hour before the test, so he correctly answers the first 10 questions before getting thoroughly stumped on the rest of the questions. For each question thereafter, Jason decides to select an answer choice for each question uniformly at random independently of all other questions. Let $J$ be the number of points that Jason receives on the test. Find $E(J)$ and $Var(J)$.

**21.**
Ages in a population have an average of 30 years and a standard deviation of 20 years. Two people are sampled randomly from the population. 

**(a)** Could the distribution of ages in the population be roughly normal? Explain.

**(b)** Explain why the ages of the two sampled people are essentially independent of each other.

**(c)** Find upper and lower bounds for the probability that the ages of the two sampled people differ by at least 60 years.

**22.**
For fixed $\alpha > 2$, a random variable $T$ has the *Pareto* distribution with shape parameter $\alpha$ and possible values $(1, \infty)$ if the density of $T$ is given by

$$
f_T(t) ~ = ~ c t^{-(\alpha + 1)}, ~~~ t > 1
$$

The Pareto family of distributions has applications in numerous fields, for example in economics.

(a) Find $c$.

(b) Find the cdf of $T$.

(c) Find $E(T)$.

(d) Find $Var(T)$.

**23.**
A data science class has $2n$ students partnered into $n$ project pairs. On the night that the first project is due, $d$ students among the $2n$ students fall sick from the flu. Assume the $d$ students are selected uniformly at random from all $2n$ students. Let $X$ be the number of project pairs that can't finish because both members are get the flu. Find $E(X)$ and $Var(X)$.

**24.**
Jason hits the streets of Las Vegas with 1000 dollars to play roulette. Roulette is a game consisting of multiple independent rounds. On each round, Jason bets $x$ dollars on black: with probability $\frac{18}{38}$, he will double that bet (that's a net gain of $x$ dollars), and with probability $\frac{20}{38}$, he will lose that money. Since Jason is an experienced Prob 140 TA, he decides to bet only 50 dollars on each round to keep his risk low. Let $J$ be the amount of money Jason has after playing 20 rounds of roulette. Find $E(J)$ and $Var(J)$.

**25.**
Dibya hits the streets of Las Vegas with 1000 dollars to play roulette. Roulette is a game consisting of multiple independent rounds. On each round, Dibya bets $x$ dollars on black: with probability $\frac{18}{38}$, he will double that bet (that's a net gain of $x$ dollars), and with probability $\frac{20}{38}$, he will lose that money. Since Dibya is a high-roller, he bets 500 dollars on each round. Let $D$ be the amount of money Dibya has after playing two rounds of roulette. Find $E(D)$ and $Var(D)$.

**26.**
Students in a class are comparing their birthdays to one another. Assume that each student has a birthday which is equally likely to be any of 365 days of the year, independent of all other students. Let $X$ be the number of days on which at least one student has a birthday. If there are $n$ students in the class, find $E(X)$ and $Var(X)$.

**27.**
Out of $n$ individual voters at an election, $r$ vote for party R and $n - r$ vote for party D. At the next election the probability of an R-voter switching to D is $p_1$, and the probability of a D-voter switching to R is $p_2$. Suppose the individuals behave independently of each other. Find the expectation and variance of the number of R-voters at the second election.

**28.**
Let $X$ be a random variable describing the relative change of Bitcoin in a year: a $1$ dollar investment in bitcoin will be worth $X$ dollars at the end of the year. Jason buys $100$ dollars worth of bitcoin. Let $Y$ be the profit made on this investment at the end of the year. For example, if $X=0.9$, then the profit is $-10$ dollars, and if $X=1.1$, the profit is $10$ dollars.

Assume that $X$ has the density, expectation, and variance given below. (This is a *lognormal* distribution, which you will encounter later in the course.)

$$
f_X(x) = \frac{1}{x\sqrt{2\pi}} e^{-\frac{(\ln x)^2}{2}}, ~~ x > 0 ~~~~~~~~~~~E(X) = 1 ~~~~~~~~~~~ Var(X) = e^2-e
$$


(a) Let $F_X$ be the cdf of $X$ and $F_Y$ the cdf of $Y$. Without doing any integrals, write $F_Y$ in terms of $F_X$.

(b) Use Part **a** to find $f_Y$, the density of $Y$.

(c) Without doing any integrals, find $E(Y)$ and $SD(Y)$.

**29.**
A building has $n+1$ floors: a ground floor $G$ and floors $1, 2, \ldots, n$. One morning, $m$ people enter the elevator on the ground floor. Each person gets out on one of the $n$ floors above the ground floor, selected uniformly at random, independent of all other people. The elevator doesn't stop at any other floors. Let $X$ be the number of floors at which the elevator stops. Find $E(X)$ and $Var(X)$.

**30.**
Suppose a sock drawer has $m$ distinguishable pairs of socks, but a prankster chooses $d$ of these $2m$ socks at random, and pokes holes in them.  Let $X$ be the number of undamaged pairs of socks. Find $E(X)$ and $Var(X)$. 

**31.**
Let $X$ have the *bilateral exponential* density given by

$$
f_X(x) ~ = ~  \frac{1}{2}e^{-|x|}, ~~~~ -\infty < x < \infty
$$

Use what you know about the exponential density to find, *without integration*,

(a) the cdf of $X$

(b) $E(X)$

(c) $Var(X)$

**32.** 
Use probability theory to show that as $n \to \infty$,

$$
e^{-n} \big{(} 1 + \frac{n}{1!} + \frac{n^2}{2!} + \cdots + \frac{n^n}{n!} \big{)} ~ \to ~ \frac{1}{2}
$$
