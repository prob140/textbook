#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
import warnings
warnings.filterwarnings('ignore')
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats


# ## Poissonizing the Multinomial ##

# This is just an extension of Poissonizing the binomial.
# 
# Suppose you have a sequence of i.i.d. multinomial trials. For example, suppose you are drawing at random with replacement from a population that has $k$ classes of indviduals in proportions $p_1, p_2, \ldots, p_k$.
# 
# If you draw a fixed number of times $n$, then the joint distribution of the counts of the classes in the sample is multinomial with parameter $n, p_1, p_2, \ldots, p_k$. For each fixed $i$, the distribution of the count in Class $i$ is binomial $(n, p_i)$.
# 
# If you replace the fixed number $n$ of trials by a Poisson $(\mu)$ random number of trials, then the multinomial gets Poissonized as follows:
# 
# - For each $i = 1, 2, \ldots , k$, the distribution of $N_i$ is Poisson $(\mu p_i)$.
# - The counts $N_1, N_2, \ldots , N_k$ in the $k$ different categories are mutually independent.
# 
# We won't go through the proof which is a straightforward extension of the proof in the case $k=2$ given in an earlier section. Rather, we will look at why the result matters.
# 
# When the number of trials is fixed, $N_1, N_2, \ldots , N_k$ are all dependent on each other in complicated ways according to the multinomial distribution. But when you let the sample size be a Poisson random variable, then the independence of the counts $N_1, N_2, \ldots , N_k$ lets you quickly calculate the chance of any particular configuration of classes in the sample.

# For example, suppose that in your population the distribution of classes is as follows:
# 
# - Class 1: 20%
# - Class 2: 30%
# - Class 3: 50%
# 
# Now suppose you draw $N$ independent times where $N$ has the Poisson $(20)$ distribution. Then in the sample,
# 
# - the number of Class A individuals has the Poisson distribution with parameter $20$% of $20$, that is Poisson $(4)$,
# - the number of Class B individuals has the Poisson $(6)$ distribution,
# - the number of Class C indidviduals has the Poisson $(10)$ distribution,
# - and these three counts are independent.
# 
# Note that the Poisson parameters of the three Class counts must add up to the original Poisson parameter of the distribution of $N$. The independence makes it easy to find the chance of any specified configuration of the three classes in the sample: just multiply the three individual Poisson probabilities. 
# 
# For example, the chance that you will get at least 3 individuals in Class A, at least 5 in Class B, and at least 8 in Class C is about 42.5%.

# In[3]:


(1 - stats.poisson.cdf(2, 4))*(1-stats.poisson.cdf(4, 6))*(1-stats.poisson.cdf(7, 10))


# The number of factors in the answer is equal to the number of classes, unlike the inclusion-exclusion formula in which the amount of work increases much more with each additional class, as you have seen in exercises.

# ```{admonition} Quick Check
# Suppose I roll a Poisson $(18)$ number of dice. What is the chance that each face appears at most twice?
# 
# ```

# ```{admonition} Answer
# :class: dropdown
# $\big{(} \sum_{k=0}^2 e^{-3}\frac{3^k}{k!} \big{)}^6$ 
# 
# ```

# Poissonization helps data scientists tackle questions like, "How many times must I sample so that my chance of seeing at least one individual of each class exceeds a given threshold?" The answer depends on the distribution of classes in the population, of course, but allowing the sample size be a Poisson random variable can make calculations much more tractable. For applications, see for example the Abstract and References of this [paper](http://people.csail.mit.edu/jayadev/papers/psn_unv_cmp.pdf).

# In[ ]:




