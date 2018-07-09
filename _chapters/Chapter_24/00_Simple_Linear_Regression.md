---
interact_link: notebooks/Chapter_24/00_Simple_Linear_Regression.ipynb
title: 'Chapter 24: Simple Linear Regression'
permalink: 'chapters/chapter-24/00-simple-linear-regression'
previouschapter:
  url: chapters/chapter-23/04-independence
  title: '23.4 Independence'
nextchapter:
  url: chapters/chapter-24/01-bivariate-normal-distribution
  title: '24.1 Bivariate Normal Distribution'
---

# Simple Linear Regression

In data science, regression models are widely used for prediction. This chapter examines linear least squares from a probabilistic perspective. The focus is on *simple* regression, that is, prediction based on one numerical attribute. 

When the joint distribution of the attribute $X$ and the response $Y$ is bivariate normal, the empirical distribution of $(X, Y)$ has the football shape so familiar from Data 8. We will start with a geometric interpretation of correlation, as that is helpful for understanding both regression and the bivariate normal. The equation of the regression line, which we will derive, can be written in several ways; by the end of the chapter we will have written it in the way that is most easily extended to multiple regression.
