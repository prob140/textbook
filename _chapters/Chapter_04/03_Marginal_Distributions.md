---
interact_link: notebooks/Chapter_04/03_Marginal_Distributions.ipynb
title: '4.3 Marginal Distributions'
permalink: 'chapters/Chapter_04/03_Marginal_Distributions'
previouschapter:
  url: chapters/Chapter_04/02_Examples
  title: '4.2 Examples'
nextchapter:
  url: chapters/Chapter_04/04_Conditional_Distributions
  title: '4.4 Conditional Distributions'
redirect_from:
  - 'chapters/chapter-04/03-marginal-distributions'
---

## Marginal Distributions

What does the joint distribution of $X$ and $Y$ tell us about the distribution of $X$ alone?

Everything, of course. Let's see how.

Here is the joint distribution table of two random variables $X$ and $Y$.



{:.input_area}
```python
joint_table
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=5</th>
      <td>0.00000</td>
      <td>0.0000</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Y=4</th>
      <td>0.00000</td>
      <td>0.0625</td>
      <td>0.09375</td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.03125</td>
      <td>0.1875</td>
      <td>0.09375</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.09375</td>
      <td>0.1875</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.09375</td>
      <td>0.0625</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.03125</td>
      <td>0.0000</td>
      <td>0.00000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



To find the distribution of $X$ we need the possible values of $X$ and all their probabilities.

At a glance, you can see that the possible values of $X$ are 0, 1, and 2.

Let's look at the event $\{ X = 0 \}$. 



{:.input_area}
```python
def indicator_X_equals_0(i, j):
    return i == 0

joint_table.event(indicator_X_equals_0, 'X', 'Y')
```


{:.output_stream}
```
P(Event) = 0.25

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=5</th>
      <td>0.00000</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Y=4</th>
      <td>0.00000</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.03125</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.09375</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.09375</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.03125</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>
</div>



These are the cells in the column labeled `X=0`. The sum of the probabilities in those cells is $P(X = 0) = 0.25$.

### Partitioning $\{X = x \}$ According to $Y$
In every cell of the column labeled `X=0`, the value of $X$ is 0 and the value of $Y$ is some possible value of $Y$. So the column `X=0` partitions the event $\{X = 0\}$ according to the value of $Y$, and displays the probability of each piece of the partition.

In other words, for every $x$ we have
$$
\{X = x \} = \bigcup_{\text{all } y} \{X = x, Y = y\}
$$
and this is a disjoint union. So by the addition rule,

$$
P(X = x) = \sum_{\text{all } y} P(X = x, Y = y)
$$

That is, $P(X = x)$ is the sum of the probabilities in the column `X=x`. Because $P(X = x)$ is the generic term in the distribution of $X$, we have learned that we can derive the distribution of $X$ from the joint distribution of $X$ and $Y$.

### Marginal Distribution of $X$

To find the numerical values of the distribution of $X$, we will use a method called `marginal` that operates on a joint distribution object and takes the variable name as its argument. The reason for using the word "marginal" will become clear as soon as we see the output.



{:.input_area}
```python
joint_table.marginal('X')
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=5</th>
      <td>0.00000</td>
      <td>0.0000</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Y=4</th>
      <td>0.00000</td>
      <td>0.0625</td>
      <td>0.09375</td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.03125</td>
      <td>0.1875</td>
      <td>0.09375</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.09375</td>
      <td>0.1875</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.09375</td>
      <td>0.0625</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.03125</td>
      <td>0.0000</td>
      <td>0.00000</td>
    </tr>
    <tr>
      <th>Sum: Marginal of X</th>
      <td>0.25000</td>
      <td>0.5000</td>
      <td>0.25000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Now at the bottom of the table you have all the column sums, which constitute the probabilities in the distribution of $X$. 

Because the sums appear in the margin of the table, the distribution is called *marginal*. It's a bit silly. But "marginal" is a commonly used term for the probability distribution of $X$ when the distribution has been derived from a joint distribution.

You should recognize that $X$ has the same distribution as the number of heads in two tosses of a coin.

### Both Marginals
What you can do for $X$, you can do as well for $Y$ by looking along the rows.



{:.input_area}
```python
joint_table.marginal('Y')
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
      <th>Sum: Marginal of Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=5</th>
      <td>0.00000</td>
      <td>0.0000</td>
      <td>0.03125</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Y=4</th>
      <td>0.00000</td>
      <td>0.0625</td>
      <td>0.09375</td>
      <td>0.15625</td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.03125</td>
      <td>0.1875</td>
      <td>0.09375</td>
      <td>0.31250</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.09375</td>
      <td>0.1875</td>
      <td>0.03125</td>
      <td>0.31250</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.09375</td>
      <td>0.0625</td>
      <td>0.00000</td>
      <td>0.15625</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.03125</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.03125</td>
    </tr>
  </tbody>
</table>
</div>
</div>



You can also get both marginals at once:



{:.input_area}
```python
joint_table.both_marginals()
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
      <th>Sum: Marginal of Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Y=5</th>
      <td>0.00000</td>
      <td>0.0000</td>
      <td>0.03125</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Y=4</th>
      <td>0.00000</td>
      <td>0.0625</td>
      <td>0.09375</td>
      <td>0.15625</td>
    </tr>
    <tr>
      <th>Y=3</th>
      <td>0.03125</td>
      <td>0.1875</td>
      <td>0.09375</td>
      <td>0.31250</td>
    </tr>
    <tr>
      <th>Y=2</th>
      <td>0.09375</td>
      <td>0.1875</td>
      <td>0.03125</td>
      <td>0.31250</td>
    </tr>
    <tr>
      <th>Y=1</th>
      <td>0.09375</td>
      <td>0.0625</td>
      <td>0.00000</td>
      <td>0.15625</td>
    </tr>
    <tr>
      <th>Y=0</th>
      <td>0.03125</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.03125</td>
    </tr>
    <tr>
      <th>Sum: Marginal of X</th>
      <td>0.25000</td>
      <td>0.5000</td>
      <td>0.25000</td>
      <td>1.00000</td>
    </tr>
  </tbody>
</table>
</div>
</div>



The bottom right corner cell is the sum of all the probabilities in the table, and also the sum of all the probabilities in each of the margins. Reassuringly, it's 1.
