#!/usr/bin/env python
# coding: utf-8

# # Variance Via Covariance #

# Additivity is a principal property of expectation. We have used it frequently to find expectation by writing the random variable as a sum of random variables whose expectation we know or can calculate. In this chapter we will study the variance of a sum of random variables. Unlike expectation, variance is not always additive. To deal with this, we will introduce the concept of *covariance*.
# 
# It is worth taking some time to understand how sample sums behave, because many interesting random variables like counts of successes can be written as sums. Binomial and hypergeometric random variables are such sums. Also, the mean of a random sample is a straightforward function of the sample sum, and you have seen that random sample means are good estimators of population means. 
