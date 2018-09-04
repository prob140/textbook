---
interact_link: notebooks/Chapter_08/04_Review_Problems_Set_2.ipynb
title: '8.4 Review Problems: Set 2'
permalink: 'chapters/Chapter_08/04_Review_Problems_Set_2'
previouschapter:
  url: chapters/Chapter_08/03_Expectations_of_Functions
  title: '8.3 Expectations of Functions'
nextchapter:
  url: chapters/Chapter_09/00_Conditioning_Revisited
  title: 'Chapter 9: Conditioning, Revisited'
redirect_from:
  - 'chapters/chapter-08/04-review-problems-set-2'
---

## Review Problems: Set 2

These problems can be solved using the main ideas of Chapters 6 through 8. The material in those chapters of course relies on all the previous chapters.

The set of exercises is divided into two parts: The Basics, and Additional Practice. The first part will remind you of the fundamental concepts and some typical calculations. The rest are for you to further develop your problem solving skills and your fluency with the notation and ideas.

### The Basics

**1.** 
A coin is tossed 12 times. Find the chance that

(a) there are six heads

(b) there are more heads than tails (use the result of Part (a))

(c) there are more than four tails

(d) one of the faces appears twice as many times as the other

**2.** 
A bridge hand is a simple random sample of 13 cards from a standard deck of 52 cards. The *face cards* are the Jacks, Queens, and Kings; there are 12 face cards in all. Let $X$ be the number of face cards in a bridge hand.

(a) Fill in the blank with the name of a distribution along with the appropriate parameters:

$X$ has the $\underline{~~~~~~~~~~~~~~~~~}$ distribution.

(b) Find $P(X > 5)$.

(c) Find $E(X)$.

**3.** 
Each time it is run, a random number generator produces each of the 100 pairs of digits 00 through 99 with equal probability, independently of all other times. Let $X$ be the number of times it produces 00 in 100 runs. 

Fill in the blanks with the names of distributions along with the appropriate parameters:

The distribution of $X$ is exactly $$\underline{~~~~~~~~~~~~~~~~~}$$ and approximately $$\underline{~~~~~~~~~~~~~~~~~}$$.

**4.** 
[Pitman 3.5.12] Two radioactive substances emit $\alpha$-particles independently of each other. A counter records a Poisson $(5.41)$ number of particles from one substance and a Poisson $(3.87)$ number of particles from the other. Find the chance that the counter records at most four particles.

**5.** 
If you bet on "red" at roulette, your chance of winning is 18/38. Successive bets are independent of each other. Suppose you keep betting on red and stop when you have won a total of six bets.

(a) What is the chance that you place exactly 10 bets?

(b) What is the chance that you place more than 10 bets?

**6.** 
Let $X$ have the distribution given in the table below.

| value | -2  | -1  | 0   | 1   |
|------:|:---:|:---:|:---:|:---:|
|**probability**| 1/8 | 1/2 | 1/4 | 1/8|

Find 

(a) $E(X)$

(b) $E(\vert X \vert )$

(c) $E(\min(X, -1))$

(d) $E(X-1)$

(e) $E((X-1)^2)$

**7.**
A student is taking a True/False test in which there are 30 questions. For each correct answer, the student will get 2 points. For each wrong answer, the student will lose 1 point. If the student leaves a question unanswered, the student will get 0 points for that question.

The student answers all of the questions by rolling a die. If the die shows 1 or 2 spots, the student doesn't answer the question. If it shows 3 or 4 spots, the student chooses False. If it shows 5 or 6 spots, the student chooses True.

Find the student's expected score on the test.

**8.**
Each move in the game Monopoly is based on the total number of spots showing on two rolls of a die. Let $X$ be the number of times I see a total of four spots in my next 10 moves in Monopoly. Find $P(X =2)$.

**9.**
A die is rolled 10 times. Find the chance that the face that has six spots does not appear and every other face appears two times.

**10.**
Let $p \in (0, 1)$ and let $X$ be the number of spots showing on a flattened die that shows its six faces according to the following chances:

- $P(X = 1) = P(X = 6)$
- $P(X = 2) = P(X = 3) = P(X = 4) = P(X = 5)$
- $P(X = 1 \text{ or } 6) = p$

(a) Find $E(X)$.

(b) Find $E(\vert X - 3.5 \vert)$. Explain algebraically and also by an intuitive argument why the answer is an increasing function of $p$.

### Additional Practice

**11.**
If you bet a dollar on a "split" at roulette, you have a 2/38 chance of winning. If you win the bet, your net gain is $\\$17$. If you lose the bet, you lose your dollar.

Suppose you make 100 bets. Find the chance that you come out ahead, that is, the chance that you end up with more money than you had at the start.

**12.**
Let $X_1, X_2, \ldots, X_n$ be i.i.d. Poisson $(\lambda)$ random variables.

(a) Find the distribution of the sample sum $S_n = X_1 + X_2 + \cdots + X_n$.

(b) Let $A_n = S_n/n$ be the sample average. For a non-negative integer $k$, find $P(A_n \le k)$.

**13.**
[Pitman 2.rev.10] According to a newspaper report, in 2 million lie detector tests, 300,000 were estimated to have produced erroneous results. Assuming these figures to be correct, answer the following:

If ten tests were picked at random from these 2 million tests, what would be the chance that at least one of them produced an erroneous result?  Sketch the histogram of the distribution of the number of erroneous results among these ten tests. 

Suppose these 2 million tests were done on a variety of machines. If a machine were picked at random, then ten tests picked at random from these tests performed on that machine, would it be reasonable to suppose that the chance that at least one of them produced an erroneous result would be the same as in a)?

**14.**
Dibya and Jason are playing tennis. The game consists of a sequence of sets. The first player to win $s$ sets wins the match. Suppose the probability that Jason wins a set is $p$ (where  $0 < p < 1$), independent of the result of any other set. What is the probability that Jason wins the match?

**15.**
Let $X$ have the Poisson $(\mu)$ distribution. Find

(a) $E(X+1)$

(b) $E(1/(X+1))$

[First read the Poisson portions of Sections 8.1 and 8.3.]

**16.**
A test for a disease produces a correct result with chance 0.99. Suppose the test is run on 300 patients.

(a) What is the chance that for at least 295 patients the result is correct?

(b) Justify a Poisson approximation for the chance in (a), and find the value of the approximation.

**17.**
Roll a fair $n$-sided die $m$ times. Find the expected number of distinct faces seen.

**18.**
Seven dice are rolled. Write down unsimplified expressions for the probabilities of each of the following events:

(a) exactly two sixes

(b) two of one kind and five of another 

(c) two fours, two fives, and three sixes

(d) each number appears

(e) the sum of the dice is 9 or more

**19.**
Use consecutive odds ratios to find the mode of the Poisson $(\mu)$ distribution. Be careful about the case where $\mu$ is an integer.

**20.**
A monkey types on a 26-letter keyboard that has lowercase letters only. Each letter is chosen independently and uniformly at random from the alphabet. If the monkey types $n$ letters ($n \ge 11$), what is the expected number of times the sequence "probability" appears? 

**21.**
I see a Poisson $(15)$ number of cars. Assume that each car has chance 0.2 of being a hybrid and chance 0.1 of being electric, independently of all other cars. Find the chance that I see 3 hybrid cars, 2 electric cars, and 8 cars of other types.

**22.**
A box contains $n_R$ red balls, $n_B$ blue balls, and $n_G$ green balls. Balls are drawn one by one without replacement until all the red balls are drawn. Let D be the number of draws made. Calculate $E(D)$. Then, evaluate it (no calculators or computers) when $n_R=5, n_B=3, n_G=3$.

**23.**
Let $n$ and $N$ be positive integers, and suppose $n$ draws made at random with replacement from $\{1, 2, 3, \ldots, N\}$. Find the expectation of the minimum of the values drawn.

**24.**
Suppose you have $N$ balls where $N$ has the Poisson $(\lambda)$ distribution. Each ball is thrown into into one of $m$ bins chosen uniformly at random, independent of all other balls. Find $P(\text{there is an empty bin})$.

**25.**
Let $X$ and $Y$ be independent random variables such that $X$ has the Poisson $(\lambda)$ distribution and $Y$ has the Poisson $(\mu)$ distribution. For a fixed integer $n$, find the conditional distribution of $X$ given $X+Y=n$. Identify it as one of the famous ones and provide the parameters in terms of $n$, $\lambda$, and $\mu$.

**26.**
Suppose there are $m$ distinguishable pairs of socks, but a prankster chooses $d$ of these $2m$ socks at random, and pokes holes in them.  Let $X$ be the number of undamaged pairs of socks. Find $E(X)$.

**27.**
The distribution of a random variable $X$ involves an unknown parameter $\theta$.

- $P(X = 1 ) = \theta$
- $P(X = 2) = 2\theta$
- $P(X = 3) = 1 - 3\theta$

(a) Find $E(X)$.

(b) Let $X_1, X_2, \ldots, X_n$ be i.i.d. with the same distribution as $X$, and let $\bar{X} = \frac{1}{n}\sum_{i}^n X_i$ be the sample average. Use $\bar{X}$ to construct an unbiased estimator of $\theta$.

**28.**
Use probability theory to explain why the math identity below is true for all $\mu > 0$. 

$$
\sum_{k = 0}^\infty \sum_{j=k+1}^\infty \frac{\mu^j}{j!} ~ = ~
\sum_{k = 1}^\infty \frac{\mu^k}{(k-1)!}
$$

**29.**
Survey respondents understandably don't like to answer questions about sensitive topics such as illegal drug use. If data scientists want to estimate the proportion of illegal drug users in a population, they have to devise methods of getting the information they need while maintaining the privacy of the individual respondents. 

*Randomized response* schemes are often used in such situations. In one such scheme, each surveyed person is given a coin and asked to answer YES or NO after following these instructions out of sight of the surveyor:

- Toss the coin. 
    - If it lands heads, then truthfully answer, "Do you use illegal drugs?"
    - If it lands tails, then toss it again and answer, "Did the second toss land heads?"

This way each respondent answers YES or NO but the surveyor doesn't know which question was answered. The data scientists then have to estimate the proportion of illegal drug users based on the overall proportion of YES answers, which includes the YES answers to the second question.

Let the unknown proportion of illegal drug users in a large population be $p$, and suppose a random sample of size $n$ is surveyed using the scheme above. You can assume that the sampling is equivalent to drawing at random with replacement.

(a) Let $X$ be the proportion of sampled people who answer YES. Find $E(X)$.

(b) Use $X$ to construct an unbiased estimate of $p$.
