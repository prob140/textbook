## Exercises ##

**1.** Let $S$, $T$, and $R$ be independent standard normal variables. Find the following without using calculus.

(a) the distribution of $5S - 7$

(b) the distribution of $5(S-T) - 7$

(c) $P(S + T > R + 1)$

(d) $E(5S - 6T + 8R - 9)$

(e) $Var(5S - 6T + 8R - 9)$

**2.** Heights of women in a large population are normally distributed with mean 65 inches and SD 3.5 inches. Two women are picked at random. Find the chance that one of the women is more than an inch taller than the other.

**3.** Let $X_i$, $1 \le i \le 5$ be i.i.d. exponential $(\lambda)$ lifetimes of electrical components.

(a) Assume that as soon as one component dies it is replaced by another, so that $T = \sum_{i=1}^5 X_i$ is the total lifetime of all five components. Find the distribution, mean, and SD of $T$.

(b) Find the distribution, mean, and SD of the shortest of the five lifetimes.

**4.** Let $Z$ be standard normal and let $X$ have the gamma $(r, \lambda)$ density. This exercise requires minimal calculation.

(a) For $c > 0$, $cX$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution.

(b) Fill in the blanks: $Z^2$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution.

(c) Let $W$ have the normal $(0, \sigma^2)$ density. Fill in the blank: $W \stackrel{d}{=} \underline{~~~~~~~~~}Z$.

(d) Fill in the blank: $W^2$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution.

**5.** Suppose two shots are fired at a target. Assume each shot hits with independent normally distributed coordinates, with the same means and equal unit variances. Let $D$ be the distance between the point where the two shots strike.

(a) Find the distribution of $D^2$.

(b) Find the distribution of $D$.

**6.** Weights in a population are normally distributed with mean 150 pounds. Just about 5% of the people weigh more than 185 pounds.

(a) Find the SD of the weights. You can leave your answer in terms of the standard normal cdf $\Phi$ if you don’t have access to a notebook cell in which to do the numerical calculation.

(b) Two people are drawn at random. Find the chance that their weights are within 10 pounds of each other. If your answer to (a) isn’t numerical, you can just call it $\sigma$ for brevity.

**7.** [This is Pitman 5.rev.22, with his permission]. In Maxwell’s model of a gas, molecules of mass $m$ are assumed to have velocity components $V_x$, $V_y,$ and $V_z$ that are independent, with a joint distribution that is invariant under rotation of the three-dimensional coordinate system. Maxwell showed that $V_x$, $V_y$, and $V_z$ must each have the normal $(0, \sigma^2)$ distribution for some $\sigma$. Taking this result for granted:

(a) Find a formula for the density of the kinetic energy $K ~ = ~ \frac{1}{2}mV_x^2 + \frac{1}{2}mV_y^2 + \frac{1}{2}mV_z^2$.

(b) Find the mean and mode of the energy distribution.

**8.** Annual household incomes in City A have a mean of 68,000 dollars and an SD of 40,000 dollars. Annual household incomes in City B have a mean of 75,000 dollars and an SD of 50,000 dollars.

A random sample of 400 households is taken in City A. Independently, a random sample of 625 households in taken in City B. You can assume that the sampling procedures can be well approximated by sampling at random with replacement.

(a) Is the distribution of annual household incomes in City A approximately normal? Why or why not? What about City B?

(b) Find or approximate the distribution of the average annual household income in the sample from City A. Justify your answer.

(c) Find or approximate the chance that the average annual household income is greater in the City B sample than in the City A sample.

(d) About how large must a sample from City A be so that there is about a 90% chance that the sample average annual household income is within 1000 dollars of the population average?

**9.** As you know, the Gamma function is defined as an integral. It turns out that its numerical values are hard to calculate exactly except in some cases. Here are two of those cases.

(a) If $n$ is an integer, what is the value of $\Gamma(n)$?

(b) Let $Z$ be standard normal. Use the density of $Z^2$ to show that $\Gamma(\frac{1}{2}) = \sqrt{\pi}$.

(c) For odd integer $n$, find $\Gamma(\frac{n}{2})$. [For even $n$, $n/2$ is an integer and you already dealt with that case in Part (a).]

**10.** Let $Z$ be standard normal. You have seen a [probabilistic argument](http://prob140.org/textbook/content/Chapter_18/01_Standard_Normal_Basics.html#variance) for the fact that $E(Z^2) = 1$. Derive the same fact by writing $E(Z^2)$ as an integral and evaluating the integral.

[Notice that you are integrating an even function, then make a variable substitution to convert your integral into a gamma integral, then use gamma facts.]

