# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline
import math
from scipy import stats

## Independence, Revisited ##

In the Bayesian world, unknown parameters are random variables, not constants. Bayesians describe their degree of uncertainty about an unknown quantity by specifying a probability distribution for that quantity. 

For example, if we are tossing a coin that has an unknown probability of landing heads, we can think of that unknown probability as a random variable with possible values in the unit interval, instead of an unknown but fixed number.

This change of paradigm leads to an entirely different approach to inference, for which we need some technique.

### Conditioning on a Continuous Variable ###
Let's take a moment for a general discussion about conditioning on a continuous variable. Our observations will parallel discussions in an earlier chapter where we found conditional densities.

Suppose $X$ is a random variable and $A$ is an event that depends on $X$.

If $X$ is a *discrete* random variable, then for any possible value $x$ of $X$ the quantity $P(A \mid X = x)$ has a clear definition by the division rule:

$$
P(A \mid X = x) ~ = ~ \frac{P(A, X = x)}{P(X = x)}
$$

When $X$ has a *density*, the denominator is 0. In this case there is one main idea to keep in mind:

- $P(A \mid X \in dx)$ is essentially constant regardless of exactly where the infinitesimal interval $dx$ is placed relative to $x$. This constant value will be denoted $P(A \mid X = x)$.

So for continuous $X$, we will define

$$
P(A \mid X = x) ~ = ~ P(A \mid X \in dx) ~ \sim ~ \frac{P(A, X \in dx)}{P(X \in dx)} 
$$

We are assuming that the limit of the right hand side as $dx$ goes to 0 exists and doesn't depend exactly how $dx$ is defined: around $x$, or to the left of $x$, or to the right, and so on. This will be true under regularity conditions. You can just assume it works.

We can now talk about tossing a coin that has a random probability of landing heads. 

Suppose a coin lands heads with probability $X$ where $X$ has density $f_X$ on the unit interval. This means that *conditionally given X=p*, the tosses are i.i.d. Bernoulli $(p)$ random variables.

A good mental image is of picking a value of $p$ according to the density $f_X$, then repeatedly tossing a coin that lands heads with that given probability $p$. Keep in mind that $p$ is chosen once, and then the same coin is tossed repeatedly.

- Let $A_{1,1}$ be the event that the first toss lands heads. Then by our definition, $P(A_{1,1} \mid X = p) = p$. Notice that this is the *conditional* chance of $A_{1,1}$ given the observed value of the random probability. It is not the unconditional chance of heads. That requires a calculation that we will do shortly.
- Let $A_{2, 2}$ be the event that the first two tosses land heads. Then $P(A_{2,2} \mid X = p) = p^2$.
- In general, let $A_{k, n}$ be the event that $k$ out of the the first $n$ tosses land heads. Then $P(A_{k, n} \mid X = p) = \binom{n}{k}p^k(1-p)^{n-k}$. 

Our familiar binomial probabilities are now conditional probabilities given the chance of heads.

We can find the unconditional probabilities as weighted averages of these conditional probabilities, as follows.

### Average Conditional Probabilities ###
Let $X$ have density $f_X$ and let $A$ be an event. Then

$$
P(A, X \in dx) ~ = ~ P(X \in dx)P(A \mid X = x) ~ \sim ~ f_X(x)dxP(A \mid X = x)
$$

So

$$
P(A) ~ = ~ \int_{\text{all x}} P(A, X \in dx) ~ = ~ \int_{\text{all x}} P(A \mid X = x)f_X(x)dx
$$

In more compact notation, $P(A) = E(P(A \mid X))$. This is an example of finding expectation by conditioning.

### Example: One Toss of a Random Coin ###

Let $X$ have any density on the unit interval $(0, 1)$. Think of the value of $X$ as the the probability that a coin lands heads. Toss the coin once. Recall that our definition of "given $X=p$" means that

$$
P(\text{coin lands heads} \mid X = p) = p
$$

Let $X$ have density $f_X$. Then

$$
P(\text{coin lands heads}) ~ = ~ \int_0^1 p \cdot f_X(p)dp ~ = ~ E(X)
$$

Thus if $X$ is uniform on $(0, 1)$, then the chance that the coin lands heads is $1/2$. If $X$ has the beta $(r, s)$ distribution then the chance that the coin lands heads is $r/(r+s)$.

### Example: Two Tosses of a Random Coin ###

Let $X$ be uniform on $(0, 1)$. Given $X = p$, toss a $p$-coin twice and observe the results of the tosses. 

We have just observed that $P(\text{first toss is a head}) = 1/2$. The first toss behaves like the toss of a fair coin. The same calculation shows that the chance that the second toss is a head (based on no knowledge of the first toss) is also $1/2$.

Now let's figure out the chance that both the tosses land heads. We know that $P(\text{both tosses are heads} \mid X = p) = p^2$. So

$$
P(\text{both tosses are heads}) ~ = ~ \int_0^1 p^2 \cdot 1dp ~ = ~ \frac{1}{3}
$$

That's *greater than* $1/4$ which is the chance of two heads given that you are tossing a fair coin twice. **The results of the two tosses are not independent.**

Let's see what's going on here. We know that

$$
\begin{align*}
P(\text{both tosses are heads}) ~ &= ~ P(\text{first toss is a head})
P(\text{second toss is a head} \mid \text{first toss is a head}) \\
&= ~ \frac{1}{2} P(\text{second toss is a head} \mid \text{first toss is a head})
\end{align*}
$$

Therefore

$$
P(\text{second toss is a head} \mid \text{first toss is a head}) ~ = ~ \frac{2}{3} ~ > ~ \frac{1}{2}
$$

Knowing that the first toss is a head is telling us something about $X$. Our updated opinion about $X$ is no longer uniform: we now lean towards higher values of $X$, which is then reflected is the chance that the second toss is also a head. We will quantify this in the next section.