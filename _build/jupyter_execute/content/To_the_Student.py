# HIDDEN
from datascience import *
from prob140 import *
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np

# To the  Student #

Data science is about making conclusions based on large amounts of data of diverse forms. But most data sets, no matter how large or complex, provide only incomplete information about the questions that interest us. When data scientists make conclusions, they often have to account for uncertainty.

Probability theory studies the nature of randomness and gives us ways to quantify uncertainty. For example, it helps explain a phenomenon familiar to you from Data 8: that large random samples can hold rich stores of information about unknown quantities. Data scientists can use this to make valid conclusions about those unknowns, in spite of the uncertainties inherent in sampling.

In a way this seems contradictory. The word "random", as it is commonly used, conjures up an image of haphazardness: all mixed up and higgledy piggledy. How can randomness help us make sense of anything?

In the Fall 2015 inaugural offering of Data 8, this question was raised by a student who posted a request anonymously in the online discussion forum.

> Would someone please explain why this is: Using **Randomness** in **Inference** allows us to understand how "sure" we may be of an answer.

This insightful question received a prompt and equally insightful answer from another anonymous student.

> When you use randomness many times and see a similar pattern, it becomes easier to make an inference about the data.

Patterns in randomness – that's what this course is about. We will discover such patterns, generate them, use them, and most of all, enjoy them.

Welcome to Prob140.

*Berkeley, 2017*