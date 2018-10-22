---
interact_link: notebooks/Chapter_18/05_Review_Problems_Set_4.ipynb
title: '18.5 Review Problems: Set 4'
permalink: 'chapters/Chapter_18/05_Review_Problems_Set_4'
previouschapter:
  url: chapters/Chapter_18/04_Chi_Squared_Distributions
  title: '18.4 Chi-Squared Distributions'
nextchapter:
  url: chapters/Chapter_19/00_Distributions_of_Sums
  title: 'Chapter 19: Distributions of Sums'
redirect_from:
  - 'chapters/chapter-18/05-review-problems-set-4'
---

## Review Problems: Set 4

These problems can be solved using the main ideas of Chapters 16 through 18. The Basics set will remind you of the fundamental concepts and some typical calculations. The rest are for you to further develop your problem solving skills and your fluency with the notation and ideas.

You can leave answers in terms of the standard normal cdf $\Phi$. You can also leave answers in terms of the Gamma function $\Gamma$ unless you are asked for a simplification.

### The Basics

**1.**
Let $X$ have density $f_X(x) = 2x$ for $0 < x < 1$. Find the density of

(a) $5X - 3$

(b) $4X^3$

(c) $X/(1+X)$

**2.**
Let $X$ have density $f(x) = 2x^{-3}e^{-x^{-2}}$ on the positive real numbers. Find the density of $X^4$.

**3.**
For a fixed $\alpha > 0$ let $X$ have the Pareto density given by

$$
f(x) ~ = ~ \frac{\alpha}{x^{\alpha+1}}, ~~ x > 1
$$

Find the density of $\log(X)$. Recognize this as one of the famous ones and provide its name and parameters.

**4.**
A Prob 140 student comes to lecture at a time that is uniformly distributed between 5:09 and 5:14. Independently of the student, the professor begins the lecture at a time that is uniformly distributed between 5:10 and 5:12. What is the chance that the lecture has already begun when the student arrives?

**5.**
For some constant $c$ let $X$ and $Y$ have a joint density given by

$$
f(x, y) ~ = ~ 
\begin{cases}
c(x - y), ~~ 0 < y < x < 1 \\
0 ~~~~~~~~~~~~~~ \text{otherwise}
\end{cases}
$$

(a) Draw the region over which $f$ is positive.

(b) Find $c$.

(c) Find $P(X > Y + 0.4)$. Before you calculate, shade the event on the diagram you drew in (a).

(d) Find the density of $X$.

(e) Are $X$ and $Y$ independent?

(f) Find $E(XY)$.


**6.**
Let $X$ and $Y$ have joint density $f$ given by

$$
f(x, y) ~ = ~ 
\begin{cases}
\frac{10}{243}x(3-x)^4 (x-y), ~~~~ 0 < y < x < 3 \\
0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \text{otherwise}
\end{cases}
$$

Write the each of the following in terms of $f$ but do not simplify the expression. Integrals should not include regions where $f(x, y) = 0$.

(a) $P(Y > 1)$

(b) the conditional density of $X$ given $Y = 1$ (please be clear about the values on which the density is positive)

(c) $E(e^{XY})$

**7.**
Let $S$, $T$, and $R$ be independent standard normal variables. Find the following without using calculus.

(a) the distribution of $5S - 7$

(b) the distribution of $5(S-T) - 7$

(c) $P(S + T > R + 1)$

(d) $E(5S - 6T + 8R - 9)$

(e) $Var(5S - 6T + 8R - 9)$

**8.**
Heights of women in a large population are normally distributed with mean 65 inches and SD 3.5 inches. Two women are picked at random. Find the chance that one of the women is more than an inch taller than the other.

**9.**
Let $X_i$, $1 \le i \le 5$ be i.i.d. exponential $(\lambda)$ lifetimes of electrical components. 

(a) Assume that as soon as one component dies it is replaced by another, so that $T = \sum_{i=1}^5 X_i$ is the total lifetime of all five components. Find the distribution, mean, and SD of $T$.

(b) Find the distribution, mean, and SD of the shortest of the five lifetimes.

**10.**
Let $Z$ be standard normal and let $X$ have the gamma $(r, \lambda)$ density. You shouldn't have to do any calculation in this exercise if you've done the reading or remember what was covered in lecture.

(a) For $c > 0$, $cX$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution.

(b) Fill in the blanks: $Z^2$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution.

(c) Let $W$ have the normal $(0, \sigma^2)$ density. Fill in the blank: $W \stackrel{d}{=} \underline{~~~~~~~~~}Z$.

(d) Fill in the blank: $W^2$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution.


### Additional Practice

**11.**
Let $X$ be a random variable. Find the density of $X^2$ if $X$ has the uniform distribution on

(a) $(0, 1)$

(b) $(-1, 1)$

(c) $(-1, 2)$

**12.**
Suppose two shots are fired at a target. Assume each shot hits with independent normally distributed coordinates, with the same means and equal unit variances. Let $D$ be the distance between the point where the two shots strike.

(a) Find the distribution of $D^2$.

(b) Find the distribution of $D$.

**13.**
Let $Z$ be standard normal.

(a) Use the change of variable formula to find the density of $1/Z$. Why do you not have to worry about the event $Z = 0$?

(b) A student who doesn't like the change of variable formula decides to first find the cdf of $1/Z$ and then differentiate it to get the density. That's a fine plan. The student starts out by writing $P(1/Z < x) = P(1/x < Z)$ and immediately the course staff say, "Are you sure?" What is the problem with what the student wrote?

(c) For all $x$, find $P(1/Z < x)$.

(d) Check by differentiation that your answer to (c) is consistent with your answer to (a).

**14.**
The joint density of $X$ and $Y$ is 

$$
f(x, y) ~ = ~
\begin{cases}
24xy, ~~~ x, y > 0  \text{ and } 0 < x+y < 1 \\
0 ~~~~~~~~~~~~~ \text{otherwise}
\end{cases}
$$

(a) Find the density of $X$. Recognize this as one of the famous ones and state its name and parameters.

(b) Without further calculation, find the density of $Y$ and justify your answer.

(c) Are $X$ and $Y$ independent? Why or why not?

(d) Find the conditional density of $X$ given $Y = 0.75$. As always, start with the possible values.

(e) Find $P(X > 0.2 \mid Y = 0.75)$.

(f) Find $E(X \mid Y = 0.75)$.

**15.**
Weights in a population are normally distributed with mean 150 pounds. Just about 5% of the people weigh more than 185 pounds.

(a) Find the SD of the weights. You can leave your answer in terms of the standard normal cdf $\Phi$ if you don't have access to a notebook cell in which to do the numerical calculation.

(b) Two people are drawn at random. Find the chance that their weights are within 10 pounds of each other. If your answer to (a) isn't numerical, you can just call it $\sigma$ for brevity.

**16.**
[This is Pitman 5.rev.22, with his permission]. In Maxwell's model of a gas, molecules of mass $m$ are assumed to have velocity components $V_x$, $V_y,$ and $V_z$ that are independent, with a joint distribution that is invariant under rotation of the three-dimensional coordinate system. Maxwell showed that $V_x$, $V_y$, and $V_z$ must each have the normal $(0, \sigma^2)$ distribution for some $\sigma$. Taking this result for granted:

(a) Find a formula for the density of the kinetic energy

$$
K ~ = ~ \frac{1}{2}mV_x^2 + \frac{1}{2}mV_y^2 + \frac{1}{2}mV_z^2
$$
        
(b) Find the mean and mode of the energy distribution.

**17.**
Let $U_i$, $1 \le i \le 20$ be i.i.d. uniform $(0, 1)$ variables, and let $U_{(k)}$ be the $k$th order statistic.

(a) What is the density of $U_{(7)}$?

(b) Without integrating the density, find the cdf of $U_{(7)}$. 

[Use the idea you used to find the tail probabilities of a sample median in Lab 4. Draw a line representing the unit interval and put down crosses representing the variables. For $U_{(7)}$ to be less than $x$, how must you distribute the crosses?]

(c) Find the joint density of $U_{(7)}$ and $U_{(12)}$.

**18.**
Annual household incomes in City A have a mean of 68,000 dollars and an SD of 40,000 dollars. Annual household incomes in City B have a mean of 75,000 dollars and an SD of 50,000 dollars. 

A random sample of 400 households is taken in City A. Independently, a random sample of 625 households in taken in City B. You can assume that the sampling procedures can be well approximated by sampling at random with replacement.

(a) Is the distribution of annual household incomes in City A approximately normal? Why or why not? What about City B?

(b) Find or approximate the distribution of the average annual household income in the sample from City A. Justify your answer.

(c) Find or approximate the chance that the average annual household income is greater in the City B sample than in the City A sample.

(d) About how large must a sample from City A be so that there is about a 90% chance that the sample average annual household income is within 1000 dollars of the population average?

**19.**
A random variable $X$ has the beta $(2, 2)$ density. Given $X = x$, the conditional distribution of the random variable $Y$ is uniform on the interval $(-x, x)$.

(a) Find $P(Y < 0.2 \mid X = 0.6)$.

(b) Find $E(Y)$.

(c) Find the joint density of $X$ and $Y$. Remember to specify the region where it is positive.

(d) Find $P(X < 0.3, \vert Y \vert < 0.3X)$.

**20.**
As you know, the Gamma function is defined as an integral. It turns out that its numerical values are hard to calculate exactly except in some cases. Here are two of those cases.

(a) If $n$ is an integer, what is the value of $\Gamma(n)$?

(b) Let $Z$ be standard normal. Use the density of $Z^2$ to show that $\Gamma(\frac{1}{2}) = \sqrt{\pi}$.

(c) For odd integer $n$, find $\Gamma(\frac{n}{2})$. [For even $n$, $n/2$ is an integer and you already dealt with that case in Part (a).]

**21.**
Let $X$ and $Y$ be i.i.d. with a joint density.

(a) Find $P(Y > X)$.

(b) Find $P(\vert Y \vert > \vert X \vert)$.

(c) If $X$ and $Y$ are i.i.d. standard normal, find $P(Y > \vert X \vert)$.

**22.**
Two points are placed independently and uniformly at random on the unit interval. This creates three segments of the interval. What is the chance that the three segments can form a triangle?

[To find probabilities of events determined by two independent uniform $(0,1)$ random variables, it's a good idea to draw the unit square.]
