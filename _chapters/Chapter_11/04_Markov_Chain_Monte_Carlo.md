---
interact_link: notebooks/Chapter_11/04_Markov_Chain_Monte_Carlo.ipynb
title: '11.4 Markov Chain Monte Carlo'
permalink: 'chapters/Chapter_11/04_Markov_Chain_Monte_Carlo'
previouschapter:
  url: chapters/Chapter_11/03_Code_Breaking
  title: '11.3 Code Breaking'
nextchapter:
  url: chapters/Chapter_11/05_Review_Conditioning_and_MC
  title: '11.5 Review Set on Conditioning and Markov Chains'
redirect_from:
  - 'chapters/chapter-11/04-markov-chain-monte-carlo'
---

## Markov Chain Monte Carlo

The goal of Markov Chain Monte Carlo (MCMC) is to generate random samples from complicated high dimensional distributions about which we have incomplete information. For example, it might be that we don't know the normalizing constant of the distribution, as we saw in the code breaking example of the previous section.

Suppose the distribution from which we want to generate a sample is called $\pi$. We are going to assume that $\pi$ is a probability distribution on a finite set, and you should imagine the set to be large. MCMC relies on a few observations.

- Let $X_0, X_1, \ldots $ be an irreducible aperiodic Markov Chain on a finite state space. Then the distribution of $X_n$ converges to a stationary distribution as $n$ gets large. If we can create a Markov Chain $\{X_n\}$ that has the desired distribution $\pi$ as its stationary distribution, then we can simulate draws from $\pi$ (or close enough to it) by running the chain for a long time and using the values $X_n$ for large $n$.

- To create a transition matrix that results in $\pi$ as the stationary distribution, the easiest way is to try to ensure that the detailed balance equations are solved. That is, the easiest way is to try to create a reversible chain.

- The chain is reversible if there is detailed balance, which we can write as 

$$
\frac{\pi(j)}{\pi(i)} = \frac{P(i, j)}{P(j, i)}
$$

The right hand side only involves the transition probabilities of the chain that we want to create. The left hand side only involves ratios of the terms in $\pi$, and therefore can be checked even if we don't know the constant that normalizes $\pi$.

### Metropolis Algorithm
Exactly who proposed the first algorithm to create such a Markov Chain is the subject of some debate. A general version was proposed by Hastings. Here we will describe an earlier version attributed to Metropolis and co-authors in 1953.

The goal is to create a transition matrix $\mathbb{P}$ so that $\pi$ and $\mathbb{P}$ together solve the detailed balance equations. 

The algorithm starts with any symmetric, irreducible transition matrix $Q$ on the state space. For example, if the state space is numerical you could start with, "Wherever the chain is, it picks one of the three closest values (including itself) with probability $1/3$ each." For a pair of states $i$ and $j$, the transition probability $Q(i, j)$ is called the *proposal probability*.

The algorithm then introduces additional randomization to create a new chain that is irreducible and aperiodic and has $\pi$ as its stationary distribution.

Here are the rules that determine the transitions of the new chain.

- Suppose the chain is at $i$ at time $n$, that is, suppose $X_n = i$. Pick a state $j$ according to the proposal probability $Q(i, j)$. This $j$ is the candidate state to which your chain might move.

- Define the *acceptance ratio*
$$
r(i, j) = \frac{\pi(j)}{\pi(i)}
$$

- If $r(i, j) \ge 1$, set $X_{n+1} = j$.

- If $r(i, j) < 1$, toss a coin that lands heads with chance $r(i, j)$. 
     - If the coin lands heads, set $X_{n+1} = j$. 
     - If the coin lands tails, set $X_{n+1} = i$.
- Repeat all the steps, with $X_{n+1}$ as the starting value.

Thus the new chain either moves to the state picked according to $Q$, or it stays where it is. We say that it *accepts a move to a new state* based on $Q$ and $r$, and otherwise it doesn't move. 

The new chain is irreducible because the proposal chain is irreducible. It is aperiodic because it can stay in place. So it has a steady state distribution. 

The alogrithm says that this steady state distribution is the same as the distribution $\pi$ that was used to define the ratios $r(i, j)$.

### How to Think About the Algorithm
Before we prove that the algorithm works, let's examine what it is doing in the context of decoders.

First notice that we are requiring $Q$ to be symmetric as well as irreducible. The symmetry requirement makes sense as each detailed balance equation involves transitions $i \to j$ as well as $j \to i$.

Fix any starting decoder and call it $i$. Now you have to decide where the chain is going to move next, that is, what the next decoder is going to be. The algorithm starts this process off by picking a decoder $j$ according to $Q$. We say that *$Q$ proposes a move to $j$*.

To decide whether or not the chain should move to $j$, remember that the distribution $\pi$ contains the likelihoods of all the decoders. You want to end up with decoders that have high likelihood, so it is natural to compare $\pi(i)$ and $\pi(j)$.

The algorithm does this by comparing the *acceptance ratio* $r(i, j) = \pi(j)/\pi(i)$ to 1. 

- If $r(i, j) \ge 1$, the likelihood of $j$ is at least as large that of $i$, so you *accept the proposal* and move to $j$. 

- If $r(i, j) < 1$, the proposed decoder $j$ has *less* likelihood than the current $i$, so it is tempting to stay at $i$. But this risks the chain getting stuck at a local maximum. The algorithm provides a chance to avoid this, by tossing a biased coin. If the coin lands heads, the chain moves to $j$ even though $j$ has a *lower* likelihood than the current decoder $i$. The idea is that from this new position there might be paths to decoders that have the highest likelihoods of all.

### The Algorithm Works
We will now show that the detailed balance equations are solved by the desired limit distribution $\pi$ and the transition matrix $\mathbb{P}$ of the chain created by the Metropolis algorithm.

Take any two states $i$ and $j$.

#### Case 1: $\pi(i) = \pi(j)$
Then $r(i, j) = 1$. By the algorithm, $P(i, j) = Q(i, j)$ and also $P(j, i) = Q(j, i) = Q(i, j)$ by the symmetry of $Q$. 

Therefore $P(i, j) = P(j, i)$ and the detailed balance equation $\pi(i)P(i, j) = \pi(j)P(j, i)$ is satisfied.

#### Case 2: $\pi(j) < \pi(i)$
Then $r(i, j) < 1$, so

$$
P(i, j) ~=~ Q(i, j)r(i, j) 
~=~ Q(j, i)\frac{\pi(j)}{\pi(i)} ~~~ \text{(symmetry of } Q \text{ and definition of }r) 
$$

Now $r(j, i) > 1$, so the algorithm says $P(j, i) = Q(j, i)$.

Therefore
$$
P(i, j) ~ = ~ P(j, i)\frac{\pi(j)}{\pi(i)}
$$
which is the same as
$$
\pi(i)P(i, j) ~ = ~ \pi(j)P(j, i)
$$

#### Case 2: $\pi(j) > \pi(i)$
Reverse the roles of $i$ and $j$ in Case 2.

That's it! A simple and brilliant idea that provides a solution to a difficult problem. In lab, you will see it in action when you implement the algorithm to decode text.
