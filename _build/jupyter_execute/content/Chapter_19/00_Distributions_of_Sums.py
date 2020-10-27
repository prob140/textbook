# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline
import math
from scipy import stats

# Distributions of Sums #

This chapter provides some general methods for working with sums of random variables, whether discrete or continuous. 

We will start with the continuous analog of the convolution formula for the distribution of a sum of two independent discrete random variables.

We will then develop a more powerful version of the probability generating function that we defined earlier to study sums of independent random variables with finitely many non-negative integer values. The new version, called the *moment generating function,* will apply to discrete as well as continuous random variables, with finite or infinite sets of possible values.




```{toctree}
:hidden:
:titlesonly:


01_Convolution_Formula
02_Moment_Generating_Functions
03_MGFs_Normal_and_the_CLT
04_Chernoff_Bound
05_Exercises
```
