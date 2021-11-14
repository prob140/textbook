#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **Standard deck of cards:** From now on we will assume the following unless otherwise specified.
# 
# - Cards being dealt from a deck means that the cards are drawn at random without replacement.
# - A *hand* of cards is a subset dealt from the deck. The order in which the cards appear in the hand doesn't matter.
# - A standard deck consists of 52 cards.
#     - There are 13 cards in each of 4 *suits*: clubs, spades, hearts, and diamonds. Clubs and spades are black. Hearts and diamonds are red.
#     - Each suit has 13 different *ranks*: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.
#     
# **Important:** 
# - If you are trying to find the distribution of a random variable, **start with its possible values**, not the probabilities.
# - Distributions can be described in a table, or by a formula, or in any other way that provides all the necessary information.

# **1.** Cards are dealt from a standard deck until the first heart appears. Let $D$ be the number of cards dealt. Find the following probabilities.
# 
# (a) $P(D = 5)$
# 
# (b) $P(D \le 5)$
# 
# (c) $P(D = 3 \mid D \le 5)$

# **2.** The distribution table for a random variable $X$ is given below.
# 
# |$x$ |$-2$|$-1$|$0$|$1$|$2$|
# |---:|:---:|:---:|:---:|:---:|:---:|
# |$P(X=x)$|$0.1$|$0.2$|$0.4$|$0.2$|$0.1$|
# 
# (a) Fill in the blank with $=$ or $\stackrel{d}{=}$, picking the stronger one if both are applicable, and leaving it blank if neither is applicable. Explain your choice.
# 
# $X ~~ \underline{~~~~~~~~~~~~~~} ~~ -X$
# 
# (b) Draw a distribution table for $\vert X \vert$.
# 
# (d) Draw a distribution table for $\min(X, 1)$.

# **3.** Suppose you roll a die until the first time you see a face that has appeared before. Let $X$ be the number of rolls required. 
# 
# **a)** What are the possible values of $X$?
# 
# **b)** Find the distribution of $X$.
# 
# **c)** Find $P(X \ge 4)$ using only multiplication, not addition. [Think about how the rolls have to come out for the event to occur.]

# **4.** Cards are dealt from a standard deck. Let X be the number of cards dealt till the first time any suit appears more than once. For example, if the sequence of suits is clubs, diamonds, hearts, diamonds then $X=4$. Find the distribution of $X$.

# **5.** Let $X_1, X_2$ be the results of two draws made at random with replacement from the 10 digits $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$. Define the following random variables.
# 
# - $S = X_1 + X_2$
# - $M = \max(X_1, X_2)$
# - $N = \min(X_1, X_2)$
# 
# (a) For each of the following pairs, fill in the blank with $=$ or $\stackrel{d}{=}$, picking the stronger one if both are applicable, and leaving it blank if neither is applicable. Explain your choice.
# 
# (i) $X_1 ~~ \underline{~~~~~~~~~~~~~~} ~~ X_2$
# 
# (ii) $S ~~ \underline{~~~~~~~~~~~~~~} ~~ M+N$
# 
# (b) Find $P(N > 3)$.
# 
# (c) Find $P(S \le 16)$.

# **6.** A population of 50 voters contains 30 from Party A and 20 from the rival Party B. Suppose you take a simple random sample of 10 voters. That's a sample drawn at random without replacement from the population, making all possible samples of size 10 equally likely.
# 
# (a) How many possible samples are there?
# 
# (b) Pick one of the options (i) and (ii) and explain your choice.
# 
# The number of samples that contain 6 Party A voters is
# 
# $~~~~~$ (i) $\binom{30}{6}$ $~~~~~~~~~~$ (ii) $\binom{30}{6}\binom{20}{4}$
# 
# (c) Let $N_A$ be the number of Party A voters in the sample. Find the distribution of $N_A$.

# **7.** A deck of five cards contains two aces and three queens. The five cards are shuffled and dealt one by one. This exercise is about the number of cards dealt till the aces appear. For example, if the order of the cards dealt was QAQQA, then the number of cards dealt until the first ace is $2$, and until the second ace is $5$.
# 
# (a) Draw a table that displays the distribution of the number of cards dealt until the first ace.
# 
# (b) Draw a table that displays the distribution of the number of cards dealt until the second ace.
# 
# (c) Explain why the probabilities in the second table are just those in the first in a different order. [Hint: think about dealing off the bottom of the deck!]

# In[ ]:




