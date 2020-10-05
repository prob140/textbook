## Exercises ##

**1.** Let $X$ have the distribution given by

|$~~~~~~~~~~~~~~~~~~~~~~~~~x$|1|2|3|
|---:|---:|---:|---:|
|$P(X=x)$| 0.2 | 0.5 | 0.3 |

Find $E(X)$ and $SD(X)$.

**2.** Suppose $P(X = x_0) = 1-p$ and $P(X = x_1) = p$ for values $x_0$ and $x_1$ such that $x_1 > x_0$.

Write $X$ as a linear function of an indicator that has value $1$ with probability $p$, and hence find $SD(X)$ in terms of $p$, $q=1-p$, and $d=x_1-x_0$.

**3.** Let $X$ have the Poisson $(\mu)$ distribution and let $Y$ have the Poisson $(\lambda)$ distribution independent of $X$.

(a) What is the distribution of $X+Y$?

(b) Which of the following statements is (or are) true? Pick all that are true and justify your choices.

(i) $E(X+Y) = E(X) + E(Y)$

(ii) $SD(X+Y) = SD(X) + SD(Y)$

(iii) $Var(X+Y) = Var(X) + Var(Y)$

**4.** Let $p∈(0,1)$ and let $X$ be the number of spots showing on a flattened
die that shows its six faces according to the following chances:

$P(X=1)=P(X=6)$

$P(X=2)=P(X=3)=P(X=4)=P(X=5)$

$P(X=1$ or $6)=p$

Find $SD(X)$ and explain why it is an increasing function of $p$. Compare your answer with the answer you got for the mean absolute deviation in [Chapter 8](http://prob140.org/textbook/content/Chapter_08/06_Exercises.html).

**5.** Consider a sequence of i.i.d. Bernoulli $(p)$ trials. Let $T$ be the number of trials till the first success and let $F$ be the number of failures before the first success. You know that $T$ has the geometric $(p)$ distribution on $\{1, 2, 3, \ldots\}$ and that $E(T) = \frac{1}{p}$. We will show later, by conditioning, that $SD(T) = \frac{\sqrt{q}}{p}$ where $q = 1-p$. For now you can just assume that it is true.

(a) Write $F$ as a function of $T$ and hence find $E(F)$ and $SD(F)$.

(b) Find the distribution of $F$. It is called the geometric $(p)$ distribution on $\{0, 1, 2, \ldots \}$.

**6.** A random variable $X$ has expectation $20$ and SD $2$. Find the best upper and
lower bounds you can on 

(a) $P(15 < X < 25)$

(b) $P(15 < X < 30)$

**7.** Consider a probabilistic model that has a numerical parameter $\theta$. A "probabilistic model" is just a set of assumptions about randomness. Let the random variable $T$ be an estimator of $\theta$. Frequently, $T$ is a statistic based on a random sample.

Recall that the [bias](http://prob140.org/textbook/content/Chapter_08/04_Additivity.html#unbiased-estimator) of $T$ is defined as $B_\theta (T) ~ = ~ E_\theta (T) - \theta$, where the subscript $\theta$ reminds us that $\theta$ is the true value of the parameter. 

The *mean squared error* of the estimator $T$ is
$MSE_\theta (T) ~ = ~ E_\theta \big{(} (T - \theta)^2 \big{)}$.

Follow the calculation in [Section 12.2](http://prob140.org/textbook/content/Chapter_12/02_Prediction_and_Estimation.html) of the textbook to show the *bias-variance decomposition* given by

$$
MSE_\theta (T) ~ = ~ Var_\theta(T) + B_\theta^2(T)
$$

Note that the square in the bias term makes sense. Bias has the same units as $T$, whereas the MSE and variance are in the square of those units.

