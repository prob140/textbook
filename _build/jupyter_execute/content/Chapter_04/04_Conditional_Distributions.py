#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# HIDDEN

# X = number of heads in first two tosses; Y = number of heads in first five tosses
def joint_probability(x, y):
    if y >= x:
        return stats.binom.pmf(x, 2, 1/2) * stats.binom.pmf(y-x, 3, 1/2)
    else:
        return 0
    
k_x = np.arange(3)
k_y = np.arange(6)

joint_table = Table().values('X', k_x, 'Y', k_y).probability_function(joint_probability)


# ## Conditional Distributions ##

# To understand the relation between two variables we must examine the conditional behavior of each of them given the value of the other. Towards this goal, we will start by examining the example of the previous section and then develop the general theory.

# In[3]:


# VIDEO: Conditional Distribution: Example
from IPython.display import YouTubeVideo

YouTubeVideo("CnFSQPrm8Js")


# In our example, the joint distribution of $X$ and $Y$ is given by `joint_table`. Here we also display the marginal distribution of $X$.

# In[4]:


joint_table.marginal('X')


# Now suppose we know that $Y = 3$. Then the outcome space is reduced to just the cells in the row labeled `Y=3`.

# In[5]:


def indicator_Y_equals_3(i, j):
    return j == 3

joint_table.event(indicator_Y_equals_3, 'X', 'Y')


# Of course, the probabilities along this row don't sum to 1. Their sum is $P(Y = 3) = 0.3125$.
# 
# By the division rule, for each $x = 0, 1, 2$ we have
# 
# $$
# P(X = x \mid Y = 3) ~ = ~ \frac{P(X = x, Y = 3)}{P(Y = 3)}
# $$
# 
# By *normalizing* all the probabilities in the row by their sum, we get the *conditional distribution of $X$ given $Y=3$*.
# 
# $$
# \begin{align*}
# P(X = 0 \mid Y = 3) ~ &= ~ \frac{0.03125}{0.3125} = 0.1 \\ \\
# P(X = 1 \mid Y = 3) ~ &= ~ \frac{0.1875}{0.3125} = 0.6 \\ \\
# P(X = 2 \mid Y = 3) ~ &= ~ \frac{0.09375}{0.3125} = 0.3
# \end{align*}
# $$

# Compare this conditional distribution to the unconditional distribution of $X$:
# 
# $$
# P(X = 0) ~ = ~ 0.25, ~~~~~ P(X = 1) ~ = ~ 0.5, ~~~~~ P(X = 2) ~ = ~ 0.25
# $$
# 
# The two distributions are different. Given $Y = 3$, the chance that $X$ is large is higher than it is if we don't have that condition. 
# 
# This shows that $X$ and $Y$ are *dependent*. We will define dependence and independence formally in the next section.

# ```{admonition} Quick Check
# Find the following (without using Python) based on the joint distribution in the example above.
# 
# (a) $P(X=0 \mid Y=1)$
# 
# (b) the conditional distribution of $X$ given $Y=1$
# 
# (c) the conditional distribution of $X$ given $Y=5$
# 
# ```

# ```{admonition} Answer
# :class: dropdown
# (a) $0.6$ 
# 
# (b) $0$ with chance 0.6, $1$ with chance 0.4 
# 
# (c) $2$ with chance 1
# 
# ```

# ### Conditional Distribution of $X$ given $Y = y$ ###
# The `conditional_dist` method operates on a joint distribution object and displays conditional distributions, as follows.

# In[6]:


# conditional distribution of X given each different value of Y

joint_table.conditional_dist('X', 'Y') 


# To understand this table, start with the row labeled `Y=3`. The entries are the probabilities in the conditional distribution of $X$ given $Y=3$. 
# 
# In the row labeled `Y=1`, the entries are the probabilities in the conditional distribution of $X$ given $Y=1$. Notice that if $Y=1$ then $X$ can't be 2. You can go back and confirm that in the joint distribution table, $P(X = 2, Y = 1) = 0$.
# 
# All the other rows can be understood in the same way. In row $y$, the given condition is $Y=y$, and the entries are the probabilities in the conditional distribution of $X$ given $Y=y$.
# 
# It is easy to see why each row in the table of conditional distributions sums to 1. The value in each cell in the row is obtained from the joint distribution table by taking the corresponding cell in that table and dividing its entry by the sum of the entries in the row.

# ### The Theory ###
# We can now generalize the calculations we did in the example above.

# In[7]:


# VIDEO: Conditional Distribution: Notation and Calculation
from IPython.display import YouTubeVideo

YouTubeVideo("8Ihsh1B0Eg4")


# Let $X$ and $Y$ be two random variables defined on the same space. If $x$ is a possible value of $X$, and $y$ and possible value of $Y$, then
# 
# $$
# P(X = x \mid Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}
# $$
# 
# The conditional probability $P(X = x \mid Y = y)$ is displayed in the $(x, y)$ cell of the table of conditional distributions above.
# 
# For a fixed value $y^*$ of $Y$, the *conditional distribution* of $X$ given $Y = y^*$ is the collection of probabilities
# 
# $$
# P(X = x \mid Y = y^*) = \frac{P(X = x, Y = y^*)}{P(Y = y^*)}
# $$
# 
# where $x$ ranges over all the values of $X$. Keep in mind that $x$ represents the values of the variable here. The value $y^*$ is the particular value of $Y$ that was observed, so it is a constant.

# ### The Probabilities in a Conditional Distribution Sum to 1 ###
# In a distribution, the probabilities have to sum to 1. To see that this is true for the conditional distribution defined above, start by using the fundamental rule. 
# 
# Find $P(Y = y^*)$ by partitioning the event $\{ Y = y^* \}$ according to the values of $X$:
# 
# $$
# P(Y = y^*) = \sum_{\text{all }x} P(X = x, Y = y^*)
# $$
# 
# Now sum the probabilities in the conditional distribution of $X$ given $Y = y^*$:
# 
# $$
# \begin{align*}
# \sum_{\text{all }x} P(X = x \mid Y = y^*) ~ &= ~
# \sum_{\text{all }x} \frac{P(X = x, Y = y^*)}{P(Y = y^*)} \\ \\
# &= ~ \frac{1}{P(Y = y^*)} \sum_{\text{all }x} P(X = x, Y = y^*) \\
# &= ~ \frac{1}{P(Y = y^*)} \cdot P(Y = y^*) \\ \\
# &= ~ 1
# \end{align*}
# $$
# 
# Thus the conditional distribution is just an ordinary probability distribution: a set of values with probabilities that sum to 1. 

# In[ ]:





# In[ ]:




