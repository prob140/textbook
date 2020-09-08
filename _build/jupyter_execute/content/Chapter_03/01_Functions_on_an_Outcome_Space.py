# HIDDEN
import warnings
warnings.filterwarnings("ignore")

from datascience import *
from prob140 import *
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np

## Functions on an Outcome Space ##

Random sampling can be thought of as repeated random trials, and therefore many outcome spaces consist of sequences. An outcome space representing two tosses of a coin is

$$ 
\Omega = \{ HH, HT, TH, TT \}
$$

If you were tossing 10 times, the outcome space would consist of the $2^{10}$ sequences of 10 elements where each element is H or T. The outcomes are a pain to list by hand, but computers are good at saving us that kind of pain.

### Product Spaces ###
The *product* of two sets $A$ and $B$ is the set of all pairs $(a, b)$ where $a \in A$ and $b \in B$. This concept is exactly what we need to describe spaces representing multiple trials.

For example, the space representing the outcome of one toss of a coin is $ \Omega_1 = \{ H, T \}$. The *product* of $\Omega_1$ with itself is the set of pairs $(H, H)$, $(H, T)$, $(T, H)$, and $(T, T)$, which you will recognize as the outcomes of two tosses of a coin. The product of this new space and $\Omega_1$ is the space representing three tosses. And so on.

The Python module `itertools` contains a function `product` that constructs product spaces. Let's import it.

from itertools import product

To see how `product` works, we will start with the outcomes of one toss of a coin. We are creating an array using `make_array` but you could use any other way of creating an array or list.

one_toss = make_array('H', 'T')

To use `product`, we have to specify the base space and the number of repetitions, and then covert the result to a list.

two_tosses = list(product(one_toss, repeat=2))
two_tosses

For three tosses, just change the number of repetitions:

three_tosses = list(product(one_toss, repeat=3))
three_tosses

### Probability Space ###
A *probability space* is an outcome space accompanied by the probabilities of all the outcomes. If you assume all eight outcomes of three tosses are equally likely, the probabilities are all 1/8:

three_toss_probs = (1/8)*np.ones(8)

The corresponding probability space:

three_toss_space = Table().with_columns(
    'omega', three_tosses,
    'P(omega)', three_toss_probs
)
three_toss_space

Product spaces get large very quickly. If you roll a die 5 times, there are almost 8,000 possible outcomes:

6**5

But we have `product` so we can still list them all! Here is a probability space representing 5 rolls of a die.

die = np.arange(1, 7, 1)

five_rolls = list(product(die, repeat=5))  # All possible results of 5 rolls

five_rolls_probs = (1/6**5)**np.ones(6**5)  # Each result has chance 1/6**5

five_rolls_space = Table().with_columns(
   'omega', five_rolls,
    'P(omega)', five_rolls_probs
)

five_rolls_space

# VIDEO: Random Variable
from IPython.display import YouTubeVideo

YouTubeVideo("h8k0M1ubIxk")

### A Function on the Outcome Space ###
Suppose you roll a die five times and add up the number of spots you see. If that seems artificial, be patient for a moment and you'll soon see why it's interesting. 

The sum of the rolls is a numerical function on the outcome space $\Omega$ of five rolls. The sum is thus a *random variable*. Let's call it $S$. Then, formally,

$$
S: \Omega \rightarrow \{ 5, 6, \ldots, 30 \}
$$

The range of $S$ is the integers 5 through 30, because each die shows at least one spot and at most six spots. We can also use the equivalent notation

$$
\Omega \stackrel{S}{\rightarrow} \{ 5, 6, \ldots, 30 \}
$$

From a computational perspective, the elements of $\Omega$ are in the column `omega` of `five_roll_space`. Let's apply this function and create a larger table.

five_rolls_sum = five_rolls_space.with_columns(
    'S(omega)', five_rolls_space.apply(sum, 'omega')
).move_to_end('P(omega)')

five_rolls_sum

We now have every possible outcome of five rolls of a die, along with its total number of spots. You can see that the first row of the table shows the smallest possible number of spots, corresponding to all the rolls showing 1 spot. The 7776th row shows the largest:

five_rolls_sum.take(7775)

All the other values of $S$ are between these two extremes. 

```{admonition} Quick Check
A standard probability space for three tosses of a coin consists of the outcome space $\Omega = \{ HHH, HHT, HTH, THH, HTT, THT, TTH, TTT \}$ with equally likely outcomes. For each of the following descriptions, say whether or not it results in a random variable defined on $\Omega$.

(i) Count $1$ if the outcome in $HHH$, $0$ otherwise

(ii) Note the index of the final toss on which $H$ appears
```

```{admonition} Answer
:class: dropdown
(i) Yes.

(ii) No. The description gets stuck at the outcome $TTT$. It doesn't say what to do in this case. Even if you decide to use $\infty$ for this outcome, you don't get a random variable because $\infty$ isn't a real number.
```

#### Functions of Random Variables ####
A random variable is a numerical function on $\Omega$. Therefore by composition, a numerical function of a random variable is also a random variable. 

For example, $S^2$ is a random variable, calculated as follows:

$$
S^2(\omega) = \big{(} S(\omega)\big{)}^2
$$

Thus for example $S^2(\text{[6 6 6 6 6]}) = 30^2 = 900$.

```{admonition} Quick Check
Let $X$ and $Y$ be random variables defined on the same probability space.

(a) Is $\max(X, Y)$ a random variable?

(b) Let $Z = 1$ if $X=Y$ and $Z=0$ otherwise. Is $Z$ a random variable?
```

```{admonition} Answer
:class: dropdown
(a) Yes (b) Yes

```

# VIDEO: Events Determined by S
from IPython.display import YouTubeVideo

YouTubeVideo("OJZDPWSKIbw")

### Events Determined by $S$ ###
From the table `five_rolls_sum` it is hard to tell how many rows show a sum of 6, or 10, or any other value. To better understand the properties of $S$, we have to organize the information in `five_rolls_sum`.

For any subset $A$ of the range of $S$, define the event $\{S \in A\}$ as

$$
\{S \in A \} = \{\omega: S(\omega) \in A \}
$$

That is, $\{ S \in A\}$ is the collection of all $\omega$ for which $S(\omega)$ is in $A$. In terms of the table, the set consists of the values of $\omega$ in all the rows in which the sum is in $A$.

Events of the form $\{ S \in A\}$ are said to be *determined by $S$*. If we know the value of $S$, then we know whether or not that value is in $A$. So we can determine whether or not the event $\{ S \in A\}$ has occurred.

Let's try out the definition in a special case. Take $A = \{5, 30\}$. Then $\{S \in A\}$ if and only if either all the rolls show 1 spot or all the rolls show 6 spots. So 

$$
\{S \in A\} = \{\text{[1 1 1 1 1], [6 6 6 6 6]}\}
$$

It is natural to ask about the chance the sum is a particular value, say 10. That's not easy to read off the table, but we can access the corresponding rows:

five_rolls_sum.where('S(omega)', are.equal_to(10))

There are 126 values of $\omega$ for which $S(\omega) = 10$. Since all the $\omega$ are equally likely, the chance that $S$ has the value 10 is 126/7776. 

We will usually be informal with notation and write $\{ S = 10 \}$ instead of $\{ S \in \{10\} \}$:

$$
P(S = 10) = \frac{126}{7776} = 1.62\%
$$

```{admonition} Quick Check
Consider a probability space representing two rolls of a die. That is the space consists of the 36 equally likely pairs $(i,j)$ where $1 \le i, j \le 6$. Let $X_1$ be the result of the first roll and $X_2$ the result of the second, and let $D = X_1 - X_2$. Here are two events determined by $D$. Write them as subsets of the outcome space and find their probabilities.

(a) $D = 0$

(b) $D > 3$
```

```{admonition} Answer
:class: dropdown
(a) $\{ (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) \}$, probability $6/36$

(b) $\{ (5,1), (6,1), (6,2) \}$, probability $3/36$
```


