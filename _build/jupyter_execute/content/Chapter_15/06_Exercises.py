#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** Let $X$ have density given by
# 
# $$f(x) ~ = ~ 
# \begin{cases}
# c(1 - x^2), ~~ -1 < x < 1 \\
# 0 ~~~~~ \text{otherwise}
# \end{cases}$$
# 
# Find
# 
# (a) $c$
# 
# (b) the cdf of $X$
# 
# (c) $P(\vert X \vert > 0.5)$
# 
# (d) $E(X)$
# 
# (e) $SD(X)$

# **2.** A Zoom call starts at 10:00. Suppose I join the call at a time uniformly distributed over the interval 10:00 to 10:05, and you join the call at an independent time normally distributed with mean 10:03 and SD $0.5$ minutes. What is the chance that we both miss the first two minutes of the call?

# **3.** Let $U_1, U_2, \ldots, U_n$ be i.i.d. uniform on the interval $(-1, 1)$. Assume $n$ is large.
# 
# (a) Let $M_n = \min(U_1, U_2, \ldots, U_n)$. For $-1 < x < 1$, find or approximate $P(M_n > x)$.
# 
# (b) Let $A_n = \frac{1}{n}\sum_{i=1}^n U_i$. For $-1 < x < 1$, find or approximate $P(A_n > x)$.

# **4.** In each of Parts (a) and (b), find $P(X > 4E(X))$ if you can. If you can’t, then approximate it if you can, and if you can’t approximate it, then provide the best upper and lower bounds that you can find.
# 
# (a) $X$ is a non-negative random variable
# 
# (b) $X$ has the exponential $(\lambda)$ distribution

# **5.** Let $X$ have the exponential $(\lambda)$ distribution and let $c$ be a positive constant. Let $Y=cX$. Find the survival function of $Y$ and hence identify the distribution of $Y$.

# **6.** For $i = 1, 2, \ldots, n$, let $X_i$ have the exponential $(\lambda_i)$ distribution, and assume that $X_1, X_2, \ldots, X_n$ are independent.
# 
# Let $M = \min(X_1, X_2, \ldots, X_n)$. Find the distribution of $M$. Recognize it as one of the famous ones and provide its name and parameters.

# **7.** For fixed $\alpha > 2$, a random variable $T$ has the *Pareto* distribution with shape parameter $\alpha$ and possible values $(1, \infty)$ if the density of $T$ is given by
# 
# $$f_T(t) ~ = ~ c t^{-(\alpha + 1)}, ~~~ t > 1.$$
# 
# (a) Find $c$.
# 
# (b) Find the cdf of $T$.
# 
# (c) Find $E(T)$.
# 
# (d) Find $Var(T)$.

# **8.** Let $X$ be a random variable describing the relative change of Bitcoin in a year: a $1$ dollar investment in bitcoin will be worth $X$ dollars at the end of the year. Jason buys $100$ dollars worth of bitcoin. Let $Y$ be the profit made on this investment at the end of the year. For example, if $X=0.9$, then the profit is $-10$ dollars, and if $X=1.1$, the profit is $10$ dollars.
# 
# Assume that $X$ has the density, expectation, and variance given below. (This is a *lognormal* distribution, which you will encounter later in the course.)
# 
# $$f_X(x) = \frac{1}{x\sqrt{2\pi}} e^{-\frac{(\ln x)^2}{2}}, ~~ x > 0 ~~~~~~~~~~~E(X) = 1 ~~~~~~~~~~~ Var(X) = e^2-e.$$
# 
# (a) Let $F_X$ be the cdf of $X$ and $F_Y$ the cdf of $Y$. Without doing any integrals, write $F_Y$ in terms of $F_X$.
# 
# (b) Use Part (a) to find $f_Y$, the density of $Y$.
# 
# (c) Without doing any integrals, find $E(Y)$ and $SD(Y)$.

# **9.** Let $X$ have the *bilateral exponential* density given by
# 
# $$f_X(x) ~ = ~  \frac{1}{2}e^{-|x|}, ~~~~ -\infty < x < \infty.$$
# 
# Use what you know about the exponential density to find, *without integration*,
# 
# (a) the cdf of $X$
# 
# (b) $E(X)$
# 
# (c) $Var(X)$

# **10.** Let $T$ have the exponential $(\lambda)$ distribution and let $X$ be the integer part of $T$. Find the distribution of $X$. Identify it as one of the famous ones and find its name and parameters.

# **11.** Let $T$ be a non-negative random variable that has density $f$. For each $t > 0$, let $S(t) = P(T > t)$. Show that $E(T) = \int_0^\infty S(t)dt$.
# 
# [Write $S(t)$ as an integral of $f$, then switch the order of integration.]

# In[ ]:




