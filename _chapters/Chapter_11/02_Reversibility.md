---
interact_link: notebooks/Chapter_11/02_Reversibility.ipynb
title: '11.2 Reversibility'
permalink: 'chapters/Chapter_11/02_Reversibility'
previouschapter:
  url: chapters/Chapter_11/01_Detailed_Balance
  title: '11.1 Detailed Balance'
nextchapter:
  url: chapters/Chapter_11/03_Code_Breaking
  title: '11.3 Code Breaking'
redirect_from:
  - 'chapters/chapter-11/02-reversibility'
---

## Reversibility

The reflecting random walk of the previous section has states 0, 1, 2, 3, 4 arranged in sequence clockwise on a circle. At each step the chain stays in place with probability $s$, moves to its clockwise neighbor with probability $r$ and to its counterclockwise neighbor with probability $p$. The stationary distribution of the chain assigns chance 0.2 to each state.

If $r > p$, then the chain is more likely to be moving clockwise than counterclockwise. For example, in steady state, the probability of the path $0, 1, 2, 3$ is

$$
P(X_0 = 0)P(0, 1)P(1, 2)P(2, 3) = 0.2r^3
$$

The probability of the *reversed* path $3, 2, 1, 0$ is

$$
P(X_0 = 3)P(3, 2)P(2, 1)P(1, 0) = 0.2p^3
$$

If $r > p$, then the original path has higher chance.

But if $r = p$, the chance of the original path is the same as that of the reversed path; in steady state, the chain is just as likely to be running in either direction. If someone simulates the chain in steady state and shows you the original path as well as the reversed path, you will not be able to tell which is which.

In this section we define what it means for a Markov Chain to be *reversible* in this way.

### Reversed Process
Let $X_0, X_1, \ldots $ be an irreducible Markov Chain with a finite state space and stationary distribution $\pi$. Start the chain off with this stationary distribution; that is, let $X_0$ have distribution $\pi$. Then for all $n \ge 1$, the distribution of $X_n$ is also $\pi$.

Fix $n > 0$ and consider the *reversed* sequence $Y_0, Y_1, \ldots, Y_n$ defined by $Y_k = X_{n-k}$ for $k = 0, 1, \ldots, n$. Call $X_0, X_1, \ldots, X_n$ the *forwards* sequence.

It is a wonderful fact that the reversed sequence is a time homogenous Markov Chain. To see why, we will check that the Markov property holds.

Before we prove the general fact, let's make some exploratory calculations. Start with $n = 1$, so that $Y_0 = X_1$ and $Y_1 = X_0$. For states $i$ and $j$.
$$
\begin{align*}
P(Y_1 = j \mid Y_0 = i) ~ &= ~ \frac{P(Y_1 = j, Y_0 = i)}{P(Y_0 = i)} \\
&= ~ \frac{P(X_0 = j, X_1 = i)}{P(X_1 = i)} \\
&= ~ \frac{\pi(j)P(j, i)}{\pi(i)}
\end{align*}
$$
because the forwards sequence is in steady state. We have found a transition probability for the reversed sequence using the transition matrix and stationary distribution of the forwards sequence.

For $n = 2$, we have $Y_0 = X_2$, $Y_1 = X_1$, and $Y_2 = X_0$. For states $k$, $i$, and $j$,
$$
\begin{align*}
P(Y_2 = j \mid Y_0 = k, Y_1 = i) ~ &= ~ \frac{P(Y_2 = j, Y_1 = i, Y_0 = k)}{P(Y_1 = i, Y_0 = k)} \\
&= ~ \frac{P(X_0 = j, X_1 = i, X_2 = k)}{P(X_1 = i, X_2 = k)} \\
&= ~ \frac{\pi(j)P(j, i)P(i, k)}{\pi(i)P(i, k)} \\
&= ~ \frac{\pi(j)P(j, i)}{\pi(i)}
\end{align*}
$$
The answer doesn't depend on $k$. That's consistent with the Markov property. Also, put together the two facts we have just proved to notice that the transition probabilities are time homogenous.

For general $n$, fix states $i$ and $j$ and an integer $m$ in the range 0 through $n-1$.
$$
\begin{align*}
& P(Y_{m+1} = j \mid Y_0 = i_0, Y_1 = i_1, \ldots, Y_{m-1} = i_{m-1}, Y_m = i) \\ \\ 
&=
\frac{P(Y_0 = i_0, Y_1 = i_1 \ldots, Y_{m-1} = i_{m-1}, Y_m = i, Y_{m+1} = j)}
{P(Y_0 = i_0, Y_1 = i_1 \ldots, Y_{m-1} = i_{m-1}, Y_m = i)} \\ \\
&= \frac{P(X_n = i_0, X_{n-1} = i_1, \ldots, X_{n-m+1} = i_{m-1}, X_{n-m} = i, X_{n-m-1} = j)}
{P(X_n = i_0, X_{n-1} = i_1, \ldots, X_{n-m+1)} = i_{m-1}, X_{n-m} = i)} \\ \\
&= \frac{\pi(j)P(j, i)P(i, i_{m-1}) \cdots P(i_1, i_0)}
{\pi(i)P(i, i_{m-1}) \cdots P(i_1, i_0)} \\ \\
&= \frac{\pi(j)P(j, i)}{\pi(i)}
\end{align*}
$$
This involves only $i$ and $j$, and not on $i_0, i_1, \ldots, i_{m-1}$ nor on $m$. So the Markov property is satisfied and the transition probabilities are time homogenous. The one-step "$i$ to $j$" transition probability for the reversed sequence is

$$
P(Y_1 = j \mid Y_0 = i) = \frac{\pi(j)P(j, i)}{\pi(i)}
$$

### Reversible Chains
The original "forwards" Markov Chain $X_0, X_1, \ldots $ is called *reversible* if for every $n$, the reversed sequence $Y_0, Y_1, \ldots Y_n$
has *the same one-step transition probabilities as the original*; that is, if

$$
\frac{\pi(j)P(j, i)}{\pi(i)} = P(i, j) ~~~ \text{for all } i, j
$$

That is, the chain is reversible if

$$
\pi(i)P(i, j) = \pi(j)P(j, i) ~~~ \text{for all } i, j
$$

In other words:

**The chain is reversible if the detailed balance equations have a positive solution.** This is consistent with our image of particles moving according to this chain in steady state: at each instant, the proportion of particles moving from $i$ to $j$ is exactly the same as the proportion moving from $j$ to $i$, for every pair of states $i$ and $j$. 

At the start of this section we looked at a random walk on a circle. Let's see what the definition of reversibility implies for this chain.

- In the previous section we showed that when $p \ne r$, the detailed balance equations have no positive solution. Therefore, when $p \ne r$, the chain is not reversible. This is consistent with our earlier analysis.

- When $p = r$, we found a solution to the detailed balance equations, and therefore the chain is reversible. This formalizes our idea that if $p = r$ then in steady state the chain "looks the same run forwards or backwards."

### Reversibility of Birth and Death Chains
Recall that a *birth and death chain* is a Markov Chain on the integers, with one-step transitions restricted to going up by 1, going down by 1, or staying in place. It is not hard to check that every irreducible birth and death chain with a finite state space is reversible. You can simply solve the detailed balance equations just as we did for the Ehrenfest chain in the previous section.

Go back and look through the examples in the text and exercises. The switching chains, the reflecting random walks (both lazy and not), both of the Ehrenfest chains, and the Bernoulli-Laplace chain are all irreducible birth and death chains, and hence are reversible.

Let's confirm this in the case of a birth and death chain which at first glance seems not to be reversible. Here is the transition diagram of a Markov Chain $X_0, X_1, \ldots $.

![B&D](trans_b_and_d.png)

This chain moves right (that is, has births) with high probability, so it seems as though we should be able to tell whether it's moving forwards or backwards. But remember that **time reversal happens in the steady state**. In the steady state, the chain is overwhelmingly likely to be shuttling between states 3 and 4. You can see this by solving the detailed balance equations.

$$
\begin{align*}
\pi(1)\cdot 1 &= \pi(2) \cdot 0.1 ~~~~ \implies \pi(2) = 10\pi(1)  \\
\pi(2) \cdot 0.9 &= \pi(3) \cdot 0.1 ~~~~ \implies \pi(3) = 90\pi(1) \\
\pi(3) \cdot 0.9 &= \pi(4) \cdot 1 ~~~~~~~ \implies \pi(4) = 81\pi(1)
\end{align*}
$$

It will visit states 2 and 1 as well, but rarely, state 1 being particularly rare. These vists will intersperse the sojourns in 3 and 4, and the paths will be indistinguishable forwards and backwards.

Let's simulate paths of this process. First, we construct the transition matrix and confirm our calculations of $\pi$.


{:.input_area}
```python
s = np.arange(1, 5)

def trans(i, j):
    if i == 1:
        if j == 2:
            return 1
        else:
            return 0
    elif i == 4:
        if j == 3:
            return 1
        else:
            return 0
    elif j == i+1:
        return 0.9
    elif j == i-1:
        return 0.1
    else:
        return 0

bnd = MarkovChain.from_transition_function(s, trans)
```


{:.input_area}
```python
pi = bnd.steady_state()
pi
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
            <td>1    </td> <td>0.00549451 </td>
        </tr>
        <tr>
            <td>2    </td> <td>0.0549451  </td>
        </tr>
        <tr>
            <td>3    </td> <td>0.494505   </td>
        </tr>
        <tr>
            <td>4    </td> <td>0.445055   </td>
        </tr>
    </tbody>
</table>
</div>



We can use `simulate_path` to plot a path of the chain. Notice that unlike our previous uses of this method, we are now passing an initial distribution as the first argument, not a particular state. The second argument is the number of steps, as before.

The graph below shows one path of length 200. Run the cell a few times and look at each path forwards as well as backwards. You won't find a systematic difference between the two. 


{:.input_area}
```python
plt.figure(figsize=(10,5))
n = 200                          # the number of steps
x = np.arange(n+1)               # the steps
y = bnd.simulate_path(pi, n, plot_path=True)    # the simulated state at each step

# Axis labels and title
plt.xlabel('$n$')
plt.ylabel('$X_n$', rotation=0)
plt.title('Reversibility: Path of Birth and Death Chain in Steady State');
```


![png]({{ site.baseurl }}/images/chapters/Chapter_11/02_Reversibility_10_0.png)

