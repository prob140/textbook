---
interact_link: notebooks/Chapter_06/03_Hypergeometric_Distribution.ipynb
title: '6.3 The Hypergeometric Distribution'
permalink: 'chapters/Chapter_06/03_Hypergeometric_Distribution'
previouschapter:
  url: chapters/Chapter_06/02_Examples
  title: '6.2 Examples'
nextchapter:
  url: chapters/Chapter_06/04_Odds_Ratios
  title: '6.4 Odds Ratios'
redirect_from:
  - 'chapters/chapter-06/03-hypergeometric-distribution'
---

## The Hypergeometric Distribution

You have seen the hypergeometric probabilities earlier. In this section we will use them to define the distribution of a random count, and study the relation with the binomial distribution.

As a review of the hypergeometric setting, suppose you have a population of a fixed size $N$, and suppose you are interested in a particular group of those $N$ individuals. Let's call them "successes" or "good elements". For example, you might be interested in:
- a population of voters, and among them the group who will vote for a particular candidate
- a population of households, and among them the group that have annual incomes below $50,000
- a deck of cards, and the suit of diamonds

Let $N = G+B$ where $G$ is the number of good elements and $B$ the remaining number of elements which we will unkindly describe as "bad". 

Now suppose you take a simple random sample (SRS) of $n$ elements from the population.

### Number of Good Elements in a SRS
Let $X$ be the number of good elements in the sample. What is the distribution of $X$?

The largest $X$ can be is $\min(G, n)$. We'll say the smallest $X$ can be is 0, though if we are very careful we will see that in fact $X$ can't be any smaller than $\max(0, n-B)$.

Let $g$ be a possible value of $X$. Then, since all $\binom{N}{n}$ samples are equally likely,

$$
P(X = g) ~ = ~ \frac{\binom{G}{g} \binom{B}{b}}{\binom{N}{n}}, ~~~
g+b=n
$$

This is called the *hypergeometric distribution* with population size $N$, number of good elements or "successes" $G$, and sample size $n$. The name comes from the fact that the terms are the coefficients in a [*hypergeometric series*](https://en.wikipedia.org/wiki/Hypergeometric_function#The_hypergeometric_series), which is a piece of mathematics that we won't go into in this course.

### Example: Aces in a Five-Card Poker Hand
The number of aces $N_a$ in a five-card poker hand has the hypergeometric distribution with population size 52, four good elements in the population, and a simple random sample size of 5.

$$
P(N_a = k) = \frac{\binom{4}{k} \binom{48}{5-k}}{\binom{52}{5}}, ~~ k = 0, 1, 2, 3, 4
$$

The `stats.hypergeom.pmf` function allows us to calculate hypergeometric probabilities. The first argument is the set of possible values for which we want the probabilities. Then come the parameters, in the order population size, number of good elements, sample size.



{:.input_area}
```python
k = np.arange(5)
N = 52 # population size
G = 4  # number of good elements in population
n = 5  # simple random sample size
stats.hypergeom.pmf(k, N, G, n)
```





{:.output_data_text}
```
array([6.58841998e-01, 2.99473636e-01, 3.99298181e-02, 1.73607905e-03,
       1.84689260e-05])
```



Those are the chances of all the different possible numbers of aces in a poker hand. They are rather hard to read, so let's try rounding them.



{:.input_area}
```python
np.round(stats.hypergeom.pmf(k, N, G, n), 3)
```





{:.output_data_text}
```
array([0.659, 0.299, 0.04 , 0.002, 0.   ])
```



The number of aces among 5 cards is overwhelmingly likely to be 0 or 1. The histogram of the distribution can be drawn using `Plot`.



{:.input_area}
```python
ace_probs = stats.hypergeom.pmf(k, N, G, n)
ace_dist = Table().values(k).probabilities(ace_probs)
Plot(ace_dist)
plt.title('Number of Aces in a 5-Card Hand');
```



![png](../../images/chapters/Chapter_06/03_Hypergeometric_Distribution_8_0.png)


### Red Cards in a Bridge Hand
Here is the distribution of the number of red cards in a bridge hand of 13 cards:



{:.input_area}
```python
k = np.arange(14)
N = 52
G = 26
n = 13
bridge_probs = stats.hypergeom.pmf(k, N, G, n)
bridge_dist = Table().values(k).probabilities(bridge_probs)

Plot(bridge_dist)
plt.title('Number of Red Cards in a 13-Card Hand');
```



![png](../../images/chapters/Chapter_06/03_Hypergeometric_Distribution_10_0.png)


This one looks rather binomial. And indeed, there is a close relation between the binomial and the hypergeometric distributions.

### Relation with the Binomial
Suppose you have a population of $N = G+B$ elements as above, and suppose you sample $n$ times *with* replacement. Then the number of good elements in the sample has the binomial distribution with parameters $n$ and $G/N$. 

If you sample *without* replacement, then the distribution of the number of good elements is hypergeometric $(N, G, n)$.

The only difference between the two settings is the randomization: sampling with or without replacement. 

If the population size $N$ is large relative to the sample size $n$, then it doesn't make much difference whether you are sampling with or without replacement. If you only take out a very small proportion of the population as you sample, you make no noticeable difference to the proportions in the population.

To see whether this intuition can be confirmed by calculation, let's visualize some hypergeometric distributions and the corresponding binomial approximations. You can change the parameters in the code below. Just make sure that $n$ is small relative to $N$.



{:.input_area}
```python
N = 100
G = 30
n = 10
k = np.arange(n+1)
hyp_probs = stats.hypergeom.pmf(k, N, G, n)
bin_probs = stats.binom.pmf(k, n, G/N)
hyp_dist = Table().values(k).probabilities(hyp_probs)
bin_dist = Table().values(k).probabilities(bin_probs)
Plots('Hypergeometric (100, 30, 10)', hyp_dist, 'Binomial (10, 0.3)', bin_dist)
```



![png](../../images/chapters/Chapter_06/03_Hypergeometric_Distribution_13_0.png)


They are pretty close, though you can see that the hypergeometric distribution is a bit taller and narrower. In a later chapter we will quantify this difference in spread.

### Fisher's Exact Test
Recall a [randomized controlled experiment](https://www.ncbi.nlm.nih.gov/pubmed/11376175) that was analyzed in Data 8. The treatment was the botulinum toxin A, a very potent toxin, used as medication for patients who had chronic back pain.

A total of 31 patients participated in the study. Of these, 15 were randomly assigned to the treatment group and the remaining 16 to the control group. Eight weeks after treatment, 11 of the 15 in the treatment group had pain relief compared to 2 out of 16 in the control group. 

In other words, of the 13 patients who had pain relief, 11 were in the treatment group and 2 in the control group. Is this evidence in favor of the treatment?

The null hypothesis says that the treatment does nothing; any difference between the two groups is due to the random assignment of patients to treatment and control. 

The alternative hypothesis says that the treatment was beneficial. 

Under the null hypothesis, the treatment did nothing, so among the 31 patients in the study, *13 would have had pain relief anyway*, regardless of the assignment to groups. 

To see which of the hypotheses is better supported by the data, we can find a P-value. This is the chance, under the null hypothesis, of getting data like the data that were observed or even more in the direction of the alternative. That is, the P-value is the chance of getting 11 or more of the "pain relief" patients in the treatment group, just by chance.

To find the chance that 11 or more of the "pain relief" group would have ended up in the treatment group, we just need a hypergeometric probability:
- N = 31, the population size
- G = 13, the total number of "pain relief" patients
- n = 15, the size of the treatment group
- g = 11 or more



{:.input_area}
```python
sum(stats.hypergeom.pmf([11, 12, 13], 31, 13, 15))
```





{:.output_data_text}
```
0.0008299755046076295
```



That's a very small P-value, which implies that the data support the alternative hypothesis more than they support the null. The treatment helped. This is consistent with the conclusion of the researchers and also with our own analysis in Data 8 – but all three analyses are different.

In Data 8 we simulated the difference between the two group proportions under the null hypothesis, by pooling the two groups and randomly permuting the pooled sample. Our conclusion was based on an empirical, approximate P-value. 

The calculation here does not require simulation and produces an exact P-value.

This method is called Fisher's exact test. That's the same Sir Ronald Fisher who formalized tests of hypotheses, suggested cutoffs for P-values, and so on. The method can be used for any sample size and any randomized controlled experiment with a binary response.

### Joint, Marginal, and Conditional Distributions
The calculations above extend easily to samples that can come out in more than two categories. Consider a five-card poker hand dealt from a well-shuffled deck. Let $H$ be the number of hearts and $S$ the number of spaces in the hand. Let us find the joint distribution of $H$ and $S$.

The hand can have cards other than hearts and spades, of course. Let $X$ be the number of those cards, which must be diamonds or clubs. Then

$$
P(H = h, S = s) ~ = ~ P(H = h, S = s, X = 5 - (h+s)) ~ = ~ 
\frac{\binom{13}{h}\binom{13}{s}\binom{26}{5-h-s}}{\binom{52}{5}}, ~~ h, s \ge 0, ~ h+s \le 5
$$

The SciPy module `special` allows you to calculate binomial coefficients, so let's import it.



{:.input_area}
```python
from scipy import special
```


The expression `special.comb(n, k)` evaluates to $\binom{n}{k}$. This allows us to calculate the joint distribution of $H$ and $S$.



{:.input_area}
```python
def joint_prob(h, s):
    if (h+s >=0) and (h+s <=5):
        numerator = special.comb(13, h) * special.comb(13, s) * special.comb(26, 5 - h -s)
        denominator = special.comb(52, 5)
        return numerator / denominator
    else:
        return 0
    
k = np.arange(6)
joint_dist = Table().values('H', k, 'S', k).probability_function(joint_prob)
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
      <th>H=0</th>
      <th>H=1</th>
      <th>H=2</th>
      <th>H=3</th>
      <th>H=4</th>
      <th>H=5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>S=5</th>
      <td>0.000495</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=4</th>
      <td>0.007153</td>
      <td>0.003576</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=3</th>
      <td>0.035764</td>
      <td>0.037195</td>
      <td>0.008583</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=2</th>
      <td>0.078031</td>
      <td>0.126801</td>
      <td>0.060864</td>
      <td>0.008583</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=1</th>
      <td>0.074780</td>
      <td>0.169068</td>
      <td>0.126801</td>
      <td>0.037195</td>
      <td>0.003576</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=0</th>
      <td>0.025310</td>
      <td>0.074780</td>
      <td>0.078031</td>
      <td>0.035764</td>
      <td>0.007153</td>
      <td>0.000495</td>
    </tr>
  </tbody>
</table>
</div>
</div>



The distribution of $H$ can be obtained by summing along the columns, or by using the `marginal` method:



{:.input_area}
```python
joint_dist.marginal('H')
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
      <th>H=0</th>
      <th>H=1</th>
      <th>H=2</th>
      <th>H=3</th>
      <th>H=4</th>
      <th>H=5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>S=5</th>
      <td>0.000495</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=4</th>
      <td>0.007153</td>
      <td>0.003576</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=3</th>
      <td>0.035764</td>
      <td>0.037195</td>
      <td>0.008583</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=2</th>
      <td>0.078031</td>
      <td>0.126801</td>
      <td>0.060864</td>
      <td>0.008583</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=1</th>
      <td>0.074780</td>
      <td>0.169068</td>
      <td>0.126801</td>
      <td>0.037195</td>
      <td>0.003576</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>S=0</th>
      <td>0.025310</td>
      <td>0.074780</td>
      <td>0.078031</td>
      <td>0.035764</td>
      <td>0.007153</td>
      <td>0.000495</td>
    </tr>
    <tr>
      <th>Sum: Marginal of H</th>
      <td>0.221534</td>
      <td>0.411420</td>
      <td>0.274280</td>
      <td>0.081543</td>
      <td>0.010729</td>
      <td>0.000495</td>
    </tr>
  </tbody>
</table>
</div>
</div>



But $H$ is the number of hearts in a five-card hand, so we already know that $H$ has the hypergeometric $(52, 13, 5)$ distribution. Let's confirm that this is the same as the marginal distribution above.



{:.input_area}
```python
stats.hypergeom.pmf(k, 52, 13, 5)
```





{:.output_data_text}
```
array([0.22153361, 0.41141957, 0.27427971, 0.08154262, 0.01072929,
       0.0004952 ])
```



If you know how many spades are in the hand, then what is the conditional distribution of $H$?



{:.input_area}
```python
joint_dist.conditional_dist('H', 'S')
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
      <th>H=0</th>
      <th>H=1</th>
      <th>H=2</th>
      <th>H=3</th>
      <th>H=4</th>
      <th>H=5</th>
      <th>Sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dist. of H | S=5</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of H | S=4</th>
      <td>0.666667</td>
      <td>0.333333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of H | S=3</th>
      <td>0.438596</td>
      <td>0.456140</td>
      <td>0.105263</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of H | S=2</th>
      <td>0.284495</td>
      <td>0.462304</td>
      <td>0.221906</td>
      <td>0.031294</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of H | S=1</th>
      <td>0.181761</td>
      <td>0.410937</td>
      <td>0.308203</td>
      <td>0.090406</td>
      <td>0.008693</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Dist. of H | S=0</th>
      <td>0.114250</td>
      <td>0.337556</td>
      <td>0.352232</td>
      <td>0.161440</td>
      <td>0.032288</td>
      <td>0.002235</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Marginal of H</th>
      <td>0.221534</td>
      <td>0.411420</td>
      <td>0.274280</td>
      <td>0.081543</td>
      <td>0.010729</td>
      <td>0.000495</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>



Let's see if we recognize these numbers. Remember that the $(h, s)$ cell of the table contains $P(H = h \mid S =s )$.

For an extreme case, look at the top row. Given that there are five spades in the hand, there can't be any hearts. That is why the table says $P(H = 0 \mid S = 5) = 1$.

Now suppose we are given that $S = 1$. Then $H$ can have values 0 through 4, and for any integer $h$ in this range we have

$$
P(H = h \mid S = 1) ~ = ~ \frac{P(H = h, S = 1)}{P(S = 1)} ~ = ~ 
\frac{\binom{13}{h}\binom{13}{1}\binom{26}{5 - h - 1}}{\binom{13}{1}\binom{39}{4}}
$$

by canceling factors of $1/\binom{52}{5}$ in the numerator and denominator. After canceling $\binom{13}{1}$ as well, we have

$$
P(H = h \mid S = 1) ~ = ~ \frac{\binom{13}{h}\binom{26}{4 - h}}{\binom{39}{4}}, ~~ 0 \le h \le 4
$$

This is the hypergeometric $(39, 13, 4)$ distribution: given that there is one spade in the hand, the other four cards are like a simple random sample drawn from the 39 hearts, diamonds, and clubs.



{:.input_area}
```python
stats.hypergeom.pmf(np.arange(5), 39, 13, 4)
```





{:.output_data_text}
```
array([0.18176071, 0.41093725, 0.30820294, 0.0904062 , 0.0086929 ])
```



These are the probabilities in the row corresponding to the given condition $S=1$ in the table of conditional distributions above.
