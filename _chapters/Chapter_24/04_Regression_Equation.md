---
interact_link: notebooks/Chapter_24/04_Regression_Equation.ipynb
title: '24.4 The Regression Equation'
permalink: 'chapters/Chapter_24/04_Regression_Equation'
previouschapter:
  url: chapters/Chapter_24/03_Regression_and_Bivariate_Normal
  title: '24.3 Regression and the Bivariate Normal'
nextchapter:
  url: chapters/Chapter_25/00_Multiple_Regression
  title: 'Chapter 25: Multiple Regression'
redirect_from:
  - 'chapters/chapter-24/04-regression-equation'
---

## The Regression Equation

The equation of the regression line for predicting $Y$ based on $X$ can be written in several equivalent ways. The regression equation, and the error in the regression estimate, are best understood in standard units. All the other representations follow by straightforward algebra.

Let $X$ and $Y$ be bivariate normal with parameters $(\mu_X, \mu_Y, \sigma_X^2, \sigma_Y^2, \rho)$. Then, as we have seen, the best predictor $E(Y \mid X)$ is a linear function of $X$ and hence the formula for $E(Y \mid X)$ is also the equation of the regression line.

### In Standard Units
Let $X^\*$ be $X$ in standard units and $Y^\*$ be $Y$ in standard units. The regression equation is

$$
E(Y^* \mid X^*) ~ = ~ \rho X^*
$$

and the amount of error in the prediction is measured by

$$
SD(Y^* \mid X^*) ~ = ~ \sqrt{1 - \rho^2}
$$

The conditional SD is in the same units as the prediction. The conditional variance is

$$
Var(Y^* \mid X^*) ~ = ~ 1 - \rho^2
$$

We know more than just the conditional expectation and conditional variance. We know that the conditional distribution of $Y^\*$ given $X^\*$ is normal. This allows us to find conditional probabilities given $X^\*$, by the usual normal curve methods. For example, 

$$
P(Y^* < y^* \mid X^* = x^*) ~ = ~ \Phi \big{(} \frac{y^* - \rho x^*}{\sqrt{1-\rho^2}} \big{)}
$$

In one of Galton's famous data sets, the distribution of the heights of father-son pairs was roughly bivariate normal with a correlation of 0.5. Of the fathers whose heights were two SDs above average, about what percent had sons whose heights were more than 2 SDs above average?

By the regression effect, you know this answer has to be less than 50%. If $Y^\*$ denotes the height of a randomly picked son in standard units, and $X^\*$ the height of his father in standard units, then the proportion is approximately

$$
P(Y^* > 2 \mid X^* = 2) ~ = ~ 1 - \Phi \big{(} \frac{2 - 0.5\times2}{\sqrt{1-0.5^2}} \big{)}
$$

which is approximately 12.4%.



{:.input_area}
```python
1 - stats.norm.cdf(2, 0.5*2, np.sqrt(1-0.5**2))
```





{:.output_data_text}
```
0.12410653949496186
```



### In the Original Units
Usually, you want to make predictions in the units in which the data were measured. Before changing units in the formulas above, keep in mind that conditioning on $X$ is equivalent to conditioning on $X^\*$. If you know the value of either of $X$ or $X^\*$, you also know the other.

The regression equation is

$$
\begin{align*}
E(Y \mid X) ~ &= ~ E(\sigma_Y Y^* + \mu_Y \mid X) \\
&= ~ \sigma_Y E(Y^* \mid X) + \mu_Y \\
&= ~ \sigma_Y \rho \big{(} \frac{X - \mu_X}{\sigma_X} \big{)} + \mu_Y \\
&= ~ \rho \frac{\sigma_Y}{\sigma_X} X + \big{(} \mu_Y - \rho\frac{\sigma_Y}{\sigma_X}\mu_X \big{)}
\end{align*}
$$

which is the same as the equation of the least squares line we had derived earlier without any assumptions about the joint distribution of $X$ and $Y$. This confirms our observation that if $X$ and $Y$ are bivariate normal, the best linear predictor is the best among all predictors.

The amount of error in the prediction is measured by

$$
SD(Y \mid X) ~ = ~ SD(\sigma_Y Y^* + \mu_Y \mid X) ~ = ~ 
\sigma_Y SD(Y^* \mid X) ~ = ~ \sqrt{1-\rho^2}\sigma_Y
$$

and

$$
Var(Y \mid X) = (1 - \rho^2)\sigma_Y^2
$$

The conditional distribution of $Y$ given $X$ is normal with the mean and variance calculated above.

### An Alternative Form
When there are just two variables, the matrix formulation of the bivariate normal is hardly necessary. But it is worth writing the regression estimate and the conditional variance using only the parameters of the multivariate normal: the mean vector and covariance matrix. This effort will be rewarded in the next chapter because exactly analogous formulas will work for multiple regression.

Define $\sigma_{X,Y} = Cov(X, Y)$. Then $X$ and $Y$ have have the multivariate normal distribution with mean vector $[\mu_X, ~ \mu_Y]^T$ and covariance matrix

$$
\begin{bmatrix}
\sigma_X^2 & \sigma_{X,Y} \\
\sigma_{Y,X} & \sigma_Y^2
\end{bmatrix}
$$

Now

$$
\rho ~ = ~ \frac{\sigma_{X,Y}}{\sigma_X \sigma_Y}
$$

and the regression equation can be written as

$$
\begin{align*}
E(Y \mid X) ~ &= ~ \sigma_Y \rho \big{(} \frac{X - \mu_X}{\sigma_X} \big{)} + \mu_Y \\
&= ~ \frac{\sigma_{X,Y}}{\sigma_X^2}(X - \mu_X) + \mu_Y \\
&= ~ \sigma_{Y,X}(\sigma_X^2)^{-1} (X - \mu_X) + \mu_Y
\end{align*}
$$

Also

$$
\rho^2 ~ = ~ \frac{\sigma_{X,Y}^2}{\sigma_X^2 \sigma_Y^2}
$$

so the variance of the error is

$$
Var(Y \mid X) ~ = ~ (1 - \rho^2)\sigma_Y^2 ~ = ~ \sigma_Y^2 - \sigma_{X,Y}^2 (\sigma_X^2)^{-1} ~ = ~ \sigma_Y^2 - \sigma_{Y,X} (\sigma_X^2)^{-1} \sigma_{X,Y}
$$
