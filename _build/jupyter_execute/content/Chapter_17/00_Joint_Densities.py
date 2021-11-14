#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')
import math
from scipy import stats


# # Joint Densities #

# We turn now to probability densities on the plane, that is, to joint distributions of two continuous random variables. The methods extend our calculations with densities of single variables, and are analogous to methods involving joint distribution tables in the discrete case.
