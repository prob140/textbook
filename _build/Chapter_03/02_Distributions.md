---
redirect_from:
  - "/chapter-03/02-distributions"
interact_link: notebooks/Chapter_03/02_Distributions.ipynb
title: 'Distributions'
prev_page:
  url: /Chapter_03/01_Functions_on_an_Outcome_Space
  title: 'Functions on an Outcome Space'
next_page:
  url: /Chapter_03/03_Equality
  title: 'Equality'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /notebooks***"
---

## Distributions

Our space is the outcomes of five rolls of a die, and our random variable $S$ is the total number of spots on the five rolls.



{:.input_area}
```python
five_rolls_sum
```





<div markdown="0" class="output output_html">
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



In the last section we found $P(S = 10)$. We could use that same process to find $P(S = s)$ for each possible value of $s$. The `group` method allows us to do this for all $s$ at the same time.

To do this, we will start by dropping the `omega` column. Then we will `group` the table by the distinct values of `S(omega)`, and use `sum` to add up all the probabilities in each group.



{:.input_area}
```python
dist_S = five_rolls_sum.drop('omega').group('S(omega)', sum)
dist_S
```





<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>S(omega)</th> <th>P(omega) sum</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5       </td> <td>0.000128601 </td>
        </tr>
        <tr>
            <td>6       </td> <td>0.000643004 </td>
        </tr>
        <tr>
            <td>7       </td> <td>0.00192901  </td>
        </tr>
        <tr>
            <td>8       </td> <td>0.00450103  </td>
        </tr>
        <tr>
            <td>9       </td> <td>0.00900206  </td>
        </tr>
        <tr>
            <td>10      </td> <td>0.0162037   </td>
        </tr>
        <tr>
            <td>11      </td> <td>0.0263632   </td>
        </tr>
        <tr>
            <td>12      </td> <td>0.0392233   </td>
        </tr>
        <tr>
            <td>13      </td> <td>0.0540123   </td>
        </tr>
        <tr>
            <td>14      </td> <td>0.0694444   </td>
        </tr>
    </tbody>
</table>
<p>... (16 rows omitted)</p>
</div>



This table shows all the possible values of $S$ along with all their probabilities. It is called a *probability distribution table* for $S$. 

The contents of the table – all the possible values of the random variable, along with all their probabilities – are called the *probability distribution of $S$*, or just *distribution of $S$* for short. The distribution shows how the total probability of 100% is distributed over all the possible values of $S$.

Let's check this, to make sure that all the $\omega$'s in the outcome space have been accounted for in the column of probabilities.



{:.input_area}
```python
dist_S.column(1).sum()
```





{:.output .output_data_text}
```
0.99999999999999911
```



That's 1 in a computing environment. This is a feature of any probability distribution:

**Probabilities in a distribution are non-negative and sum to 1**.

### Visualizing the Distribution
In Data 8 you used the `datascience` library to work with distributions of data. The `prob140` library builds on `datascience` to provide some convenient tools for working with probability distributions and events. 

First, we will construct a probability distribution object which, while it looks very much like the table above, expects a probability distribution in the second column and complains if it finds anything else.

To keep the code easily readable, let's extract the possible values and probabilities separately as arrays:



{:.input_area}
```python
s = dist_S.column(0)
p_s = dist_S.column(1)
```


To turn these into a probability distribution object, start with an empty table and use the `values` and `probability` Table methods. The argument of `values` is a list or an array of possible values, and the argument of `probability` is a list or an array of the corresponding probabilities. 



{:.input_area}
```python
dist_S = Table().values(s).probability(p_s)
dist_S
```





<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Probability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>5    </td> <td>0.000128601</td>
        </tr>
        <tr>
            <td>6    </td> <td>0.000643004</td>
        </tr>
        <tr>
            <td>7    </td> <td>0.00192901 </td>
        </tr>
        <tr>
            <td>8    </td> <td>0.00450103 </td>
        </tr>
        <tr>
            <td>9    </td> <td>0.00900206 </td>
        </tr>
        <tr>
            <td>10   </td> <td>0.0162037  </td>
        </tr>
        <tr>
            <td>11   </td> <td>0.0263632  </td>
        </tr>
        <tr>
            <td>12   </td> <td>0.0392233  </td>
        </tr>
        <tr>
            <td>13   </td> <td>0.0540123  </td>
        </tr>
        <tr>
            <td>14   </td> <td>0.0694444  </td>
        </tr>
    </tbody>
</table>
<p>... (16 rows omitted)</p>
</div>



That looks exactly like the table we had before except for more readable column labels. But now for the benefit: to visualize the distribution in a histogram, just use the `prob140` method `Plot` as follows.



{:.input_area}
```python
Plot(dist_S)
```



{:.output .output_png}
![png](../images/Chapter_03/02_Distributions_14_0.png)



#### Notes on `Plot`
- Recall that `hist` in the `datascience` library displays a histogram of raw data contained in a column of a table. `Plot` in the `prob140` library displays a probability histogram based on a probability distribution as the input.

- `Plot` only works on probability distribution objects created using the `values` and `probability` methods. It won't work on a general member of the `Table` class.

- `Plot` works well with random variables that have integer values. Many of the random variables you will encounter in the next few chapters will be integer-valued. For displaying the distributions of other random variables, binning decisions are more complicated.

#### Notes on the Distribution of $S$
Here we have the bell shaped curve appearing as the distribution of the sum of five rolls of a die. Notice two differences between this histogram and the bell shaped distributions you saw in Data 8.
- This one displays an exact distribution. It was computed based on *all* the possible outcomes of the experiment. It is not an approximation nor an empirical histogram.
- The statement of the Central Limit Theorem in Data 8 said that the distribution of the sum of a *large* random sample is roughly normal. But here you're seeing a bell shaped distribution for the sum of only five rolls. If you start out with a uniform distribution (which is the distribution of a single roll), then you don't need a large sample before the probability distribution of the sum starts to look normal.

### Visualizing Probabilities of Events
As you know from Data 8, the interval between the points of inflection of the bell curve contains about 68% of the area of the curve. Though the histogram above isn't exactly a bell curve – it is a discrete histogram with only 26 bars – it's pretty close. The points of inflection appear to be 14 and 21, roughly.

The `event` argument of `Plot` lets you visualize the probability of the event, as follows.



{:.input_area}
```python
Plot(dist_S, event = np.arange(14, 22, 1))
```



{:.output .output_png}
![png](../images/Chapter_03/02_Distributions_18_0.png)



The gold area is the equal to $P(14 \le S \le 21)$.

The `prob_event` method operates on probability distribution objects to return the probability of an event. To find $P(14 \le S \le 21)$, use it as follows.



{:.input_area}
```python
dist_S.prob_event(np.arange(14, 22, 1))
```





{:.output .output_data_text}
```
0.6959876543209863
```



The chance is 69.6%, not very far from 68%.

### Math and Code Correspondence
$P(14 \le S \le 21)$ can be found by partitioning the event as the union of the events $\{S = s\}$ in the range 14 through 21, and using the addition rule.

$$
P(14 \le S \le 21) = \sum_{s = 14}^{21} P(S = s)
$$

Note carefully the use of lower case $s$ for the generic possible value, in contrast with upper case $S$ for the random variable; not doing so leads to endless confusion about what formulas mean.

This one means:
- First extract the event $\{ S = s\}$ for each value $s$ in the range 14 through 21:



{:.input_area}
```python
event_table = dist_S.where(0, are.between(14, 22))
event_table
```





<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Value</th> <th>Probability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>14   </td> <td>0.0694444  </td>
        </tr>
        <tr>
            <td>15   </td> <td>0.0837191  </td>
        </tr>
        <tr>
            <td>16   </td> <td>0.0945216  </td>
        </tr>
        <tr>
            <td>17   </td> <td>0.100309   </td>
        </tr>
        <tr>
            <td>18   </td> <td>0.100309   </td>
        </tr>
        <tr>
            <td>19   </td> <td>0.0945216  </td>
        </tr>
        <tr>
            <td>20   </td> <td>0.0837191  </td>
        </tr>
        <tr>
            <td>21   </td> <td>0.0694444  </td>
        </tr>
    </tbody>
</table>
</div>



- Then add the probabilities of all those events:



{:.input_area}
```python
event_table.column('Probability').sum()
```





{:.output .output_data_text}
```
0.6959876543209863
```



The `prob_event` method does all this in one step. Here it is again, for comparison.



{:.input_area}
```python
dist_S.prob_event(np.arange(14, 22, 1))
```





{:.output .output_data_text}
```
0.6959876543209863
```



You can use the same basic method in various ways to find the probability of any event determined by $S$. Here are two examples.

**Example 1.**
$$
P(S^2 = 400) = P(S = 20) = 8.37\%
$$
from the table above.

**Example 2.**
$$
P(S > 20) = \sum_{s=20}^{30} P(S = s)
$$

A quick way of finding the numerical value:



{:.input_area}
```python
dist_S.prob_event(np.arange(20, 31, 1))
```





{:.output .output_data_text}
```
0.30516975308642047
```



**Example 3.**
$$
P(\big{\vert} S - 10 \big{|} \le 6) ~ = ~ P(4 \le S \le 16) ~ = ~ \sum_{s=4}^{16} P(S=s)
$$



{:.input_area}
```python
dist_S.prob_event(np.arange(4, 17, 1))
```





{:.output .output_data_text}
```
0.39969135802469169
```


