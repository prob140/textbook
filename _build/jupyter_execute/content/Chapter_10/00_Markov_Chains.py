# Markov Chains # 

A *stochastic process* is a collection of random variables on a probability space. We will study a kind of process that evolves over *discrete time*, that is, random variables $X_0, X_1, X_2, \ldots$. A good visual image is that the process starts with value $X_0$ at time 0, and then takes steps at times 1, 2, and so on, with $X_n$ representing the value at time $n$.

We have already seen examples of such processes. For example, an i.i.d. sequence of Bernoulli $(p)$ trials forms such a process, going back and forth between the two values 0 and 1, each move independent of all the others. But in many interesting processes, the value of the process in the future depends on its present and past values. We can use the past and present to predict the future behavior of the process.

Markov Chains form a class of stochastic processes. They are named after  [Andrey Markov](https://en.wikipedia.org/wiki/Andrey_Markov) (1856-1922) whom you will encounter in several sections of this course. Informally, in a Markov Chain the distribution of the process in the future depends only on its present value, not on how it arrived at its present value. Such processes turn out to have powerful applications even though the probabilistic assumption is rather simple.




```{toctree}
:hidden:
:titlesonly:


01_Transitions
02_Deconstructing_Chains
03_Long_Run_Behavior
04_Examples
```
