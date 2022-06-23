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
import math
from scipy import stats
from scipy import misc


# ## Expectations of Functions ##

# Once we have a random variable, we often want to work with functions of it. For example, if a random variables is an estimator, we usually want to see how far it is from the value it is trying to estimate. For example, we might want to see how far a random variable $X$ is from the number 10. That's a function of $X$. Let's call it $Y$. Then
# 
# $$
# Y = |X - 10|
# $$
# 
# This section is about finding the expectation of a function of a random variable whose distribution you know. Throughout, we will assume that all the expectations that we are discussing are well defined.
# 
# In what follows, let $X$ be a random variable whose distribution (and hence also expectation) are known.

# ### Linear Function Rule ###
# 
# Let $X$ be a random variable with expectation $E(X)$ and let $Y = aX + b$ for some constants $a$ and $b$. 
# 
# This kind of transformation happens for example when you change units of measurement. 
# 
# - If you switch from Celsius to Fahreneheit, then $a = 9/5$ and $b = 32$. 
# - If you switch from inches to centimeters, then $a = 2.54$ and $b = 0$.
# 
# We can find $E(Y)$ by applying the definition of expectation on the domain $\Omega$. For every $\omega \in \Omega$, we have $Y(\omega) = aX(\omega) + b$. So
# 
# $$
# \begin{align*}
# E(Y) ~ &= ~ \sum_{\text{all }\omega} (aX(\omega)+b)P(\omega) \\
# &= ~a \sum_{\text{all }\omega} X(\omega)P(\omega ) + ~b \sum_{\text{all }\omega} P(\omega )\\
# &= ~aE(X) + b
# \end{align*}
# $$
# 
# For example, $E(2X - 3) = 2E(X) - 3$. Also $E(X/2) = E(X)/2$, and $E(1 - X) = 1 - E(X)$.
# 
# The expectation of a linear transformation of $X$ is the linear transformation of the expectation of $X$. This is a handy result as we will often be transforming variables linearly.

# ```{admonition} Quick Check
# Let $X$ be a random variable with $E(X) = 5$.
# 
# Find $E(20 + 2X - (10 - X))$.
# 
# ```

# ```{admonition} Answer
# :class: dropdown
# $25$
# 
# ```

# But expectation behaves differently under non-linear transformation.

# In[2]:


# VIDEO: Non-linear Function: Observation
from IPython.display import YouTubeVideo

YouTubeVideo('BWNa1Ri7eII')


# ### Non-linear Function Rule ###
# Now let $Y = g(X)$ where $g$ is any numerical function. Remember that $X$ is a function on $\Omega$. So the function that defines the random variable $Y$ is a *composition*:
# 
# $$
# Y(\omega) = (g \circ X) (\omega) ~~~~~~~~~ \text{for } \omega \in \Omega
# $$
# 
# This allows us to write $E(Y)$ in three equivalent ways:
# 
# **On the range of $Y$**
# 
# $$
# E(Y) =  \sum_{\text{all }y} yP(Y=y)
# $$
# 
# **On the domain $\Omega$**
# 
# $$
# E(Y) = E(g(X)) = \sum_{\omega \in \Omega} (g \circ X) (\omega) P(\omega)
# $$
# 
# **On the range of $X$**
# 
# $$
# E(Y) = E(g(X)) = \sum_{\text{all }x} g(x)P(X=x)
# $$
# 
# As before, it is a straightforward matter of grouping to show that all the forms are equivalent.
# 
# The first form looks the simplest, but there's a catch: you need to first find $P(Y=y)$. The second form involves an unnecessarily high level of detail.
# 
# The third form is the one to use. It uses the known distribution of $X$. It says that to find $E(Y)$ where $Y = g(X)$ for some function $g$:
# - Take a generic value $x$ of $X$.
# - Apply $g$ to $x$; this $g(x)$ is a generic value of $Y$.
# - Weight $g(x)$ by $P(X=x)$, which is known.
# - Do this for all $x$ and add. The sum is $E(Y)$.
# 
# The crucial thing to note about this method is that **we didn't have to first find the distribution of $Y$**. That saves us a lot of work. 

# In[3]:


# VIDEO: Non-linear Function: Calculation

YouTubeVideo('jVBrCMCzO3o')


# Let's see how our method works in some examples.

# ### $Y = \vert X-3 \vert$ ###
# Let $X$ have a distribution we worked with earlier:

# In[4]:


x = np.arange(1, 6)
probs = make_array(0.15, 0.25, 0.3, 0.2, 0.1)
dist = Table().values(x).probability(probs)
dist = dist.relabel('Value', 'x').relabel('Probability', 'P(X=x)')
dist


# Let $g$ be the function defined by $g(x) = \vert x-3 \vert$, and let $Y = g(X)$. In other words, $Y = \vert X - 3 \vert$. 
# 
# To calculate $E(Y)$, we first have to create a column that transforms the values of $X$ into values of $Y$:

# In[5]:


dist_with_Y = dist.with_column('g(x)', np.abs(dist.column('x')-3)).move_to_end('P(X=x)')

dist_with_Y


# To get $E(Y)$, find the appropriate weighed average: multiply the `g(x)` and `P(X=x)` columns, and add. The calculation shows that $E(Y) = 0.95$.

# In[6]:


ev_Y = sum(dist_with_Y.column('g(x)') * dist_with_Y.column('P(X=x)'))
ev_Y


# ### $Y = \min(X, 3)$ ###
# Let $X$ be as above, but now let $Y = \min(X, 3)$. We want $E(Y)$. What we know is the distribution of $X$:

# In[7]:


dist


# To find $E(Y)$ we can just go row by row and replace the value of $x$ by the value of $\min(x, 3)$, and then find the weighted average:

# In[8]:


ev_Y = 1*0.15 + 2*0.25 + 3*0.3 + 3*0.2 + 3*0.1
ev_Y


# ### $E(X(X-1))$ for a Poisson Variable $X$ ###
# 
# Let $X$ have the Poisson $(\mu)$ distribution. 
# 
# $$
# \begin{align*}
# E(X(X-1)) &= \sum_{k=0}^\infty k(k-1) e^{-\mu} \frac{\mu^k}{k!} \\ \\
# &= e^{-\mu} \mu^2 \sum_{k=2}^\infty \frac{\mu^{k-2}}{(k-2)!} \\ \\
# &= e^{-\mu}\mu^2 e^\mu \\ \\
# &= \mu^2
# \end{align*}
# $$
# 
# In the next section we will use this to find $E(X^2)$. For now, notice that 
# 
# $$
# E(X^2) ~ = ~ \sum_{k=0}^\infty k^2 e^{-\mu} \frac{\mu^k}{k!} ~ \ge ~ \sum_{k=0}^\infty k(k-1) e^{-\mu} \frac{\mu^k}{k!} ~ = ~ E(X(X-1)) ~ = ~ \mu^2
# $$
# 
# Since $E(X) = \mu$, we have $E(X^2) \ge (E(X))^2$. We will see later that this inequality is true for all random variables for which the expected square is finite.

# In[7]:




