#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats


# ## Best Linear Predictor ##

# Let $Y$ and the $p \times 1$ vector $\mathbf{X}$ be jointly distributed, and suppose you are trying to predict $Y$ based on a linear function of $\mathbf{X}$. For the predictor
# 
# $$
# \hat{Y}_{\mathbf{c}, d} ~ = \mathbf{c}^T\mathbf{X} + d
# $$
# 
# the mean squared error of prediction is
# 
# $$
# MSE(\hat{Y}_{\mathbf{c}, d}) ~ = ~ E\big{(} (Y - \hat{Y}_{\mathbf{c}, d})^2 \big{)}
# $$
# 
# In this section we will identify the linear predictor that minimizes the mean squared error. We will also find the variance of the error made by this best predictor.

# ### A Linear Predictor ###
# In the case of simple regression, we found the best linear predictor by using calculus to minimize the mean squared error over all slopes and intercepts. We could do the multivariable version of that calculation here. But because of the work we did in the case of one predictor, we will take a different approach. 
# 
# We will guess the answer based on the answer in the case of simple regression, and then establish that our guess is correct.
# 
# In the case of simple regression, we wrote the regression equation in the form
# 
# $$
# \hat{Y} ~ = ~ \sigma_{Y,X}(\sigma_X^2)^{-1}(X - \mu_X) + \mu_Y
# $$
# 
# Now define
# 
# $$
# \hat{Y}_\mathbf{b} ~ = ~ \boldsymbol{\Sigma}_{Y, \mathbf{X}}\boldsymbol{\Sigma}_\mathbf{X}^{-1} (\mathbf{X} - \boldsymbol{\mu}_\mathbf{X}) + \mu_Y
# ~ = ~ \mathbf{b}^T(\mathbf{X} - \boldsymbol{\mu}_\mathbf{X}) + \mu_Y
# $$
# 
# where
# 
# $$
# \mathbf{b} ~ = ~ \boldsymbol{\Sigma}_\mathbf{X}^{-1} \boldsymbol{\Sigma}_{\mathbf{X}, Y}
# $$
# 
# is the $p \times 1$ vector of the coefficients of the linear function.
# 
# Clearly $\hat{Y}_\mathbf{b}$ is a linear predictor of $Y$ based on $\mathbf{X}$. We will show that it is the least squares linear predictor. The steps will follow those that we used to show that conditional expectation is the least squares predictor among all predictors.

# ### Projection ###
# Notice that $E(\hat{Y}_\mathbf{b}) ~ = ~ \mu_Y$. The predictor has the same mean as the variable being predicted.
# 
# Define the error in the prediction to be
# 
# $$
# W ~ = ~ Y - \hat{Y}_\mathbf{b}
# $$
# 
# Then
# 
# $$
# E(W) ~ = ~ 0
# $$
# 
# We will now show that $W$ is uncorrelated with all linear combinations of elements of $\mathbf{X}$.
# 
# $$
# \begin{align*}
# Cov(W, \mathbf{a}^T\mathbf{X}) ~ &= ~ Cov(Y - \hat{Y}_\mathbf{b}, \mathbf{a}^T\mathbf{X}) \\
# &= ~ Cov(Y, \mathbf{a}^T\mathbf{X}) - Cov(\hat{Y}_\mathbf{b}, \mathbf{a}^T\mathbf{X}) \\
# &= ~ Cov(Y, \mathbf{a}^T\mathbf{X}) - Cov(\mathbf{b}^T\mathbf{X}, \mathbf{a}^T\mathbf{X}) \\
# &= ~ \mathbf{a}^T\boldsymbol{\Sigma}_{\mathbf{X}, Y} - \mathbf{a}^T\boldsymbol{\Sigma}_\mathbf{X} \mathbf{b} \\
# &= ~ \mathbf{a}^T\boldsymbol{\Sigma}_{\mathbf{X}, Y} - \mathbf{a}^T\boldsymbol{\Sigma}_\mathbf{X} \boldsymbol{\Sigma}_\mathbf{X}^{-1}\boldsymbol{\Sigma}_{\mathbf{X}, Y} \\
# &= ~ 0
# \end{align*}
# $$
# 
# Because $E(W) = 0$, we also have $E(W\mathbf{a}^T\mathbf{X}) = Cov(W, \mathbf{a}^T\mathbf{X}) = 0$ for all $\mathbf{a}$.

# ### Least Squares ###
# To show that $\hat{Y}_\mathbf{b}$ minimizes the mean squared error, start with an exercise: show that the best linear predictor must have the same mean as the variable being predicted. That is, show that the best linear predictor must have mean $\mu_Y$. 
# 
# Once you have done that, you can restrict the search for the best linear predictor to all unbiased linear predictors. Define the generic one of these by
# 
# $$
# \hat{Y}_\mathbf{h} ~ = ~ \mathbf{h}^T(\mathbf{X} - \boldsymbol{\mu}_\mathbf{X}) + \mu_Y
# $$
# 
# where $\mathbf{h}$ is some $p \times 1$ vector of coefficients. Then
# 
# $$
# \begin{align*}
# MSE(\hat{Y}_\mathbf{h}) ~ &= ~ E\big{(} (Y - \hat{Y}_\mathbf{h})^2 \big{)}\\
# &= ~ E\big{(} \big{(} (Y - \hat{Y}_\mathbf{b}) + (\hat{Y}_\mathbf{b} - \hat{Y}_\mathbf{h}) \big{)}^2 \big{)} \\
# &= ~ E\big{(} (Y - \hat{Y}_\mathbf{b})^2 \big{)} + E\big{(} (\hat{Y}_\mathbf{b} - \hat{Y}_\mathbf{h})^2 \big{)} + 2E\big{(}(Y - \hat{Y}_\mathbf{b})(\hat{Y}_\mathbf{b} - \hat{Y}_\mathbf{h})\big{)} \\
# &= ~ MSE(\hat{Y}_\mathbf{b}) + E\big{(} (\hat{Y}_\mathbf{b} - \hat{Y}_\mathbf{h})^2 \big{)} + 2E\big{(} W(\mathbf{b} - \mathbf{h})^T(\mathbf{X} - \boldsymbol{\mu}_\mathbf{X}) \big{)} \\
# &= ~ MSE(\hat{Y}_\mathbf{b}) + E\big{(} (\hat{Y}_\mathbf{b} - \hat{Y}_\mathbf{h})^2 \big{)} \\
# &\ge ~ MSE(\hat{Y}_\mathbf{b})
# \end{align*}
# $$

# ### Regression Equation and Predicted Values ###
# The least squares linear predictor is given by
# 
# $$
# \hat{Y} ~ = ~ \mathbf{b}^T(\mathbf{X} - \boldsymbol{\mu}_\mathbf{X}) + \mu_Y ~ = ~ \boldsymbol{\Sigma}_{Y, \mathbf{X}}\boldsymbol{\Sigma}_\mathbf{X}^{-1} (\mathbf{X} - \boldsymbol{\mu}_\mathbf{X}) + \mu_Y
# $$
# 
# This is the same as $\hat{Y}_\mathbf{b}$. We are just dropping the subscript for convenience, now that we have established that it is the best linear predictor.
# 
# As we have seen above, the predictor is unbiased:
# 
# $$
# E(\hat{Y}) ~ = ~ E(Y)
# $$
# 
# The variance of the predicted values is
# 
# $$
# \begin{align*}
# Var(\hat{Y}) ~ &= ~ \mathbf{b}^T \boldsymbol{\Sigma}_\mathbf{X} \mathbf{b} \\
# &= ~ \boldsymbol{\Sigma}_{Y, \mathbf{X}}\boldsymbol{\Sigma}_\mathbf{X}^{-1} \boldsymbol{\Sigma}_\mathbf{X} \boldsymbol{\Sigma}_\mathbf{X}^{-1} \boldsymbol{\Sigma}_{\mathbf{X}, Y} \\
# &= ~ \boldsymbol{\Sigma}_{Y, \mathbf{X}}\boldsymbol{\Sigma}_\mathbf{X}^{-1} \boldsymbol{\Sigma}_{\mathbf{X}, Y}
# \end{align*}
# $$

# ### Error Variance ###
# The error in the prediction is $W = Y - \hat{Y}$. Because $\hat{Y}$ is a linear function of $\mathbf{X}$, we have
# 
# $$
# 0 ~ = ~ Cov(W, \hat{Y}) ~ = ~ Cov(Y - \hat{Y}, \hat{Y}) ~ = ~ Cov(Y, \hat{Y}) - Var(\hat{Y})
# $$
# 
# Therefore
# 
# $$
# Cov(Y, \hat{Y}) ~ = ~ Var(\hat{Y})
# $$
# 
# The variance of the error is
# 
# $$
# \begin{align*}
# Var(W) ~ &= ~ Cov(Y - \hat{Y}, Y - \hat{Y}) \\
# &= ~ Var(Y) - 2Cov(Y, \hat{Y}) + Var(\hat{Y}) \\
# &= ~ Var(Y) - Var(\hat{Y}) \\
# &= ~ \sigma_Y^2 - \boldsymbol{\Sigma}_{Y, \mathbf{X}}\boldsymbol{\Sigma}_\mathbf{X}^{-1} \boldsymbol{\Sigma}_{\mathbf{X}, Y}
# \end{align*}
# $$
# 
# In the case of simple regression under the bivariate normal model, we saw that the error variance was
# 
# $$
# \sigma_Y^2 - \sigma_{Y,X}(\sigma_X^2)^{-1}\sigma_{X,Y}
# $$
# 
# This is a special case of the more general formula that we have established here. The bivariate normal assumption isn't needed.

# As in the case of simple regression, we have made no assumption about the joint distribution of $Y$ and $\mathbf{X}$ other than to say that $\boldsymbol{\Sigma}_\mathbf{X}$ is positive definite. Regardless, there is a unique best linear predictor of $Y$ based on $\mathbf{X}$.
