## Exercises ##

**1.** Let $X_0, X_1, X_2, \ldots$ be a Markov chain with time-homoegeneous transition probabilities. Suppose that for a fixed state $i$, the transition probability $P(i, i)$ is positive. In other words, the chain has positive probability of staying put at this state $i$.

Suppose the chain starts at this state $i$. That is, suppose you are given $X_0 = i$. Let $T$ be the first time the chain leaves $i$. Formally, $T = \min\{n \ge 1: X_n \ne i\}$.

Find the distribution of $T$. Recognize it as one of the famous ones and provide its name and parameters.

**2.** Let $X_0, X_1, \ldots $ be an irreducible, aperiodic Markov Chain on a finite state space $S$. Let $\mathbb{P}$ be the transition matrix of the chain. Let $\lambda$ be the initial distribution of the chain. That is, let $\lambda$ be a vector containing the distribution of $X_0$.

(a) Find the distribution of $X_n$ in terms of $\lambda$, $\mathbb{P}$, and $n$.

(b) What happens to the distribution of $X_n$ as $n \to \infty$? Prove your answer.

**3.** Fix $p \in (0, 1)$ and a positive integer $N$, and let $q = 1-p$. Consider the Markov Chain with transition probabilities given by:

- $P(0, 1) ~ = ~ p$ and $P(0, 0) = q$.
- $P(N, N) = p$ and $P(N, N-1) = q$.
- For $1 \le i \le N-1$, $P(i, i+1) ~ = ~ p$ and $P(i, i-1) = q$

(a) Is there a probability distribution that satisfies the detailed balance equations? 

(b) Find the stationary distribution of the chain.

**4.** Every transition matrix is a *stochastic matrix* because all its rows sum to 1. If all the columns also sum to 1, the matrix is called *doubly stochastic*.

(a) Suppose an irreducible, aperiodic Markov chain on a finite state space has a doubly stochastic transition matrix. Show that the stationary distribution is uniform on the state space.

[Use uniqueness and the balance equations.]

(b) For $n \ge 1$, let $S_n$ be the total number of spots on $n$ rolls of a die. For large $n$, approximately what is the probability that $S_n$ is a multiple of 7? [Think about remainders, and use Part **a**.]

**5.** I don’t know why this problem has become a classic. But versions of it appear in many texts and exercise sets with diverse people getting wet.

It’s essentially an exercise in setting up a useful chain based on which you can easily find the desired proportion.

A professor has two umbrellas, each of which could either be in her office or in her car. The professor walks from her car to her office; she also walks from her office to her car. Assume that on each of these walks:

- It rains with probability 0.7, independently of all other walks.
- If it is not raining, the professor ignores the umbrellas.
- If it is raining, she uses an umbrella if there is one, and gets wet if there isn’t.

In the long run, what is the expected proportion of walks on which the professor gets wet?


### Selections from Konstantopoulos ###
Emeritus Prof. David Aldous' former student Takis Konstantopoulos created a great [resource](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) of exercises on Markov Chains. Selected problems are listed below. 

The exercises are numerous. Here are some to try. Resist the impulse to read the answers before you try the exercises yourself. 

- 7 ('topological properties' means whether it is irreducible and what its period is; for the irreducible aperiodic ones, find the long run proportion of time spent at each state)
- 16 

- 21

- 25

- 27 (you can do this one without calculation)

- 36

