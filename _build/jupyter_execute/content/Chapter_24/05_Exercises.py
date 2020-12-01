## Exercises ##

**1.** Let $X$ and $Y$ be jointly distributed random variables and let $\hat{Y}$ be the linear regression estimate of $Y$ based on $X$. Show that the mean squared error of this estimate is $(1 - r^2)Var(Y)$ where $r$ is the correlation between $X$ and $Y$. This leads to the Data 8 formula for the [SD of the residuals](https://www.inferentialthinking.com/chapters/15/6/Numerical_Diagnostics.html#SD-of-the-Residuals) in simple linear regression. 

[Use [Alternative Form I](http://prob140.org/textbook/content/Chapter_24/04_Regression_Equation.html#regression-equation-alternative-form-i) of the regression equation, and preserve deviations as we did [here](http://prob140.org/textbook/content/Chapter_24/01_Linear_Least_Squares.html#step-2).]

**2.** Let $X$ and $Y$ be standard bivariate normal with correlation $\rho$.

(a) Suppose I ask you for the least squares estimate of $Y$ based on $X$, but I don't tell you $X$. What is your estimate, and what is its mean squared error?

(b) Suppose I now show you $X$. Now what is your least squares estimate of $Y$, and what is its mean squared error?

(c) What is your least squares estimate of $Y$ based only on linear functions of $X$, and what is its mean squared error?

**3.** Let $(X, Y)$ be the weight and height of a person picked at random from a population, and suppose the distribution of $(X, Y)$ is bivariate normal with correlation 0.6. Suppose also that

- $X$ has mean 150 pounds and SD 25 pounds
- $Y$ has mean 68 inches and SD 3 inches

Sketch the conditional density of $Y$ given $X = 170$ pounds. Mark the numerical values of the conditional mean and SD appropriately on your sketch.

**4.** Let $X$ and $Y$ have a bivariate normal distribution (not necessarily standard) with correlation $\rho \in (0, 1)$. Suppose you are given that $X$ is on the 30th percentile.

(a) Pick the right option for the least squares estimate of $Y$, and explain.

(i) Below the 30th percentile

(ii) On the 30th percentile

(iii) Above the 30th percentile

(b) Write a single math expression for the percentile rank corresponding to the least squares estimate of $Y$. Your answer can involve $\rho$ and the standard normal cdf $\Phi$.

**5.** Let $X$ and $Y$ be standard bivariate normal with correlation $\rho \in (0, 1)$.

(a) Without calculation, pick the right option and explain. $P(X > 0, Y < 0)$ is

(i) less than $0.25$

(ii) equal to $0.25$

(iii) greater than $0.25$

(b) Now find $P(X > 0, Y < 0)$ in terms of $\rho$.

[No integration is needed. Write $Y$ in terms of $X$ and standard normal $Z$ independent of $X$, sketch the region, and use what you know about the joint density of $(X, Z)$.]

**6.** Let $X$ and $Y$ be standard bivariate normal with correlation $\rho$. Find $E(\max(X, Y))$. The easiest way is to use the fact that for any two numbers $a$ and $b$, $\max(a, b) = (a + b + \vert a - b \vert)/2$. Check the fact first, and then use it.

**7.** Suppose that $X$ is normal $(\mu_X, \sigma_X^2$), $Y$ is normal $(\mu_Y, \sigma_Y^2)$, and the two random variables are independent. Let $S = X+Y$.

(a) Find the conditional distribution of $X$ given $S=s$.

(b) Find the least squares predictor of $X$ based on $S$ and provide its mean squared error.

(c) Find the least squares linear predictor of $X$ based on $S$ and provide its mean squared error.