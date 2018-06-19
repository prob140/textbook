---
interact_link: notebooks/Chapter_25/00_Multiple_Regression.ipynb
title: 'Chapter 25: Multiple Regression'
previouschapter:
  url: chapters/Chapter_24/04_Regression_Equation
  title: '24.4 The Regression Equation'
nextchapter:
  url: chapters/Chapter_25/01_Bilinearity_in_Matrix_Notation
  title: '25.1 Bilinearity in Matrix Notation'
---

# Multiple Regression #

The most common use of regression is to predict the value of a numerical variable based on the values of several other variables. In our probabilistic setting, the goal is to predict $Y$ based on the $p$ predictor variables $X_1, X_2, \ldots, X_p$; here $p$ is not a probability but a positive integer denoting the number of predictors. 

Finding the least squares function of the form $\hat{Y} = a_1X_1 + a_2X_2 + \cdots + a_pX_p + b$ is called *multiple linear regression*. The term "linear" refers to the fact that the function is linear in the parameters $a_1, a_2, \ldots, a_p, b$. It does not refer to the shape of the function being fit. For example, you could fit a quadratic function of $X_1$ by taking $X_2 = X_1^2$. Then $\hat{Y} = a_1X_1 + a_2X_2 + b = a_1X_1 + a_2X_1^2 + b$ is a quadratic function of $X_1$. But it is still linear in the coefficients, and those are what you have to estimate.

In this chapter we will extend our calculations for simple regression to the case of multiple regression. Indeed, we will capitalize on our work on simple regression to make an inspired guess for how multiple regression must work. Then we will check that our guess is correct.
