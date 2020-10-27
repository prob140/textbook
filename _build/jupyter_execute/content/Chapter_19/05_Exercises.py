## Exercises ##

**1.** Let $X_i$, $i = 1,2$ be independent random variables such that $X_i$ has the exponential $(\lambda_i)$ distribution. Suppose $\lambda_1 \ne \lambda_2$.

(a) Use the convolution formula to find the density of the sum $S = X_1 + X_2$.

(b) Show by algebra that the expression you got for the density in Part (a) is non-negative for all positive $\lambda_1 \ne \lambda_2$.

(c) For $i=1, 2$, let $f_i$ denote the exponential density of $X_i$. Show that the density you got in part (a) is equal to $c_1f_1 + c_2f_2$ for two constants $c_1$ and $c_2$ such that $c_1+c_2 = 1$. Are $c_1$ and $c_2$ both positive?

**2.** A coin lands heads with probability $p$. Let $X$ be the number of tosses till the first head appears and let $Y$ be the number of tails before the first head.

(a) Find the moment generating function of $X$.

(b) Use the answer to (a) to find $E(X)$. Note that by now you have found $E(X)$ in several ways: by the tail sum formula, by conditioning on the first toss, by the pgf, and now by the mgf.

(c) Use the answer to (a) to find the moment generating function of $Y$.

**3.** Recognizing distributions saves a lot of work. See if you can do the following without explicit integration or differentation.

(a) $W$ is a normal $(0, \sigma^2)$ random variable. For $n = 0, 1, 2, 3$, and $4$, find $E(W^n)$. 

(b) $X$ and $Y$ are i.i.d. with moment generating function $M(t) = e^{t + t^2}$, $-\infty < t < \infty$. What is the distribution of $(X-Y)^2$?


**4.** **Markov and Chebyshev Bounds on the Poisson-Binomial Upper Tail** 

For $j \ge 1$ let $I_j$ be independent indicators such that $P(I_j = 1) = p_j$. Let $X = I_1 + I_2 + \ldots + I_n$. Then $X$ is the number of successes in $n$ independent trials that are not necessarily identically distributed.

We say that $X$ has the Poisson-binomial distribution with parameters $p_1, p_2, \ldots, p_n$. As you saw in lab, the binomial is the special case when all the $p_j$'s are equal.

These distributions arise in statistical learning theory, the theory of randomized algorithms, and other areas.

Let $E(X) = \mu$. For $c > 0$, you are going to find an upper bound on $P(X \ge (1+c)\mu)$. That's the chance that $X$ exceeds its mean by some percent. 

In the special case of the binomial, $\mu = np$ and so $P(X \ge (1+c)\mu)$ can be rewritten as $P(\frac{X}{n} - p \ge cp)$. That's the chance that the sample proportion exceeds $p$ by some percent.

(a) Find $\mu = E(X)$ and $\sigma^2 = Var(X)$ in terms of $p_1, p_2, \ldots, p_n$.

(b) Find Markov's bound on $P(X \ge (1+c)\mu)$.

(c) Find Chebyshev's bound on $P(X \ge (1+c)\mu)$ in terms of $\mu$ and $\sigma$.

(d) If all the $p_j$'s are equal to $p$, what is the value of the bound in (c)?

**5.** **Chernoff Bound on Poisson-Binomial Upper Tail**

This exercise continues the previous one and uses the same notation.

(a) Show that the mgf of $I_j$ is given by $M_{I_j}(t) = 1 + p_j(e^t - 1)$ for all $t$.

(b) Use (a) to derive an expression for $M_X(t)$, the mgf of $X$ evaluated at $t$.

(c) An useful exponential bound is that $e^x \ge 1 + x$ for all $x$. You don't have to show it but please look at the [graphs](http://prob140.org/resources/exponential_approximations/). Use the fact to show that $M_X(t) \le \exp\big{(}\mu(e^t -1)\big{)}$ for all $t$. Notice that the right hand side is the mgf of a Poisson random variable that has the same mean as $X$.

(d) Use Chernoff's method and the bound in (c) to show that 

$$
P\big{(}X \ge (1+c)\mu\big{)} 
~ \le ~ 
\Big{(} \frac{\exp(c)}{ (1+c)^{1+c}} \Big{)}^\mu
$$

Remember that $\mu = np$ when all the $p_j$'s are equal. If $g(c) = \exp(c)/(1+c)^{1+c}$ is small then the bound above will decrease exponentially as $n$ gets large. That is the focus of the next exercise.

**6.** **Simplified Chernoff Bounds on Poisson-Binomial Upper Tail**

The bound in the previous exercise is a bit complicated. Often, simpler versions are used because they are good enough even though they are weaker.

(a) It is not hard to show that $\log(1+c) \ge \frac{2c}{2+c}$ for $c > 0$. You don't have to show it but please look at the [graphs](http://prob140.org/resources/exponential_approximations/).
Use the fact to show that $c - (1+c)\log(1+c) \le -\frac{c^2}{2+c}$ for $c > 0$. 

(b) Show that if $X$ has a Poisson-binomial distribution with mean $\mu$ then

$$
P\big{(} X \ge (1+c)\mu\big{)} ~ \le ~ \exp\big{(}-\frac{c^2}{2+c}\mu\big{)}, ~~~~ c > 0
$$

(c) A simpler but weaker version of the bound in (b) is also often used. Show that

$$
P\big{(} X \ge (1+c)\mu\big{)} ~ \le ~ \exp\big{(}-\frac{c^2}{3}\mu\big{)}, ~~~~ c \in (0, 1)
$$

**7.** Let $N$ be a non-negative integer valued random variable, and let $X, X_1, X_2, \ldots $ be i.i.d. and independent of $N$. As before, define the *random sum* $S$ by

$$
\begin{align*}
S ~~&=~~0~~ \mbox{if}~N=0 \\
&=~~ X_1 + X_2 + \cdots + X_n ~~ \mbox{if}~N = n > 0 
\end{align*}
$$

(a) Let $M$ be our usual notation for moment generating functions.
By conditioning on $N$, show that

$$
M_S(t) ~~=~~ M_N\big{(}\log M_X(t) \big{)}
$$

You can assume that all the quantities above are well defined. 

(b) Let $N$ have the geometric $(p)$ distribution on $\{1, 2, 3, \ldots \}$. Find the mgf of $N$. This doesn't use Part (a).

(c) Let $X_1, X_2, \ldots $ be i.i.d. exponential $(\lambda)$ variables and let $N$ be geometric as in Part (b). Use the results of Parts (a) and (b) to identify the distribution of $S$.

**8.** Let $U_1, U_2, \ldots $ be i.i.d. uniform on $(0, 1)$. For $n \ge 1$, let $S_n = \sum_{i=1}^n U_i$. 

Let $f_{S_n}$ be the density of $S_n$. The formula for $f_{S_n}$ is piecewise polynomial on the possible values $(0, n)$. In this problem we will just focus on the density on the interval $(0, 1)$ and discover a nice consequence.

(a) For $0 < x < 1$, find $f_{S_2}(x)$. 

(b) Use Part (a) and the convolution formula to find $f_{S_3}(x)$ for $0 < x < 1$.

(c) Guess a formula for $f_{S_n}(x)$ for $0 < x < 1$ and prove it by induction.

(d) Use Part (c) to find $P(S_n < 1)$.

(e) Let $N = \min\{n: S_n > 1\}$. Use Part (d) to find $E(N)$.

