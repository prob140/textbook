---
interact_link: notebooks/Chapter_01/02_Equally_Likely_Outcomes.ipynb
title: '1.2 Equally Likely Outcomes'
permalink: 'chapters/Chapter_01/02_Equally_Likely_Outcomes'
previouschapter:
  url: chapters/Chapter_01/01_Outcome_Space_and_Events
  title: '1.1 Outcome Space and Events'
nextchapter:
  url: chapters/Chapter_01/03_Collisions_in_Hashing
  title: '1.3 Collisions in Hashing'
redirect_from:
  - 'chapters/chapter-01/02-equally-likely-outcomes'
---

## Equally Likely Outcomes

"If a coin is tossed, what is the chance that it lands heads?" Ask this question and the most common answer that you will get is $1/2$. If you press for a reason, don't be surprised to hear, "Because the coin has two faces." A coin does indeed have two faces, but notice an assumption hidden inside the "reasoning" you have been given: that each of the two faces has the same chance as the other. 

The assumption of equally likely outcomes is a simple and ancient model of randomness. It defines probabilities as proportions. The assumption that $\Omega$ is finite makes proportions easy to identify as fractions of the total number of outcomes.

For some $n > 1$, let $\Omega$ consist of $n$ outcomes. Let $A \subseteq \Omega$ be an event. Define $\\#(A)$ to be the number of outcomes in the subset $A$. Thus $\\#(\Omega ) = n$, $\\#(\phi ) = 0$, and $0 < \\#(A) < n$ for any other event $A$.

For an event $A$, let $P(A)$ denote **the probability that $A$ occurs**, or **the chance that $A$ occurs**. We will use the words "probability" and "chance" synonymously, and we will often use "happens" instead of the more formal "occurs".

### Probabilities on a Space of Equally Likely Outcomes
If all $n$ outcomes in $\Omega$ are assumed to be equally likely, then the probability that the event $A$ occurs is defined by

$$
P(A) ~=~ \frac{\#(A)}{\#(\Omega )} ~=~ \frac{\#(A)}{n}
~=~ \text{proportion of outcomes in } A
$$

This idea that probabilities are proportions lies at the heart of many calculations. As you will see later, rules for combining proportions become rules for combining probabilities, whether or not all outcomes are equally likely. But for now we will work in settings where it is natural to assume that outcomes are equally likely.

### Example 1: Random Permutations
Let $\Omega$ be the space of all permutations of the letters $a$, $b$, and $c$. Then $\Omega$ contains $n=6$ outcomes:

$$
\Omega ~=~ \{ abc, ~acb, ~bac, ~bca, ~cab, ~cba \}
$$

If we assume that all six permutations are equally likely, we are working with what are called *random permutations* of the three letters. Under this assumption, we can augment our table of events with a column of chances.

Event | Verbal Description                               | Subset $~~~~~~~~~~~~$| Probability
:----:|:-------------------------------------------------|:-------------|:------:| 
$A$   | $a$ appears first                                |$\\{abc, ~acb\\}$ | $\frac{2}{6} = \frac{1}{3}$ 
$B$   | $b$ and $c$ are not next to each other           |$\\{bac, ~cab\\}$ | $\frac{1}{3}$
$C$   | the letters are in alphabetical order            | $\\{abc\\}$ | $\frac{1}{6}$    
$D$   | $a$ appears first, $b$ next, but $c$ isn't third | $\phi$ | $0$       
$E$   | $c$ is either first, second, or third            | $\Omega$ | $1$ 
$F$   | the letters form a word that means "taxi" | $\\{ cab \\}$ | $\frac{1}{6}$

Notice that
$$
P(a \text{ appears last}) = \frac{\#\{ bca, ~cba \}}{6} ~=~ \frac{1}{3}
~=~ \frac{\#\{ bac, ~cab \}}{6} ~=~ P(a \text{ appears second})
$$

Thus the assumption that all the permutations are equally likely makes all three positions of $a$ equally likely as well. The same is true of the positions of $b$ and $c$, as you should check.

### Example 2: Random Number Generator
Suppose a random number generator returns a pair of digits from among the 100 pairs 00, 01, 02, $\ldots$, 98, 99, in a way that makes all the pairs equally likely to be returned. 

You will have noticed that the pairs correspond to the 100 integers 0 through 99. In what follows, it will be useful to remind yourself of the product rule of counting: 
- There are 10 choices for the first digit: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.
- Corresponding to each choice of the first digit there are 10 choices for the second digit.
- So in total there are $10 \times 10 = 100$ pairs of digits. 

Here a "pair" is an sequence of two digits, one following the other. The pair 27 is different from the pair 72. These are sometimes called "ordered pairs". In this text, all sequences are ordered.

Now let's compute the probabilities of a few events. By assumption, all pairs are equally likely. So each answer will consist of counting the number of pairs in the event, and then dividing by the total number of pairs, which is 100.

**(i)** What is the probability that the pair consists of two different digits?

We have to count the number of pairs $ab$ where $a \ne b$. The digit $a$ can be chosen in 10 ways; for each of those ways, there are only 9 ways of choosing $b$ because $b$ has to be different from $a$. So the answer is
$$
P(\text{the pair consists of two different digits}) ~=~ \frac{90}{100} ~=~ 0.9
$$

**(ii)** What is the chance that the two digits are the same?

Let's try to use our answer to (i). In every one of the 100 pairs, either the two digits are the same or they are different. No pair can be in both categories, so by rules of proportion we have  

$$
P(\text{the two digits are the same}) ~=~ 1 ~-~
P(\text{the pair consists of two different digits}) ~=~ 0.1
$$

To check this by counting, you have to count pairs of the form $aa$. There are 10 ways to choose $a$, and there are no further choices to make. So the answer is $10/100 = 0.1$, confiriming our calculation above.
