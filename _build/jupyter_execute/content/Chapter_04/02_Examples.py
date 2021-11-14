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


# ## Examples ##

# This section is a workout in finding probabilities of events determined by two jointly distributed random variables. We will apply the computational methods of the previous section and also the mathematical framework for finding probabilities that was developed there.
# 
# In some of the examples you may find yourself wondering why we are bothering to write out math notation for numerical answers that we have already obtained using Python. It is because the Python visualizations help us understand the math. That understanding then helps us answer questions in generality, not just in particular numerical settings, as you will see in the final example.

# ### Fair and Loaded Dice ###
# I have two dice, one of which is fair. The other die is shaped so that it is biased towards larger numbers of spots. The distribution of the number of spots on one roll of this biased shape is given by
# 
# |value| 1 | 2 | 3 | 4 | 5 | 6 |
# |----:|:---:|:---:|:---:|:---:|:---:|:---:|
# |**probability**|  1/16  | 1/16  | 3/16  | 3/16  | 4/16  |  4/16 |
# 
# Suppose I roll each die once.

# ### Equality ###
# 
# **Question:** What is the chance that I get the same number on both dice?
# 
# **Answer 1, by symmetry:** No matter what number appears on the biased shape, the chance that the fair die shows that number is 1/6. So the answer is 1/6.
# 
# Not convinced? Then let's calculate.
# 
# **Answer 2:** Let $F$ be the number on the fair die and let $S$ be the number on the biased shape. It is reasonable to assume that the outcome of one die doesn't affect chances for the other. So for every $i$ and $j$ such that $1 \le i, j \le 6$, we have
# 
# $$
# P(F = i, S = j) ~ = ~ P(F = i)P(S = j) ~ = ~ \frac{1}{6}P(S = j)
# $$
# 
# We want $P(F = S)$. For this we have to add up the probabilities of the $(i, j)$ pairs that satisfy $i = j$. Those are just the pairs $(i, i)$ for $1 \le i \le 6$.
# 
# $$
# P(F = S) ~ = ~ \sum_{i=1}^6 P(F = i, S = i) ~ = ~ \sum_{i=1}^6 \frac{1}{6}P(S = i) ~ = ~ \frac{1}{6} \sum_{i=1}^6 P(S = i) ~ = ~ \frac{1}{6} \cdot 1 ~ = ~ \frac{1}{6}
# $$

# ### Difference ###
# 
# **Question:** What is the chance that the number on the biased shape exceeds the number on the fair die by more than 2?
# 
# **Answer:** We can visualize the event $\{ S > F + 2 \}$ using the methods of the previous section.
# 
# We know that the joint distribution of $F$ and $S$ is given by 
# 
# $$
# P(F = i, S = j) ~ = ~
# \begin{cases} 
# \frac{1}{6} \cdot \frac{1}{16}, ~~~ 1 \le i \le 6, ~ j = 1, 2 \\
# \frac{1}{6} \cdot \frac{3}{16}, ~~~ 1 \le i \le 6, ~ j = 3, 4 \\
# \frac{1}{6} \cdot \frac{4}{16}, ~~~ 1 \le i \le 6, ~ j = 5, 6
# \end{cases}
# $$
# 
# We can display this in a joint distribution table. 

# In[2]:


spots = np.arange(1, 7)                     # possible values of F; same set for S

fair = (1/6) * np.ones(6)  
biased = make_array(1/16, 1/16, 3/16, 3/16, 4/16, 4/16)

def joint_probability(i, j):                # returns P(F = i, S = j)
    return fair.item(i-1) * biased.item(j-1)

# joint distribution table of F and S
two_dice = Table().values('F', spots, 'S', spots).probability_function(joint_probability)
two_dice


# Define the indicator function of the event $\{S > F + 2 \}$ and then use the `event` method.

# In[3]:


def indicator(i, j):
    return j > i + 2

two_dice.event(indicator, 'F', 'S')


# The answer $P(S > F + 2) \approx 0.24$ has been obtained by adding the chances of all the cells $(i, j)$ for which $j > i+2$ or equivalently $i < j-2$. Since $j$ can be at most 6, this implies $1 \le i \le 3$, as is visible in the display.
# 
# Expressed in math notation, the calculation is
# 
# $$
# P(S > F + 2) ~ = ~ \mathop{\sum \sum}_{j > i+2} P(F = i, S= j)
# ~ = ~ \sum_{i=1}^3\sum_{j=i+3}^6 P(F = i, S= j)
# $$
# 
# For each fixed value of $i$, the inner sum is the sum of the terms visible in the column labeled $F = i$. The outer sum adds up the three column sums.

# ### Absolute Difference ###
# 
# **Question:** What is the chance that the numbers on the two dice differ by no more than 1?
# 
# **Answer:** The goal is to find $P(\vert F - S \vert \le 1)$. We defined `two_dice`, the joint distribution of $F$ and $S$, in the previous problem. So now our work is simple.

# In[4]:


def indicator_absdiff_atmost_1(i, j):
    return abs(i - j) <= 1

two_dice.event(indicator_absdiff_atmost_1, 'F', 'S')


# The calculation shows that $P(\vert F - S \vert \le 1) \approx 0.448$.
# 
# The event is a diagonal band of cells, bounded by the lines $j = i-1$ and $j = i+1$. That is because the condition $\vert i - j \vert \le 1$ is the same as $i-1 \le j \le i+1$.
# 
# Notice the edge cases $i=1$ and $i=6$. When $i=1$, the condition $\vert i - j \vert \le 1$ is only satisfied by $j=1$ and $j=2$, because $j = -1$ is not a possible outcome of the dice. Nor is $j = 7$ when $i = 6$. So there are two terms to add in each of the columns labeled $F=1$ and $F=6$, and three in each of the other columns.
# 
# Check carefully that you agree that in math notation the calculation is
# 
# $$
# P(\vert F - S \vert \le 1) ~ = ~ \sum_{j=1}^2 P(F = 1, S = j) ~ + ~ \sum_{i=2}^5\sum_{j=i-1}^{i+1} P(F = i, S = j) ~ + ~ \sum_{j=5}^6 P(F = 6, S = j)
# $$

# ### Sum ###
# 
# **Question:** What is the chance that the sum of the numbers on the two dice is 7?
# 
# **Answer:** This time we'll write out the math first.
# 
# The event $\{ F + S = 7 \}$ consists of all possible pairs $(i, j)$ such that $i + j = 7$. For each fixed $i$, there is exactly one $j$ that satisfies $i+j = 7$, and that's $j = 7-i$. So
# 
# $$
# P(F+S = 7) ~ = ~ \sum_{i=1}^6 P(F = i, S = 7-i) ~ = ~ \sum_{i=1}^6 \frac{1}{6}P(S = 7-i)
# ~ = ~ \frac{1}{6} \sum_{i=1}^6 P(S = 7-i) ~ = ~ \frac{1}{6}
# $$
# 
# because $\sum_{i=1}^6 P(S = 7-i) = P(S=6) + P(S=5) + \cdots + P(S=1) = 1$.
# 
# Notice that the argument doesn't depend on the nature of the bias in $S$. The chance that the sum of the numbers on two dice equals 7 is 1/6 as long as one of the dice is fair.
# 
# We can check the answer by computation.

# In[5]:


def indicator_sum_7(i, j):
    return i + j == 7

two_dice.event(indicator_sum_7, 'F', 'S')


# **Question:** Now suppose I have two $n$-sided dice, at least one of which is fair. I roll each of them once. What is the chance that the sum of the two numbers is $n+1$?
# 
# **Answer:** We can't use our computational methods for this one because the model isn't numerical. But we know how to solve the problem mathematically.
# 
# Let $F_n$ be the number on a fair die and $D_n$ the number on the other die.
# 
# $$
# \begin{align*}
# P(F_n + D_n = n+1) ~ &= ~ \sum_{i=1}^n P(F_n = i, D_n = n+1-i) \\
# &= ~ \sum_{i=1}^n \frac{1}{n}P(D_n = n+1-i) \\
# &= ~ \frac{1}{n} \sum_{i=1}^n P(D_n = n+1-i) \\
# &= ~ \frac{1}{n}
# \end{align*}
# $$

# In[ ]:




