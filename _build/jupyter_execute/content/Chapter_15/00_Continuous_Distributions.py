#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')


# # Continuous Distributions #

# The normal curve, used by us as an approximation to discrete distributions, can be thought of as a distribution in its own right provided we allow the possible values to be the entire real line. In this chapter we will develop methods for working with random variables whose possible values are an interval of numbers. 
# 
# The interval of possible values might be bounded or unbounded, but even a bounded interval has uncountably many numbers in it. So we will use calculus to find probabilities and expectations. You will see that almost all the results we developed for discrete distributions have continuous analogs. 
# 
# It is worth noting that not all distributions fall neatly into one of the two categories "discrete" and "continuous". Some are a bit of both. We will see examples of such distributions later in the course. For now, we will focus on the continuous case.

# In[2]:




