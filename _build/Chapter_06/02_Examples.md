---
redirect_from:
  - "/chapter-06/02-examples"
interact_link: notebooks/Chapter_06/02_Examples.ipynb
title: 'Examples'
prev_page:
  url: /Chapter_06/01_Binomial_Distribution
  title: 'The Binomial Distribution'
next_page:
  url: /Chapter_06/03_Hypergeometric_Distribution
  title: 'The Hypergeometric Distribution'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## Examples

In this section we will work with the binomial distribution in a variety of settings. The formula and code are straightforward enough. What you have to keep in mind are the conditions under which the binomial distribution is valid. It is the distribution of:

- the number of successes
- in a known number of independent trials
- with the same probability of success on each trial.

So don't use it for the number of aces in a hand of cards dealt without replacement.

### Example 1: Random Number Generator
A random number generator draws repeatedly at random with replacement from the 10 digits $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.

**Question 1.** The generator is run 20 times. Find the chance that 0 appears more than two times.

**Answer 1.**
- Are we looking at a number of successes? Yes, when 0 is "success".
- Known number of independent trials? Yes, $n = 20$, and the draws are with replacement.
- Same probability of success on each trial? Yes, $p = 0.1$.

The answer can be written in two equivalent ways:

$$
\sum_{k=3}^{20} \binom{20}{k} 0.1^k 0.9^{20-k}
= 1 - \sum_{k=0}^2 \binom{20}{k} 0.1^k 0.9^{20-k}
$$

The second form would be quicker if you were going to complete the numerical calculations by hand. But you are not going to be doing that. Rather, you will do:



{:.input_area}
```python
sum(stats.binom.pmf(np.arange(3, 21), 20, 0.1))
```





{:.output .output_data_text}
```
0.32307319481053343
```



or, equivalently,



{:.input_area}
```python
1 - sum(stats.binom.pmf(np.arange(3), 20, 0.1))
```





{:.output .output_data_text}
```
0.32307319481053431
```



**Question 2.** A class has seven GSIs and Tutors. Each  of them runs the random number generator 20 times, independently of the others. What is the chance that at most three of them get two 0's?

**Answer 2.** You can't think of this just as one set of $7 \times 20 = 140$ runs of the generator, because you have to keep track of each of the 7 sets of 20 runs separately.

So now what's a "trial"? It's a course staff member: GSI or tutor. There are 7 of them, and their results are independent of each other. "Success" means "gets two 0's in 20 runs". We want the chance of at most three successes. 

We're all set to use the binomial: $n = 7$, $k = 0, 1, 2, 3$, and $p$ is the probability of getting two 0's in 20 runs. Hence



{:.input_area}
```python
p = stats.binom.pmf(2, 20, 0.1)

sum(stats.binom.pmf(np.arange(4), 7, p))
```





{:.output .output_data_text}
```
0.89236130614839881
```



As a math formula, this is

$$
\sum_{k=0}^3 \binom{7}{k}p^k(1-p)^{7-k} ~~ \text{where } 
p = \binom{20}{2} 0.1^2 0.9^{18}
$$

### Example 2: Both Heads and Tails
Toss a coin 10 times. 

**Question.** What is the chance that you get at least 3 heads and at least 3 tails?

**Answer.** Here is a great first step in working with any distribution: identify the set of possible values that make your event occur.

Those are 3, 4, 5, 6, and 7 heads, and now the answer is clear:

$$
\sum_{k=3}^7 \binom{10}{k} 0.5^k 0.5^{10-k}
$$

which is



{:.input_area}
```python
sum(stats.binom.pmf(np.arange(3, 8), 10, 1/2))
```





{:.output .output_data_text}
```
0.89062500000000089
```



Resist the impulse to start off by calculating $P(H \ge 3)$, the chance of at least three heads, with $H$ denoting the number of heads. It's not very helpful here. To see why, let $T$ be the number of tails in the 10 tosses. Then

$$
P(H \ge 3, T \ge 3) = P(H \ge 3)P(T \ge 3 \mid H \ge 3)
$$ 

The first factor is easily found, but the second isn't clear at all. It's not $P(T \ge 3)$ because $H$ and $T$ are far from independent: $T = 10 - H$.

### Example 3: Conditional Distribution of the Trial that Results in the First Success
I have rolled a die 24 times. 

**Question.** Find the conditional distribution of the roll in which I saw "six", given that I saw 1 six in the 24 rolls.

**Answer.** Let $R$ be the roll in which the six appeared, and let $S$ be the total number of sixes in the 24 rolls. We want the conditional distribution of $R$ given $S = 1$.

When you are trying to find a distribution, always start with its possible values. I got 1 six, so its position $R$ can be any roll in the range 1 through 24.

For $k = 1, 2, \ldots 24$,

$$
\begin{align*}
P(R = k \mid S = 1) &= \frac{P(R = k, S = 1)}{P(S=1)} \\ \\
&= \frac{P(k-1 \text{ non-sixes, then six, then } 24-k \text{ non-sixes})}{P(S = 1)} \\ \\
&= \frac{(5/6)^{k-1} (1/6) (5/6)^{24-k}}
{\binom{24}{1}(1/6)^1(5/6)^{23}} \\ \\
&= \frac{1}{24}
\end{align*}
$$

Note the absence of $k$ in the answer. Given that I got 1 six, the position in which that six appeared is uniformly distributed across all the rolls.
