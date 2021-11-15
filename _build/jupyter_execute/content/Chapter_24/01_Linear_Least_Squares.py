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


# ## Least Squares Linear Predictor ##

# In this section we are going to see if we can identify the best among all linear predictors of one numerical variable based on another, regardless of the joint distribution of the two variables.
# 
# For jointly distributed random variables $X$ and $Y$, you know that $E(Y \mid X)$ is the least squares predictor of $Y$ based on functions of $X$. We will now *restrict the allowed functions to linear functions* and see if we can find the best among those. In later sections we will see the connection between this best linear predictor, the best among all predictors, and the bivariate normal distribution.

# In[1]:


# VIDEO: Simple Regression
from IPython.display import YouTubeVideo

YouTubeVideo('p-Dmvjh7MP4')


# ### Minimizing Mean Squared Error ###
# Let $h(X) = aX + b$ for constants $a$ and $b$, and let $MSE(a, b)$ denote $MSE(h)$.
# 
# $$
# MSE(a, b) ~ = ~ E\big{(} (Y - (aX + b))^2 \big{)} 
# $$
# 
# To find the *least squares linear predictor*, we have to minimize this MSE over all $a$ and $b$. We will do this using calculus, in two steps:
# - Fix $a$ and find the value $b_a^*$ that minimizes $MSE(a, b)$ for that fixed value of $a$.
# - Then plug in the minimizing value $b_a^*$ in place of $b$ and minimize $MSE(a, b_a^*)$ with respect to $a$.
# 
# #### Step 1 ####
# Fix $a$ and minimize $MSE(a, b)$ with respect to $b$.
# 
# $$
# \begin{align*}
# MSE(a, b) ~ &= ~ E\big{(} ((Y-aX) - b)^2\big{)}\\
# &= ~ E((Y-aX)^2) -2bE(Y-aX) + b^2
# \end{align*}
# $$
# 
# Differentiate this with respect to $b$.
# 
# $$
# \frac{d}{db} MSE(a, b) ~ = ~ -2E(Y-aX) + 2b
# $$
# 
# Set this equal to 0 and solve to see that the minimizing value of $b$ for the fixed value of $a$ is
# 
# $$
# b_a^* ~ = ~ E(Y-aX) ~ = ~ E(Y) - aE(X)
# $$
# 
# #### Step 2 ####
# Now we have to minimize the following function with respect to $a$:
# 
# $$
# \begin{align*}
# E\big{(} (Y - (aX + b_a^*))^2 \big{)} ~ &= ~
# E\big{(} (Y - (aX + E(Y) - aE(X)))^2 \big{)} \\
# &= ~ E\Big{(} \big{(} (Y - E(Y)) - a(X - E(X))\big{)}^2 \Big{)} \\
# &= ~ E\big{(} (Y - E(Y))^2 \big{)} - 2aE\big{(} (Y - E(Y))(X - E(X)) \big{)} + a^2E\big{(} (X - E(X))^2 \big{)} \\
# &= ~ Var(Y) - 2aCov(X, Y) + a^2Var(X) \\
# \end{align*}
# $$
# 
# The derivative with respect to $a$ is $-2Cov(X, Y) + 2aVar(X)$. Thus the minimizing value of $a$ is
# 
# $$
# a^* ~ = ~ \frac{Cov(X, Y)}{Var(X)} 
# $$
# 
# At this point we should check that what we have is a minimum, not a maximum, but based on your experience with prediction you might just be willing to accept that we have a minimum. If you're not, then differentiate again and look at the sign of the resulting function.

# ### Slope and Intercept of the Regression Line ###
# The least squares straight line is called the *regression line*.You now have a proof of its equation, familiar to you from Data 8. Let $r_{X,Y}$ be the correlation between $X$ and $Y$ and let $\sigma_X$ and $\sigma_Y$ be the standard deviations of $X$ and $Y$ respectively. As you know, $r_{X,Y} = \frac{Cov(X,Y)}{\sigma_X\sigma_Y}$. So the slope and intercept are given by
# 
# $$
# \begin{align*} 
# \text{slope of regression line} ~ &= ~ \frac{Cov(X,Y)}{Var(X)} ~ = ~ r_{X,Y} \frac{\sigma_Y}{\sigma_X} \\ \\
# \text{intercept of regression line} ~ &= ~ E(Y) - \text{slope} \cdot E(X)
# \end{align*}
# $$

# ### Regression in Standard Units ###
# If both $X$ and $Y$ are measured in standard units, then the slope of the regression line is the correlation $r_{X,Y}$ and the intercept is 0. 
# 
# In other words, given that $X = x$ standard units, the predicted value of $Y$ is $r_{X,Y}x$ standard units. When $r_{X,Y}$ is positive but not 1, this result is called the *regression effect*: the predicted value of $Y$ is closer to 0 than the given value of $X$.

# ### The Line and the Joint Distribution ###
# 
# The calculations above show that *regardless of the joint distribution of $X$ and $Y$*, that is, regardless of the relation between $X$ and $Y$,
# 
# - The equation of the regression line holds.
# 
# - The regression line goes through the point $(E(X), E(Y))$.
# 
# - There is a unique best straight line predictor among all straight lines. If the relation between $X$ and $Y$ isn't roughly linear then you won't want to use the best straight line for predictions, because the best straight line is only the best among a bad class of predictors. But it exists.

# ### The Regression Line for Data ###
# 
# In Data 8, the setting for simple linear regression was that we had a deterministic set of points $\{(x_i, y_i): 1 \le i \le n\}$ and we were using a line of the from $y = ax+b$ as our predictor. 
# 
# The equation of the regression line based on the data is a special case of the random variable calculations of this section. The mean squared error of the prediction is easily seen to be equal to $MSE(a, b)$ as defined in this section for a randomly picked point:
# 
# $$
# \frac{1}{n} \sum_{i=1}^n (y_i - (ax_i + b))^2 ~ = ~ \sum_{i=1}^n (y_i - (ax_i + b))^2 \frac{1}{n} ~ = ~ MSE(a, b)
# $$
# 
# for $(X, Y)$ picked uniformly at random from the set $\{(x_i, y_i): 1 \le i \le n\}$. 
# 
# We have already found the minimizing values of $a$ and $b$. The least-squares slope and intercept are
# 
# $$
# \begin{align*}
# b^* ~ &= ~ \frac{Cov(X,Y)}{Var(X)} ~ = ~ r_{X,Y} \frac{\sigma_Y}{\sigma_X} \\
# a^* ~ &= ~ E(Y) - b^*E(X)
# \end{align*}
# $$
# 
# where the quantities on the right are calculated based on the uniform distribution. For example, 
# 
# $$
# E(Y) ~ = ~ \sum_{i=1}^n y_i\cdot\frac{1}{n} ~ = ~ \frac{1}{n}\sum_{i=1}^n y_i ~ = ~ \bar{y}
# $$
# 
# That's the average of the $y$-values. The variance is 
# 
# $$
# \sigma_Y^2 = E((Y - E(Y))^2) = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2
# $$ 
# 
# by plugging in $E(Y) = \bar{y}$ and using the uniform distribution again. So also $\sigma_X^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2$ and
# 
# $$
# Cov(X, Y) = E((X-E(X))(Y-E(Y)) = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
# $$
# 

# In[ ]:




