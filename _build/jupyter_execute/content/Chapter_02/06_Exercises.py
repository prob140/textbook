## Exercises ##

**1.** Often, the axioms and rules derived in Sections [2.1](http://prob140.org/textbook/content/Chapter_02/01_Addition.html) and [2.3](http://prob140.org/textbook/content/Chapter_02/03_Multiplication.html) can be combined in different ways to find the same probability.

(a) Derive the *inclusion-exclusion formula* for two events:

For any two events $A$ and $B$, $P(A \cup B) ~ = ~ P(A) + P(B) - P(AB)$.

The formula's name reflects the fact that you include the chance of each event and then exclude the chance of the intersection.

(b) A die is rolled twice. Find the chance that at least one of the rolls shows six spots, in each of the three ways below.

(i) By listing the outcomes and counting how many are in the event in question

(ii) By using Part (a)

(iii) By the complement rule

**2.** Cell phone use is spreading widely but in many places there is still a divide. For example, among adults in India in 2018,

- 30% did not own a cell phone
- 17% were non-users in that they neither owned nor shared a cell phone
- Among the non-users, 31% said they would like to get a cell phone in the future

Suppose you picked an adult at random in India in 2018.

(a) What is the chance that the selected person was a non-user who didn't say they would like to get a cell phone in the future?

(b) Given that the selected person didn't own a cell phone, what is the chance that they shared one?

**3.** A True/False test consists of 25 questions. A student knows the answers to 18 of the questions. The remaining 7 answers they guess at random by tossing a fair coin each time. If it lands heads they answer True and if it lands tails they answer False.

One of the 25 questions is picked at random. Given that the student got the right answer, what is the chance that they knew the answer?

**4.** A poker hand is 5 cards dealt at random without replacement from a standard deck of 52 cards.

(a) How many 5-card poker hands are there?

(b) I play poker two times. Make the reasonable assumption that the hand I get the second time is unaffected by the first. What is the chance I get the same hand both times?

**5.** There are three boxes, each with two drawers. Box 1 has a gold coin in each drawer and Box 2 has a silver coin in each drawer. Box 3 has a silver coin in one drawer and a gold coin in the other. One box is chosen at random, and then a drawer is chosen at random from the box. Find the probability that Box 1 is chosen, given that the chosen drawer yields a gold coin.

**6.** A standard deck consists of 13 cards in each of 4 suits: clubs, spades, hearts, diamonds. Four cards are dealt at random without replacement from the 52 cards. Find the chance that at least one of the suits doesn't appear.

**7.** A procedure for estimating a parameter is based on random sampling and has a 95% chance of producing a good estimate. Suppose I run this procedure $n$ times such that the results of all the different runs have no effect on each other. 

(a) What is the chance that at least one of the $n$ estimates is not good?

(b) About how big does $n$ have to be for the chance in Part (a) to be 50%?

**8.** I have two dice. Die I has 1 red face and 5 blue faces. Die II has 3 red faces and 3 blue faces. I pick one of the dice at random and roll it twice. 

(a) What is the chance that I roll Die II?

(b) Given that I see both colors, is the chance that I rolled Die II the same as the answer to (a), greater than the answer to (a), or less than the answer to (a)? Without calculation, pick the correct option and explain your choice.

(c) Now do the calculation. Given that I saw both colors, what is the chance that I rolled Die II? Is your numerical answer consistent with your answer to (b)?

(d) What is the chance that I see a red face on the first roll?

(e) What is the chance that I see a blue face on the second roll?

(f) True or false (explain):

$$
\begin{align*}
&P(\text{red on the first roll and blue on the second roll}) \\
&= P(\text{red on the first roll}) \times P(\text{blue on the second roll})
\end{align*}
$$

**9.** Assume the additivity axiom $P(A \cup B) = P(A) + P(B)$ if $A$ and $B$ are mutually exclusive. Show by induction that for integers $n \ge 1$, 

$$
P(\cup_{i=1}^n A_i) ~ = ~ \sum_{i=1}^n P(A_i) ~~~ \text{if }  A_1, A_2, \ldots, A_n \text{ are mutually exclusive}
$$

**10.** The multiplication rules says $P(AB) = P(A)P(B \mid A)$. Show by induction that for integers $n \ge 1$,

$$
P(A_1A_2 \cdots A_n) ~ = ~ P(A_1)P(A_2 \mid A_1)P(A_3 \mid A_1A_2) \cdots P(A_n \mid A_1A_2 \cdots A_{n-1})
$$

**11.** Eight rooks are placed at positions sampled randomly without replacement on an $8\times8$ chessboard. Two rooks attack each other if they are in the same row or in the same column. What is the probability that none of them attacks any of the others?

**12.** The Statistics Department used to have a “birthday cake” tradition: once a month, there would be a cake to celebrate the birthdays of all department members whose birthdays were in that month. Suppose this tradition continues and suppose the department has $n$ members. Assume that each member’s birthday is equally likely to be one of the 12 months of the year, independently of all others.

Consider one calendar year (January through December), starting in January.

(a) What is the probability that no birthday cake will be needed after September?

(b) What is the probability that there will be birthday cake in September but not after that?

**13.** Down's Syndrome is a chromosomal disorder (a type of unusual genetic condition) that is associated with maternal age: older mothers are more likely to have babies with this syndrome than younger mothers are. The authors of an article on this syndrome in the US define "births to older mothers" as births in which the mother's age is at least 35 years, and "births to younger mothers" as births in which the mother is younger than 35. The authors make three statements about births in the population they studied.

- 1 in 700 babies is born with Down's Syndrome.
- Among births to **older** mothers, Down's Syndrome appears more 4 times more frequently than it does among births to younger mothers.
- Among births with Down's Syndrome, **younger** mothers appear 4 times more frequently than older mothers.

(a) Use the results of this chapter to explain why the last two statements don't contradict each other.

(b) If possible, find the proportion of births to older mothers in this population. If this is not possible, explain why not.

(c) If possible, find the proportion older mothers among births without Down's Syndrome.

**14.** I toss $n$ coins. You toss $n+1$ coins. What is the chance that you get more heads than I do?

[Hint: You don't need any "$n$ choose $k$"s for this. [Example 2.2.3](http://prob140.org/textbook/content/Chapter_02/02_Examples.html#example-3-second-random-digit-greater-than-the-first) has a helpful idea.]

