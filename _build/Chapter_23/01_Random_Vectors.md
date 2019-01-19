---
redirect_from:
  - "/chapter-23/01-random-vectors"
interact_link: notebooks/Chapter_23/01_Random_Vectors.ipynb
title: 'Random Vectors'
prev_page:
  url: /Chapter_23/00_Multivariate_Normal_RVs
  title: 'Chapter 23: Jointly Normal Random Variables'
next_page:
  url: /Chapter_23/02_Multivariate_Normal_Distribution
  title: 'Multivariate Normal Distribution'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## Random Vectors

A *vector valued random variable*, or more simply, a *random vector*, is a list of random variables defined on the same space. We will think of it as a column.

$$
\mathbf{X} ~ = ~ 
\begin{bmatrix}
X_1 \\
X_2 \\
\vdots \\
X_n
\end{bmatrix}
$$

For ease of display, we will sometimes write $\mathbf{X} = [X_1 X_2 \ldots X_n]^T$ where $\mathbf{M}^T$ is notation for the transpose of the matrix $\mathbf{M}$.

The *mean vector* of $\mathbf{X}$ is $\boldsymbol{\mu} = [\mu_1 ~ \mu_2 ~ \ldots ~ \mu_n]^T$ where $\mu_i = E(X_i)$.

The *covariance matrix* of $\mathbf{X}$ is the $n \times n$ matrix $\boldsymbol{\Sigma}$ whose $(i, j)$ element is $Cov(X_i, X_j)$. 

The $i$th diagonal element of $\boldsymbol{\Sigma}$ is the variance of $X_i$. The matrix is symmetric because of the symmetry of covariance.

### Linear Transformation: Mean Vector
Let $\mathbf{A}$ be an $m \times n$ numerical matrix and $\mathbf{b}$ an $m \times 1$ numerical vector. Consider the $m \times 1$ random vector  $\mathbf{Y} = \mathbf{AX} + \mathbf{b}$. Then the $i$th element of $\mathbf{Y}$ is 

$$
Y_i ~ = ~ \mathbf{A}_{i*}\mathbf{X} + \mathbf{b}(i)
$$ 

where $\mathbf{A}_{i*}$ denotes the $i$th row of $\mathbf{A}$ and $\mathbf{b}(i)$ denotes the $i$th element of $\mathbf{b}$. Written longhand,

$$
Y_i ~ = ~ a_{i1}X_1 + a_{i2}X_2 + \cdots + a_{in}X_n + b_i
$$

where $a_{ij}$ is the $(i, j)$ entry of $\mathbf{A}$ and $b_i = \mathbf{b}(i)$.

Thus $Y_i$ is a linear combination of the elements of $\mathbf{X}$. Therefore by linearity of expectation,

$$
E(Y_i) ~ = ~ \mathbf{A}_{i*} \boldsymbol{\mu} + \mathbf{b}(i)
$$

Let $\boldsymbol{\mu}_\mathbf{Y}$ be the mean vector of $\mathbf{Y}$. Then by the calculation above,

$$
\boldsymbol{\mu}_\mathbf{Y} ~ = ~ \mathbf{A} \boldsymbol{\mu} + \mathbf{b}
$$


### Linear Transformation: Covariance Matrix

$Cov(Y_i, Y_j)$ can be calculated using bilinearity of covariance.

$$
\begin{align*}
Cov(Y_i, Y_j) ~ &= ~ Cov(\mathbf{A}_{i*}\mathbf{X}, \mathbf{A}_{j*}\mathbf{X}) \\
&= ~ Cov\big{(} \sum_{k=1}^n a_{ik}X_k, \sum_{l=1}^n a_{jl}X_l \big{)} \\
&= ~ \sum_{k=1}^n\sum_{l=1}^n a_{ik}a_{jl}Cov(X_k, X_l) \\
&= ~ \sum_{k=1}^n\sum_{l=1}^n a_{ik}Cov(X_k, X_l)t_{lj} ~~~~~ \text{where } t_{lj} = \mathbf{A}^T(l, j) \\
\end{align*}
$$

This is the $(i, j)$ element of $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^T$. So if $\boldsymbol{\Sigma}_\mathbf{Y}$ denotes the covariance matrix $\mathbf{Y}$, then

$$
\boldsymbol{\Sigma}_\mathbf{Y} ~ = ~ \mathbf{A} \boldsymbol{\Sigma} \mathbf{A}^T
$$

### Constraints on $\boldsymbol{\Sigma}$
We know that $\boldsymbol{\Sigma}$ has to be symmetric and that all the elements on its main diagonal must be non-negative. Also, no matter what $\mathbf{A}$ is, the diagonal elements of $\boldsymbol{\Sigma}\_\mathbf{Y}$ must all be non-negative as they are the variances of the elements of $\mathbf{Y}$. By the formula for $\boldsymbol{\Sigma}_\mathbf{Y}$ this means

$$
\mathbf{a} \boldsymbol{\Sigma} \mathbf{a}^T ~ \ge ~ 0 ~~~~ \text{for all } 1\times n \text{ vectors } \mathbf{a}
$$

which is the same as saying

$$
\mathbf{a}^T \boldsymbol{\Sigma} \mathbf{a} ~ \ge ~ 0 ~~~~ \text{for all } n\times 1 \text{ vectors } \mathbf{a}
$$

because $\mathbf{a} \boldsymbol{\Sigma} \mathbf{a}^T$ is a scalar and therefore the same as its transpose.

That is, $\boldsymbol{\Sigma}$ must be positive semidefinite. Usually, we will be working with positive definite covariance matrices, because if $\mathbf{a}^T \boldsymbol{\Sigma} \mathbf{a} = 0$ for some $\mathbf{a}$ then some linear combination of the elements of $\mathbf{X}$ is constant. Hence you can write some of the elements as linear combinations of the others and just study a reduced set of elements.
