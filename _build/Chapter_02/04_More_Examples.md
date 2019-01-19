---
redirect_from:
  - "/chapter-02/04-more-examples"
interact_link: notebooks/Chapter_02/04_More_Examples.ipynb
title: 'More Examples'
prev_page:
  url: /Chapter_02/03_Multiplication
  title: 'Multiplication'
next_page:
  url: /Chapter_02/05_Updating_Probabilities
  title: 'Updating Probabilities'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## More Examples

Just a plus rule and a times rule – that's all it takes to get going. Here are some examples of standard problem solving techniques.

### Example 1: A Fundamental Method – Start by Partitioning
A box contains 6 dark chocolates and 4 milk chocolates. I pick two at random without replacement.

**Question.** What is the chance that I get one of each kind?

**Answer.** You will have noticed that the problem doesn't specify whether the dark has to come first, or the milk. Either could happen. So list the distinct ways the event can happen, that is, partition the event:
- first dark then milk: chance $(6/10)\cdot(4/9)$ by the multiplication rule
- first milk then dark: chance $(4/10)\cdot(6/9)$

(Aha! The two terms are equal! Get ready for many more such symmetries in sampling without replacement.)

Now add the chances of the two bits. The answer is $2\cdot(6/10)\cdot(4/9)$.

This method should become as natural as breathing. You should also redo the problem under the unnatural assumption that the chocolates are drawn with replacement, to see what changes and what stays the same.

### Example 2: Polya's Urn Scheme
A box contains $b$ black balls and $w$ white balls. A ball is drawn at random, and then replaced in the urn along with $d$ more balls of its color. Then a ball is drawn at random from the urn.

**Question 1.** What is the chance that the first ball drawn is black?

**Answer 1.** Not much effort required.

$$
P(\text{first ball black}) = \frac{b}{b+w}
$$

**Question 2.** What is the chance that the second ball drawn is black?

**Answer 2.** Your mind goes naturally to what the first ball was, so partition according to the color of that one, and add. The fundamental method strikes again.

$$
\begin{align*}
P(\text{second ball black}) &= P(WB) + P(BB) \\ \\
&= \frac{w}{b+w} \cdot \frac{b}{b+w+d} ~+~ \frac{b}{b+w} \cdot \frac{b+d}{b+w+d} \\ \\
&= \frac{wb + b^2 + bd}{(b+w)(b+w+d)} \\ \\
&= \frac{b(b+w+d)}{(b+w)(b+w+d)} \\ \\
&= \frac{b}{b+w}
\end{align*}
$$

That's the same as the chance that the first ball is black, no matter what $d$ is. This scheme is interesting!

**Question 3.** What is the chance that the second ball drawn is black, given that the first one drawn was black?

**Answer 3.** We already used this in the calculation above. Conditional probabilities "going forwards in time" can often just be read off the information in the question, as in this case:

$$
P(\text{second ball black} \mid \text{first ball black}) =
\frac{b+d}{b+w+d}
$$

**Question 4.** What is the chance that the first ball drawn is black, given that the second one drawn was black?

**Answer 4.** This kind of "going back in time" conditional probability isn't easy to just read off. **This is where the division rule comes in.**

$$
\begin{align*}
P(\text{first ball black} \mid \text{second ball black}) &=
\frac{P(BB)}{P(\text{second ball black})} \\ \\
&= \frac{\frac{b}{b+w} \cdot \frac{b+d}{b+w+d}}{\frac{b}{b+w}} \\ \\
&= \frac{b+d}{b+w+d}
\end{align*}
$$

This one does depend on $d$, but it's the same as Answer 3. Forwards and backwards don't seem to make a difference. 

Now you begin to see why this scheme carries the name of its renowned originator [George Polya](https://en.wikipedia.org/wiki/George_Pólya) (1887-1985). You can keep repeating the scheme – replace the drawn ball with another $d$ balls of its color, and draw again – to get a *process* with beautiful and useful properties for updating opinions as data comes in. We'll see that later in the course.
