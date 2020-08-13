# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline
import math
from scipy import stats

# Collections of Events #

Most questions in data science involve multiple variables and events. Random variables and their joint distributions give us a way to set up probabilistic models for how our data originate. Some techniques are particularly useful for working with large collections of variables and events. These include:
- Using bounds when exact values are difficult to calculate
- Noticing patterns when working with small collections and then generalizing to larger ones
- Using symmetry, both for insight and for simplifying calculation

In this chapter we will study powerful examples of all these techniques. 


```{toctree}
:hidden:
:titlesonly:


01_Bounding_the_Chance_of_a_Union
02_Inclusion_Exclusion
03_The_Matching_Problem
04_Sampling_Without_Replacement
05_Review_Problems_Set_1
```
