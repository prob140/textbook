# Markov Chain Monte Carlo #

What do stock markets, mutating viruses, and computer search engines have in common? They have all been analyzed using Markov Chain models. Understanding the long run behavior of Markov Chains helps us understand many different random phenomena.

In data science, Markov Chains are also used for quite a different purpose. Markov Chains help data scientists draw random samples from distributions that are too complicated for standard sampling methods to handle. Markov Chains can also be used to approximate expectations of random quantities whose distributions are either very complicated or involve unknown quantities that are too difficult to estimate using standard methods.

Sometimes, this can be achieved by creating a Markov Chain that has the complicated distribution as its stationary distribution, and then running the chain for a long time till it gets close to stationarity. This method is called Markov Chain Monte Carlo, abbreviated to MCMC.




```{toctree}
:hidden:
:titlesonly:


01_Balance_and_Detailed_Balance
02_Code_Breaking
03_Metropolis_Algorithm
04_Exercises
```
