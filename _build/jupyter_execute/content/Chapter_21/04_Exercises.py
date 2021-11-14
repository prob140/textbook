#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** Show that if $r > 1$ and $s > 1$ then the mode of the beta $(r, s)$ distribution is $(r-1)/(r+s-2)$. Remember to ignore multiplicative constants and take the log before maximizing.

# **2.** A coin lands heads with chance $X$ where $X$ has the beta $(2, 2)$ density. The coin is tossed five times. That is, for every $p \in (0, 1)$, conditionally given $X=p$ the tosses are i.i.d. Bernoulli $(p)$ random variables.
# 
# (a) What is the chance that the first toss lands heads?
# 
# (b) Given that the first toss lands heads, what is the chance that the second toss lands heads?
# 
# (c) Given that four out of the first five tosses land heads, find the posterior distribution and posterior mean of $X$.
# 
# (d) Find the chance that four out of the first five tosses land heads, and compare it with the chance that four out of five tosses of a fair coin land heads.

# **3.** The chance of heads of a random coin is picked according to the beta $(r, s)$ distribution. The coin is tossed repeatedly.
# 
# (a) What is the chance that the first three tosses are heads and the next three tosses are tails?
# 
# (b) Given that the first three tosses are heads and the next three tosses are tails, what is the chance that the seventh toss is a head?
# 
# (c) Given that three out of the first six tosses are heads, what is the chance that the seventh toss is a head? Compare with the answer to (b).

# **4.** Person A creates a coin by picking its chance of heads uniformly on $(0, 1)$. In three tosses of that coin, Person A gets two heads.
# 
# Independently of Person A, Person B creates a coin by picking its chance of heads uniformly on $(0, 1)$. In three tosses of that coin, Person B gets one head.
# 
# (a) Given the data, what is the distribution of the chance of heads of Person A's coin?
# 
# (b) Given the data, what is the distribution of the chance of heads of Person B's coin?
# 
# (c) Given the data, what is the probability that Person A's coin has a higher chance of heads than Person B's coin? You should be able to do this by using beta facts, without any direct integration.
