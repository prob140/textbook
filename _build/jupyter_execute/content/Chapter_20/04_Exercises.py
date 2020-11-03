## Exercises ##

**1.** Let $X_1, X_2, \ldots, X_n$ be i.i.d. Poisson $(\mu)$ random variables. Find the maximum likelihood estimate of $\mu$.

**2.** Let $X_1, X_2, \ldots, X_n$ be i.i.d. uniform on $(0, \theta)$. 

(a) Find the MLE of $\theta$. [Don't leap into a calculation. Sketch a graph of the function you are trying to maximize, and be careful about its domain. You could start with a specific example, such as $n=3$ and observations 1.4, 17.8, and 12.3.]

(b) Is the MLE unbiased? If not, use the MLE to construct an unbiased estimate of $\theta$.

**3.** *Capture-recapture* methods are sometimes used to estimate population sizes. A standard image is that a pond contains $N$ fish for some fixed but unknown $N$, and that $G$ of the $N$ fish have been captured, tagged, and returned alive to the pond. 

In the recapture phase, assume that a simple random sample of $n$ fish is drawn from the $N$ fish in the pond (you might have to use some imagination to believe this assumption). We can observe $X$, the random number of tagged fish in the sample. 

The goal is to use the observation to estimate $N$.

(a) For large $n$, the sample proportion $X/n$ is likely to be close to a constant. Identify the constant and hence construct an estimate of $N$ based on $X$. Later in this exercise you will see how your estimate is related to the MLE of $N$.

(b) For $N \ge n$, find the likelihood $lik(N)$. You can assume $n > G$. 

(c) Find the likelihood ratio $R(N) = \frac{lik(N)}{lik(N-1)}$ for $N > n$. Simplify the answer as much as you can.

(d) Find the maximum likelihood estimate of $N$ by comparing the likelihood ratios and 1. How does the MLE compare with your estimate in (a)?

**4.** A coin that has a uniform $(0, 1)$ probability of landing heads is tossed three times. That is, if $X$ has the uniform distribution on $(0, 1)$, then conditionally given $X=p$, the data are three i.i.d. Bernoulli $(p)$ random variables.

(a) Prove or find the correct chance: The chance that the first toss lands heads is $1/2$.

(b) Prove or find the correct chance: The chance that the second toss lands heads is $1/2$.

(c) Prove or find the correct chance: The chance that all three tosses land heads is $(1/2)^3$.

(d) Prove or disprove: The three tosses are independent of each other.

**5.** A coin lands heads with probability $X$ where the prior density of $X$ is uniform on the interval $(0, 1)$. The coin is tossed 100 times. Formally, for each $p \in (0, 1)$, conditionally given $X=p$ the tosses are 100 i.i.d. Bernoulli $(p)$ random variables.

Suppose there are 81 heads and 19 tails.

(a) Given these data, what is the mode of the posterior distribution of $X$?

(b) Given these data, what is the MAP estimate of the probability of heads?

(c) Given these data, what is the mean of the posterior distribution of $X$?

(d) Given these data, what is the chance that the 101st toss of this coin lands heads?

**6.** Let $X$ have an exponential distribution. In this exercise you will compare two scenarios: one where the rate of the exponential is a constant, and one where the rate is a random variable.

(a) If $X$ has the exponential $(0.5)$ distribution, find the numerical value of $P(X > 4)$.

(b) Now suppose $X$ has the exponential $(Y)$ distribution where $Y$ is a random variable with the gamma $(0.5, 1)$ distribution. That is, for each $y > 0$, let the conditional distribution of $X$ given $Y = y$ be exponential $(y)$. For each statement (i) and (ii), say whether is true or false. If it is true, prove it. If it is false, find the correct numerical value of the quantity involved.

(i) $E(Y) = 0.5$.

(ii) $P(X > 4)$ is equal to the answer in (a).