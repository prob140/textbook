## Outcome Space and Events ##

Any experiment involving randomness results in one of a number of possible outcomes. The outcome space is the collection of all such outcomes. 

Formally, an **outcome space** is just a set, usually denoted by $\Omega$. That's the upper case Greek letter Omega. 

We will assume for now that $\Omega$ is finite. In a sense this is not restrictive, as even the largest data sets are finite and the most powerful computers perform finitely many operations per task. However, we will soon see that allowing infinitely many possible outcomes not only results in a rich and elegant theory but also gives us deeper insights into problems involving finite outcome spaces. So the assumption that $\Omega$ is finite will be lifted in later chapters, once we have acquired some fluency with working in the finite case.

An **outcome** $\omega$ is an element of the outcome space $\Omega$. Though $\omega$ looks like the letter w, it's the lower case Greek omega and is usually more rounded in appearance than w.

An **event** is a subset of $\Omega$. The empty set $\phi$ and the entire space $\Omega$ are allowed as subsets. By convention, early letters of the alphabet like $A$ and $B$ are commonly used as notation for events. Also by convention, we will denote sets by enclosing their elements in braces $\{ \}$.

### Example: Permutations ###
Suppose you are shuffling three cards labeled $a$, $b$, and $c$. Then the space of all possible outcomes is

$$
\Omega ~=~ \{ abc, ~acb, ~bac, ~bca, ~cab, ~cba \}
$$

The event $\{abc, ~ acb \}$  can be described as "$a$ appears first". Such verbal descriptions of events are made formal by defining the events as subsets. This is the first step in developing a theory that is precise and consistent while also capable of being expressed in language that is natural for applications.

Event | Verbal Description                               | Subset      |
:----:|:-------------------------------------------------|:-------------
$A$   | $a$ appears first                                |$\{abc, acb\}$ 
$B$   | $b$ and $c$ are not next to each other           |$\{bac, cab\}$
$C$   | the letters are in alphabetical order            | $\{abc\}$     
$D$   | $a$ appears first, $b$ next, but $c$ isn't third | $\phi$        
$E$   | $c$ is either first, second, or third            | $\Omega$ 
$F$   | the letters form a word that means "taxi" | $\{ cab \}$

**A note about "types":** The outcome $\omega = cab$ is different from the event $F = \{ cab \}$. The outcome is an element of the outcome space, and the event is a subset of the outcome space. This subset happens to consist of just one outcome, but it's still a subset, not an element. You can think of this as analogous to different types in Python: `'cab'` is a string whereas `['cab']` is a list.

The table contains six events and you can come up with many more. For each one, see if you can give an interesting verbal description.

<span style="color: #114466">
    <b>Quick Check:</b> A natural outcome space for three tosses of a coin is $\Omega = \{HHH, HHT, HTH, HTT, THH, THT, THH, TTT\}$. 

**a)** What is the event that corresponds to the description "no two consecutive tosses land the same way"?

**b)** Give a verbal description of the event $\{HTT, THT, TTH, TTT\}$.

<details>
    <summary>Answer </summary>
    (a) $\{HTH, THT\}~~$ (b) One way to describe it is "at most one head"
</details> 
</span>

When you shuffle cards for a game, the goal is to make the order of the cards "random". Preferably, you'd like any permutation to be just as likely as any other. So let's start working with equally likely outcomes.

