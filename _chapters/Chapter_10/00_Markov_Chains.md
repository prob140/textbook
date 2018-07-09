---
interact_link: notebooks/Chapter_10/00_Markov_Chains.ipynb
title: 'Chapter 10: Markov Chains'
permalink: 'chapters/chapter-10/00-markov-chains'
previouschapter:
  url: chapters/chapter-09/03-expected-waiting-times
  title: '9.3 Expected Waiting Times'
nextchapter:
  url: chapters/chapter-10/01-transitions
  title: '10.1 Transitions'
---

# Markov Chains #

A *stochastic process* is a collection of random variables on a probability space. We will study a kind of process that evolves over *discrete time*, that is, random variables $X_0, X_1, X_2, \ldots $. Our image is that the process starts with value $X_0$ at time 0, and then takes steps at times 1, 2, and so on, with $X_n$ representing the value at time $n$.

We have already seen examples of such processes. For example, an i.i.d. sequence of Bernoulli $(p)$ trials forms such a process, going back and forth between the two values 0 and 1, each move independent of all the others. But in many interesting processes, the value of the process in the future depends on its present and past values. We can use the past and present to predict the future behavior of the process.

Markov Chains form a class of stochastic processes. They are named after  [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov) (1856-1922) whom you will encounter in several sections of this course. Informally, in a Markov Chain the distribution of the process in the future depends only on its present value, not on how it arrived at its present value. This is called the *Markov property.* Formally,

- For each $n \ge 1$, the conditional distribution of $X_{n+1}$ given $X_0, X_1, \ldots , X_n$ depends only on $X_n$.
- That is, for every sequence of possible values $i_0, i_1, \ldots, i_n, i_{n+1}$,

$$ P(X_{n+1} = i_{n+1} \mid X_0 = i_0, X_1 = i_1 , \ldots, X_{n-1} = i_{n-1}, X_n = i_n) = P(X_{n+1} = i_{n+1} \mid X_n = i_n) $$

For example, consider a *random walk* where a gambler starts with a fortune of $\$a$ for some positive integer $a$, and bets on successive tosses of a fair coin. If the coin lands heads he gains a dollar, and if it lands tails he loses a dollar. 

Let $X_{0} = a$, and for $n > 0$ let $X_{n+1} = X_n + I_n$ where $I_1, I_2, \ldots $ is an i.i.d. sequence of Bernoulli $(1/2)$ trials. The Markov property holds for this process: given the gambler's fortune at time $n$, the distribution of his fortune at time $n+1$ doesn't depend on his fortune before time $n$. So the process $X_0, X_1, X_2, \ldots $ is a Markov Chain representing the evolution of the gambler's fortune over time. 

The *state space* of a Markov Chain is the set of possible values of the random variables in the chain. The state space of the random walk described above is the set of all integers. In this course we will restrict the state space to be discrete and typically finite.

### Conditional Independence
Recall that two random variables $X$ and $Y$ are independent if the conditional distribution of $X$ given $Y$ is just the unconditional distribution of $X$.

Random variables $X$ and $Y$ are said to be *conditionally independent given $Z$* if the conditional distribution of $X$ given both $Y$ and $Z$ is just the conditional distribution of $X$ given $Z$. That is, if you know $Z$, then additional knowledge about $Y$ doesn't change your opinion about $X$.

In a Markov Chain, if you define time $n$ to be the present, time $n+1$ to be the future, and times $0$ through $n-1$ to be the past, then the Markov property says that the past and future are conditionally independent given the present.
