## Exercises ##

**1.** My bridge partner and I are playing a game of bridge against two other people. In the game, four hands of 13 cards each are dealt to the four players, at random without replacement from a standard deck. Let $X$ be the number of hearts in my hand and let $Y$ be the number of hearts in my partner's hand. For $k = 0, 1, 2, \ldots, 13$, find $E(Y \mid X=k)$.

**2.** I draw a simple random sample of $n_0$ balls from an urn that contains $b_0$ blue balls and $r_0$ red balls. I put the balls in my sample in another urn that already contains $b_1$ blue balls and $r_1$ red balls. I then draw a simple random sample of $n_1$ balls from the second urn. Find the expected number of blue balls in this sample.

**3.** A snack-delivery robot is attempting to deliver candy to Shahzar. Whenever it leaves its home base, it can take one of two paths picked independently of past behavior.

- With probability $4/5$, it heads directly towards Shahzar and reaches him at a random time with an expected duration of 10 minutes.
- With probability $1/5$, it heads off in the wrong direction and returns to its home base (without finding Shahzar) at a random time with an expected duration of 30 minutes, and then immediately leaves again as described.

Find the expected time between when the robot leaves home base and when it reaches Shahzar.

**4.** Ophelia has to call a utility company to get help with a problem at her apartment. Once she reaches a customer service representative, the length of the call till her problem is solved is random with an expectation of 7 minutes.

But it is not easy to reach a customer service representative.

- When Ophelia calls, there is 90% chance that she will be put on hold for a random time with an expected duration of 12 minutes before reaching a customer service representative.
- There is a 10% chance that she will be put on hold for a random time with an expected duration of 8 minutes at which point the call will be cut off for no reason and she will have to call again. 

Ophelia needs her problem to be fixed, so she keeps calling until she reaches a representative and her problem is solved. You can assume there is no lag between repeated calls and that all durations of holds and conversations with representatives are independent of each other.

Find the expected length of time Ophelia is on the phone till her problem is solved.

**5.** You have seen this model before; it is used in many contexts, for example to model contagion. Start with one white and one black ball. Draw one ball at random, then replace it in the urn along with another ball of its color. Keep doing this.

Let $B_n$ be the number of black balls in the urn just before the $n$th ball is drawn. So $B_1 = 1$ with probability 1. 

(a) Just before the $n$th ball is drawn, how many balls are there in the urn?

(b) For each $n$, find $E(B_{n+1} \mid B_n)$.

(c) Use induction and Part **b** to find $E(B_n)$ for each $n$.

(d) Let $X_n$ be the proportion of black balls in the urn just before the $n$th ball is drawn. Find $E(X_n)$ for each $n$.

**6.** Consider a sequence of i.i.d. trials, each of which results in one of three mutually exclusive categories of outcomes. On each trial, let the chance of Category $i$ be $p_i > 0$ with $p_1 + p_2 + p_3 = 1$.

Show that the chance that Category 1 appears before Category 2 is $p_1/(p_1 + p_2)$. This is called the *craps principle*.

[The goal is for you to practice conditioning, so don't use geometric sums. Just condition on the first couple of trials. Either the event happens right away, or $\ldots$ what?]

**7.** Use induction and a textbook [example](http://prob140.org/textbook/content/Chapter_09/03_Expected_Waiting_Times.html#waiting-till-hh) to find the expected waiting time till you see $n$ successes in a row in a sequence of i.i.d. Bernoulli $(p)$ trials.

