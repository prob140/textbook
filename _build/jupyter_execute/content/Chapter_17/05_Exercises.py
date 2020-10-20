## Exercises ##

**1.** A Prob 140 student comes to lecture at a time that is uniformly distributed between 5:09 and 5:14. Independently of the student, the professor begins the lecture at a time that is uniformly distributed between 5:10 and 5:12. What is the chance that the lecture has already begun when the student arrives?

**2.** For some constant $c$ let $X$ and $Y$ have a joint density given by

$$f(x, y) ~ = ~ 
\begin{cases}
c(x - y), ~~ 0 < y < x < 1 \\
0 ~~~~~~~~~~~~~~ \text{otherwise}
\end{cases}$$.

(a) Draw the region over which $f$ is positive.

(b) Find $c$.

(c) Find $P(X > Y + 0.4)$. Before you calculate, shade the event on the
diagram you drew in (a).

(d) Find the density of $X$.

(e) Are $X$ and $Y$ independent?

(f) Find $E(XY)$.

**3.** Let $X$ and $Y$ have joint density $f$ given by

$$f(x, y) ~ = ~ 
\begin{cases}
\frac{40}{243}x(3-x)(x-y), ~~~~ 0 < y < x < 3 \\
0 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \text{otherwise}
\end{cases}$$

Write the each of the following in terms of $f$ but do not simplify the
expression. Integrals should not include regions where $f(x, y) = 0$.

(a) $P(Y > 1)$

(b) the conditional density of $X$ given $Y = 1$ (please be clear about
the values on which the density is positive)

(c) $E(e^{XY})$

**4.** The joint density of $X$ and $Y$ is

$$f(x, y) ~ = ~
\begin{cases}
24xy, ~~~ x, y > 0  \text{ and } 0 < x+y < 1 \\
0 ~~~~~~~~~~~~~ \text{otherwise}
\end{cases}$$.

(a) Find the density of $X$. Recognize this as one of the famous ones and state its name and parameters.

(b) Without further calculation, find the density of $Y$ and justify your answer.

(c) Are $X$ and $Y$ independent? Why or why not?

(d) Find the conditional density of $X$ given $Y = 0.75$. As always, start with the possible values.

(e) Find $P(X > 0.2 \mid Y = 0.75)$.

(f) Find $E(X \mid Y = 0.75)$.

**5.** Let $U_i$, $1 \le i \le 20$ be i.i.d. uniform $(0, 1)$ variables, and let $U_{(k)}$ be the $k$th order statistic.

(a) What is the density of $U_{(7)}$?

(b) Without integrating the density, find the cdf of $U_{(7)}$.

[Draw a line representing the unit interval and put down crosses representing the variables. For $U_{(7)}$ to be less than $x$, how must you distribute the crosses?]

(c) Find the joint density of $U_{(7)}$ and $U_{(12)}$.

**6.** A random variable $X$ has the beta $(2, 2)$ density. Given $X = x$, the conditional distribution of the random variable $Y$ is uniform on the interval $(-x, x)$.

(a) Find $P(Y < 0.2 \mid X = 0.6)$.

(b) Find $E(Y)$.

(c) Find the joint density of $X$ and $Y$. Remember to specify the
region where it is positive.

(d) Find $P(X < 0.3, \vert Y \vert < 0.3X)$.

**7.** Let $X$ and $Y$ be i.i.d. with a joint density.

(a) Find $P(Y > X)$.

(b) Find $P(\vert Y \vert > \vert X \vert)$.

(c) If $X$ and $Y$ are i.i.d. standard normal, find $P(Y > \vert X \vert)$.

**8.** Two points are placed independently and uniformly at random on the unit interval. This creates three segments of the interval. What is the chance that the three segments can form a triangle?

[To find probabilities of events determined by two independent uniform $(0,1)$ random variables, it’s a good idea to draw the unit square.]

**9.** Let $X$ have the beta $(r, s)$ density. Find $Var(X)$. You can assume $r$ and $s$ are integers.