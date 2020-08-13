# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline
import math
from scipy import stats
from scipy import misc

# Reversing Markov Chains #

What do stock markets, mutating viruses, and computer search engines have in common? They have all been analyzed using Markov Chain models. Understanding the long run behavior of Markov Chains helps us understand many different random phenomena.

In data science, Markov Chains are also used for quite a different purpose. Markov Chains help data scientists draw random samples from distributions that are too complicated for standard sampling methods to handle. Markov Chains can also be used to approximate expectations of random quantities whose distributions are either very complicated or involve unknown quantities that are too difficult to estimate using standard methods.

Sometimes, this can be achieved by creating a Markov Chain that has the complicated distribution as its stationary distribution, and then running the chain for a long time till it gets close to stationarity. This method is called Markov Chain Monte Carlo, abbreviated to MCMC. Surprisingly, it involves understanding what happens when Markov Chains are run backwards, that is, when they are *reversed*.

To understand and implement MCMC algorithms you have to study the reversibility of Markov Chains and also do the computations. In this chapter and the accompanying lab we will give you a brief introduction to this area of data science. 




```{toctree}
:hidden:
:titlesonly:


01_Detailed_Balance
02_Reversibility
03_Code_Breaking
04_Markov_Chain_Monte_Carlo
05_Review_Conditioning_and_MC
```
