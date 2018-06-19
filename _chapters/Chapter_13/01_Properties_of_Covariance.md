---
interact_link: notebooks/Chapter_13/01_Properties_of_Covariance.ipynb
title: '13.1 Properties of Covariance'
previouschapter:
  url: chapters/Chapter_13/00_Variance_Via_Covariance
  title: 'Chapter 13: Variance Via Covariance'
nextchapter:
  url: chapters/Chapter_13/02_Sums_of_IID_Samples
  title: '13.2 Sums of IID Samples'
---

## Properties of Covariance ##

Let's examine how covariance behaves. In the next two sections we will use our observations to calculate variances of sample sums.

Establishing properties of covariance involves simple observations and routine algebra. We have done some of it below, and we expect that you can fill in the rest.

Recall that the covariance of $X$ and $Y$ is 

$$
Cov(X, Y) ~ = ~ E(D_XD_Y) ~ = ~ E[(X - \mu_X)(Y - \mu_Y)]
$$

### Constants Don't Vary ###
That title has a "duh" quality. But it's still worth noting that for any constant $c$,
$$
Cov(X, c) = 0
$$

### Variance is a Covariance ##
Covariance is an extension of the concept of variance, because

$$
Var(X) = E(D_X^2) = E(D_XD_X) = Cov(X, X)
$$

The variance of $X$ is the covariance of $X$ and itself.

### Covariance is Symmetric ###
Clearly $Cov(Y, X) = Cov(X, Y)$. It follows that

$$
Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y) = Var(X) + Var(Y) + Cov(X, Y) + Cov(Y, X)
$$

This way of thinking about the variance of a sum will be useful later.

### Covariance and Expected Products ###
Covariance *is* an expected product: it is the expected product of deviations. It can also be written in terms of the expected product of $X$ and $Y$, as follows.

\begin{align*}
Cov(X, Y) &= E[(X - \mu_X)(Y - \mu_Y)] \\
&= E(XY) - E(X)\mu_Y - \mu_XE(Y) + \mu_X\mu_Y \\
&= E(XY) - \mu_X\mu_Y
\end{align*}

So covariance is the *mean of the product minus the product of the means*. Take $X = Y$ to get the familiar fact that variance is the mean of the square minus the square of the mean.

This result simplifies proofs of facts about covariance, as you will see below. But as a computational tool, it is only useful when the distributions of $X$ and $Y$ are very simple – for example, when each has just a few possible values. In other calculations of covariance it is rarely a good idea to try to use this result. Rather, we will use the properties below.

### Addition Rule ###
A routine application of the property above shows that for any random variables $X$, $Y$, and $Z$,

$$
Cov(X+Y, Z) ~ = ~ Cov(X, Z) + Cov(Y, Z)
$$

Just write $Cov(X+Y, Z) = E[(X+Y)Z] - E(X+Y)E(Z)$, expand both products, and collect terms.

### The Main Property: Bilinearity ###
This is the key to using covariance. First, easy algebra shows that for constants $a$ and $b$,
$$
Cov(aX, bY) = abCov(X, Y)
$$

Put this together with the addition rule to get

$$
Cov(aX + bY, cZ) = acCov(X, Z) + bcCov(Y, Z)
$$

You can see that covariance behaves like products. By induction,

$$
Cov(\sum_{i=1}^n a_iX_i, \sum_{j=1}^m b_jY_j) ~ = ~
\sum_{i=1}^n\sum_{j=1}^m a_ib_jCov(X_i, Y_j)
$$

That might look intimidating, but in fact this property greatly simplifies calculation. It says that you can expand covariance like the product of two sums. For example,

$$
Cov(10X - Y, 3Y + Z) = 30Cov(X, Y) + 10Cov(X, Z) - 3Cov(Y, Y) - Cov(Y, Z)
$$

You can replace $Cov(Y, Y)$ by $Var(Y)$.

These properties simplify calculations. But they don't give a sense of what covariance means. Indeed it's not easy to understand covariance physically as it has nasty units: for example, if $X$ is a weight in kilograms and $Y$ is height in centimeters, then the units of covariance is *kilogram centimeters*. Later in the course we will see how to normalize covariance to get the *correlation coefficient* that you used so often in Data 8. For now, here is a property that begins to show you that covariance can be helpful in quantifying dependence and independence.

### Independent Implies Uncorrelated ###
Let $X$ and $Y$ be independent. Then

\begin{align*}
E(XY) &= \sum_x\sum_y xyP(X=x, Y=y) ~~~~~~ \text{(expectation of a function)} \\
&= \sum_x\sum_y xyP(X=x)P(Y=y) ~~~~ \text{(independence)} \\
&= \sum_x xP(X=x) \sum_y yP(Y=y) \\
&= E(X)E(Y)
\end{align*}

Therefore if $X$ and $Y$ are independent, then $Cov(X, Y) = 0$. We say that $X$ and $Y$ are *uncorrelated*.

We have shown that independent random variables are uncorrelated. But it is not true that uncorrelated random variables have to be independent. You will show this in an exercise.
