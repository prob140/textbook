---
interact_link: notebooks/Chapter_04/05_Dependence_and_Independence.ipynb
title: '4.5 Dependence and Independence'
permalink: 'chapters/chapter-04/05-dependence-and-independence'
previouschapter:
  url: chapters/chapter-04/04-updating-distributions
  title: '4.4 Updating Distributions'
nextchapter:
  url: chapters/chapter-05/00-collections-of-events
  title: 'Chapter 5: Collections of Events'
---

## Dependence and Independence

Conditional distributions help us formalize our intuitive ideas about whether two random variables are independent of each other. Let $X$ and $Y$ be two random variables, and suppose we are given the value of $X$. Does that change our opinion about $Y$? If the answer is yes, then we will say that $X$ and $Y$ are dependent. If the answer is no, no matter what the given value of $X$ is, then we will say that $X$ and $Y$ are independent.

Let's start with some examples and then move to precise definitions and results.

### Dependence
Here is the joint distribution of two random variables $X$ and $Y$. From this, what can we say about whether $X$ and $Y$ are dependent or independent?


{:.input_area}
```python
dist1
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X=0</th>
      <th>X=1</th>
      <th>X=2</th>
      <th>X=3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=3</th>
      <td>0.037037</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.166667</td>
      <td>0.055556</td>
      <td>0.000000</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.250000</td>
      <td>0.166667</td>
      <td>0.027778</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.125000</td>
      <td>0.125000</td>
      <td>0.041667</td>
      <td>0.00463</td>
    </tr>
  </tbody>
</table>
</div>
</div>



You can see at once that if $X = 3$ then $Y$ can only be 0, whereas if $X = 2$ then $Y$ can be either 1 or 2. Knowing the value of $X$ changes the distribution of $Y$. That's dependence. 

Here is an example in which you can't quickly determine dependence or independence by just looking at the possible values.


{:.input_area}
```python
dist2
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X=3</th>
      <th>X=4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=7</th>
      <td>0.3</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>Y=6</th>
      <td>0.2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>Y=5</th>
      <td>0.1</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>
</div>
</div>



But you can tell by looking at the conditional distributions of $Y$ given $X$. They are different.


{:.input_area}
```python
dist2.conditional_dist('Y', 'X')
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dist. of Y | X=3</th>
      <th>Dist. of Y | X=4</th>
      <th>Marginal of Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=7</th>
      <td>0.500000</td>
      <td>0.25</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>Y=6</th>
      <td>0.333333</td>
      <td>0.50</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>Y=5</th>
      <td>0.166667</td>
      <td>0.25</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>Sum</th>
      <td>1.000000</td>
      <td>1.00</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>



It follows (and you should try to prove this), that at least some of the conditional distributions of $X$ given the different values of $Y$ will also be different from each other and from the marginal of $X$.

Notice that not all the conditional distributions are different. The conditional distribution of $X$ given $Y=5$ is the same as the conditional distribution of $X$ given $Y=6$. But given $Y=7$, the conditional distribution changes. $X$ and $Y$ are dependent.


{:.input_area}
```python
dist2.conditional_dist('X', 'Y')
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X=3</th>
      <th>X=4</th>
      <th>Sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dist. of X | Y=7</th>
      <td>0.75</td>
      <td>0.25</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of X | Y=6</th>
      <td>0.50</td>
      <td>0.50</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of X | Y=5</th>
      <td>0.50</td>
      <td>0.50</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Marginal of X</th>
      <td>0.60</td>
      <td>0.40</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Independence

Here is a joint distribution table in which you can't immediately tell whether there is dependence. 


{:.input_area}
```python
dist3
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X=0</th>
      <th>X=1</th>
      <th>X=2</th>
      <th>X=3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=4</th>
      <td>0.000096</td>
      <td>0.000289</td>
      <td>0.000289</td>
      <td>0.000096</td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.001929</td>
      <td>0.005787</td>
      <td>0.005787</td>
      <td>0.001929</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.014468</td>
      <td>0.043403</td>
      <td>0.043403</td>
      <td>0.014468</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.048225</td>
      <td>0.144676</td>
      <td>0.144676</td>
      <td>0.048225</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.060282</td>
      <td>0.180845</td>
      <td>0.180845</td>
      <td>0.060282</td>
    </tr>
  </tbody>
</table>
</div>
</div>



But look what happens when you condition $X$ on $Y$.


{:.input_area}
```python
dist3.conditional_dist('X', 'Y')
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X=0</th>
      <th>X=1</th>
      <th>X=2</th>
      <th>X=3</th>
      <th>Sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dist. of X | Y=4</th>
      <td>0.125</td>
      <td>0.375</td>
      <td>0.375</td>
      <td>0.125</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of X | Y=3</th>
      <td>0.125</td>
      <td>0.375</td>
      <td>0.375</td>
      <td>0.125</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of X | Y=2</th>
      <td>0.125</td>
      <td>0.375</td>
      <td>0.375</td>
      <td>0.125</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of X | Y=1</th>
      <td>0.125</td>
      <td>0.375</td>
      <td>0.375</td>
      <td>0.125</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of X | Y=0</th>
      <td>0.125</td>
      <td>0.375</td>
      <td>0.375</td>
      <td>0.125</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Marginal of X</th>
      <td>0.125</td>
      <td>0.375</td>
      <td>0.375</td>
      <td>0.125</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>



All the rows are the same. That is, all the conditional distributions of $X$ given different values of $Y$ are the same, and hence are the same as the marginal of $X$ too. 

Given the value of $Y$, the probabilities for $X$ don't change at all. That's independence.

You could have drawn the same conclusion by conditioning $Y$ on $X$:


{:.input_area}
```python
dist3.conditional_dist('Y', 'X')
```




<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dist. of Y | X=0</th>
      <th>Dist. of Y | X=1</th>
      <th>Dist. of Y | X=2</th>
      <th>Dist. of Y | X=3</th>
      <th>Marginal of Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=4</th>
      <td>0.000772</td>
      <td>0.000772</td>
      <td>0.000772</td>
      <td>0.000772</td>
      <td>0.000772</td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.015432</td>
      <td>0.015432</td>
      <td>0.015432</td>
      <td>0.015432</td>
      <td>0.015432</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.115741</td>
      <td>0.115741</td>
      <td>0.115741</td>
      <td>0.115741</td>
      <td>0.115741</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.385802</td>
      <td>0.385802</td>
      <td>0.385802</td>
      <td>0.385802</td>
      <td>0.385802</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.482253</td>
      <td>0.482253</td>
      <td>0.482253</td>
      <td>0.482253</td>
      <td>0.482253</td>
    </tr>
    <tr>
      <th>Sum</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



### Independence of Two Events
The concept of independence seems intuitive, but it is possible to run into a lot of trouble by not being careful about its definition. So let's define it formally.

There are two equivalent definitions of the independence of two events. The first encapsulates the main idea of independence, and the second is useful for calculation.

Two events $A$ and $B$ are *independent* if $P(B \mid A) = P(B)$. Equivalently, $A$ and $B$ are independent if $P(AB) = P(A)P(B)$.

### Independence of Two Random Variables
What we have observed in the examples of this section can be turned into a formal definition of independence.

Two random variables $X$ and $Y$ are *independent* if for every value $x$ of $X$ and $y$ of $Y$,
$$
P(Y = y \mid X = x) = P(Y = y)
$$
That is, no matter what the given $x$ is, the conditional distribution of $Y$ is the same as if we didn't know that $X=x$.

An equivalent definition in terms of the independence of events is that for any values of $x$ and $y$, the events $\{ X=x\}$ and $\{Y=y\}$ are independent. 

That is, $X$ and $Y$ are independent if for any values $x$ of $X$ and $y$ of $Y$, 

$$
P(X = x, Y = y) ~ = ~ P(X=x)P(Y=y) 
$$

Independence simplifies the conditional probabilities in the multiplication rule.

It is a fact that if $X$ and $Y$ are independent random variables, then any event determined by $X$ is independent of any event determined by $Y$. For example, if $X$ and $Y$ are independent and $x$ is a number, then $\{X=x\}$ is independent of $\{Y>x\}$. Also, any function of $X$ is independent of any function of $Y$.

You can prove these facts by partitioning and then using the definition of independence. The proofs are routine but somewhat labor intensive. You are welcome to just accept the facts if you don't want to prove them.

### Mutual Independence
Events $A_1, A_2, \ldots A_n$ are *mutually independent* (or *independent* for short) if given that any subset of the events has occurred, the conditional chances of all other subsets remain unchanged.

That's quite a mouthful. In practical terms it means that it doesn't matter which of the events you know have happened; chances involving the remaining events are unchanged.

In terms of random variables, $X_1, X_2, \ldots , X_n$ are independent if given the values of any subset, chances of events determined by the remaining variables are unchanged.

In practice, this just formalizes statements such as "results of different tosses of a coin are independent" or "draws made at random with replacement are independent".

Try not to become inhibited by the formalism. Notice how the theory not only supports intuition but also develops it. You can expect your probabilistic intuition to be much sharper at the end of this course than it is now!

### "i.i.d." Random Variables
If random variables are mutually independent and identically distributed, they are called "i.i.d." That's one of the most famous acronyms in probability theory. You can think of i.i.d. random variables as draws with replacement from a population, or as the results of independent replications of the same experiment.

Suppose the distribution of $X$ is given by
$$
P(X = i) = p_i, ~~~ i = 1, 2, \ldots, n
$$
where $\sum_{i=1}^n p_i = 1$. Now let $X$ and $Y$ be i.i.d. What is $P(X = Y)$? We'll answer this question by using the fundamental method, now in random variable notation.

$$
\begin{align*}
P(X = Y) &= \sum_{i=1}^n P(X = i, Y = i) ~~~ \text{(partitioning)} \\
&= \sum_{i=1}^n P(X = i)P(Y = i) ~~~ \text{(independence)} \\
&= \sum_{i=1}^n p_i \cdot p_i ~~~ \text{(identical distributions)} \\
&= \sum_{i=1}^n p_i^2
\end{align*}
$$

The last expression is easy to calculate if you know the numerical values of all the $p_i$.

In the same way,

$$
\begin{align*}
P(Y > X) &= \sum_{i=1}^n P(X = i, Y > i) \\
&= \sum_{i=1}^n P(X = i)P(Y > i) \\
&= \sum_{i=1}^{n-1} P(X = i)P(Y > i)
\end{align*}
$$

because $P(Y > n) = 0$. Now for each $i < n$, $P(Y > i) = P(X > i) = \sum_{j=i+1}^n p_j$. Call this sum $b_i$ for "bigger than $i$". Then

$$
\begin{align*}
P(Y > X) &= \sum_{i=1}^{n-1} P(X = i)P(Y > i) \\
&= \sum_{i=1}^{n-1} p_ib_i
\end{align*}
$$

This is also a straightforward calculation if you know all the $p_i$. For $n=4$ it boils down to
$$
p_1 \cdot(p_2 + p_3 + p_4) ~~ + ~~ p_2 \cdot (p_3 + p_4) ~~ + ~~ p_3 \cdot p_4
$$
