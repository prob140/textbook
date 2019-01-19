---
redirect_from:
  - "/chapter-05/05-review-problems-set-1"
interact_link: notebooks/Chapter_05/05_Review_Problems_Set_1.ipynb
title: 'Review Problem Set 1'
prev_page:
  url: /Chapter_05/04_Sampling_Without_Replacement
  title: 'Sampling Without Replacement'
next_page:
  url: /Chapter_06/00_Random_Counts
  title: 'Chapter 6: Random Counts'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## Review Problem Set 1

These problems can be solved using the main ideas of Chapters 1 through 5. It is divided into two parts: The Basics, and Additional Practice. The first part will remind you of the fundamental concepts and some typical calculations. The rest are for you to further develop your problem solving skills and your fluency with the notation and ideas.

### The Basics

**1.**
A procedure for estimating a parameter is based on random sampling and has a 95% chance of producing a good estimate. Suppose I run this procedure $n$ times such that the results of all the different runs have no effect on each other. What is the chance that at least one of the $n$ estimates is **not** good?

**2.**
A monkey hits the keys of a typewriter at random, picking each of the 26 letters of the English alphabet uniformly each time regardless of what it has picked at all other times.

(a) What is the chance that the first six letters are ORANGE, in that order?

(b) What is the chance that the first six letters can form the word ORANGE, by rearrangement if necessary?

**3.**
A die is rolled 8 times. Say whether each of the following statements is true or false. If you say it is false, provide the correct chance.

(a) The chance that all 8 rolls show the face with four spots is $(1/6)^8$.

(b) The chance that all 8 rolls show the same face is $(1/6)^8$.

**4.**
Box A contains 1 black and 3 white marbles, and box B contains 2 black and 4 white marbles. A box is selected at random, then a marble is drawn at random from the selected box. Given that the marble is black, find the probability that Box A was chosen.

**5.**
There are 30 students enrolled in a lab. Find the chance that at least one student has the same birthday as the instructor’s, assuming that the instructor’s birthday is a fixed day and every student’s birthday is equally likely to be any of 365 days of the year regardless of everyone else’s birthday.

**6.**
A die is rolled six times. Find the chance that all six faces appear.

**7.**
A bag contains $m$ M&M's, of which $g$ are green, $r$ red, and $b$ brown. There are no other colors, so $m = g+r+b$. Assume $m \ge 10$. I pick 10 M&M's at random **without** replacement. 

(a) What is the chance that the tenth M&M I pick is green?

(b) What is the chance that second M&M I pick is red and the tenth is green?

**8.**
A coin that lands heads with chance 1/1000 is tossed 2500 times. Find the chance that all the tosses show tails. Find an approximation to this chance in terms of $e$.

**9.**
A population consists of 20 people, of whom 8 are women and 12 are men. A simple random sample of 5 people will be drawn from the population. Which of the following is the chance that the sample contains exactly 3 women? Why?

(i) $$\frac{\binom{8}{3}}{\binom{20}{5}}$$


(ii) $$\frac{\binom{8}{3} \binom{12}{2}}{\binom{20}{5}}$$

**10.**
A standard deck consists of 52 cards. There are 13 cards in each of four suits. Cards are dealt one by one at random without replacement from the deck. Let $X$ be the number of cards dealt till the first time any suit appears more than once. For example, if the sequence of suits is Clubs, Diamonds, Hearts, Diamonds then $X = 4$. Find the distribution of $X$.

**11.**
In a box of numbered tickets, 20% of the tickets are numbered 0, 30% are numbered 1, and 50% are numbered 2. Two tickets are drawn from the box at random with replacement. Let $M$ be the maximum and $S$ the sum of the two numbers drawn.

(a) Find the joint distribution of $M$ and $S$.

(b) Find the conditional distribution of $S$ given $M = 1$.

**12.**
A roulette wheel has 38 pockets. Of these, 18 are red, 18 black, and 2 green. 
The wheel is spun 20 times. 
Assume that on each spin, each pocket is equally likely to appear; and assume that the spins are independent of each other. 
Find the probability that all three colors appear.

### Additional Practice

**13.**
A deck consists of 52 cards. A poker hand is 5 	cards dealt at random without replacement.

(a) How many 5-card poker hands are there?

(b) I play poker two times. What is the chance I get the same hand both times?

**14.**
A population consists of 10 children, 15 women, and 20 men. I sample 5 people at random without replacement. In the sample, let $K$ be the number of children, $W$ the number of women, and $M$ the number of men.

(a) Find the joint distribution of $K$ and $W$.

(b) Find the distribution of $W$.

(c) Find the conditional distribution of $W$ given that $K = 2$.

**15.**
A lie detector is known to be reliable 80% of the time when the person is guilty, and 90% reliable when the person is innocent. A suspect is chosen at random from a group of suspects of whom only 1% have ever committed a crime. If the test indicates that the suspect is guilty, what is the probability that the suspect is innocent?

**16.**
Assume as usual that if events $A$ and $B$ in a probability space are mutually exclusive, then $P(A \cup B) = P(A) + P(B)$. Show by the method of induction that 

$$
P(\bigcup_{i=1}^n A_i) ~ = ~ \sum_{i=1}^n P(A_i) ~~~~~ \mbox{if } A_1, A_2, \ldots, A_n \mbox{ are mutually exclusive}
$$

**17.**
The multiplication rule says that $P(A_1A_2) = P(A_1)P(A_2 \vert A_1)$. 
Use induction to show that for events $A_1, A_2, \ldots, A_n$, 

$$
P(A_1A_2 \ldots A_n) ~ = ~ P(A_1)P(A_2 \vert A_1)P(A_3 \vert A_1A_2) \cdots P(A_n \vert A_1A_2 \ldots A_{n-1})
$$

**18.**
There are three boxes, each with two drawers. Box 1 has a gold coin in each drawer and box 2 has a silver coin in each drawer. Box 3 has a silver coin in one drawer and a gold coin in the other. One box is chosen at random, and then a drawer is chosen at random from the box. Find the probability that box 1 is chosen, given that the chosen drawer yields a gold coin.

19.
Let $X$ be the minimum of $n$ integers drawn at random with replacement from the set $1, 2, 3, \ldots, N$.

(a) For each $k$ in the range 1 through $N$, find $P(X \ge k)$.

(b) For each $k$ in the range 1 through $N$, use Part (a) to find $P(X = k)$.

**20.**
A hat contains $n$ coins, $f$ of which are fair, and $b$ of which are biased to land heads with probability $2/3$. A coin is drawn at random from the hat and tossed twice. The first time it lands heads, and the second time it lands tails. Given this information, what is the probability that it is a fair coin?

**21.**
A mail room has $n$ empty mail slots, for some fixed positive integer $n$. The slots are labeled $1$ through $n$. I have $2n$ letters. For each letter, I pick a mail slot uniformly at random and put the letter in it. Assume that my choices for the $2n$ letters are independent of each other. 

(a) Find the chance that Slot 1 is empty after I have deposited all $2n$ letters. 

(b) Assuming that $n$ is very large, find an exponential approximation for the probability in Part (a).

**22.**
A population has three classes of individuals, in the proportions 0.6, 0.3, and 0.1. If you sample $n$ individuals at random with replacement, what is the chance that all three classes appear in the sample?

**23.**
Eight rooks are placed at positions sampled randomly without replacement on an $8 \times 8$ chessboard. What is the probability that none of them attacks any of the others? (Two rooks attack each other if they are in the same row or in the same column.)

**24.**
A deck of five cards contains two aces and three queens. The five cards are shuffled and dealt one by one. This problem is about the number of cards dealt till the aces appear. For example, if the order of the cards dealt was QAQQA, then the number of cards dealt until the first ace is $2$, and until the second ace is $5$.

(a) Draw a table that displays the distribution of the number of cards dealt until the first ace. 

(b) Draw a table that displays the distribution of the number of cards dealt until the second ace.

(c) Explain why the probabilities in the second table are just those in the first in a different order. [Hint: think about dealing off the bottom of the deck!]

**25.**
Cards are dealt from a well-shuffled standard deck until the first heart appears. Let $D$ be the number of cards dealt.

(a) Find $P(D = 5)$.
    
(b) Find $P(D \le 5)$?

(c) Find $P(D = 3 \mid D \le 5)$.

**26.**
In a raffle with $100$ tickets, $10$ people buy $10$ tickets each. Three winning tickets are drawn at random from this pool of $100$ tickets. Let $W$ be the number of people who win. Find:

(a) $P(W > 1)$

(b) $P(W = 3)$

**27.**
Consider a $5$ card hand dealt from a standard card deck. Assume that all ${52 \choose 5}$ hands are equally likely. Find the probability of being dealt:

(a) four of a kind (ranks a,a,a,a,b)

(b) one pair (ranks a,a,b,c,d)

**28.**
A classroom has $n$ students, where $2$ of the students are twins. Assume that each year consists of 365 days, each of the non-twins is equally likely to be born on any day independent of one another, and the twins are equally likely to be born on any day, independent of the rest.  If $r$ students are sampled from this room without replacement, find an *exact* expression for the probability that two students have the same birthday in this sample. 

**29.**
Seven dice are rolled. Write an expression for  $P(\text{three of one face and four of another})$.

**30.**
In a hand of 13 cards drawn randomly from a pack of 52, find the chance that at most one of the following ranks appears: Jack, Queen, King, Ace.

**31.**
Let $U_1$ and $U_2$ be independent, each uniformly distributed on $\{1, 2, \ldots, n\}$. Let $S = U_1 + U_2$.

(a) Find $P(U_1 = U_2)$.

(b) Use Part (a) and symmetry to find $P(U_1 < U_2)$ and $P(U_1 > U_2)$.

(c) Find the distribution of $S$.


**32.**
Three events $A$, $B$, and $C$ are subsets of an outcome space. Let $N$ be the number of these events that occur. The goal of this problem is to find the distribution of $N$ in terms of the probabilities $P(A)$, $P(B)$, $P(C)$, $P(AB)$, $P(AC)$, $P(BC)$, and $P(ABC)$ only; no complements. Do this in the following steps.

(a) What are the possible values of $N$?

(b) Find $P(N = 3)$.

(c) Find $P(N = 0)$. It's a good idea to draw a Venn diagram.

(d) Find $P(N = 2)$. Use your Venn diagram again.

(e) Find the remaining components of the distribution of $N$.

**33.**
The Statistics Department used to have a "birthday cake" tradition: once a month, there would be a cake to celebrate the birthdays of all department members whose birthdays were in that month. Suppose this tradition continues and suppose the department has $n$ members. Assume that each member's birthday is equally likely to be one of the 12 months of the year, independently of all others.

Consider one calendar year (January through December), starting in January.

(a) What is the probability that no birthday cake will be needed after September?

(b) What is the probability that there will be birthday cake in September but not after that?

**34.**
A standard deck of 52 cards contains 4 kings. Cards are drawn at random without replacement till there are none left in the deck. Find the chance that the last king appears on the 40th draw.

**35.**
Two draws are made at random from a box containing four tickets numbered 1, 2, 2, and 3. Let $X_1$ be the number on the first ticket drawn and $X_2$ the number on the second. In each part below, say whether the statement is true or false and justify your reasoning.

(a) If the draws are made with replacement, then $X_1$ and $X_2$ are independent.

(b) If the draws are made without replacement, then $X_1$ and $X_2$ are independent.

(c) If the draws are made with replacement, then $X_1$ and $X_2$ are have the same distribution.

(d) If the draws are made without replacement, then $X_1$ and $X_2$ have the same distribution.

**36.**
There are 100 men and 100 women who have agreed to participate in a randomized controlled experiment. The researchers are going to pick 100 participants at random without replacement to form the treatment group. Write an expression for the chance that the treatment group contains at least 45 people of each of the two genders.

**37.**
There are $n$ GSIs and $m$ different slots for office hours. Assume $n \ge m$. Suppose each GSI selects a slot uniformly at random, independently of all the other GSIs. What is the chance that none of the slots is left unselected?

**38.**
*Polya's urn scheme* is a model for contagion and is used in many different contexts. At the start, the urn has $w$ white balls and $b$ blue balls. Every minute, one ball is drawn at random from the urn and then replaced in the urn along with $d$ additional balls of its color. Let $B_n$ be the event that the ball drawn at the $n$th minute is blue. Let's define the 0th minute to be the start, so that $P(B_1) = b/(w+b)$.

(a) Find $P(B_2)$. Make sure you simplify the answer as much as possible; you will see why.

(b) Guess a formula for $P(B_n)$ and prove it by induction.
