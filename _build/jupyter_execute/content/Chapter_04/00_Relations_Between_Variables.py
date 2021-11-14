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


# # Relations Between Variables #

# Many questions in data science have at their center a question about the relation between variables. 
# - How can attributes be used to tell whether or not a cell is cancerous?
# - What is the relation between average income and water usage in Californian counties?
# - Do car buyers pay more for good mileage or for rapid acceleration?
# You encountered these and many other such questions in Data 8.
# 
# Probability theory helps us pose and answer precise questions about the relation between random variables. In particular, it helps us understand the conditional behavior of one set of random variables given the values of another set.
# 
# In this chapter we will study multiple random variables defined on the same set of outcomes.

# In[2]:




