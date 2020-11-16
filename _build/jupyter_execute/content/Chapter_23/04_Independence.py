# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline

## Independence ##

If the elements of $\mathbf{X}$ are mutually independent then $Cov(X_i, X_j) = 0$ for all $i \ne j$ and hence the covariance matrix $\boldsymbol{\Sigma}$ is a diagonal matrix with the $i$th diagonal element equal to $Var(X_i)$.

In the other direction, zero covariance doesn't in general imply independence, and pairwise independence doesn't imply mutual independence. But once again, the multivariate normal turns out to have a wonderful property:

If $\mathbf{X}$ is multivariate normal and its elements are pairwise uncorrelated – that is, $Cov(X_i, X_j) = 0$ for all 
$i \ne j$ – then the elements of $\mathbf{X}$ are mutually independent.

That is, **multivariate normal random variables are independent if and only if they are uncorrelated.**

This is easy to see from the form of the density of $\mathbf{X}$. If $\boldsymbol{\Sigma}$ is a diagonal matrix then so is $\boldsymbol{\Sigma}^{-1}$. The $i$th diagonal element of $\boldsymbol{\Sigma}^{-1}$ is $1/\sigma_i^2$ where $\sigma_i^2 = Var(X_i)$. So

$$
(\mathbf{x} - \boldsymbol{\mu})\boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) ~ = ~ \sum_{i=1}^n \frac{(x_i - \boldsymbol{\mu}(i))^2}{\sigma_i^2}
$$

and therefore

$$
\exp\big{(} -\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})\boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \big{)} ~ = ~ \prod_{i=1}^n \exp\big{(}-\frac{1}{2} \big{(}\frac{x_i - \boldsymbol{\mu}(i)}{\sigma_i}\big{)}^2\big{)}
$$

In the constant of integration, $\det(\boldsymbol{\Sigma}) = \sigma_1^2 \sigma_2^2 \cdots \sigma_n^2$.

Therefore the density of $\mathbf{X}$ is the product of the marginal normal densities.

Thus for a multivariate normal random vector, "pairwise uncorrelated" is equivalent to "mutually independent" and is a much easier condition to check.

The result makes it easy to see if two coordinates of a multivariate normal vector are independent. All you have to do is find the covariance between the two. If the covariance is $0$, they are independent. 

### Sum and Difference, Revisited ###
Let $\mathbf{X} = [X_1, X_2]^T$ have a bivariate normal distribution. Let $S = X_1 + X_2$ and $D = X_1 - X_2$. We know that $S$ and $D$ have a bivariate normal distribution and that

$$
Cov(S, D) ~ = ~ Var(X_1) - Var(X_2)
$$

If $X_1$ and $X_2$ have the same variance then $S$ and $D$ are uncorrelated, and hence also independent by what we have just proved. 

Thus for example the sum and difference of two i.i.d. normal random variables are independent.

You have shown in exercises that the sum and differences of any two i.i.d. random variables are uncorrelated. If in addition the two variables are normal, then their sum and difference are independent, not just uncorrelated.