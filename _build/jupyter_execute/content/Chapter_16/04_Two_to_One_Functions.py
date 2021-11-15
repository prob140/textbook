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


# ## Two-to-One Functions ##

# Let $X$ have density $f_X$. As you have seen, the random variable $Y = X^2$ comes up frequently in calculations. Thus far, all we have needed is $E(Y)$ which can be found by the formula for the expectation of a non-linear function of $X$. To find the density of $Y$, we can't directly use the change of variable formula of the previous section because the function $g(x) = x^2$ is not monotone. It is two-to-one because both $\sqrt{x}$ and $-\sqrt{x}$ have the same square.
# 
# In this section we will find the density of $Y$ by developing a modification of the change of variable formula for the density of a monotone function of $X$. The modification extends in a straightforward manner to other two-to-one functions and also to many-to-one functions.

# ### Density of $Y = X^2$ ###
# If $X$ can take both positive and negative values, we have to account for the fact that there can be two mutually exclusive ways in which the event $\{ Y \in dy \}$ can happen: either $X$ has to be near the positive square root of $y$ or near the negative square root of $y$.

# In[3]:


# NO CODE

x = np.arange(-5, 5.01, 0.01)
y = x ** 2
y_star = 12
x_star = y_star ** 0.5
neg_x_star = -1 * y_star ** 0.5
plt.plot(x, y, color='darkblue', lw=2)
plt.plot([0, 0], [0, 25], color='k', lw=1)
plt.plot([x_star, x_star], [0, y_star], color='k', lw=2)
plt.plot([neg_x_star, neg_x_star], [0, y_star], color='k', lw=2)
plt.plot([neg_x_star, x_star], [y_star, y_star], color='k', lw=2)
plt.scatter(2, y_star, marker='>', color='red', s=40)
plt.scatter(-2, y_star, marker='<', color='red', s=40)
plt.scatter(-2, y_star, marker='<', color='red', s=40)
plt.scatter(neg_x_star, 5, marker='v', color='red', s=40)
plt.scatter(x_star, 5, marker='v', color='red', s=40)
plt.ylim(-0.5, 25)
plt.xticks(np.arange(-5, 5.1))
plt.xlabel('$x$')
plt.ylabel('$y$', rotation=0)
plt.title('$y = x^2$');


# So the density of $Y$ at $y$ has two components, as follows. For $y > 0$,
# 
# $$
# f_Y(y) ~ = ~ a + b
# $$
# 
# where
# 
# $$
# a = \frac{f_X(x_1)}{2x_1} ~~~~ \text{at } x_1 = \sqrt{y}
# $$
# 
# and
# 
# $$
# b = \frac{f_X(x_2)}{\vert 2x_2 \vert} ~~~~ \text{at } x_2 = -\sqrt{y}
# $$
# 
# We have used $g'(x) = 2x$ when $g(x) = x^2$.
# 
# For a more formal approach, start with the cdf of $Y$:
# 
# $$
# \begin{align*}
# F_Y(y) ~ &= ~ P(Y \le y) \\
# &= ~ P(\vert X \vert \le \sqrt{y}) \\
# &= ~ P(-\sqrt{y} \le X \le \sqrt{y}) \\
# &= ~ F_X(\sqrt{y}) - F_X(-\sqrt{y})
# \end{align*}
# $$
# 
# Differentiate both sides to get our formula for $f_Y(y)$; keep an eye on the two minus signs in the second term and make sure you combine them correctly.
# 
# This approach can be extended to any many-to-one function $g$. For every $y$, there will be one component for each value of $x$ such that $g(x) = y$.

# ```{admonition} Quick Check
# $U$ is uniform on $(0, 1)$. To find the density of $V = U^2$, do you have to take into account the fact that the square is a two-to-one function? Either way, find the density of $V$, and check that your answer integrates to 1.
# 
# ```

# ```{admonition} Answer
# :class: dropdown
# No, the square is one-to-one on $(0, 1)$. For $v \in (0, 1)$, $f_V(v) = 1/2\sqrt{v}$.
# 
# ```

# ```{admonition} Quick Check
# $R$ is uniform on $(-1, 1)$. To find the density of $S = R^2$, do you have to take into account the fact that the square is a two-to-one function? Either way, write the density of $R$, find the density of $S$, and check that your answers integrate to 1.
# 
# ```

# ```{admonition} Answer
# :class: dropdown
# $f_R(r) = \frac{1}{2}$ for $r \in (-1, 1)$. Yes, the square is two-to-one on $(-1, 1)$. For $s \in (0, 1)$, $f_S(s) = 1/2\sqrt{s}$.
# 
# ```

# ### Square of the Standard Normal ###
# Let $Z$ be standard normal and let $W = Z^2$. The possible values of $W$ are non-negative. For a possible value $w \ge 0$, the formula we have derived says that the density of $W$ is given by:
# 
# $$
# \begin{align*}
# f_W(w) ~ &= ~ \frac{f_Z(\sqrt{w})}{2\sqrt{w}} ~ + ~ \frac{f_Z(-\sqrt{w})}{2\sqrt{w}} \\ \\
# &= ~ \frac{\frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}w}}{2\sqrt{w}} ~ + ~ \frac{\frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}w}}{2\sqrt{w}} \\ \\
# &= \frac{1}{\sqrt{2\pi}} w^{-\frac{1}{2}} e^{-\frac{1}{2}w}
# \end{align*}
# $$
# 
# By algebra, the density can be written in an equivalent form that we will use more frequently.
# 
# $$
# f_W(w) ~ = ~ \frac{\frac{1}{2}^{\frac{1}{2}}}{\sqrt{\pi}} w^{\frac{1}{2} - 1} e^{-\frac{1}{2}w}
# $$
# 
# This is a member of the family of *gamma* densities that we will study later in the course. In statistics, it is called the *chi squared density with one degree of freedom*.

# In[ ]:




