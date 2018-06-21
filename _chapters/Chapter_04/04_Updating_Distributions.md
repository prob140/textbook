---
interact_link: notebooks/Chapter_04/04_Updating_Distributions.ipynb
title: '4.4 Updating Distributions'
previouschapter:
  url: chapters/Chapter_04/03_Conditional_Distributions
  title: '4.3 Conditional Distributions'
nextchapter:
  url: chapters/Chapter_04/05_Dependence_and_Independence
  title: '4.5 Dependence and Independence'
---

## Updating Distributions ##

As we saw when we studied Bayes' Rule, conditioning gives us a way of updating our opinions based on new data. Let's see how conditional distributions can be used to represent our opinion about a random parameter, based on data.

### Example: A Randomly Picked Coin ###
Suppose I have one fair coin and three biased coins. Suppose that each of the biased coins lands heads with chance 0.9. I pick one of the coins at random, toss it twice and tell you the number of heads. What can you say about whether the coin was fair or biased?

Before I have told you the number of heads, your *prior* opinion should be that the chance of the fair coin is 0.25 and the chance that the coin is biased is 0.75.

The goal of this example is to see how the information about the number of heads affects this opinion.

Let $R$ be the probability with which the random coin lands heads. The possible values of $R$ are 0.5 and 0.9, and the prior probability distribution of $R$ is given by the following table.


{:.input_area}
```python
coins = [0.5, 0.9]
prior = [0.25, 0.75]
Table().values(coins).probability(prior)
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
            <td>0.5  </td> <td>0.25       </td>
        </tr>
        <tr>
            <td>0.9  </td> <td>0.75       </td>
        </tr>
    </tbody>
</table>
</div>



Let $H$ be the number of heads in the two tosses. Then the joint distribution of $R$ and $H$ consists of terms of the form

$$
P(R = r, H = h) ~~ \text{where } r \in \{0.5, 0.9\} \text{ and }
h \in \{ 0, 1, 2 \}
$$

There are six such terms. Let's work out a couple of them. By the multiplication rule,

$$
P(R = 0.9, H = 2) = P(R = 0.9)P(H = 2 \mid R = 0.9)
= 0.75 \cdot 0.9^2 = 0.6075
$$

The event $\{H = 1\}$ happens if either there is a head followed by a tail or a tail followed by a head. So

$$
P(R = 0.5, H = 1) = P(R = 0.5)P(H = 1 \mid R = 0.5)
= 0.25 [(0.5 \cdot 0.5) + (0.5 \cdot 0.5)] = 0.125
$$

We can use the same kind of reasoning to work out $P(R = r, H = h)$ for all values of $r$ and $h$. 

Let's do that directly in Python. The function `joint_probs` takes $r$ and $h$ as arguments and returns $P(R = r, H = h)$.


{:.input_area}
```python
def joint_probs(r, h):
    """Return P(R = r, H = h)"""
    
    # Start with the distribution of the number of heads in two tosses
    # of a coin that lands heads with a known chance r;
    # these are the chances of h=0, h=1, and h=2
    
    heads_2_tosses = make_array((1-r)**2, 2*r*(1-r), r**2)
    
    if r == 0.5:
        return 0.25*heads_2_tosses.item(h)
    elif r == 0.9:
        return 0.75*heads_2_tosses.item(h)
```

We can now use `prob140` methods to construct a joint distribution table for $R$ and $H$, as described in the section on Joint Distributions. Recall that we used `coins` and `prior` to construct the prior distribution of $R$:


{:.input_area}
```python
coins, prior
```




{:.output_data_text}
```
([0.5, 0.9], [0.25, 0.75])
```




{:.input_area}
```python
heads = np.arange(3)
joint_tbl = Table().values('R', coins, 'H', heads).probability_function(joint_probs)
joint_dist = joint_tbl.to_joint()

joint_dist
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
      <th>R=0.5</th>
      <th>R=0.9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>H=2</th>
      <td>0.0625</td>
      <td>0.6075</td>
    </tr>
    <tr>
      <th>H=1</th>
      <td>0.1250</td>
      <td>0.1350</td>
    </tr>
    <tr>
      <th>H=0</th>
      <td>0.0625</td>
      <td>0.0075</td>
    </tr>
  </tbody>
</table>
</div>
</div>



The values of $P(R = 0.9, H = 2)$ and $P(R = 0.5, H = 1)$ agree with those that we calculated directly.

Let's check that the marginal of $R$ agrees with the assumption that the coin is picked at random from one fair coin and three biased coins. With no information about the number of heads, the distribution of $R$ should just be the prior. And it is, as you can see in the bottom margin of the table below.


{:.input_area}
```python
joint_dist.marginal('R')
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
      <th>R=0.5</th>
      <th>R=0.9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>H=2</th>
      <td>0.0625</td>
      <td>0.6075</td>
    </tr>
    <tr>
      <th>H=1</th>
      <td>0.1250</td>
      <td>0.1350</td>
    </tr>
    <tr>
      <th>H=0</th>
      <td>0.0625</td>
      <td>0.0075</td>
    </tr>
    <tr>
      <th>Sum: Marginal of R</th>
      <td>0.2500</td>
      <td>0.7500</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Now suppose I pick the coin (in secret), toss it twice, and tell you the number of heads. Given the value of $H$, what can you say about $R$?

To start off, it's a good idea to find the conditional distribution of $R$ given the value of $H$. Here are all those conditional distributions, for different given values of $H$. 


{:.input_area}
```python
joint_dist.conditional_dist('R', 'H')
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
      <th>R=0.5</th>
      <th>R=0.9</th>
      <th>Sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dist. of R | H=2</th>
      <td>0.093284</td>
      <td>0.906716</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of R | H=1</th>
      <td>0.480769</td>
      <td>0.519231</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of R | H=0</th>
      <td>0.892857</td>
      <td>0.107143</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Marginal of R</th>
      <td>0.250000</td>
      <td>0.750000</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Read this table from the bottom row upwards. Remember that the coin was randomly picked.
- If I tell you nothing about the number of heads, all you can tell me about the coin is that there is 25% chance that it is fair and 75% chance that it is a biased coin.
- If I tell you that I got 0 heads, your opinion about the coin changes dramatically in favor of the fair coin. The biased coins have a very small chance of producing no heads, so even though one of them was very likely to have been picked, the data tilt the balance in favor of the fair coin.
- If I tell you that I got 1 head, you're in a bit of a quandary. The biased coins have a modest chance (18%) of producing 1 head compared to the 50% chance that the fair coin produces 1 head. But the coin picked had a 75% chance of being biased compared to a 25% chance of being fair. The size of these two effects makes you quite uncertain about which kind of coin to lean towards. You have only a slight lean towards 'biased'.
- If I tell you that I got 2 heads, your opinion shifts dramatically towards the biased coins. Not only are they very likely to produce two heads, they are also very likely to have been picked.

### Updating Your Opinion Based on Data ###
This is a simple example of something that comes up often in machine learning. 
- You start out with a *prior* opinion about an unknown quantity. In our case the prior distribution was that the fair coin would be picked with chance 25%.
- For every value of the unknown quantity, the data have a *likelihood*. For each of our four coins, we know the likelihood of getting any specified number of heads given that we tossed that coin.
- After you see the data, your opinion about the unknown quantity might change, sometimes quite drastically. The change depends on the prior as well as the likelihood.
- You can then toss some more, and update your opinion once again based on the number of heads in the new set of tosses.
