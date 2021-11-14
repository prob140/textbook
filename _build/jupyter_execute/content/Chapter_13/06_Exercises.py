#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** For random variables $X$ and $Y$, suppose
# 
# - $E(X)=5$ , $Var(X)=2$
# - $E(Y)=-3$ , $Var(Y)=7$
# 
# Let $W=8X-9Y+10$.
# 
# (a) Find $E(W)$ and $Var(W)$ if X and Y are independent.
# 
# (b) Find $E(W)$ and $Var(W)$ if $Cov(X, Y)=-1.5$ .
# 
# (c) If $Cov(X, Y)=-1.5$, find $Cov(X, W)$.

# **2.** Show that if $X$ and $Y$ are independent random variables then $Var(X + Y) = Var(X - Y)$.

# **3.** Show that if $X$ and $Y$ are i.i.d. then $X + Y$ and $X - Y$ are uncorrelated.

# **4.** Find the expectation and SD of
# 
# (a) the number of times red faces appear in 12 rolls of a die that has two red faces and four green faces
# 
# (b) the number of face cards in a 5-card poker hand
# 
# (c) one random draw from the 10 digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9

# **5.** A proportion $p$ of the members of a population have a college degree. Draws are made at random with replacement from this population. Find the expectation and standard deviation of the number of sampled people who have college degrees,
# 
# (a) if the number of draws is a fixed integer $n$
# 
# (b) if the number of draws has the Poisson $(\mu)$ distribution independent the educational levels of the people drawn

# **6.** Dibya is taking a 50-question multiple choice test that has 5 answer choices for each question. He gets 5 points for writing his name on the test, and he earns 2 points for each question he answers correctly. Dibya did not study for the test, so he decides to select an answer choice for each question uniformly at random independently of all other questions. Assuming that he correctly writes his name, find the expectation and variance of the number of points he gets on the test.

# **7.** Consider a sequence of i.i.d. Bernoulli $p$ trials. Fix a positive integer $r$ and let $T_r$ be the number of trials till the $r$th success. 
# 
# (a) Find $E(T_r)$.
# 
# (b) Find $SD(T_r)$. Recall from an earlier exercise set that $SD(T_1) = \frac{\sqrt{q}}{p}$ where $q = 1-p$.
# 
# (c) Find the distribution of $T_r$. This is the *negative binomial* distribution on the possible values of $T_r$.
# 
# [Find $P(T_r = k)$ by thinking about what must happen on the $k$th trial.]

# **8.** Let $X_1$ and $X_2$ be i.i.d. with mean $\mu$ and variance $\sigma^2$. Find a constant $c$ so that $P(\vert X_1 - X_2 \vert < c) \ge 0.99.$

# **9.** Throw $n$ balls into $m$ bins $(m \geq 3)$. Each ball is thrown into a bin chosen uniformly at random, independent of all other balls. For $i$=1,2,3, let $X_i$ be the number of balls in Bin $i$. Find $Cov(X_1, X_2+X_3)$.
# 
# [Hint: You know the distribution of $X_1 + X_2$ and hence also its variance. Use this to find a useful covariance.]

# **10.** A fair die is rolled $n$ times. Let $X$ be the number of ones and $Y$ be the number of twos. Find $Cov(X, Y)$ in the two ways indicated below.
# 
# (a) Express each of $X$ and $Y$ as the sum of indicators and use bilinearity.
# 
# (b) Recognize the distributions of $X$, $Y$, and $X+Y$, and use the formula for the variance of a sum.

# **11.** A fair coin is tossed 300 times. Let $H_{100}$ be the number of heads in the first 100 tosses, and $H_{300}$ the total number of heads in all 300 tosses. Find $Cov(H_{100},H_{300})$.

# **12.** A random variable $X$ has expectation 10 and standard deviation 5.
# 
# (a) Find the best upper bound you can on $P(X\geq 20)$.
# 
# (b) Can $X$ be binomially distributed?

# **13.** A data science class has $2n$ students partnered into $n$ project pairs. On the night that the first project is due, $d$ students among the $2n$ students fall sick from the flu. Assume the $d$ students are selected uniformly at random from all $2n$ students. Let $X$ be the number of project pairs that can’t finish because both members get the flu. Find $E(X)$ and $Var(X)$.

# **14.** Roulette can be played played in multiple independent rounds. On each round, if you bet $x$ dollars on black then with probability $\frac{18}{38}$ you will double that bet (that’s a net gain of $x$ dollars), and with probability $\frac{20}{38}$, you will lose that money.
# 
# (a) Jason hits the streets of Las Vegas with 1000 dollars to play roulette. Since Jason is an experienced Prob 140 TA, he decides to bet only 50 dollars on each round to keep his risk low. Let $J$ be the amount of money Jason has after playing 20 rounds of roulette. Find $E(J)$ and $SD(J)$.
# 
# (b) Dibya hits the streets of Las Vegas with 1000 dollars to play roulette. Since Dibya is a high-roller, he bets 500 dollars on each round. Let $D$ be the amount of money Dibya has after playing two rounds of roulette. Find $E(D)$ and $Var(D)$.

# **15.** Students in a class are comparing their birthdays. Assume that each student has a birthday which is equally likely to be any of 365 days of the year, independent of all other students. Suppose there are $n$ students in the class, and let $X$ be the number of days on which at least one student has a birthday. Find $E(X)$ and $Var(X)$.

# **16.** Out of $n$ individual voters at an election, $r$ vote for party R and $n - r$ vote for party D. At the next election the probability of an R-voter switching to D is $p_1$, and the probability of a D-voter switching to R is $p_2$. Suppose the individuals behave independently of each other. Find the expectation and variance of the number of R-voters at the second election.

# **17.** A standard deck of 52 cards has 4 aces. Cards are dealt at random without replacement until an ace appears. Let $X$ be the number of cards dealt *before* the first ace. For example, if the sequence is Non-ace, Non-ace, Ace, then $X = 2$. If an ace appears on the first draw then $X=0$.
# 
# (a) What is the chance that the 2 of Clubs appears before all the aces?
# 
# [Think how many cards are involved and use symmetry.]
# 
# (b) Use the method of indicators to find $E(X)$. You have found this expectation before in a different way, but writing $X$ as a sum of indicators will help you find the variance in the next part.
# 
# [Think about the largest $X$ can be, and hence work out how many indicators you need and what each one should represent. Part (a) will also be helpful.]
# 
# (c) Use your representation of $X$ as a sum of indicators to find $Var(X)$.

# **18.** In the German tanks problem, the random variables $X_1, X_2, \ldots, X_n$ are a simple random sample of size $n$ drawn from $1, 2, 3, \dots, N$ where $N$ is a fixed but unknown positive integer. We constructed two unbiased estimators of $N$:
# 
# - $T_1 = 2\bar{X}_n - 1$ where $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$
# - $T_2 = M\cdot\frac{n+1}{n} - 1$ where $M = \max(X_1, X_2, \ldots, X_n)$
# 
# (a) Find $Var(T_1)$.
# 
# (b) [Hard] Show that $Var(T_2) = \frac{(N-n)(N+1)}{n(n+2)}$. 
# 
# [Hint: [Recall](http://prob140.org/textbook/content/Chapter_08/04_Additivity.html#second-unbiased-estimator-of-the-maximum-possible-value) that we found $E(M)$ by using the symmetry of the gaps. Suppose you could find the variance of the length of the first gap. justify why no further calculation would be needed to find $Var(M)$. Then find the variance of the length of the first gap by writing it as the sum of indicators.]
# 
# (c) Show that $Var(T_2) \le Var(T_1)$.
