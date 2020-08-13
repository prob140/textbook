## Review Set on Conditioning and Markov Chains ##

David Aldous' former student Takis Konstantopoulos created a great [resource](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) of exercises on Markov Chains. Selected problems are listed below along with some others. Resist the impulse to read the answers to the Konstantopoulos exercises before you try the exercises yourself. 

**1.** **Bridge Hands**

My bridge partner and I are playing a game of bridge against two other people. In the game, four hands of 13 cards each are dealt to the four players, at random without replacement from a standard deck. Let $X$ be the number of hearts in my hand and let $Y$ be the number of hearts in my partner's hand. For $k = 0, 1, 2, \ldots, 13$, find $E(Y \mid X=k)$.



**2.** **Random Urn**

I draw a simple random sample of $n_0$ balls from an urn that contains $b_0$ blue balls and $r_0$ red balls. I put the balls in my sample in another urn that already contains $b_1$ blue balls and $r_1$ red balls. I then draw a simple random sample of $n_1$ balls from the second urn. Find the expected number of blue balls in this sample.



**3.** **Polya's Urn**

You have seen this model before; it is used in many contexts, for example to model contagion. Start with one white and one black ball. Draw one ball at random, then replace it in the urn along with another ball of its color. Keep doing this.

Let $B_n$ be the number of black balls in the urn just before the $n$th ball is drawn. So $B_1 = 1$ with probability 1. 

**(a)** Just before the $n$th ball is drawn, how many balls are there in the urn?

**(b)** For each $n$, find $E(B_{n+1} \mid B_n)$.

**(c)** Use induction and Part **b** to find $E(B_n)$ for each $n$.

**(d)** Let $X_n$ be the proportion of black balls in the urn just before the $n$th ball is drawn. Find $E(X_n)$ for each $n$.



**4.** **Craps Principle**

This gambling observation can be formalized as follows. Consider a sequence of i.i.d. trials, each of which results in one of three categories of outcomes. On each trial, let the chance of Category $i$ be $p_i > 0$ with $p_1 + p_2 + p_3 = 1$.

Show that the chance that Category 1 appears before Category 2 is $p_1/(p_1 + p_2)$.

[The goal is for you to practice conditioning, so don't use geometric sums. Just condition on the first couple of trials. Either the event happens right away, or $\ldots$ what?]




**5.** **Waiting for 00**

A random number generator draws repeatedly at random with replacement from the 10 digits $\{0, 1, 2, \ldots, 9\}$. Run the generator till the pattern 00 appears. Let $X$ be the number of times the generator has to be run. Thus for example if the first three runs produce 7 followed by 0 followed by 0, then $X = 3$. Find $E(X)$ by conditioning on the first run.




**6.** **Markov Chain Fundamentals**

Let $X_0, X_1, \ldots $ be an irreducible, aperiodic Markov Chain on a finite state space $S$. Let $\mathbb{P}$ be the transition matrix of the chain. Let $\lambda$ be the initial distribution of the chain. That is, let $\lambda$ be a vector containing the distribution of $X_0$.

**(a)** Find the distribution of $X_n$ in terms of $\lambda$, $\mathbb{P}$, and $n$.

**(b)** What happens to the distribution of $X_n$ as $n \to \infty$? Prove your answer.



**7.** **Reflecting Random Walk on a Finite Set**

Fix $p \in (0, 1)$ and a positive integer $N$, and let $q = 1-p$. Consider the Markov Chain with transition probabilities given by:

- $P(0, 1) ~ = ~ p$ and $P(0, 0) = q$.
- $P(N, N) = p$ and $P(N, N-1) = q$.
- For $1 \le i \le N-1$, $P(i, i+1) ~ = ~ p$ and $P(i, i-1) = q$

**(a)** Is there a probability distribution that satisfies the detailed balance equations? 

**(b)** Find the stationary distribution of the chain.



### Selections from Konstantopoulos ###
[The exercises](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) are numerous. Here are some to try.

- 7 ('topological properties' means whether it is irreducible and what its period is; for the irreducible aperiodic ones, find the long run proportion of time spent at each state)
- 16 

- 21

- 25

- 27 (you can do this one without calculation)

- 36

