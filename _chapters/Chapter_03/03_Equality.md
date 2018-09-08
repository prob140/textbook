---
interact_link: notebooks/Chapter_03/03_Equality.ipynb
title: '3.3 Equality'
permalink: 'chapters/Chapter_03/03_Equality'
previouschapter:
  url: chapters/Chapter_03/02_Distributions
  title: '3.2 Distributions'
nextchapter:
  url: chapters/Chapter_04/00_Relations_Between_Variables
  title: 'Chapter 4: Relations Between Variables'
redirect_from:
  - 'chapters/chapter-03/03-equality'
---

## Equality

We know what it means for two numbers to be equal. Equality of random variables, however, can be of more than one kind.

### Equal
Two random variables $X$ and $Y$ defined on the same outcome space are *equal* if their values are the same for every outcome in the space. The notation is $X = Y$ and it means that

$$
X(\omega) = Y(\omega) \text{ for all } \omega \in \Omega
$$
Informally, this says that no matter what the outcome, if $X$ is 10 then $Y$ must be 10 too; if $X$ is 11, $Y$ must be 11, and so on.

An example will make this clear. Let $N_H$ be the number of heads in three tosses of a coin, and let $N_T$ be the number of tails in the same three tosses. Then the two random variables $N_H$ and $3 - N_T$ are equal. For every possible outcome of the three tosses, the value of $N_H$ is equal to the value of $3 - N_T$.

We write this simply as $N_H = 3 - N_T$.

### Equal in Distribution
$N_H$ and $N_T$, as defined above, are not equal. For example,

$$
N_H(\text{TTT}) = 0 ~~~ \text{but} ~~~ N_T(\text{TTT}) = 3
$$ 

However, there is a sense in which the number of heads "behaves in the same way" as the number of tails. The two random variables have the same probability distribution.

The outcome space is `three_tosses`:



{:.input_area}
```python
coin = make_array('H', 'T')
three_tosses = list(product(coin, repeat=3))
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



There are only eight outcomes, so it is easy to inspect the table and write the distributions of $N_H$ and $N_T$. Both take the values 0, 1, 2, and 3, with probabilities 1/8, 3/8, 3/8, and 1/8 respectively. This distribution is shown in the table below.



{:.input_area}
```python
dist = Table().values(np.arange(4)).probability(make_array(1, 3, 3, 1)/8)
dist
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Probability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0    </td> <td>0.125      </td>
        </tr>
        <tr>
            <td>1    </td> <td>0.375      </td>
        </tr>
        <tr>
            <td>2    </td> <td>0.375      </td>
        </tr>
        <tr>
            <td>3    </td> <td>0.125      </td>
        </tr>
    </tbody>
</table>
</div>



We say that $N_H$ and $N_T$ are *equal in distribution*. 

In general, two random variables $X$ and $Y$ are equal in distribution if they have the same probability distribution. This is denoted

$$
X \stackrel{d}{=} Y
$$

### Relation between the Equalities
Equality is stronger than equality in distribution. If two random variables are the same, outcome by outcome, then they must have the same distribution because they are the same function on the outcome space. 

That is, for any two random variables $X$ and $Y$,

$$
X = Y \implies X \stackrel{d}{=} Y
$$

But as the example of heads and tails in three tosses shows, the converse need not be true.

### Example: Two Cards Dealt from a Small Deck
A deck contains 10 cards, labeled 1, 2, 2, 3, 3, 3, 4, 4, 4, 4. Two cards are dealt at random without replacement. Let $X_1$ be the label on the first card and $X_2$ be the label on the second card.

**Question 1.** Are $X_1$ and $X_2$ equal?

**Answer 1.** No, because the outcome could be 31 in which case $X_1 = 3$ and $X_2 = 1$.

**Question 2.** Are $X_1$ and $X_2$ equal in distribution?

**Answer 2.** Let's find the two distributions and compare. Clearly the possible values are 1, 2, 3, and 4 in each case. The distribution of $X_1$ is easy: 

$$
P(X_1 = i ) = \frac{i}{10} , ~~ i = 1, 2, 3, 4
$$

When a distribution is defined by a formula like this, you can define a function that does what the formula says:



{:.input_area}
```python
def prob1(i):
    return i/10
```


Then you can create a probability distribution object using `value` as before but now with `probability_function` that takes the name of the function as its argument:



{:.input_area}
```python
possible_i = np.arange(1, 5, 1)
dist_X1 = Table().values(possible_i).probability_function(prob1)
dist_X1
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Probability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1    </td> <td>0.1        </td>
        </tr>
        <tr>
            <td>2    </td> <td>0.2        </td>
        </tr>
        <tr>
            <td>3    </td> <td>0.3        </td>
        </tr>
        <tr>
            <td>4    </td> <td>0.4        </td>
        </tr>
    </tbody>
</table>
</div>



Convince yourself that the function `prob2` below returns $P(X_2 = i)$ for each $i$. The event has been partitioned according to the value of $X_1$.



{:.input_area}
```python
def prob2(i):
    if i == 1:
        return (9/10)*(1/9)
    else:
        return (i/10)*((i-1)/9) + ((10-i)/10)*(i/9)
```




{:.input_area}
```python
dist_X2 = Table().values(possible_i).probability_function(prob2)
dist_X2
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Probability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1    </td> <td>0.1        </td>
        </tr>
        <tr>
            <td>2    </td> <td>0.2        </td>
        </tr>
        <tr>
            <td>3    </td> <td>0.3        </td>
        </tr>
        <tr>
            <td>4    </td> <td>0.4        </td>
        </tr>
    </tbody>
</table>
</div>



The two distributions are the same! Here is yet another example of symmetry in sampling without replacement. The conclusion is

$$
X_1 \stackrel{d}{=} X_2
$$
