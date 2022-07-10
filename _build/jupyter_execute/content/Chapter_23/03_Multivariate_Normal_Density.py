#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
import warnings
warnings.filterwarnings('ignore')
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy import stats


# ## Multivariate Normal Density ##

# It is reasonable to expect that if a random vector $\mathbf{X}$ is multivariate normal then its components should have a joint density function. But we have to be careful about the components in order to discuss joint densities.
# 
# For an example of what could go wrong, let $\mathbf{Z} = [Z_1 ~ Z_2]^T$ consist of i.i.d. standard normal variables, and let $\mathbf{X} = [Z_1 ~ 2Z_1]^T$. Then the components of $\mathbf{X}$ don't have a joint density on the plane since all the probability is on the line $y = 2x$. We have a *degenerate* situation in which one component is a linear transformation of the other.
# 
# Another example is $\mathbf{X} = [Z_1 ~ Z_2 ~ Z_1+Z_2]^T$. The three components don't have a joint density in three dimensions, since the third component is a linear combination of the first two. 
# 
# For a data scientist, there is no benefit in carrying around variables that are deterministic functions of other variables in a dataset. So we will avoid degenerate cases such as those above. To do this, let's make an observation about the linear transformations involved.
# 
# In both cases, if you write $\mathbf{X}$ as $\mathbf{AZ}$ then the matrix $\mathbf{A}$ is not invertible, and the covariance matrix of $\mathbf{X}$ is positive semi-definite instead of positive definite.
# 
# Thus we are going to restrict the definition of multivariate normal vectors to **invertible** linear transformations of i.i.d. standard normal vectors and **positive definite** covariance matrices.

# In[2]:


# VIDEO: Multivariate Normal
from IPython.display import YouTubeVideo

YouTubeVideo('lUd7UVydEoI')


# ### The Density ###
# 
# From now on, we will usually say "density" even when we mean "joint density". The dimension of the random vector will tell you how many coordinates the density function has.
# 
# Let $\boldsymbol{\Sigma}$ be a positive definite matrix. An $n$-dimensional random vector $\mathbf{X}$ has the *multivariate normal density with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$* if the joint density of the elements of $\mathbf{X}$ is given by
# 
# $$
# f_\mathbf{X}(\mathbf{x}) ~ = ~ \frac{1}{(\sqrt{2\pi})^n \sqrt{\det(\boldsymbol{\Sigma})} }
# \exp\big{(}-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})\big{)}
# $$
# 
# We will say that the elements of $\mathbf{X}$ are *jointly normal* or *jointly Gaussian*.
# 
# You should check that the formula is correct when $n = 1$. In this case $\boldsymbol{\Sigma} = [\sigma^2]$ is just a scalar. It is a number, not a larger matrix; its determinant is itself; its inverse is simply $1/\sigma^2$. Also, $\mathbf{x} = x$ and $\boldsymbol{\mu} = \mu$ are just numbers. The formula above reduces to the familiar normal density function with mean $\mu$ and variance $\sigma^2$.
# 
# You should also check that the formula is correct in the case when the elements of $\mathbf{X}$ are i.i.d. standard normal. In that case $\mathbf{\mu} = \mathbf{0}$ and $\boldsymbol{\Sigma} = \mathbf{I}_n$, the $n$-dimensional identity matrix.
# 
# When $n=2$ the multivariate normal distribution is called *bivariate* normal.

# In[3]:


# VIDEO: Multivariate Normal: Parameters
YouTubeVideo('ao4fqXghbmI')


# In lab you went through a detailed development of the multivariate normal joint density function, starting with $\mathbf{Z}$ consisting of two i.i.d. standard normal components and then taking linear combinations. It turns out that all non-degenerate multivariate normal random vectors can be generated in this way. In fact, there are three useful equivalent definitions of a random vector $\mathbf{X}$ with the multivariate normal density.

# In[4]:


# VIDEO: Multivariate Normal: Definition

YouTubeVideo('owX4JKA-2F8')


# **Definition 1:** $\mathbf{X} = \mathbf{AZ} + \mathbf{b}$ for some i.i.d. standard normal $\mathbf{Z}$, an invertible $\mathbf{A}$, and a column vector $\mathbf{b}$.
# 
# **Definition 2:** $\mathbf{X}$ has the joint density above.
# 
# **Definition 3:** Every linear combination of elements of $\mathbf{X}$ is normally distributed.
# 
# At the end of this section there is a note on establishing the equivalences. Parts of it are hard. Just accept that they are true, and let's examine the properties of the distribution.
# 
# **The key to understanding the multivariate normal is Definition 1: every multivariate normal vector that has a density is an invertible linear transformation of i.i.d. standard normals.** Let's see what Definition 1 implies for the density.

# In[5]:


# VIDEO: Multivariate Normal: Density
YouTubeVideo('tIvp_0HPeIo')


# In[6]:


# VIDEO: Quadratic Form
YouTubeVideo('rITtghijhb4')


# ### Quadratic Form ###
# The shape of the density is determined by the *quadratic form* $\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})$. The level surfaces are ellipsoids. In two dimensions these are the ellipses you saw in lab. 
# 
# Here is the joint density surface of standard normal variables $X_1$ and $X_2$ that are jointly normal with $Cov(X_1, X_2) = 0.8$. The call is `Plot_bivariate_normal(mu, cov)` where the mean vector `mu` is a list and the covariance matrix is a list of lists specifying the rows.

# In[7]:


mu = [0, 0]
cov = [[1, 0.8], [0.8, 1]]
Plot_bivariate_normal(mu, cov)


# Note the elliptical contours, and that the probability is concentrated around a straight line. 
# 
# In more than two dimensions we can no longer draw joint density surfaces. But in three dimensions we can make i.i.d. draws from a multivariate normal joint density and plot the resulting points. Here is an example of the empirical distribution of 1000 observations of standard normal variables $X_1$, $X_2$, and $X_3$ that are jointly normal with $Cov(X_1, X_2) = 0.6$, $Cov(X_1, X_3) = 0.5$, and $Cov(X_2, X_3) = 0.2$. Note the elliptical cloud.
# 
# The call is `Scatter_multivariate_normal(mu, cov, n)` where `n` is the number of points to generate. The function checks whether the specified matrix is positive semidefinite.

# In[8]:


mu2 = [0, 0, 0]
cov2 = [[1, 0.6, 0.5], [0.6, 1, 0.2], [0.5, 0.2, 1]]
Scatter_multivariate_normal(mu2, cov2, 1000)


# To see how the quadratic form arises, let $\mathbf{X}$ be multivariate normal. By Definition 1, $\mathbf{X} = \mathbf{AZ} + \mathbf{b}$ for some invertible $\mathbf{A}$ and vector $\mathbf{b}$, and some i.i.d. standard normal $\mathbf{Z}$. 
# 
# By multiplication of the marginals, the joint density of $\mathbf{Z}$ is 
# 
# $$
# f(\mathbf{z}) ~ = ~ \frac{1}{(\sqrt{2\pi})^n} \exp\big{(}-\frac{1}{2}(z_1^2 + z_2^2 + \cdots + z_n^2)\big{)} ~ = ~ \frac{1}{(\sqrt{2\pi})^n }
# \exp\big{(}-\frac{1}{2}\mathbf{z}^T\mathbf{z}\big{)}
# $$
# 
# The preimage of $\mathbf{x}$ under the linear transformation $\mathbf{x} = \mathbf{Az} + \mathbf{b}$ is 
# 
# $$
# \mathbf{z} ~ = ~ \mathbf{A}^{-1}(\mathbf{x} - \mathbf{b})
# $$
# 
# and so by change of variable the quadratic form in the density of $\mathbf{X}$ is
# 
# $$
# \frac{1}{2}\mathbf{z}^T\mathbf{z} ~ = ~ 
# \frac{1}{2} (\mathbf{x} - \mathbf{b})^T (\mathbf{A}^{-1})^T \mathbf{A}^{-1}(\mathbf{x} - \mathbf{b}) ~ = ~
# \frac{1}{2} (\mathbf{x} - \mathbf{b})^T (\mathbf{AA}^T)^{-1} (\mathbf{x} - \mathbf{b})
# $$
# 
# Let $\mathbf{\mu_X}$ be the mean vector of $\mathbf{X}$. Because $\mathbf{X} = \mathbf{AZ} + \mathbf{b}$, we have $\mathbf{\mu_X} = \mathbf{b}$. 
# 
# The covariance matrix of $\mathbf{Z}$ is $\mathbf{I}_n$. So the covariance matrix of $\mathbf{X}$ is
# 
# $$
# \boldsymbol{\Sigma}_\mathbf{X} ~ = ~ \mathbf{A} \mathbf{I}_n \mathbf{A}^T ~ = ~ \mathbf{A} \mathbf{A}^T
# $$
# 
# So the quadratic form in the density of $\mathbf{X}$ becomes $\frac{1}{2} (\mathbf{x} - \mathbf{\mu_X})^T \boldsymbol{\Sigma}_\mathbf{X}^{-1} (\mathbf{x} - \mathbf{\mu_X})$.

# In[9]:


# VIDEO: Volume
YouTubeVideo('g_S0UeHYc2k')


# ### Constant of Integration ###
# By linear change of variable, the density of $\mathbf{X}$ is given by
# $$
# f_\mathbf{X}(\mathbf{x}) ~ = ~ f(\mathbf{z}) \cdot \frac{1}{s}
# $$
# 
# where $\mathbf{z}$ is the preimage of $\mathbf{x}$ and $s$ is the volume of the parallelopiped formed by the transformed unit vectors. That is, $s = \|\det(\mathbf{A})\|$. Now
# 
# $$
# \det(\boldsymbol{\Sigma}_\mathbf{X}) ~ = ~ \det(\mathbf{AA}^T) ~ = ~ (\det(\mathbf{A}))^2
# $$
# 
# Therefore the constant of integration in the density of $\mathbf{X}$ is
# 
# $$
# \frac{1}{(\sqrt{2\pi})^n \sqrt{\det(\boldsymbol{\Sigma}_\mathbf{X})} }
# $$

# We have shown how the joint density function arises and what its pieces represent. In the process, we have proved the Definition 1 implies Definition 2. Now let's establish that all three definitions are equivalent.

# ### The Equivalences ###
# Here are some pointers for how to see the equivalences of the three definitions. One of the pieces is not easy to establish.
# 
# Definition 1 is at the core of the properties of the multivariate normal. We will try to see why it is equivalent to the other two definitions.
# 
# We have seen that Definition 1 implies Definition 2. 
# 
# To see that Definition 2 implies Definition 1, it helps to remember that a positive definite matrix $\boldsymbol{\Sigma}$ can be decomposed as $\boldsymbol{\Sigma} = \mathbf{AA}^T$ for some lower triangular $\mathbf{A}$ that has only positive elements on its diagonal and hence is invertible. This is called the *Cholesky decomposition*. Set $\mathbf{Z} = \mathbf{A}^{-1}(\mathbf{X} - \boldsymbol{\mu})$ to see that Definition 1 implies Definition 2. 
# 
# So Definitions 1 and 2 are equivalent.
# 
# You already know that linear combinations of independent normal variables are normal. If $\mathbf{X}$ is an invertible linear transformation of i.i.d. standard normal variables $\mathbf{Z}$, then any linear combination of elements of $\mathbf{X}$ is also a linear combination of elements of $\mathbf{Z}$ and hence is normal. This means that Definition 1 implies Definition 3.
# 
# Showing that Definition 3 implies Definition 1 requires some math. Multivariate moment generating functions are one way to see why the result is true, if we accept that moment genrating functions determine distributions, but we won't go into that here. 

# In[ ]:




