---
interact_link: notebooks/Chapter_13/04_Finite_Population_Correction.ipynb
title: '13.4 Finite Population Correction'
permalink: 'chapters/Chapter_13/04_Finite_Population_Correction'
previouschapter:
  url: chapters/Chapter_13/03_Sums_of_Simple_Random_Samples
  title: '13.3 Sums of Simple Random Samples'
nextchapter:
  url: chapters/Chapter_14/00_The_Central_Limit_Theorem
  title: 'Chapter 14: The Central Limit Theorem'
redirect_from:
  - 'chapters/chapter-13/04-finite-population-correction'
---

## Finite Population Correction

Data scientists often have to work with a relatively small sample from an enormous population. So suppose we are drawing at random $n$ times from a population of size $N$ where $N$ is large and $n$ is small relative to $N$. Just go with the flow for now – all of this will become more precise as this section develops.

Suppose the population mean is $\mu$ and the population SD is $\sigma$. Let $S_n$ be the sample sum. Then, regardless of whether the sample is drawn with replacement or without,
$$
E(S_n) = n\mu
$$

The variance of the sample sum is different in the two cases.

|$~~~~~~~~~~~~~~~~~$ | sampling with replacement | sampling without replacement|
|:---------:|:-------------------------:|:---------------------------:|
|$Var(S_n)$ |$n\sigma^2$                | $n\sigma^2\frac{N-n}{N-1}$  |
|$SD(S_n)$  |$\sqrt{n}\sigma$           | $\sqrt{n}\sigma\sqrt{\frac{N-n}{N-1}}$  |

The "without replacement" column is the same as the "with replacement" column apart from what are called *correction factors*. The one for the SD is called the *finite population correction* or fpc.

$$
\text{finite population correction} ~ = ~ \sqrt{\frac{N-n}{N-1}}
$$

The name arises because sampling with replacement can be thought of as sampling without replacement from an infinite population. Every time you draw, you leave the proportions in the population exactly the same as they were before you drew.

A more realistic version of that image is drawing without replacement from an enormous finite population. Every time you draw, you leave the proportions in the population *almost* exactly the same as they were before you drew.

We used this idea earlier when we said that sampling without replacement is almost the same as sampling with replacement provided you are drawing a relatively small sample from a very large population.

The fpc gives us a way to quantify this idea.

### The Size of the FPC
First note that when $N$ is even moderately large,
$$
\frac{N-n}{N-1} ~ \approx ~ \frac{N-n}{N} ~ = ~ 1 - \frac{n}{N}
$$

which is the fraction of the population that is left after sampling.

If $N$ is large and $n$ is small relative to $N$, then

$$
\frac{N-n}{N-1} ~ \approx ~ 1 - \frac{n}{N} ~ \approx ~ 1
$$
which also implies
$$
\sqrt{\frac{N-n}{N-1}} ~ \approx ~ 1
$$

So whether you are sampling with replacement or without, the variance of the sample sum can be taken to be $n\sigma^2$. The formula is exact in the case of sampling with replacement and an excellent approximation in the case of sampling without replacement from a large population when the sample size is small relative to the population size.

The table below gives the fpc for a variety of population and sample sizes.



{:.input_area}
```python
pop = make_array(1000, 10000, 50000, 100000, 500000, 1000000)

def fpc(pct):
    samp = np.round(pop*pct/100, 0)
    return np.round(((pop-samp)/(pop-1))**0.5, 6)
```




{:.input_area}
```python
Table().with_columns(
  'Population Size', pop,
  '1% Sample', fpc(1),
  '5% Sample', fpc(5),
  '10% Sample', fpc(10),
  '20% Sample', fpc(20)
)
```





<div markdown="0">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Population Size</th> <th>1% Sample</th> <th>5% Sample</th> <th>10% Sample</th> <th>20% Sample</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1000           </td> <td>0.995485 </td> <td>0.975167 </td> <td>0.949158  </td> <td>0.894875  </td>
        </tr>
        <tr>
            <td>10000          </td> <td>0.995037 </td> <td>0.974728 </td> <td>0.948731  </td> <td>0.894472  </td>
        </tr>
        <tr>
            <td>50000          </td> <td>0.994997 </td> <td>0.974689 </td> <td>0.948693  </td> <td>0.894436  </td>
        </tr>
        <tr>
            <td>100000         </td> <td>0.994992 </td> <td>0.974684 </td> <td>0.948688  </td> <td>0.894432  </td>
        </tr>
        <tr>
            <td>500000         </td> <td>0.994988 </td> <td>0.97468  </td> <td>0.948684  </td> <td>0.894428  </td>
        </tr>
        <tr>
            <td>1000000        </td> <td>0.994988 </td> <td>0.97468  </td> <td>0.948684  </td> <td>0.894428  </td>
        </tr>
    </tbody>
</table>
</div>



The values in each column are essentially constant, because each is essentially the square root of the fraction *not* sampled:



{:.input_area}
```python
sample_pct = make_array(1, 5, 10, 20)

(1 - sample_pct/100)**0.5
```





{:.output_data_text}
```
array([ 0.99498744,  0.97467943,  0.9486833 ,  0.89442719])
```



All of these fpc values are fairly close to 1, especially in the 1% column where they are all essentially 0.995. That is why the fpc is often dropped from variance calculations.

### The (Non) Effect of the Population Size
The SD of a simple random sample sum depends only on the sample size and the population SD, provided the population size is large enough that the fpc is close to 1.

That's clear from the formula. If the fpc is close to 1, as it often is, then

$$
SD(S_n) \approx \sqrt{n}\sigma
$$

which involves only the sample size $n$ and the population SD $\sigma$. 

To understand this intuitively, suppose you are trying to determine the composition of a liquid based on the amount in a test tube. If the liquid is well mixed, does it matter whether the amount in the test tube was drawn from a bowl or from a bathtub? It doesn't, because both the bowl and the bathtub are so much larger than the test tube that they might as well be inifinite.
