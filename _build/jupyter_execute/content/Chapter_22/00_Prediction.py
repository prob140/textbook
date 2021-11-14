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
from scipy import stats


# # Prediction #

# This chapter is about predicting the value of one variable based on information about another. Our main predictor will be conditional expectation, which we defined earlier but will now examine as a guess for one variable given the value of another. 
# 
# We will define a criterion for comparing predictions, and identify the best predictor using that criterion. In the process we will define a quantity called *conditional variance* and use it to find variance.

# In[2]:




