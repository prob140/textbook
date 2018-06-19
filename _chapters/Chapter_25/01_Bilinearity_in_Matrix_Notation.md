---
interact_link: notebooks/Chapter_25/01_Bilinearity_in_Matrix_Notation.ipynb
title: '25.1 Bilinearity in Matrix Notation'
previouschapter:
  url: chapters/Chapter_25/00_Multiple_Regression
  title: 'Chapter 25: Multiple Regression'
nextchapter:
  url: chapters/Chapter_25/02_Best_Linear_Predictor
  title: '25.2 Best Linear Predictor'
---

## Bilinearity in Matrix Notation ##

As a preliminary to regression, we will express bilinearity in a compact form using matrix notation. The results of this section are not new. They are simply restatements of familiar results about variances and covariances, using new notation and matrix representations.

Let $\mathbf{X}$ be a $p \times 1$ vector of predictor variables. We know that for an $m \times p$ matrix $\mathbf{A}$ and an $m \times 1$ vector $\mathbf{b}$,

$$
Var(\mathbf{AX} + \mathbf{b}) ~ = ~ \mathbf{A}\boldsymbol{\Sigma}_\mathbf{X} \mathbf{A}^T
$$

The results below are special cases of this.

### Linear Combinations ###
To define two generic linear combinations of elements of $\mathbf{X}$, let

$$
\mathbf{A} ~ = ~ 
\begin{bmatrix}
a_1 & a_2 & \cdots & a_p \\
c_1 & c_2 & \cdots & c_p 
\end{bmatrix}
~ = ~ 
\begin{bmatrix}
\mathbf{a}^T \\
\mathbf{c}^T
\end{bmatrix}
~~~~~~ \text{and} ~~~~~~
\mathbf{b} ~ = ~
\begin{bmatrix}
b \\
d
\end{bmatrix}
$$
Then
$$
\mathbf{AX} + \mathbf{b} ~ = ~ 
\begin{bmatrix}
a_1X_1 + a_2X_2 + \cdots + a_pX_p + b \\
c_1X_1 + c_2X_2 + \cdots + c_pX_p + d
\end{bmatrix}
~ = ~ 
\begin{bmatrix}
\mathbf{a}^T\mathbf{X} + b \\
\mathbf{c}^T\mathbf{X} + d
\end{bmatrix}
$$

### Covariance of Two Linear Combinations ###
The covariance of the two linear combinations is the $(1, 2)$ element of the covariance matrix of $\mathbf{AX} + \mathbf{b}$, which is the $(1, 2)$ element of $\mathbf{A}\boldsymbol{\Sigma}_\mathbf{X}\mathbf{A}^T$.

$$
Cov(\mathbf{a}^T\mathbf{X} + b, \mathbf{c}^T\mathbf{X} + d) 
~ = ~ \mathbf{a}^T \boldsymbol{\Sigma}_\mathbf{X} \mathbf{c}
$$

### Variance of a Linear Combination ###
The variance of the first linear combination is the $(1, 1)$ element of $\mathbf{A}\boldsymbol{\Sigma}_\mathbf{X}\mathbf{A}^T$.

$$
Var(\mathbf{a}^T\mathbf{X} + b) ~ = ~ 
\mathbf{a}^T \boldsymbol{\Sigma}_\mathbf{X} \mathbf{a}
$$

### Covariance Vector ###
To predict $Y$ based on $\mathbf{X}$ we will need to work with the covariance of $Y$ and each of the elements of $\mathbf{X}$. Let

$$
\sigma_{X_i, Y} ~ = ~ Cov(X_i, Y) 
$$
and define the *covariance vector* of $\mathbf{X}$ and $Y$ to be
$$
\boldsymbol{\Sigma}_{\mathbf{X}, Y} ~ = ~ 
\begin{bmatrix}
\sigma_{X_1, Y} \\
\sigma_{X_2, Y} \\
\vdots \\
\sigma_{X_p, Y}
\end{bmatrix}
$$

It will be convenient to also have a notation for the transpose of the covariance vector:

$$
\boldsymbol{\Sigma}_\mathbf{Y, X} ~ = ~ \boldsymbol{\Sigma}_\mathbf{X, Y}^T ~ = ~
[\sigma_{X_1, Y} ~ \sigma_{X_2, Y} ~ \ldots ~ \sigma_{X_p, Y}]
$$

By the linearity of covariance,
$$
Cov(\mathbf{a}^T\mathbf{X}, Y) ~ = ~ \mathbf{a}^T \boldsymbol{\Sigma}_{\mathbf{X}, Y}
$$
