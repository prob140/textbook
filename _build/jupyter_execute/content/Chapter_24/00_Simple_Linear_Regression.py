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


# # Simple Linear Regression #

# In data science, regression models are widely used for prediction. This chapter examines linear least squares from a probabilistic perspective. The focus is on *simple* regression, that is, prediction based on one numerical attribute. 
# 
# When the joint distribution of the attribute $X$ and the response $Y$ is bivariate normal, the empirical distribution of $(X, Y)$ has the football shape so familiar from Data 8. We will start with a geometric interpretation of correlation, as that is helpful for understanding both regression and the bivariate normal. The equation of the regression line, which we will derive, can be written in several ways; by the end of the chapter we will have written it in the way that is most easily extended to multiple regression.

# In[2]:




