---
interact_link: notebooks/Chapter_25/04_Multiple_Regression.ipynb
title: '25.4 Multiple Regression'
permalink: 'chapters/Chapter_25/04_Multiple_Regression'
previouschapter:
  url: chapters/Chapter_25/03_Multivariate_Normal_Conditioning
  title: '25.3 Conditioning and the Multivariate Normal'
nextchapter:
  url: chapters/Chapter_25/05_Further_Review_Exercises
  title: '25.5 Further Review Exercises'
redirect_from:
  - 'chapters/chapter-25/04-multiple-regression'
---

## Multiple Regression

Regression provides one way of predicting a numerical variable, called a *response*, based on other variables called *predictor variables*. The multiple regression model says in essence that

$$
\text{response} ~ = ~ \text{linear combination of predictor variables} + \text{ random noise }
$$

You can think of the first term on the right hand side as a *signal*. The problem is that we don't get to observe the signal. The observed response is the sum of the signal and the noise. The data scientist's task is to use the observations to extract the signal as accurately as possible.

It is worth looking more closely at exactly what is linear in linear regression, now that we are allowing more than one predictor variable. For example, notice that you can fit a quadratic function of $x$ by using the two predictor variables $x_1 = x$ and $x_2 = x^2$. Then the signal

$$
\beta_0 + \beta_1x_1 + \beta_2x_2 ~ = ~ \beta_0 + \beta_1x + \beta_2x^2
$$ 

is a quadratic function of $x$. But it is linear in the coefficients, and it is a linear combination of the two predictor variables $x_1$ and $x_2$.

### The Model

As in all of statistical inference, properties of estimates depend on the assumptions under which they are calculated. The *multiple regression model* is a commonly used set of assumptions that describes a particular kind of linear relation between a numerical response variable and a set of predictor variables. You should use it only if you believe that it makes sense for your data.

The model assumes that there are $n$ individuals, on each of whom you have measured the response and the predictor variables. For $1 \le i \le n$, the relation between the variables is assumed to be

$$
Y_i = \beta_0 + \beta_1x_{i,1} + \beta_2x_{i,2} + \cdots + \beta_{p-1}x_{i,p-1} + \epsilon_i
$$

in the notation described below.

- $x_{i,1}, x_{i,2}, \ldots, x_{i,p-1}$ are the observed constant values of $p-1$ predictor variables for individual $i$. They are not random variables. If you prefer to think of the predictor variables as random, this model assumes that you have conditioned on them.

- The intercept $\beta_0$ and slopes $\beta_1, \beta_2, \ldots, \beta_{p-1}$ are unobservable constants and are parameters of the model. There are $p$ of them, hence the notation $p$ for "parameters".

- $\epsilon_i$ is an unobservable random error that has the normal $(0, \sigma^2)$ distribution for some unobservable $\sigma^2$, and $\epsilon_1, \epsilon_2, \ldots, \epsilon_n$ are i.i.d.

- $Y_i$ is the observable response of individual $i$. It is random because $\epsilon_i$ is one of its components.

We will assume that $n > p$, that is, we will assume we have more individuals than parameters. Indeed in this course it is fine for you to think of $n$ as much larger than $p$. 

Two special cases are already familiar.

#### $p = 1$: Prediction by a Constant
When $p = 1$ there is just one parameter: the intercept. There are no predictor variables at all. The model says that for each individual $i$, the response is $Y_i = \beta_0 + \epsilon_i$. This is a case of trying to estimate the response by a constant. 

#### $p = 2$: Simple Linear Regression
The two parameters are the intercept and a slope. The model says that for each individual $i$, the response is $Y_i = \beta_0 + \beta_1x_{i,1} + \epsilon_i$. That is, the response is the value on a hidden straight line, plus some normal noise. This is the simple regression model you used in Data 8.

For any $p$, the model can be written compactly as

$$
\mathbf{Y} ~ = ~ \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}
$$

in the matrix notation described below.

- The *design matrix* $\mathbf{X}$ is an $n \times p$ matrix of real numbers, not random variables. Column 0 of $\mathbf{X}$ is a vector of 1's and Column $j$ for $1 \le j \le p-1$ consists of the $n$ observations on the $j$th predictor variable. For each $i$ in the range 1 through $n$, Row $i$ contains the values of all the predictor variables for individual $i$.

- The *parameter vector* $\boldsymbol{\beta} = [\beta_0 ~~ \beta_1 ~~ \ldots ~~ \beta_{p-1}]^T$ is a $p \times 1$ vector of the coefficients.

- The *error vector* $\boldsymbol{\epsilon}$ is an $n \times 1$ multivariate normal $(\mathbf{0}, \sigma^2\mathbf{I}_n)$ random vector. Its mean vector is an $n \times 1$ vector of 0's and $\mathbf{I}_n$ is the $n \times n$ identity matrix.

- The *response vector* $\mathbf{Y}$ is a random vector that is the sum of the linear signal $\mathbf{X}\boldsymbol{\beta}$ and the normal noise $\boldsymbol{\epsilon}$.

### Ordinary Least Squares
Based on the observations of the predictor variables and the response, the goal is to find the best estimates of the intercept and slopes in the model.

These estimates can then be used to predict the response of a new individuals, assuming that the model holds for the new individual as well.

We must select a criterion by which we will decide whether one estimate is better than another. To develop one such criterion, start by noting that any linear function of the predictor variables can be written as $\mathbf{X}\boldsymbol{\gamma}$ where $\boldsymbol{\gamma}$ is some $p \times 1$ vector of coefficients. Think of $\mathbf{X}\boldsymbol{\gamma}$ as an estimate of $\mathbf{Y}$. Then the error in the estimate is $\mathbf{Y} - \mathbf{X}\boldsymbol{\gamma}$.

The goal of *ordinary least squares* (OLS) is to find the vector $\boldsymbol{\gamma}$ that minimises the mean squared error

$$
MSE(\boldsymbol{\gamma}) ~ = ~ \frac{1}{n} \sum_{i=1}^n (Y_i - (\mathbf{X}\boldsymbol{\gamma})_i)^2
$$

This is the same as the $\boldsymbol{\gamma}$ that minimizes the sum of squared errors

$$
SSE(\boldsymbol{\gamma}) ~ = ~ \sum_{i=1}^n (Y_i - (\mathbf{X}\boldsymbol{\gamma})_i)^2
$$

Again for compactness it will help to use matrix notation. For an $n \times 1$ vector $\mathbf{w}$, 

$$
\sum_{i=1}^n w_i^2 ~ = ~ \mathbf{w}^T\mathbf{w} ~ = ~ \mathbf{w} \cdot \mathbf{w} ~ = ~ \| \mathbf{w} \|^2
$$

which is sometimes called the *squared norm* of $\mathbf{w}$.

In this notation, the goal of OLS is to find the $p \times 1$ vector $\hat{\boldsymbol{\beta}}$ that minimizes $\| \mathbf{Y} - \mathbf{X}\boldsymbol{\gamma}\|^2$ over all vectors $\boldsymbol{\gamma}$.

Typically you will also have to estimate the unknown error variance $\sigma^2$. But we will not cover that in this class except in the case $p = 1$.

### Estimate of $\boldsymbol{\beta}$

Remember that we have assumed $n > p$. Assume also that $\mathbf{X}$ is of full column rank $p$, that is, none of the predictor variables is a linear combination of the others. By a theorem in linear algebra, it follows that the square matrix $\mathbf{X}^T\mathbf{X}$ has full rank $p$ and is therefore invertible.

The claim is that OLS estimate of $\boldsymbol{\beta}$ is the vector $\hat{\boldsymbol{\beta}}$ defined by

$$
\hat{\boldsymbol{\beta}} ~ = ~ (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
$$

The claim is motivated by our earlier formula 

$$
\mathbf{b} ~ = ~ \boldsymbol{\Sigma}_\mathbf{X}^{-1}\boldsymbol{\Sigma}_\mathbf{XY}
$$

for the coefficients of the least squares linear predictor a random variable $Y$ based on a random vector $\mathbf{X}$. In fact the new formula is an application of the old one but we will prove it afresh in our new setting.

Before we begin the proof, notice that $\hat{\boldsymbol{\beta}}$ is a linear function of $\mathbf{Y}$. This makes it straightforward to identify its distribution, which you will do in exercises.

Also note that the estimated $\mathbf{Y}$ is 

$$
\hat{\mathbf{Y}} ~ = ~ \mathbf{X}\hat{\boldsymbol{\beta}} ~ = ~ \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
$$

which is also a linear function of $\mathbf{Y}$.

### Projection

Define the $i$th *residual* as the prediction error $e_i = Y_i - \hat{Y}_i$. Then the $n \times 1$ vector of residuals is

$$
\mathbf{e} ~ = ~ \mathbf{Y} - \hat{\mathbf{Y}} ~ = ~ \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}
$$

As we have seen repeatedly, the key to least squares is that the prediction error is orthogonal to the space of allowed functions. Our space of allowed functions is all linear functions of $\mathbf{X}$. So we will show:

**The residual vector is orthogonal to each column of $\mathbf{X}$.**

To see this, calculate the $p \times 1$ vector $\mathbf{X}^T\mathbf{e}$. Each of its elements is the dot product of $\mathbf{e}$ and one column of $\mathbf{X}$. We will show that each of the elements is 0.

$$
\mathbf{X}^T\mathbf{e} ~ = ~ \mathbf{X}^T(\mathbf{Y} - \hat{\mathbf{Y}}) ~ = ~ \mathbf{X}^T\mathbf{Y} - \mathbf{X}^T\hat{\mathbf{Y}} ~ = ~ \mathbf{X}^T\mathbf{Y} - \mathbf{X}^T\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y} ~ = ~ \mathbf{X}^T\mathbf{Y} - \mathbf{X}^T\mathbf{Y} ~ = ~ 0
$$

It is important to keep in mind the distinction between the residual vector $\mathbf{e}$ and the error vector $\boldsymbol{\epsilon}$ in the model.

- $\mathbf{e}$ is an observable random vector consisting of the deviations of $\mathbf{Y}$ from the estimated plane $\mathbf{X}\hat{\boldsymbol{\beta}}$. Elements of $\mathbf{e}$ are not independent of each other.

- $\boldsymbol{\epsilon}$ is an unobservable random vector consisting of the deviations of $\mathbf{Y}$ from the true plane $\mathbf{X}\boldsymbol{\beta}$. Elements of $\boldsymbol{\epsilon}$ are mutually independent.

### Least Squares

Let $\boldsymbol{\gamma}$ be any $p \times 1$ vector. Then

$$
\begin{align*}
SSE(\boldsymbol{\gamma}) ~  &= ~ \| \mathbf{Y} - \mathbf{X}\boldsymbol{\gamma} \|^2 \\
&= ~ \| (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) + (\mathbf{X}\hat{\boldsymbol{\beta}} - \mathbf{X}\boldsymbol{\gamma}) \|^2 \\
&= ~ \|\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}\|^2 ~+~ \| \mathbf{X}\hat{\boldsymbol{\beta}} - \mathbf{X}\boldsymbol{\gamma} \|^2 + 2(\mathbf{X}\hat{\boldsymbol{\beta}} - \mathbf{X}\boldsymbol{\gamma})^T(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) \\
&= ~ SSE(\hat{\boldsymbol{\beta}}) ~+~ \| \mathbf{X}\hat{\boldsymbol{\beta}} - \mathbf{X}\boldsymbol{\gamma} \|^2 + 2((\mathbf{X}(\hat{\boldsymbol{\beta}} - \boldsymbol{\gamma}))^T\mathbf{e} \\
&= ~ SSE(\hat{\boldsymbol{\beta}}) ~+~ \| \mathbf{X}\hat{\boldsymbol{\beta}} - \mathbf{X}\boldsymbol{\gamma} \|^2 + 2(\hat{\boldsymbol{\beta}} - \boldsymbol{\gamma})^T\mathbf{X}^T \mathbf{e} \\
&= ~ SSE(\hat{\boldsymbol{\beta}}) ~+~ \| \mathbf{X}\hat{\boldsymbol{\beta}} - \mathbf{X}\boldsymbol{\gamma} \|^2  ~~~~ \text{ by orthogonality} \\
&\ge ~ SSE(\hat{\boldsymbol{\beta}})
\end{align*}
$$

In exercises you will find the distributions of $\hat{\boldsymbol{\beta}}$ of $\hat{\mathbf{Y}}$. Both will depend on the unknown error variance $\sigma^2$. 

### Estimate of $\sigma^2$

It should come as no surprise that under the multiple regression model, the best estimate of $\sigma^2$ has a chi-squared distribution. There is some work involved in establishing that the estimate is

$$
S^2 ~ = ~ \frac{1}{n-p} \sum_{i=1}^n (Y_i - \hat{Y}_i)^2 ~ = ~ \frac{1}{n-p} \| \mathbf{e} \|^2
$$

Some more work establishes that $\frac{n-p}{\sigma^2}S^2$ has the chi-squared $(n-p)$ distribution. 

We'll leave that work for another course. For now, just notice that if the number of data points $n$ is large compared to the number of parameters $p$, then

$$
S^2 ~ = ~ \frac{1}{n-p} \sum_{i=1}^n (Y_i - \hat{Y}_i)^2 ~ \approx ~ \frac{1}{n} \sum_{i=1}^n (Y_i - \hat{Y}_i)^2
$$

which is the natural mean squared error.

#### Special Case
As noted earlier, in the case $p = 1$ you are trying to find the best constant by which to estimate $Y$.

You know that the least squares constant is $\bar{Y}$, and you showed in exercises that 

$$
S^2 ~ = ~ \frac{1}{n-1} \sum_{i=1}^n (Y_i - \bar{Y})^2
$$

is an unbiased estimate of $\sigma^2$. Another exercise is to show that $\frac{n-1}{\sigma^2}S^2$ has the chi-squared $n-1$ distribution under the assumption of normality. This is the special case of the result stated above for general $p$.
