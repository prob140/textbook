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


# ## Least Squares Predictor ##

# As the function that picks off the "centers of vertical strips," the conditional expectation $b(X) = E(Y \mid X)$ is a natural estimate or predictor of $Y$ given the value of $X$. We will now see how good $b(X)$ is if we use mean squared error as our criterion.

# In[2]:


# VIDEO: Least Squares
from IPython.display import YouTubeVideo

YouTubeVideo('G_3rcPnInc0')


# ### Minimizing the MSE ###
# Let $h(X)$ be any function of $X$, and consider using $h(X)$ to predict $Y$. Define the *mean squared error of the predictor $h(X)$* to be
# 
# $$
# MSE(h) ~ = ~ E\Big{(}\big{(}Y - h(X)\big{)}^2\Big{)}
# $$
# 
# We will show that $b(X)$ is the best predictor of $Y$ based on $X$, in the sense that it minimizes this mean squared error over all functions $h(X)$.
# 
# Recall our notation $D_w = Y - b(X)$. We know that if $g(X)$ is any function of $X$, then $E\big{(}D_wg(X)\big{)} = 0$.
# 
# $$
# \begin{align*}
# MSE(h) ~ &= ~ E\big{(}\big{(}Y - h(X)\big{)}^2\big{)} \\
# &= ~ E\big{(}\big{(} (Y - b(X)) + (b(X) - h(X) \big{)}^2 \big{)} \\
# &= ~ E\big{(} \big{(} D_w + g(X) \big{)}^2 \big{)} ~~~~~ \text{ where } g(X) = b(X) - h(X) \\
# &= ~ E\big{(} D_w^2 \big{)} + E\big{(}\big{(}g(X)\big{)}^2\big{)} + 2E\big{(}D_wg(X)\big{)} \\
# &= ~ E\big{(} D_w^2 \big{)} + E\big{(}\big{(}g(X)\big{)}^2\big{)} \\
# &\ge ~ E\big{(}D_w^2 \big{)} \\
# &= ~ E\big{(}\big{(}Y - b(X)\big{)}^2\big{)} \\
# &= ~ MSE(b)
# \end{align*}
# $$

# ### Best Predictor ###
# The result above shows that the least squares predictor of $Y$ based on $X$ is the conditional expectation $b(X) = E(Y \mid X)$. 
# 
# In terms of the scatter diagram of observed values of $X$ and $Y$, the result is saying that the best predictor of $Y$ given $X$, by the criterion of smallest mean squared error, is the average of the vertical strip at the given value of $X$.

# In[3]:


# VIDEO: Conditional Variance: Definition
YouTubeVideo('J-pCOpndoBI')


# ### Conditional Variance ###
# 
# Calculations "within a vertical strip" are calculations given the value of $X$. For example, to predict $Y$ for a given value of $X$, the least squares predictor is the "center of the vertical strip" $b(X) = E(Y \mid X)$.
# 
# The error in this estimate can be quantified by calculating the "variance in the vertical strip", that is, the mean squared error within the vertical strip. 
# 
# Formally, the mean squared error "within a strip" is defined as the random variable 
# 
# $$
# Var(Y \mid X) ~ = ~ E\big{(} (Y - b(X))^2 \mid X \big{)}
# $$ 
# 
# This random variable is a function of $X$ and is called the *conditional variance of $Y$ given $X$*. Its value at $x$ is $Var(Y \mid X=x)$, that is, the variance of the values of $Y$ in the vertical strip at $x$.
# 
# Let's return to the language of prediction. Given $X$, the mean squared error of the predictor $b(X)$ is the conditional variance $Var(Y \mid X)$. 
# 
# So, given $X$, the *root mean squared error* or rms error is the *SD of the vertical strip*, that is, the conditional SD of $Y$ given $X$:
# 
# $$
# SD(Y \mid X) ~ = ~ \sqrt{Var(Y \mid X)}
# $$
# 
# The value of this random variable measures the variability within the strip at the given value of $X$. 
# 
# A *homoscedastic* scatter diagram is one for which this conditional SD is essentially a constant, that is, if $SD(Y \mid X=x)$ is pretty much the same for all $x$. If not, the scatter is called *heteroscedastic*.

# ### The Value of the MSE ###
# 
# Overall across the entire scatter diagram, the mean squared error of the predictor $b(X)$ is the average of the mean squared errors in the individual strips. This is intuitively clear and can be established by applying iterated expectation to the definition of mean squared error.
# 
# $$
# \begin{align*}
# MSE(b) ~ &= ~ E\big{(}\big{(}Y - b(X)\big{)}^2\big{)} \\
# &= ~ E\Big{(} E\big{(}\big{(}Y - b(X)\big{)}^2\big{)} \mid X \big{)} \Big{)} \\
# &= ~ E\big{(} Var(Y \mid X) \big{)}
# \end{align*}
# $$
# 
# That is, the mean squared error of the least squares predictor is the *expectation of the conditional variance*.

# ### The Shape of the Scatter ###
# Notice that the results in this section make no assumption about the joint distribution of $X$ and $Y$. The scatter diagram of the generated $(X, Y)$ points can have any arbitrary shape.
# 
# So it seems as though the question of prediction has been settled once and for all: if you want the least squares predictor, use conditional expectation. However, the functional form of the conditional expectation of $Y$ given $X$ depends on the joint distribution of $X$ and $Y$ (which also determines the shape of the scatter diagram), and is not always straightforward to find.
# 
# So data scientists also find least squares estimates among smaller classes of estimates, the most common class being the set of linear functions of the given variable. This is called linear regression and is the topic of a later chapter.
