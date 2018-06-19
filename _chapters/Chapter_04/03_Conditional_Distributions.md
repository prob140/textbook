---
interact_link: notebooks/Chapter_04/03_Conditional_Distributions.ipynb
title: '4.3 Conditional Distributions'
previouschapter:
  url: chapters/Chapter_04/02_Marginal_Distributions
  title: '4.2 Marginal Distributions'
nextchapter:
  url: chapters/Chapter_04/04_Updating_Distributions
  title: '4.4 Updating Distributions'
---

## Conditional Distributions ##

To understand the relation between two variables you must examine the conditional behavior of each of them given the value of the other. Towards this goal, we will start by examining the simple example of the previous sections and then develop the general theory.

In our example about heads in three tosses of a coin, where $X$ is the number of heads in the first two tosses and $Y$ the number of heads in the last two tosses, the joint distribution of $X$ and $Y$ and the two marginals are displayed in the table below.


{:.input_area}
```python
joint_dist.both_marginals()
```




<div markdown="0">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X=0</th>
      <th>X=1</th>
      <th>X=2</th>
      <th>Sum: Marginal of Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=2</th>
      <td>0.000</td>
      <td>0.125</td>
      <td>0.125</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.125</td>
      <td>0.250</td>
      <td>0.125</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.125</td>
      <td>0.125</td>
      <td>0.000</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>Sum: Marginal of X</th>
      <td>0.250</td>
      <td>0.500</td>
      <td>0.250</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Given a particular value $x$ of $X$, that is, given that there were $x$ heads in the first two tosses, we can work out the *conditional distribution* of the number of heads in the last two tosses.

In random variable language, for each value $x$ of $X$, the random variable $Y$ has a conditional distribution given $X = x$. We can get all three of these conditional distributions as follows:


{:.input_area}
```python
# conditional distribution of Y given each different value of X

joint_dist.conditional_dist('Y', 'X') 
```




<div markdown="0">
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dist. of Y | X=0</th>
      <th>Dist. of Y | X=1</th>
      <th>Dist. of Y | X=2</th>
      <th>Marginal of Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=2</th>
      <td>0.0</td>
      <td>0.25</td>
      <td>0.5</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.5</td>
      <td>0.50</td>
      <td>0.5</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.5</td>
      <td>0.25</td>
      <td>0.0</td>
      <td>0.25</td>
    </tr>
    <tr>
      <th>Sum</th>
      <td>1.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>
</div>
</div>



To understand this table, start with the first column. In that column, the given condition is $X = 0$, that is, there were no heads in the first two tosses. Under this condition, $Y$ can't be 2, which is why you see the probability 0 in the top cell. If $X = 0$ then $Y$ can only be 1 or 0, according to whether the third toss was a head or a tail. That explains the probability of 0.5 in each of the remaining two cells.

You can work out all the other probabilities in this way. But you don't have to go back to the original outcomes to figure out these conditional probabilities. Just use the joint distribution table displayed at the start of the example, and the division rule.

For example,

$$
P(Y = 1 \mid X = 0) = \frac{P(X = 0, Y = 1)}{P(X = 0)} = \frac{0.125}{0.25} = 0.5
$$

It is easy to see why each column in the table of conditional distributions sums to 1. Each cell in one column is obtained from the joint distribution table by taking the corresponding cell in that table and dividing it by the sum of its column. So the columns in the resulting table sum to 1.

### The Theory ###
We will now generalize the calculations we did in the example above.

Let $X$ and $Y$ be two random variables defined on the same space. If $x$ is a possible value of $X$, and $y$ and possible value of $Y$, then
$$
P(Y = y \mid X = x) = \frac{P(X = x, Y = y)}{P(X = x)}
$$

Therefore, for a fixed value $x^*$ of $X$, the *conditional distribution* of $Y$, given $X = x^*$ is the collection of probabilities
$$
P(Y = y \mid X = x^*) = \frac{P(X = x^*, Y = y)}{P(X = x^*)}
$$
where $y$ ranges over all the values of $Y$. Keep in mind that $y$ represents values of the variable here. The value $x^*$ is the particular value of $X$ that was observed; it is a constant.

### The Probabilities in a Conditional Distribution Sum to 1 ###
In a distribution, the probabilities have to sum to 1. To see that this is true for the conditional distribution defined above, start by using the fundamental rule. 

Find $P(X = x^*)$ by partitioning the event $\{ X = x^* \}$ according to the values of $Y$:

$$
P(X = x^*) = \sum_{\text{all }y} P(X = x^*, Y = y)
$$

Now let's sum the probabilities in the conditional distribution of $Y$ given $X = x^*$, and see if the sum is 1.

\begin{align*}
\sum_{\text{all }y} P(Y = y \mid X = x^*) &=
\sum_{\text{all }y} \frac{P(X = x^*, Y = y)}{P(X = x^*)} \\ \\
&= \frac{1}{P(X = x^*)} \sum_{\text{all }y} P(X = x^*, Y = y) \\
&= \frac{1}{P(X = x^*)} \cdot P(X = x^*) \\
&= 1
\end{align*}
