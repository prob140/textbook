---
interact_link: notebooks/Chapter_20/00_Approaches_to_Estimation.ipynb
title: 'Chapter 20: Approaches to Estimation'
previouschapter:
  url: chapters/Chapter_19/04_Chernoff_Bound
  title: '19.4 Chernoff Bound'
nextchapter:
  url: chapters/Chapter_20/01_Maximum_Likelihood
  title: '20.1 Maximum Likelihood'
---

# Approaches to Estimation #

In Data 8 we defined a *parameter* to be a number associated with a population or with a distribution in a model. In all of the inference we have done so far, we have assumed that a parameter is a fixed number, possibly unknown. We have developed methods of estimation that attempt to capture an unknown fixed parameter in a confidence interval based on the data in random draws from the population.

We will start this chapter by developing a general method that allows us to come up with good estimates of fixed parameters. Essentially, it looks among all the possible values of the parameter and picks the one that maximizes the chance of getting the observed sample.

But there is another way of thinking about unknown parameters. Instead of imagining them as fixed, we can think of them as random; the randomness is due to our own degree of uncertainty about the parameters. For example, if we think that the chance that a kind of email message is a phishing attempt is somewhere around 70%, then we can imagine the chance itself to be random, picked from a distribution that puts much of its mass around 70%.

Once we have gathered data about various kinds of email messages and whether or not they are phishing attempts, we can update our belief based on the data. We can represent this updated opinion as a distribution calculated by Bayes' Rule after the data have been collected. 

In this chapter we will set out the basic terminology and method of this way of updating our opinion about a parameter. We will then make connections between the results of the two approaches.
