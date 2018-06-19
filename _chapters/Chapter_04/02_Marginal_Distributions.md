---
interact_link: notebooks/Chapter_04/02_Marginal_Distributions.ipynb
title: '4.2 Marginal Distributions'
previouschapter:
  url: chapters/Chapter_04/01_Joint_Distributions
  title: '4.1 Joint Distributions'
nextchapter:
  url: chapters/Chapter_04/03_Conditional_Distributions
  title: '4.3 Conditional Distributions'
---

## Marginal Distributions ##

Joint distribution tables partition the entire outcome space according to the values of the pair $(X, Y)$.

In our example, we are tossing a coin three times. $X$ is the number of heads in the first two tosses and $Y$ the number of heads in the last two tosses. Here once again is the joint distribution table for $X$ and $Y$.


{:.input_area}
```python
joint_dist
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=2</th>
      <td>0.000</td>
      <td>0.125</td>
      <td>0.125</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.125</td>
      <td>0.250</td>
      <td>0.125</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.125</td>
      <td>0.125</td>
      <td>0.000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



The space has been partitioned into 9 pieces, each with its own chance. The total of all the chances is 1 as we saw in the previous section.

### Partitioning $\{X = x \}$ According to $Y$ ###
Now look along the column labeled `X = 0`. In every cell of that column, the value of $X$ is 0 and $Y$ is some element in the range of $Y$. So the column `X=0` partitions the event $\{X = 0\}$ according to the value of $Y$, and displays the probability of each piece of the partition.

Indeed for every $x$,
$$
\{X = x \} = \bigcup_{\text{all } y} \{X = x, Y = y\}
$$
and this is a disjoint union. So by the addition rule,

$$
P(X = x) = \sum_{\text{all } y} P(X = x, Y = y)
$$

That is, $P(X = x)$ is the sum of the probabilities in the column `X=x`. Because $P(X = x)$ is the generic term in the distribution of $X$, we have learned that we can derive the distribution of $X$ from the joint distribution of $X$ and $Y$.

To find the numerical values of the distribution of $X$, we will use a method called `marginal` which takes the name `X` as its argument and operates on a joint distribution object. The reason for using the word "marginal" will become clear as soon as we see the output.


{:.input_area}
```python
joint_dist.marginal('X')
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=2</th>
      <td>0.000</td>
      <td>0.125</td>
      <td>0.125</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.125</td>
      <td>0.250</td>
      <td>0.125</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.125</td>
      <td>0.125</td>
      <td>0.000</td>
    </tr>
    <tr>
      <th>Sum: Marginal of X</th>
      <td>0.250</td>
      <td>0.500</td>
      <td>0.250</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Now at the bottom of the table you have all the column sums, which constitute the distribution of $X$. These sums appear in the margin of the table, and hence the distribution is called *marginal*. 

This is just a new name for the probability distribution of $X$, the number of heads in the first two tosses. 

### Both Marginals ###
What you can do for $X$, you can do as well for $Y$ by looking along the rows.


{:.input_area}
```python
joint_dist.marginal('Y')
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
  </tbody>
</table>
</div>
</div>



$Y$ is also the number of heads in two tosses of a coin (the last two of three tosses), so the probabilities in the margin make sense.

You can also get both marginals at once:


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



The bottom right corner cell is the sum of all the probabilities in the table, and also the sum of all the probabilities in each of the margins. Reassuringly, it's 1.

Compare the two marginal distributions. They are the same (possible values and the corresponding probabilities). So $X \stackrel{d}{=} Y$.
