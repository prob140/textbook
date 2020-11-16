## Exercises ##

**1.** A random vector $\mathbf{Y} = [Y_1 ~~ Y_2 ~~ \cdots ~~ Y_n]^T$ has mean vector $\boldsymbol{\mu}$ and covariance matrix $\sigma^2 \mathbf{I}_n$ where $\sigma > 0$ is a number and $\mathbf{I}_n$ is the $n \times n$ identity matrix. 

(a) Pick one option and explain: $Y_1$ and $Y_2$ are

$~~~~~$ (i) independent. $~~~~~~~~$ (ii) uncorrelated but might not be independent. $~~~~~~~~$ (iii) not uncorrelated.

(b) Pick one option and explain: $Var(Y_1)$ and $Var(Y_2)$ are

$~~~~~$ (i) equal. $~~~~~~~~$ (ii) possibly equal, but might not be. $~~~~~~~~$ (iii) not equal.

(c) For $m \le n$ let $\mathbf{A}$ be an $m \times n$ matrix of real numbers, and let $\mathbf{b}$ be an $m \times 1$ vector of real numbers. Let $\mathbf{V} = \mathbf{AY} + \mathbf{b}$. Find the mean vector $\boldsymbol{\mu}_\mathbf{V}$ and covariance matrix $\boldsymbol{\Sigma}_\mathbf{V}$ of $\mathbf{V}$.

(d) Let $\mathbf{c}$ be an $m \times 1$ vector of real numbers and let $W = \mathbf{c}^T\mathbf{V}$ for $\mathbf{V}$ defined in Part (c). In terms of $\mathbf{c}$, $\boldsymbol{\mu}_\mathbf{V}$ and $\boldsymbol{\Sigma}_\mathbf{V}$, find $E(W)$ and $Var(W)$.

**2.** Let $[U ~ V ~ W]^T$ be multivariate normal with mean vector $[0 ~ 0 ~ 0]^T$ and covariance matrix 
$\begin{bmatrix}
1 & \rho_1 & \rho_2 \\
\rho_1 & 1 & \rho_3 \\
\rho_2 & \rho_3 & 1
\end{bmatrix}$

(a) What is the distribution of $U$?

(b) What is the distribution of $U+2V$?

(c) What is the joint distribution of $U$ and $U+2V$?

(d) Under what condition on the parameters is $U$ independent of $U+2V$?

**3.** Let $[X_1 ~~ X_2 ~~ X_3]^T$ be multivariate normal with mean vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$ given by

$$
\boldsymbol{\mu} ~ = ~
\begin{bmatrix}
\mu \\
\mu \\
\mu
\end{bmatrix}
~~~~~~~~~~~
\boldsymbol{\Sigma} ~ = ~ 
\begin{bmatrix}
\sigma_1^2 & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_2^2 & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_3^2
\end{bmatrix}
$$

Find $P\big{(} (X_1 + X_2)/2 < X_3 + 1 \big{)}$.

**4.** Let $X$ be standard normal. Construct a random variable $Y$ as follows:

- Toss a fair coin.
- If the coin lands heads, let $Y = X$.
- If the coin lands tails, let $Y = -X$.

(a) Find the cdf of $Y$ and hence identify the distribution of $Y$.

(b) Find $E(XY)$ by conditioning on the result of the toss.

(c) Are $X$ and $Y$ uncorrelated? 

(d) Are $X$ and $Y$ independent?

(e) Is the joint distribution of $X$ and $Y$ bivariate normal?

**5.** **Normal Sample Mean and Sample Variance, Part 1**

Let $X_1, X_2, \ldots, X_n$ be i.i.d. with mean $\mu$ and variance $\sigma^2$. Let

$$
\bar{X} ~ = ~ \frac{1}{n} \sum_{i=1}^n X_i
$$

denote the sample mean and 

$$
S^2 ~=~ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

denote the sample variance as defined earlier in the course.

(a) For $1 \le i \le n$ let $D_i = X_i - \bar{X}$. Find $Cov(D_i, \bar{X})$.

(b) Now assume in addition that $X_1, X_2, \ldots, X_n$ are i.i.d. normal $(\mu, \sigma^2)$. What is the joint distribution of $\bar{X}, D_1, D_2, \ldots, D_{n-1}$? Explain why $D_n$ isn't on the list.

(c) True or false (justify your answer): The sample mean and sample variance of an i.i.d. normal sample are independent of each other.

**6.** **Normal Sample Mean and Sample Variance, Part 2**

(a) Let $R$ have the chi-squared distribution with $n$ degrees of freedom. What is the mgf of $R$?

(b)
For $R$ as in Part (a), suppose
$R = V + W$ where $V$ and $W$ are independent and $V$ has the chi-squared 
distribution with $m < n$ degrees of freedom. Can you identify the distribution of $W$? Justify your answer.

(c) Let $X_1, X_2, \ldots , X_n$ be any sequence of random variables and let $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$. Let $\alpha$ be
any constant. Prove the *sum of squares decomposition*

$$
\sum_{i=1}^n (X_i - \alpha)^2 ~=~ \sum_{i=1}^n (X_i - \bar{X})^2 ~+~ n(\bar{X} - \alpha)^2
$$

(d) Now let $X_1, X_2, \ldots , X_n$ be i.i.d. normal with mean $\mu$ and variance $\sigma^2 > 0$. Let $S^2$ be the "sample variance" defined by 

$$
S^2 ~=~ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

Find a constant $c$ such that $cS^2$ has a chi-squared distribution. Provide the degrees of freedom.

[Use Parts (b) and (c) as well as the result of the previous exercise.]