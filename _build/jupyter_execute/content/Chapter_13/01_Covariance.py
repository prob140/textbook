# HIDDEN
import warnings
warnings.filterwarnings('ignore')
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline

# Covariance #

Let $X$ be a random variable. In what follows, we will use some familiar shorthand:

- $\mu_X = E(X)$, $\sigma_X = SD(X)$

Let $D_X = X - \mu_X$ denote the deviation of $X$ from its mean. Then the variance of $X$ can be written as

$$
Var(X) = \sigma_X^2 = E(D_X^2)
$$

# VIDEO: Covariance: Definition

from IPython.display import YouTubeVideo

YouTubeVideo('0yvoSUYo2GY')

### Variance of a Sum ###

Now let $X$ and $Y$ be two random variables on the same space, and let $S = X+Y$. Then $E(S) = \mu_X + \mu_Y$, and the deviation of $S$ is the sum of the deviations of $X$ and $Y$:

$$
D_S ~ = ~ S - \mu_S ~ = ~ X + Y - (\mu_X + \mu_Y) ~ = ~ D_X + D_Y
$$

This gives us some insight into the variance of the sum $S$.

$$
\begin{align*}
Var(S) &= E(D_S^2) \\
&= E[(D_X + D_Y)^2] \\
&= E(D_X^2) + E(D_Y^2) + 2E(D_XD_Y) \\
&= Var(X) + Var(Y) + 2E(D_XD_Y)
\end{align*}
$$

The first thing to note is that while the expectation of a sum is the sum of the expectations, the calculation above shows that the variance of a sum is in general **not** the sum of the variances. There's an extra term. 

To calculate the variance of a sum, we have to understand that extra term. 

### Covariance ###

The *covariance of $X$ and $Y$*, denoted $Cov(X, Y)$, is the expected product of the deviations of $X$ and $Y$:

$$
Cov(X, Y) ~ = ~ E(D_XD_Y) ~=~ E\big{(} (X - \mu_X)(Y - \mu_Y) \big{)}
$$

The expectation and variance of $X$ are based on the distribution of $X$ alone. The expectation and variance of $Y$ are based on the distribution of $Y$ alone. But covariance depends on the *joint* distribution of $X$ and $Y$ and thus takes into account the relation between $X$ and $Y$.

Covariance has two main uses. First, it is a tool for calculating the variance of a sum. The fundamental calculation is the one we did above. Here is the result again, using the language of covariance.

$$
Var(X+Y) ~ = ~ Var(X) + Var(Y) + 2Cov(X, Y)
$$

```{admonition} Quick Check
Apply the definition of covariance to recognize $Cov(X, X)$ as a quantity you know from earlier chapters. Which quantity is it?

```

```{admonition} Answer
:class: dropdown
$Var(X)$

```

```{admonition} Quick Check
Find $Var(2X)$ in two ways:

(a) by using linear transformation rules

(b) by writing $Var(2X) = Var(X+X)$ and applying the formula for the variance of a sum


```

```{admonition} Answer
:class: dropdown
Both answers are $4Var(X)$

```

The focus of this chapter is utilizing covariance to find variances of sums. But covariance has a second important application, which we will study later in the course. Here is a preview.

# VIDEO: Covariance: Main Uses

YouTubeVideo('yJ580tGWdGg')

### Correlation ###

Covariance has strange units. If $X$ is measured in pounds and $Y$ in inches then $Cov(X,Y)$ is measured in pound-inches which are hard to understand. But we can get rid of the units of covariance by dividing it by the two standard deviations, and then something wonderful happens.

$$
\frac{Cov(X, Y)}{\sigma_X\sigma_Y} ~ = ~ \frac{E\big{(} (X - \mu_X)(Y - \mu_Y) \big{)}}{\sigma_X\sigma_Y} ~ = ~ 
E \big{(} \frac{X-\mu_X}{\sigma_X} \cdot \frac{Y-\mu_Y}{\sigma_Y} \big{)}
$$

This is the *mean of the products of standard units* which you will recognize from Data 8 as the definition of correlation.

The *correlation* between random variables $X$ and $Y$ is defined as the normalized covariance:

$$
r(X, Y) ~ = ~ \frac{Cov(X, Y)}{\sigma_X\sigma_Y}
$$

As you know, correlation is widely used in data analysis and inference. We will return to it when we study prediction. For now, you will just establish its basic properties in exercises.