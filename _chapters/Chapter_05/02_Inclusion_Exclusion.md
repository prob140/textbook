---
interact_link: notebooks/Chapter_05/02_Inclusion_Exclusion.ipynb
title: '5.2 Inclusion-Exclusion'
permalink: 'chapters/Chapter_05/02_Inclusion_Exclusion'
previouschapter:
  url: chapters/Chapter_05/01_Bounding_the_Chance_of_a_Union
  title: '5.1 Bounding the Chance of a Union'
nextchapter:
  url: chapters/Chapter_05/03_The_Matching_Problem
  title: '5.3 The Matching Problem'
redirect_from:
  - 'chapters/chapter-05/02-inclusion-exclusion'
---

## Inclusion-Exclusion

While we have bounds on the probability of the union of $n$ events, we don't yet have a formula for the exact chance except in the case $n = 2$. For $n = 2$ we have 

$$
P(A \cup B) = P(A) + P(B) - P(AB)
$$

### Union of $n$ Events
Let's see if we can guess the formula for larger $n$, by applying what we know about the union of two events. 

For $n = 3$, the event $A_1 \cup A_2 \cup A_3$ can be written as $B \cup A_3$ where $B = A_1 \cup A_2$. So by applying the formula for the case of two events in every line, we have

$$
\begin{align*}
P(A_1 \cup A_2 \cup A_3) ~ = ~ P(B \cup A_3) &= ~ P(B) + P(A_3) - P(BA_3) \\
&= ~ P(A_1) + P(A_2) - P(A_1A_2) + P(A_3) - P(A_1A_3 \cup A_2A_3)\\
&= ~ \sum_{i=1}^3 P(A_i) - \mathop{\sum \sum}_{1 \le i < j \le 3} P(A_iA_j) + P(A_1A_2A_3)
\end{align*}
$$

A clear pattern is emerging. Writing it out will be easier if we have some rough-and-ready abbreviations of descriptions, so for example let "all the double-intersections" mean "all terms of the form $P(A_iA_j)$ where $i$ and $j$ are different".

It is important to note that the set "$1 \le i < j \le n$" specifies all unordered pairs of distinct indices. If the indices are distinct, one of them has to be less than the other, so it is part of the indicated set. If $i$ and $j$ are in the set, then $i < j$, so $i$ and $j$ are distinct.

In the same way, $1 \le i < j < k \le n$ specifies all unordered triples of distinct indices. And so on.

**Guess.** Based on what we saw for three events, we will guess that the chance of the union of $n$ events can be calculated by:

- including the probabilities of all the events; then
- excluding the probabilities of all the double-intersections; then
- including the probabilities of all the triple-intersections; then
- excluding the probabilities of all the quadruple intersections; and so on.

### General Inclusion-Exclusion Formula
For events $A_1, A_2, \ldots, A_n$, 

$$
\begin{align*}
& P\big{(}\bigcup_{i=1}^n A_i \big{)} \\
&= \sum_{i=1}^n P(A_i) - \mathop{\sum \sum}_{1 \le i < j \le n} P(A_iA_j) + \mathop{\sum \sum \sum}_{1 \le i < j < k \le n} P(A_iA_jA_k) - \cdots + (-1)^{n+1} P(A_1A_2 \ldots A_n) \\
\end{align*}
$$

You can prove this by induction if you feel inclined; just go through steps analogous to those above for the case $n=3$. We will prove the formula in a later chapter by a different method.

For now, let's accept it and move on.

### The Number of Terms in Each Sum
To end the section we will count the number of terms in each of the sums in the inclusion-exclusion formula, so we know the extent of the work that has to be done to apply it.

Here is the formula again for reference:

$$
\begin{align*}
& P\big{(}\bigcup_{i=1}^n A_i \big{)} \\
&=
\sum_{i=1}^n P(A_i) - \mathop{\sum \sum}_{1 \le i < j \le n} P(A_iA_j) + \mathop{\sum \sum \sum}_{1 \le i < j < k \le n} P(A_iA_jA_k) - \cdots + (-1)^{n+1} P(A_1A_2 \ldots A_n)
\end{align*}
$$


Clearly there are $n$ terms in the first sum. For reasons that will become clear in the next step, we will write that as

$$
\binom{n}{1} = n
$$

In the second sum the terms correspond to distinct unordered pairs chosen from the indices 1 through $n$. That number is

$$
\binom{n}{2} = \frac{n(n-1)}{2}
$$

In the third sum, the number of terms is the number of sets of three:

$$
\binom{n}{3} = \frac{n(n-1)(n-2)}{3!}
$$
and so on.

This shows that a lot of terms are being added and subtracted in the inclusion-exclusion formula. 

But sometimes we get lucky, and many of the terms are equal. Then the sums simplify dramatically. For a beautiful example, keep reading.
