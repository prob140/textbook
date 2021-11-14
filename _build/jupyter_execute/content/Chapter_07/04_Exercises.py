#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** Two radioactive substances emit $\alpha$-particles independently of each other. A counter records a Poisson $(5.41)$ number of particles from one substance and a Poisson $(3.87)$ number of particles from the other. Find the chance that the counter records at most four particles.

# **2.** A gambler places two different kinds of bets. All her bets are independent of each other.
# 
# - She has chance $1/n$ of winning the first kind of bet. She decides to place this bet $n$ times.
# - She has chance $1/m$ of winning the second kind of bet. She decides to place this bet $m$ times.
# 
# Suppose $m \ne n$ and assume both $m$ and $n$ are large.
# 
# Let $T$ be the total number of bets the gambler wins. Find or approximate the distribution of $T$. Your answer should be one of the famous distributions along with the appropriate parameters.

# **3.** In the first hour that a bank opens, the customers who enter are of three kinds: those who only require teller service, those who only want to use the ATM, and those who only require special services (neither the tellers nor the ATM). Assume that the numbers of customers of the three kinds are independent of each other and also that:
# 
# - the number that only require teller service has the Poisson (6) distribution,
# - the number that only want to use the ATM has the Poisson (2) distribution, and
# - the number that only require special services has the Poisson (1) distribution.
# 
# Suppose you observe the bank in the first hour that it opens. In each part below, find the chance of the event described.
# 
# (a) 12 customers enter the bank
# 
# (b) more than 12 customers enter the bank
# 
# (c) customers do enter but none requires special services

# **4.** On every page of a book, the number of misprints has the Poisson $(\mu)$ distribution, and misprints on different pages are independent of each other.
# 
# (a) What is the distribution of the number of misprints on the first 20 pages?
# 
# (b) A proof-reader reads the book starting at Page 1. Assume that the proof-reader finds every misprint. What is the chance that he finds the fifth misprint on Page 21?
# 
# (c) I also read the book starting at Page 1. Assume that I notice each misprint with chance $3/4$ independently of all other misprints. What is the chance that I notice at least one misprint on the first 20 pages and also miss at least one misprint on those pages?
# 

# **5.** Let $X_1, X_2, \ldots, X_n$ be i.i.d. Poisson $(\lambda)$ random variables, and let $S_n = X_1 + X_2 + \cdots + X_n$.
# 
# Let $A_n = S_n/n$ be the *sample average*. For a non-negative integer $k$, find $P(A_n \le k)$.
# 

# **6.** Use consecutive odds ratios to find the mode of the Poisson($\mu$) distribution. Be careful about the case where $\mu$ is an integer.

# **7.** Each car that I see has chance 0.2 of being a hybrid and chance 0.1 of being electric, independently of all other cars. 
# 
# (a) Suppose I see $15$ cars. Find the chance that I see 3 hybrid cars, 2 electric cars,
# and 10 cars of other types.
# 
# (b) Suppose the number of cars I see has the Poisson $(15)$ distribution. Find the chance that I see 3 hybrid cars, 2 electric cars,
# and 10 cars of other types.

# **8.** Suppose you have $N$ balls where $N$ has the Poisson $(\lambda)$ distribution. Each ball is thrown into into one of $m$ bins chosen uniformly at random, independent of all other balls. Find $P(\text{there is an empty bin})$.

# In[ ]:




