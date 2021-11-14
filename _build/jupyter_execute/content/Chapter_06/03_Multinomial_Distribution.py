#!/usr/bin/env python
# coding: utf-8

# ## Multinomial Distribution ##

# Bernoulli trials come out in one of two ways. But many trials come out in multiple different ways, all of which we might want to track. A die can land six different ways. A jury member can have one of several different educational levels. In general, an individual might belong to one of several classes.
# 
# The *multinomial distribution* is a joint distribution that extends the binomial to the case where each repeated trial has more than two possible outcomes. Let's look at it first in an example, and then we will define it in general.
# 
# A box contains 2 blue tickets, 5 green tickets, and 3 red tickets. Fifteen draws are made at random with replacement. To find the chance that there are 4 blue, 9 green, and 2 red tickets drawn, we could start by writing all possible sequences of 4 B's, 9 G's, and 2 R's. 
# 
# Each such sequence has chance $0.2^4 0.5^9 0.3^2$, so all we need for completing the probability calculation is the number of sequences we could write.
# 
# - There are $\binom{15}{4}$ ways of choosing places to write the B's.
# - For each of these ways, there are $\binom{11}{9}$ ways of choosing 9 of the remaining 11 places to write the G's.
# - The remaining 2 places get filled with R's.
# 
# So 
# 
# $$
# \begin{align*}
# P(\text{4 blue, 9 green, 2 red}) 
# &= \binom{15}{4} \cdot \binom{11}{9} 0.2^4 0.5^9 0.3^2 \\ \\
# &= \frac{15!}{4!11!} \cdot \frac{11!}{9!2!} 0.2^4 0.5^9 0.3^2 \\ \\
# &= \frac{15!}{4!9!2!} 0.2^4 0.5^9 0.3^2
# \end{align*}
# $$
# 
# Notice how this simply extends the binomial probability formula by including a third category. 
# 
# Analogously, or formally by induction, you can extend the formula to any finite number of categories or classes.

# ### Multinomial Distribution ###
# 
# Fix a positive integer $n$. Suppose we are running $n$ i.i.d. trials where each trial can result in one of $k$ classes. For each $i = 1, 2, \ldots, k$, let the chance of getting Class $i$ on a single trial be $p_i$, so that $\sum_{i=1}^k p_i = 1$.
# 
# For each $i = 1, 2, \ldots , k$, let $N_i$ be the number of trials that result in Class $i$, so that $\sum_{i=1}^k N_i = n$.
# 
# Then the *joint* distribution of $N_1, N_2, \ldots , N_k$ is
# given by
# 
# $$
# P(N_1 = n_1, N_2 = n_2, \ldots , N_k = n_k)
# ~ = ~ \frac{n!}{n_1!n_2! \ldots n_k!}p_1^{n_1}p_2^{n_2} \cdots p_k^{n_k}
# $$
# 
# where $n_i \ge 0$ for $1 \le i \le k$ and $\sum_{i=1}^k n_i = n$. 
# 
# This is called the *multinomial distribution* with parameters $n$ and $p_1, p_2, \ldots, p_k$.
# 
# When there just two classes, then $k = 2$ and the formula reduces to the familiar binomial formula written as the joint distribution of the number of successes and the number of failures:
# 
# $$
# P(N_1 = n_1, N_2 = n_2) = \frac{n!}{n_1!n_2!} p_1^{n_1}p_2^{n_2} ~~ \text{where } p_1+p_2=1 \text{ and }
# n_1+n_2=n
# $$

# ```{admonition} Quick Check
# In a population, 20% of the individuals are in Class A, 50% in Class B, and 30% in Class C. If 20 individuals are drawn at random with replacement, what is the chance that the sample contains 3 individuals in Class A, 13 in Class B, and 4 in Class C? 
# 
# ```

# ```{admonition} Answer
# :class: dropdown
# $ \frac{20!}{3!13!4!}0.2^3 0.5^{13} 0.3^4$
# 
# ```

# ### Binomial Marginals ###
# 
# No matter how many classes there are, the marginal distribution of each $N_i$ is binomial $(n, p_i)$. 
# 
# You don't have to sum terms in the joint distribution to work this out. 
# 
# - $N_i$ is the number of Class $i$ individuals in the sample
# - Each sampled individual is in Class $i$ with probability $p_i$
# - There are $n$ independent draws. 
# 
# That's the binomial setting.

# ### A Roulette Example ###
# 
# A Nevada roulette wheel has 18 red pockets, 18 black pockets, and 2 green pockets. Each time the wheel is spun, all 38 pockets are equally likely to win, independent of all other spins.
# 
# **Question:** If the wheel is spun 10 times, what is the chance that red and black win an equal number of times?
# 
# **Answer:** Let $N_r$ be the number of times red wins, $N_b$ the number of times black wins, and $N_g$ the number of times green wins.
# 
# $$
# \begin{align*}
# P(N_r = N_b) ~ &= ~ \sum_{i=0}^5 P(N_r = i, N_b = i, N_g = 10-2i) \\ \\
# &= ~ \sum_{i=0}^5 \frac{10!}{i!i!(10-2i)!} \big{(}\frac{18}{38}\big{)}^i \big{(}\frac{18}{38}\big{)}^i \big{(}\frac{2}{38}\big{)}^{10-2i}
# \end{align*}
# $$

# In[ ]:




