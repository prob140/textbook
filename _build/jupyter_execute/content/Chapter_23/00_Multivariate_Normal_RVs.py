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


# # Jointly Normal Random Variables #

# Galton's observations about oval scatter plots became the foundation of multiple regression, one of most commonly used methods in data analysis. Inference in multiple regression and its modern variants is often based on *multivariate normal* models. 
# 
# In this chapter we will study what it means for a collection of random variables to be *jointly normally distributed*. We will introduce matrix notation for linear combinations of random variables and then study the main properties of the multivariate normal distribution. This is the necessary groundwork for using multivariate normal models in prediction, which we will do in the next chapter.

# In[2]:




