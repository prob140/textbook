## Exercises ##

**1.** A bridge hand is a simple random sample of 13 cards from a standard deck of 52 cards. The *face cards* are the Jacks, Queens, and Kings; there are 12 face cards in all. Let $X$ be the number of face cards in a bridge hand.

(a) Fill in the blank with the name of a distribution along with the appropriate parameters:
$X$ has the $\underline{~~~~~~~~~~~~~~~~~}$ distribution.

(b) Find $P(X > 5)$.

(c) Find $E(X)$.

**2.** Let $X$ have the distribution given in the table below.

| value | -2  | -1  | 0   | 1   |
|------:|:---:|:---:|:---:|:---:|
|**probability**| 1/8 | 1/2 | 1/4 | 1/8|

Find 

(a) $E(X)$

(b) $E(\vert X \vert )$

(c) $E(\min(X, -1))$

(d) $E(X-1)$

(e) $E((X-1)^2)$

**3.** A student is taking a True/False test in which there are 30 questions. For each correct answer, the student will get 2 points. For each wrong answer, the student will lose 1 point. If the student leaves a question unanswered, the student will get 0 points for that question. 

The student answers all of the questions by rolling a die. If the die shows 1 or 2 spots, the student doesn’t answer the question. If it shows 3 or 4 spots, the student chooses False. If it shows 5 or 6 spots, the student chooses True. Find the student’s expected score on the test.

**4.** Let $p \in (0, 1)$ and let $X$ be the number of spots showing on a flattened die that shows its six faces according to the following chances:

- $P(X = 1) = P(X = 6)$

- $P(X = 2) = P(X = 3) = P(X = 4) = P(X = 5)$

- $P(X = 1 \text{ or } 6) = p$

(a) Find $E(X)$.

(b) Find $E(\vert X - 3.5 \vert)$. Explain algebraically and also by an intuitive argument why the answer is an increasing function of $p$.

**5.** A fair $n$-faced die is rolled $m$ times. Find the expected number of distinct faces seen.

**6.** Fix a positive integer $n$. Suppose you decide to run i.i.d. Bernoulli $(p)$ trials until either a trial results in 1 or you have run $n$ trials, whichever happens first. Let $T$ be the number of trials you run.

(a) Find $E(T)$ by using the tail sum formula.

(b) Find $E(T)$ by using the non-linear function rule.

**7.** A group of 100 students contains 20 Data Science majors. I pick students from the group one by one at random, until I pick a Data Science major. Let $S$ be the number of students I pick.

In each part below, provide a numerical answer as an integer $n$ or as a ratio of integers $\frac{n_1}{n_2}$, without using a calculator or computer.

(a) Find $E(S)$ if the students are picked with replacement.

(b) Find $E(S)$ if the students are picked without replacement.

**8.** A robot types on a 26-letter keyboard that has lowercase letters only. Each letter is chosen independently and uniformly at random from the alphabet. If the robot types $n$ letters ($n \geq 11$), what is the expected number of times the sequence *probability* appears?

**9.** A box contains $n_R$ red balls, $n_B$ blue balls, and $n_G$ green balls. Balls are drawn one by one without replacement until all the red balls are drawn. Let $D$ be the number of draws made. Find $E(D)$. Then evaluate it (no calculators or computers) when $n_R=5, n_B=3, n_G=3$.

**10.** Let $n$ and $N$ be positive integers, and suppose n draws made at random with replacement from $\{1, 2, 3, \ldots, N \}$. Find the expectation of the minimum of the values drawn.

**11.** Suppose there are $m$ distinguishable pairs of socks, but a prankster chooses $d$ of these $2m$ socks at random and pokes holes in them. Let $X$ be the number of undamaged pairs of socks. Find $E(X)$.

**12.** The distribution of a random variable $X$ involves an unknown parameter $\theta$.

- $P(X = 1 ) = \theta$
- $P(X = 2) = 2\theta$
- $P(X = 3) = 1 - 3\theta$

(a) Find $E(X)$.

(b) Let $X_1, X_2, \ldots, X_n$ be i.i.d. with the same distribution as $X$, and let $\bar{X} = \frac{1}{n}\sum_{i}^n X_i$ be the sample average. Use $\bar{X}$ to construct an unbiased estimator of $\theta$.

**13.** Use probability theory to explain why the math identity below is true for all $\mu > 0$.

$$\sum_{k = 0}^\infty \sum_{j=k+1}^\infty \frac{\mu^j}{j!} ~ = ~
\sum_{k = 1}^\infty \frac{\mu^k}{(k-1)!}$$

**14.** Survey respondents understandably don’t like to answer questions about sensitive topics such as illegal drug use. If data scientists want to estimate the proportion of illegal drug users in a population, they have to devise methods of getting the information they need while maintaining the privacy of the individual respondents.

*Randomized response* schemes are often used in such situations. In one such scheme, each surveyed person is given a coin and asked to answer YES or NO after following these instructions out of sight of the surveyor:

- Toss the coin.
    - If it lands heads, then truthfully answer, “Do you use illegal drugs?”
    - If it lands tails, then toss it again and answer, “Did the second toss land heads?”

This way each respondent answers YES or NO but the surveyor doesn’t know which question was answered. The data scientists then have to estimate the proportion of illegal drug users based on the overall proportion of YES answers, which includes the YES answers to the second question.

Let the unknown proportion of illegal drug users in a large population be $p$, and suppose a random sample of size $n$ is surveyed using the scheme above. You can assume that the sampling is equivalent to drawing at random with replacement.

(a) Let $X$ be the proportion of sampled people who answer YES. Find $E(X)$.

(b) Use $X$ to construct an unbiased estimate of $p$.