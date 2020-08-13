# HIDDEN
from datascience import *
from prob140 import *
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline

# Multiple Regression #

The most common use of regression is to predict the value of a numerical variable based on the values of several other variables. In our probabilistic setting, we have a finite number of jointly distributed random variables and the goal is to predict one of them based on all the others. 

In the previous chapters we did this in the case where there was just one predcitor variable. In particular, we developed the theory of simple linear regression.

In this chapter we will extend our calculations for simple regression to the case of multiple regression. Indeed, we will capitalize on our work on simple regression to make an inspired guess for how multiple regression must work. Then we will check that our guess is correct.




```{toctree}
:hidden:
:titlesonly:


01_Bilinearity_in_Matrix_Notation
02_Best_Linear_Predictor
03_Multivariate_Normal_Conditioning
04_Multiple_Regression
05_Further_Review_Exercises
```
