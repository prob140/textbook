#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')


# # Multiple Regression #

# The most common use of regression is to predict the value of a numerical variable based on the values of several other variables. In our probabilistic setting, we have a finite number of jointly distributed random variables and the goal is to predict one of them based on all the others. 
# 
# In the previous chapters we did this in the case where there was just one predcitor variable. In particular, we developed the theory of simple linear regression.
# 
# In this chapter we will extend our calculations for simple regression to the case of multiple regression. Indeed, we will capitalize on our work on simple regression to make an inspired guess for how multiple regression must work. Then we will check that our guess is correct.

# In[2]:




