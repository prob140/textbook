---
interact_link: notebooks/Chapter_03/01_Functions_on_an_Outcome_Space.ipynb
title: '3.1 Functions on an Outcome Space'
permalink: 'chapters/Chapter_03/01_Functions_on_an_Outcome_Space'
previouschapter:
  url: chapters/Chapter_03/00_Random_Variables
  title: 'Chapter 3: Random Variables'
nextchapter:
  url: chapters/Chapter_03/02_Distributions
  title: '3.2 Distributions'
redirect_from:
  - 'chapters/chapter-03/01-functions-on-an-outcome-space'
---

## Functions on an Outcome Space

Random sampling can be thought of as repeated random trials, and therefore many outcome spaces consist of sequences. An outcome space representing two tosses of a coin is

$$ 
\Omega = \{ \text{HH, HT, TH, TT} \}
$$

If you were tossing 10 times, the outcome space would consist of the $2^{10}$ sequences of 10 elements where each element is H or T. The outcomes are a pain to list by hand, but computers are good at saving us that kind of pain.

### Product Spaces
The *product* of two sets $A$ and $B$ is the set of all pairs $(a, b)$ where $a \in A$ and $b \in B$. This concept is exactly what we need to describe spaces representing multiple trials.

For example, the space representing the outcome of one toss of a coin is $ \Omega_1 = \{ \text{H, T}\}$. The *product* of $\Omega_1$ with itself is the set of pairs (H, H), (H, T), (T, H) and (T, T), which you will recognize as the outcomes of two tosses of a coin. The product of this new space and $\Omega_1$ is the space representing three tosses. And so on.

The Python module `itertools` contains a function `product` that constructs product spaces. Let's import it.



{:.input_area}
```python
from itertools import product
```


To see how `product` works, we will start with the outcomes of one toss of a coin. We are creating an array using `make_array` but you could use any other way of creating an array or list.



{:.input_area}
```python
one_toss = make_array('H', 'T')
```


To use `product`, we have to specify the base space and the number of repetitions, and then covert the result to a list.



{:.input_area}
```python
two_tosses = list(product(one_toss, repeat=2))
two_tosses
```





{:.output_data_text}
```
[('H', 'H'), ('H', 'T'), ('T', 'H'), ('T', 'T')]
```



For three tosses, just change the number of repetitions:



{:.input_area}
```python
three_tosses = list(product(one_toss, repeat=3))
three_tosses
```





{:.output_data_text}
```
[('H', 'H', 'H'),
 ('H', 'H', 'T'),
 ('H', 'T', 'H'),
 ('H', 'T', 'T'),
 ('T', 'H', 'H'),
 ('T', 'H', 'T'),
 ('T', 'T', 'H'),
 ('T', 'T', 'T')]
```



A *probability space* is an outcome space accompanied by the probabilities of all the outcomes. If you assume all eight outcomes of three tosses are equally likely, the probabilities are all 1/8:



{:.input_area}
```python
three_toss_probs = (1/8)*np.ones(8)
```


The corresponding probability space:



{:.input_area}
```python
three_toss_space = Table().with_columns(
    'omega', three_tosses,
    'P(omega)', three_toss_probs
)
three_toss_space
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>omega</th> <th>P(omega)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>['H' 'H' 'H']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['H' 'H' 'T']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['H' 'T' 'H']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['H' 'T' 'T']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['T' 'H' 'H']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['T' 'H' 'T']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['T' 'T' 'H']</td> <td>0.125   </td>
        </tr>
        <tr>
            <td>['T' 'T' 'T']</td> <td>0.125   </td>
        </tr>
    </tbody>
</table>
</div>



Product spaces get large very quickly. If you roll a die 5 times, there are almost 8,000 possible outcomes:



{:.input_area}
```python
6**5
```





{:.output_data_text}
```
7776
```



But we have `product` so we can still list them all! Here is a probability space representing 5 rolls of a die.



{:.input_area}
```python
die = np.arange(1, 7, 1)

five_rolls = list(product(die, repeat=5))  # All possible results of 5 rolls

five_roll_probs = (1/6**5)**np.ones(6**5)  # Each result has chance 1/6**5

five_roll_space = Table().with_columns(
   'omega', five_rolls,
    'P(omega)', five_roll_probs
)

five_roll_space
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>omega</th> <th>P(omega)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[1 1 1 1 1]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 2]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 3]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 4]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 5]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 6]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 1]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 2]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 3]</td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 4]</td> <td>0.000128601</td>
        </tr>
    </tbody>
</table>
<p>... (7766 rows omitted)</p>
</div>



### A Function on the Outcome Space
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



{:.input_area}
```python
five_rolls_sum = Table().with_columns(
    'omega', five_rolls,
    'S(omega)', five_roll_space.apply(sum, 'omega'),
    'P(omega)', five_roll_probs
)
five_rolls_sum
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>omega</th> <th>S(omega)</th> <th>P(omega)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[1 1 1 1 1]</td> <td>5       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 2]</td> <td>6       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 3]</td> <td>7       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 4]</td> <td>8       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 5]</td> <td>9       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 1 6]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 1]</td> <td>6       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 2]</td> <td>7       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 3]</td> <td>8       </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 4]</td> <td>9       </td> <td>0.000128601</td>
        </tr>
    </tbody>
</table>
<p>... (7766 rows omitted)</p>
</div>



We now have every possible outcome of five rolls of a die, along with its total number of spots. You can see that the first row of the table shows the smallest possible number of spots, corresponding to all the rolls showing 1 spot. The 7776th row shows the largest:



{:.input_area}
```python
five_rolls_sum.take(7775)
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>omega</th> <th>S(omega)</th> <th>P(omega)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[6 6 6 6 6]</td> <td>30      </td> <td>0.000128601</td>
        </tr>
    </tbody>
</table>
</div>



All the other values of $S$ are between these two extremes. 

#### Functions of Random Variables
A random variable is a numerical function on $\Omega$. Therefore by composition, a numerical function of a random variable is also a random variable. 

For example, $S^2$ is a random variable, calculated as follows:

$$
S^2(\omega) = \big{(} S(\omega)\big{)}^2
$$

Thus for example $S^2(\text{[6 6 6 6 6]}) = 30^2 = 900$.

### Events Determined by $S$
From the table `five_rolls_sum` it is hard to tell how many rows show a sum of 6, or 10, or any other value. To better understand the properties of $S$, we have to organize the information in `five_rolls_sum`.

For any subset $A$ of the range of $S$, define the event $\{S \in A\}$ as

$$
\{S \in A \} = \{\omega: S(\omega) \in A \}
$$

That is, $\{ S \in A\}$ is the collection of all $\omega$ for which $S(\omega)$ is in $A$. In terms of the table, the set consists of the values of $\omega$ in all the rows in which the sum is in $A$.

Try out the definition in a special case. Take $A = \{5, 30\}$. Then $\{S \in A\}$ if and only if either all the rolls show 1 spot or all the rolls show 6 spots. So 
$$
\{S \in A\} = \{\text{[1 1 1 1 1], [6 6 6 6 6]}\}
$$

It is natural to ask about the chance the sum is a particular value, say 10. That's not easy to read off the table, but we can access the corresponding rows:



{:.input_area}
```python
five_rolls_sum.where('S(omega)', are.equal_to(10))
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>omega</th> <th>S(omega)</th> <th>P(omega)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[1 1 1 1 6]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 2 5]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 3 4]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 4 3]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 5 2]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 1 6 1]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 2 1 5]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 2 2 4]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 2 3 3]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>[1 1 2 4 2]</td> <td>10      </td> <td>0.000128601</td>
        </tr>
    </tbody>
</table>
<p>... (116 rows omitted)</p>
</div>



There are 126 values of $\omega$ for which $S(\omega) = 10$. Since all the $\omega$ are equally likely, the chance that $S$ has the value 10 is 126/7776. 

We will usually be informal with notation and write $\{ S = 10 \}$ instead of $\{ S \in \{10\} \}$:
$$
P(S = 10) = \frac{126}{7776} = 1.62\%
$$
