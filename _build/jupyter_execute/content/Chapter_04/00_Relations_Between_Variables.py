# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline

# Relations Between Variables #

Many questions in data science have at their center a question about the relation between variables. 
- How can attributes be used to tell whether or not a cell is cancerous?
- What is the relation between average income and water usage in Californian counties?
- Do car buyers pay more for good mileage or for rapid acceleration?
You encountered these and many other such questions in Data 8.

Probability theory helps us pose and answer precise questions about the relation between random variables. In particular, it helps us understand the conditional behavior of one set of random variables given the values of another set.

In this chapter we will study multiple random variables defined on the same set of outcomes.




```{toctree}
:hidden:
:titlesonly:


01_Joint_Distributions
02_Examples
03_Marginal_Distributions
04_Conditional_Distributions
05_Dependence_and_Independence
06_Exercises
```
