---
interact_link: notebooks/Chapter_02/02_Examples.ipynb
title: '2.2 Examples'
permalink: 'chapters/Chapter_02/02_Examples'
previouschapter:
  url: chapters/Chapter_02/01_Addition
  title: '2.1 Addition'
nextchapter:
  url: chapters/Chapter_02/03_Multiplication
  title: '2.3 Multiplication'
redirect_from:
  - 'chapters/chapter-02/02-examples'
---

## Examples

Let's see if we can use the results we've developed to calculate some chances. Some of the steps will be clear without calculation; others will require more work. 

### Example 1: Both Heads and Tails in $n$ Tosses
A coin is tossed $n$ times so that all $2^n$ possible sequences of heads and tails are equally likely. 

**Question.** What is the chance of getting at least one head and at least one tail?

**Answer.** There are many sequences in which each face appears at least once. For example, if $n=4$, such sequences include HTTT, HTHT, TTHT, and so on. 

**Method – Complement:** 
When an event can happen in many different ways, it might be a good idea to look at the ways in which it *doesn't* happen, in case there are fewer of those.** 

For $n=4$, the only sequences in which we *don't* get at least one occurrence of each face are HHHH and TTTT. Indeed, for any $n$, there are only two sequences in which we don't get both faces: all heads, and all tails. These are the two sequences in which all the elements are the same.

Let $A$ be the event that we get at least one head and at least one tail. The question asks for $P(A)$. Because $A^c$ is the event "all the elements of the sequence are the same", we have
$$
P(A^c) = \frac{2}{2^n} = \frac{1}{2^{n-1}}
$$
By the complement rule,
$$
P(A) = 1 - \frac{1}{2^{n-1}}
$$
Notice that the answer tends to 1 as $n$ gets large. With a large number of tosses, you are almost certain to see both heads and tails.


### Example 2: Maximum of 12 Rolls of a Die
A die is rolled 12 times so that all $6^{12}$ sequences of faces are equally likely. Define the *maximum* of the 12 rolls to be the largest of the numbers that appear on the 12 faces. For example, the maximum of the sequence "354222143351" is 5.

**Question 1.** What is the chance that the maximum is less than 5?

**Answer 1.** The key is to observe that the event "the maximum is less than 5" is the same as the event "all the 12 faces are less than 5". For this to occur, each of the 12 faces has to have one of the four values 1 through 4. So
$$
P(\text{maximum is less than 5}) = \frac{4^{12}}{6^{12}}
$$
Yes, we could simplify that further, but we're not going to, for reasons that will soon become clear.

**Question 2.** What is the chance that the maximum is less than 4?

**Answer 2.** Nothing new here, other than replacing 5 by 4 in Question 1. 
$$
P(\text{maximum is less than 4}) = \frac{3^{12}}{6^{12}}
$$

**Question 3.** What is the chance that the maximum is equal to 4?

**Answer 3.** The task of writing down all the sequences in which the maximum is equal to 4 isn't pleasant. Let's see if we can use what we already know. For the maximum to be equal to 4:

- The maximum has to be less than 5,
- and it can't be less than 4.

We're thinking of the set $\{4\}$ as a difference: $\{1, 2, 3, 4\} \backslash \{1, 2, 3\}$.

So by the difference rule,

$$
\begin{align*}
P(\text{maximum is equal to 4}) &= P(\text{maximum is less than 5}) - P(\text{maximum is less than 4}) \\
&= \frac{4^{12}}{6^{12}} - \frac{3^{12}}{6^{12}}
\end{align*}
$$

There is nothing special about 12 rolls. You can replace 12 by $n$ throughout, and the argument will go through just as above.

The maximum is an example of an *extremum*, the other being the minimum. 

**Problem solving technique:** When you work with extrema, remember the observation we used in this example: saying that the maximum is small is the same as saying that all the elements are small. Analogously, saying the minimum is large is the same as saying that all the elements are large.

### Example 3: Second Random Digit Greater than the First
A random number generator produces two digits so that all the 100 pairs of digits are equally likely.

**Question.** What is the chance that the second digit is greater than the first?

**Answer, Method I – Partition:** Make an organized list of all the ways in which the event can happen. A good way to list the pairs in which the second digit is greater than the first is to *partition* the pairs according to the value of the first digit:

- first digit 0, second 1 through 9
- first digit 1, second 2 through 9
- first digit 2, second 3 through 9
- and so on, down to
- first digit 8, second digit 9

This partition makes it easy to count all the pairs in which the second digit is greater than the first: there are $9+8+7+6+5+4+3+2+1 = (9\times10)/2 = 45$ of them among the 100 possible pairs. So the answer is 0.45.

**Answer, Method II – Symmetry:** Convince yourself of some symmetry: the chance that the second digit is greater than the first is the same as the chance that the first digit is greater than the second. One way to do this is to partition the second event according to the value of the second digit and notice the correspondence with the partition in Method I.

So if $p = P(\text{second digit is greater than the first})$, the addition rule says
$$
\begin{align*}
1 &= P(\text{first digit is greater than the second}) + P(\text{the two digits are equal}) + P(\text{second digit is greater than the first}) \\
&= p + \frac{10}{100} + p
\end{align*}
$$

because there are 10 pairs of equal digits: 00, 11, 22, $\ldots$, 99. Now solve for $p$:

$$
p = \frac{1 - 0.1}{2} = 0.45
$$
as before.

It is a good idea to learn both methods. Partitions and symmetry will be used throughout this course.
