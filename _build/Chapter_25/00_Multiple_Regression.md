---
redirect_from:
  - "/chapter-25/00-multiple-regression"
interact_link: notebooks/Chapter_25/00_Multiple_Regression.ipynb
title: 'Chapter 25: Multiple Regression'
prev_page:
  url: /Chapter_24/04_Regression_Equation
  title: 'The Regression Equation'
next_page:
  url: /Chapter_25/01_Bilinearity_in_Matrix_Notation
  title: 'Bilinearity in Matrix Notation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

# Multiple Regression

The most common use of regression is to predict the value of a numerical variable based on the values of several other variables. In our probabilistic setting, we have a finite number of jointly distributed random variables and the goal is to predict one of them based on all the others. 

In the previous chapters we did this in the case where there was just one predcitor variable. In particular, we developed the theory of simple linear regression.

In this chapter we will extend our calculations for simple regression to the case of multiple regression. Indeed, we will capitalize on our work on simple regression to make an inspired guess for how multiple regression must work. Then we will check that our guess is correct.
