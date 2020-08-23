## Exercises ##

**Course conventions:** You can assume the following unless otherwise stated.

- A coin is equally likely to land heads or tails, regardless of the results of other tosses.
- A die is equally likely to show any of its six sides, regardless of the results of other rolls.
- Choosing at random means that all elements in the set of choices are equally likely.

We will make more formal statements about these assumptions in the next chapter.

**1.** A die is rolled 8 times. Say whether each of the following statements is
true or false. If you say it is false, provide the correct chance.

(a)  The chance that all 8 rolls show the face with four spots is
    $\frac{1}{6^8}$.

(b)  The chance that all 8 rolls show the same face is $\frac{1}{6^8}$.



**2.** Ryan rolls a die six times. Find the chance that Ryan sees all the faces of the die.

**3.** Huiyi, Xinran, and Ewen arrive for a meeting in a random order. Letting $H$, $X$, and $E$ represent Huiyi, Xinran, and Ewen, respectively, all permutations of $H$, $X$, and $E$ are equally likely.

(a) For each event below, write the subset of permutations and probability for that event.

$A_1$: Huiyi arrives first

$A_2$: Huiyi arrives second

$A_3$: Huiyi arrives third

(b) What is the probability that Ewen arrives before Xinran?

**4.** There are 30 students enrolled in a lab. Find the chance that at least
one student has the same birthday as the instructor’s, assuming that the
instructor’s birthday is a fixed day and every student’s birthday is
equally likely to be any of 365 days of the year regardless of everyone
else’s birthday.

**5.** A monkey hits the keys of a typewriter at random, picking each of the 26
letters of the English alphabet uniformly each time regardless of what
it has picked at all other times.

(a)  What is the chance that the first six letters are ORANGE, in that order?

(b)  What is the chance that the first six letters can form the word ORANGE, by rearrangement if necessary?
    

**6.** A class has $n$ GSIs and $m$ slots for office hours. Suppose each GSI chooses an office hour slot at random, regardless of the choices of the other GSIs. What is the chance that all the GSIs choose the same slot? 

**7.** A mail room has $n$ empty mail slots, for some fixed positive integer $n$.
The slots are labeled 1 through $n$. 

I have $2n$ letters. For each letter, I pick a mail slot at random and put the letter in it, regardless of my choices for the the other letters.

(a) Find the chance that Slot 1 is empty after I have deposited all $2n$ letters.

(b) Assuming that $n$ is very large, find an exponential approximation for the probability in Part (a).

**8.** A data scientist has a sample that consists of $n$ people. As you know from Data 8, a bootstrap sample consists of $n$ people drawn at random with replacement from the original sample. That means each person drawn is put back in the sample before the next person is drawn.

(a) Find the chance that the bootstrap sample is exactly the same as the original sample.

(b) A Prob 140 student is in the original sample. Find the chance that this student is not selected in the bootstrap sample.

(c) Assume that $n$ is large, and find an exponential approximation to the chance in Part (b).

**9.** You will need a code cell to get numerical answers to some parts of this question. But you shouldn't need to import any libraries.

At the end of [Section 1.5](http://prob140.org/textbook/content/Chapter_01/05_An_Exponential_Approximation.html), there is an approximate value of the chance of a collison in $n$ trials involving $N$ available codes.

Let's call it Approximation 1:

$$
P(\text{collision}) ~ \sim ~ 1 - e^{-\frac{n^2}{2N}}
$$

A simpler approximation is often used is Approximation 2:

$$
P(\text{collision}) ~ \approx ~ \frac{n^2}{2N}
$$

See [Wikipedia](https://en.wikipedia.org/wiki/Birthday_attack#Simple_approximation), for example, and keep in mind that their $H$ is our $N$.

(a) Derive Approximation 2 from Approximation 1. Refer to [properties of the exponential function](http://prob140.org/resources/exponential_approximations/) if you need to.

(b) As you have seen, for $N = 365$ the chance of a collision is just over 0.5 when $n = 23$. Use Approximation 2 to find an approximate value of $n$ by setting $P(\text{collision})$ to be 0.5 and $N$ to be 365. 

(c) The answer to Part (b) is not great as an approximation to 23, but it's not terrible either. The simple approximation is a great way to get a rough sense of how many trials you need to for a specified collision probability when $N$ is too large for exact calculations. 

For example, suppose you use a 64-bit hash. Then there are $N = 2^{64} \approx 1.8 \times 10^{19}$ hash values. Use Approximation 2 to find an approximate number of trials $n$ so that the probability of a collision is about 0.25. Use the code cell below to write an expression that evaluates to the numerical value of the $n$ that you found.

**10.** Ophelia is forming a committee of 6 students. There are 40 students from whom she can choose. Of these, 15 are first-year students, 10 are second-year students, 6 are third-year students, 4 are fourth-year students, and 5 are graduate students.

(a) How many different committees of 6 students can be formed from a group of 40 students?

(b) Assume that Ophelia chooses at random from all the different possible committees. What is the chance that she picks a committee that has no second-year students?

(c) As in Part (b), assume that Ophelia chooses at random from all the different possible committees. What is the chance that she picks a committee that consists of equal numbers of first-year students and graduate students?

