# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline
from scipy import stats

# The Central Limit Theorem #

The standard deviation is one measure of spread, but you can imagine many others. Why choose the SD over all of them? The main reason is the connection between the SD and the normal curve. Why is the normal curve so important? This chapter contains an answer to that question.

We will start by looking at the exact distribution of the sum of an i.i.d. sample. We already know its mean and SD. In this chapter, we will study the shape of the distribution: the exact shape if we can calculate it, and a remarkable approximation when the sample size is large and exact calculations are not feasible.




```{toctree}
:hidden:
:titlesonly:


01_Exact_Distribution_of_a_Sum
02_PGFs_in_NumPy
03_Central_Limit_Theorem
04_SciPy_and_Normal_Curves
05_The_Sample_Mean
06_Confidence_Intervals
07_Exercises
```
