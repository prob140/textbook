---
interact_link: notebooks/Chapter_24/02_Linear_Least_Squares.ipynb
title: '24.2 Least Squares Linear Predictor'
permalink: 'chapters/Chapter_24/02_Linear_Least_Squares'
previouschapter:
  url: chapters/Chapter_24/01_Bivariate_Normal_Distribution
  title: '24.1 Bivariate Normal Distribution'
nextchapter:
  url: chapters/Chapter_24/03_Regression_and_Bivariate_Normal
  title: '24.3 Regression and the Bivariate Normal'
redirect_from:
  - 'chapters/chapter-24/02-linear-least-squares'
---

## Least Squares Linear Predictor

In this section we are going to step away from the bivariate normal distribution and see if we can identify the best among all linear predictors of one numerical variable based on another, regardless of the joint distribution of the two variables.

For jointly distributed random variables $X$ and $Y$, you know that $E(Y \mid X)$ is the least squares predictor of $Y$ based on functions of $X$. We will now restrict the allowed functions to linear functions and see if we can find the best among those. In the next section we will see the connection between this best linear predictor, the best among all predictors, and the bivariate normal distribution.

### Minimizing Mean Squared Error
Let $h(X) = aX + b$ for constants $a$ and $b$, and let $MSE(a, b)$ denote $MSE(h)$.

$$
MSE(a, b) ~ = ~ E\big{(} (Y - (aX + b))^2 \big{)} 
$$

To find the *least squares linear predictor*, we have to minimize this MSE over all $a$ and $b$. We will do this using calculus, in two steps:
- Fix $a$ and find the value $b_a^\*$ that minimizes $MSE(a, b)$ for that fixed value of $a$.
- Then plug in the minimizing value $b_a^\*$ in place of $b$ and minimize $MSE(a, b_a^\*)$ with respect to $a$.

#### Step 1
Fix $a$ and minimize $MSE(a, b)$ with respect to $b$.

$$
\begin{align*}
MSE(a, b) ~ &= ~ E\big{(} ((Y-aX) - b)^2\big{)}\\
&= ~ E((Y-aX)^2) -2bE(Y-aX) + b^2
\end{align*}
$$

Differentiate this with respect to $b$.

$$
\frac{d}{db} MSE(a, b) ~ = ~ -2E(Y-aX) + 2b
$$

Set this equal to 0 and solve to see that the minimizing value of $b$ for the fixed value of $a$ is

$$
b_a^* ~ = ~ E(Y-aX) ~ = ~ E(Y) - aE(X)
$$

#### Step 2
Now we have to minimize the following function with respect to $a$:

$$
\begin{align*}
E\big{(} (Y - (aX + b_a^*))^2 \big{)} ~ &= ~
E\big{(} (Y - (aX + E(Y) - aE(X)))^2 \big{)} \\
&= ~ E\Big{(} \big{(} (Y - E(Y)) - a(X - E(X))\big{)}^2 \Big{)} \\
&= ~ E\big{(} (Y - E(Y))^2 \big{)} - 2aE\big{(} (Y - E(Y))(X - E(X)) \big{)} + a^2E\big{(} (X - E(X))^2 \big{)} \\
&= ~ Var(Y) - 2aCov(X, Y) + a^2Var(X)
\end{align*}
$$

The derivative with respect to $a$ is $-2Cov(X, Y) + 2aVar(X)$. Thus the minimizing value of $a$ is

$$
a^* ~ = ~ \frac{Cov(X, Y)}{Var(X)} 
$$

At this point we should check that what we have is a minimum, not a maximum, but based on your experience with prediction you might just be willing to accept that we have a minimum. If you're not, then differentiate again and look at the sign of the resulting function.

### Slope and Intercept of the Regression Line
The least squares straight line is called the *regression line*.You now have a proof of its equation, familiar to you from Data 8. Let $r_{X,Y}$ be the correlation between $X$ and $Y$. Then the slope and intercept are given by

$$
\begin{align*} 
\text{slope of regression line} ~ &= ~ \frac{Cov(X,Y)}{Var(X)} ~ = ~ r_{X,Y} \frac{\sigma_Y}{\sigma_X} \\ \\
\text{intercept of regression line} ~ &= ~ E(Y) - \text{slope} \cdot E(X)
\end{align*}
$$

### Regression in Standard Units
If both $X$ and $Y$ are measured in standard units, then the slope of the regression line is the correlation $r_{X,Y}$ and the intercept is 0. 

In other words, given that $X = x$ standard units, the predicted value of $Y$ is $r_{X,Y}x$ standard units. When $r_{X,Y}$ is positive but not 1, this result is called the *regression effect*: the predicted value of $Y$ is closer to 0 than the given value of $X$.

### The Line and the Shape of the Scatter Diagram

The calculations above show that:

- The regression line goes through the point $(E(X), E(Y))$.

- The equation of the regression line holds regardless of the joint distribution of $X$ and $Y$. 

- There is always a best straight line predictor among all straight lines, regardless of the relation between $X$ and $Y$. If the relation isn't roughly linear you won't want to use the best straight line for predictions, because the best straight line is only best among a bad class of predictors. But it exists.
