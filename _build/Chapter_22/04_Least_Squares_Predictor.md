---
redirect_from:
  - "/chapter-22/04-least-squares-predictor"
interact_link: notebooks/Chapter_22/04_Least_Squares_Predictor.ipynb
title: 'Least Squares Predictor'
prev_page:
  url: /Chapter_22/03_Examples
  title: 'Examples'
next_page:
  url: /Chapter_23/00_Multivariate_Normal_RVs
  title: 'Chapter 23: Jointly Normal Random Variables'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## Least Squares Predictor

As the function that picks off the "centers of vertical strips," the conditional expectation $b(X) = E(Y \mid X)$ is a natural estimate or predictor of $Y$ given the value of $X$. We will now see how good $b(X)$ is if we use mean squared error as our criterion.

### Minimizing the MSE
Let $h(X)$ be any function of $X$, and consider using $h(X)$ to predict $Y$. Define the *mean squared error of the predictor $h(X)$* to be

$$
MSE(h) ~ = ~ E\Big{(}\big{(}Y - h(X)\big{)}^2\Big{)}
$$

We will show that $b(X)$ is the best predictor of $Y$ based on $X$, in the sense that it minimizes this mean squared error over all functions $h(X)$.

Recall our notation $D_w = Y - b(X)$. Earlier we showed that:
- $E(D_w) = 0$ 
- $D_w$ is uncorrelated with any function of $X$. Therefore if $g(X)$ is any function of $X$, then $E\big{(}D_wg(X)\big{)} = 0$.

$$
\begin{align*}
MSE(h) ~ &= ~ E\Big{(}\big{(}Y - h(X)\big{)}^2\Big{)} \\
&= ~ E\Big{(}\big{(} (Y - b(X)) + (b(X) - h(X) \big{)}^2 \Big{)} \\
&= ~ E\Big{(}\big{(}Y - b(X)\big{)}^2\Big{)} + E\Big{(}\big{(}b(X) - h(X)\big{)}^2\Big{)} + 2E\Big{(}D_w\big{(}b(X) - h(X)\big{)}\Big{)} \\
&= ~ E\Big{(}\big{(}Y - b(X)\big{)}^2\Big{)} + E\Big{(}\big{(}b(X) - h(X)\big{)}^2\Big{)} \\
&\ge ~ E\Big{(}\big{(}Y - b(X)\big{)}^2\Big{)} \\
&= ~ MSE(b)
\end{align*}
$$

### Best Predictor
The result above shows that the least squares predictor of $Y$ based on $X$ is the conditional expectation $b(X) = E(Y \mid X)$. 

In terms of the scatter diagram of observed values of $X$ and $Y$, the result is saying that the best predictor of $Y$ given $X$, by the criterion of smallest mean squared error, is the average of the vertical strip at the given value of $X$.

Given $X$, the root mean squared error of this estimate is the *SD of the strip*, that is, the conditional SD of $Y$ given $X$:

$$
SD(Y \mid X) ~ = ~ \sqrt{Var(Y \mid X)}
$$

This is a random variable; its value measures the variability within the strip at the given value of $X$.

Overall across the entire scatter diagram, the root mean squared error of the estimate $E(Y \mid X)$ is

$$
RMSE(b) ~ = ~ \sqrt{E\Big{(}\big{(}Y - b(X)\big{)}^2\Big{)}} ~ = ~ \sqrt{E\big{(} Var(Y \mid X) \big{)}}
$$

Notice that the result makes no assumption about the joint distribution of $X$ and $Y$. The scatter diagram of the generated $(X, Y)$ points can have any arbitrary shape.

It seems as though the question of prediction has been settled once and for all: if you want the least squares predictor, use conditional expectation. However, the functional form of the conditional expectation of $Y$ given $X$ depends on the joint distribution of $X$ and $Y$ (which also determines the shape of the scatter diagram), and is not always straightforward to find.

So data scientists also find least squares estimates among smaller classes of estimates, the most common class being the set of linear functions of the given variable. This is called linear regression and is the topic of a later chapter.
