#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** A non-negative integer valued random variable $X$ has probability generating function given by $G(s) = 0.4s + 0.3s^3 + 0.3s^5$ for all $s$.
# 
# (a) Find the distribution of $X$.
# 
# (b) Find the probability generating function of $2X$.
# 
# (c) Find the probability generating function of $X+Y$ where $Y$ is independent of $X$ and has the same distribution as $X$.
# 
# (d) Use the result of Part (c) to find the distribution of $X+Y$.

# **2.** My friend and I gamble on rolls of a die. Each time the die is rolled, 
# 
# - my friend gives me a dollar if the number of spots is five or six,
# - I give my friend a dollar if the number of spots is one or two,
# - and no money changes hands if the number of spots is three or four.
# 
# If we play this game $400$ times, approximately what is the chance that my net gain is more than $20$ dollars? 

# **3.** Sketch the rough shape of the distribution of the proportion of heads in $400$ tosses of a coin. Find the numerical values of the expectation and the SD and mark them appropriately on your sketch.

# **4.** Sketch the rough shape of the Poisson $(625)$ distribution and explain your choice. Find the numerical values of the expectation and SD and mark them appropriately on your sketch.

# **5.** Let $A_n$ be the average of an i.i.d. random sample of size $n$ drawn from a population that has mean $100$ and SD $2$.
# 
# (a) What can you say about the value of $P(A_n \text{ is in the interval } 100 \pm 2)$ if $n = 4$?
# 
# (b) What can you say about the value of $P(A_n \text{ is in the interval } 100 \pm 0.2)$ if $n = 400$?

# **6.** In the old days, the SD of the General Math SAT scores remained quite steady at around $100$ points every year while the mean fluctuated. In such a situation, how large should an i.i.d. sample of scores be so that you can be about $95\%$ confident of estimating the population mean score in a particular year correct to within $1$ point?

# **7.** Ages in a large population have an average of $30$ years and a standard deviation of $20$ years. Two people are sampled randomly from the population.
# 
# (a) Could the distribution of ages in the population be roughly normal? Explain.
# 
# (b) Explain why the ages of the two sampled people are essentially independent of each other.
# 
# (c) Find upper and lower bounds for the probability that the ages of the two sampled people differ by at least $60$ years.

# **8.** Use probability theory to show that as $n \to \infty$,
# 
# $$e^{-n} \big{(} 1 + \frac{n}{1!} + \frac{n^2}{2!} + \cdots + \frac{n^n}{n!} \big{)} ~ \to ~ \frac{1}{2}$$
