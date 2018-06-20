---
interact_link: notebooks/Chapter_24/01_Bivariate_Normal_Distribution.ipynb
title: '24.1 Bivariate Normal Distribution'
previouschapter:
  url: chapters/Chapter_24/00_Simple_Linear_Regression
  title: 'Chapter 24: Simple Linear Regression'
nextchapter:
  url: chapters/Chapter_24/02_Linear_Least_Squares
  title: '24.2 Least Squares Linear Predictor'
---

## Bivariate Normal Distribution ##

The multivariate normal distribution is defined in terms of a mean vector and a covariance matrix. The units of covariance are often hard to understand, as they are the product of the units of the two variables.

Normalizing the covariance so that it is easier to interpret is a good idea. As you have seen in exercises, for jointly distributed random variables $X$ and $Y$ the *correlation* between $X$ and $Y$ is defined as

$$
r_{X,Y} ~ = ~ \frac{Cov(X, Y)}{\sigma_X\sigma_Y} ~ = ~ 
E\Big{(}  \frac{X-\mu_X}{\sigma_X}  \cdot \frac{Y-\mu_Y}{\sigma_Y}  \Big{)}
~ = ~ E(X^*Y^*)
$$

where $X^*$ is $X$ in standard units and $Y^*$ is $Y$ in standard units.

#### Properties of Correlation ####
You showed all of these in exercises.

- $r_{X,Y}$ depends only on standard units and hence is a pure number with no units
- $r_{X,Y} = r_{Y,X}$
- $-1 \le r_{X,Y} \le 1$ 
- If $Y = aX + b$ then $r_{X,Y}$ is $1$ or $-1$ according to whether the sign of $a$ is positive or negative. 

We say that $r_{X,Y}$ measures the *linear association* between $X$ and $Y$. 

#### Variance of a Sum ####
Rewrite the formula for correlation to see that 
$$
Cov(X, Y) ~ = ~ r_{X,Y}\sigma_X\sigma_Y
$$
So the variance of $X+Y$ is
$$
\sigma_{X+Y}^2 ~ = ~ \sigma_X^2 + \sigma_Y^2 + 2r_{X,Y}\sigma_X\sigma_Y
$$

Notice the parallel with the formula for the length of the sum of two vectors, with correlation playing the role of the cosine of the angle between two vectors. If the angle is 90 degrees, the the cosine is 0. This corresponds to correlation being zero and hence the random variables being uncorrelated. 

We will visualize this idea in the case where the joint distribution of $X$ and $Y$ is bivariate normal.

### Standard Bivariate Normal Distribution ###
Let $X$ and $Z$ be independent standard normal variables, that is, bivariate normal random variables with mean vector $\mathbf{0}$ and covariance matrix equal to the identity. Now fix a number $\rho$ (that's the Greek letter rho, the lower case r) so that $-1 < \rho < 1$, and let

$$
\mathbf{A} ~ = ~ 
\begin{bmatrix}
1 & 0 \\
\rho & \sqrt{1 - \rho^2}
\end{bmatrix}
$$

Define a new random variable $Y = \rho X + \sqrt{1-\rho^2}Z$, and notice that

$$
\begin{bmatrix}
X \\
Y
\end{bmatrix} 
~ = ~
\begin{bmatrix}
1 & 0 \\
\rho & \sqrt{1 - \rho^2}
\end{bmatrix}
\begin{bmatrix}
X \\
Z
\end{bmatrix}
~ = ~ 
\mathbf{A}
\begin{bmatrix}
X \\
Z
\end{bmatrix}
$$

So $X$ and $Y$ have the bivariate normal distribution with mean vector $\mathbf{0}$ and covariance matrix

$$
\mathbf{AIA}^T ~ = ~ 
\begin{bmatrix}
1 & 0 \\
\rho & \sqrt{1 - \rho^2}
\end{bmatrix}
\begin{bmatrix}
1 & \rho \\
0 & \sqrt{1 - \rho^2}
\end{bmatrix}
~ = ~ 
\begin{bmatrix}
1 & \rho \\
\rho & 1
\end{bmatrix}
$$

We say that $X$ and $Y$ have the *standard bivariate normal distribution with correlation $\rho$*.

The graph below shows the empirical distribution of 1000 $(X, Y)$ points in the case $\rho = 0.6$. You can change the value of $rho$ and see how the scatter diagram changes. It will remind you of numerous such simulations in Data 8.


{:.input_area}
```python
# Plotting parameters
plt.figure(figsize=(5, 5))
plt.axes().set_aspect('equal')
plt.xlabel('$X$')
plt.ylabel('$Y$', rotation=0)
plt.xticks(np.arange(-4, 4.1))
plt.yticks(np.arange(-4, 4.1))

# X, Z, and Y
x = stats.norm.rvs(0, 1, size=1000)
z = stats.norm.rvs(0, 1, size=1000)
rho = 0.6
y = rho*x + np.sqrt((1-rho**2))*z
plt.scatter(x, y, color='darkblue', s=10);
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_3_0.png)


### Correlation as a Cosine ###
We have defined

$$
Y ~ = ~ \rho X + \sqrt{1 - \rho^2} Z
$$
where $X$ and $Z$ are i.i.d. standard normal.

Let's understand this construction geometrically. A good place to start is the joint density of $X$ and $Z$, which has circular symmetry.

The $X$ and $Z$ axes are orthogonal. Let's see what happens if we twist them. 

Take any positive angle $\theta$ degrees and draw a new axis at angle $\theta$ to the original $X$ axis. Every point $(X, Z)$ has a *projection* onto this axis. 

The figure below shows the projection of the point $(X, Z) = (1, 2)$ onto the gold axis which is at an angle of $\theta$ degress to the $X$ axis. The blue segment is the value of $X$. You get that by dropping the perpendicular from $(1, 2)$ to the horizontal axis. That's called *projecting* $(1, 2)$ onto the horizontal axis. 

The red segment is the projection of $(1, 2)$ onto the gold axes, obtained by dropping the perpendicular from $(1, 2)$ to the gold axis.

Vary the values of $\theta$ in the cell below to see how the projection changes as the gold axis rotates.


{:.input_area}
```python
theta = 20
projection_1_2(theta)
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_6_0.png)


Let $Y$ be the length of the red segment, and remember that $X$ is the length of the blue segment. When $\theta$ is very small, $Y$ is almost equal to $X$. When $\theta$ approaches 90 degrees, $Y$ is almost equal to $Z$.

A little trigonometry shows that $Y ~ = ~ X \cos(\theta) + Z\sin(\theta)$.


{:.input_area}
```python
projection_trig()
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_8_0.png)


Thus
$$
Y ~ = ~ X\cos(\theta) + Z\sin(\theta) ~ = ~ \rho X + \sqrt{1 - \rho^2}Z
$$
where $\rho = \cos(\theta)$.

The sequence of graphs below illustrates the transformation for $\theta = 30$ degrees.


{:.input_area}
```python
theta = 30
projection_1_2(theta)
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_10_0.png)


The bivariate normal distribution is the joint distribution of the blue and red lengths $X$ and $Y$ when the original point $(X, Z)$ has i.i.d. standard normal coordinates. This transforms the circular contours of the joint density surface of $(X, Z)$ into the elliptical contours of the joint density surface of $(X, Y)$. 


{:.input_area}
```python
cos(theta), (3**0.5)/2
```




{:.output_data_text}
```
(0.86602540378443871, 0.8660254037844386)
```




{:.input_area}
```python
rho = cos(theta)
Plot_bivariate_normal([0, 0], [[1, rho], [rho, 1]])
plt.title('Standard Bivariate Normal Distribution, Correlation = '+str(round(rho, 2)));
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_13_0.png)


### Small $\theta$ ###

As we observed earlier, when $\theta$ is very small there is hardly any change in the position of the axis. So $X$ and $Y$ are almost equal. 


{:.input_area}
```python
theta = 2
projection_1_2(theta)
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_15_0.png)


The bivariate normal density of $X$ and $Y$, therefore, is essentially confined to the $X = Y$ line. The correlation $\cos(\theta)$ is large because $\theta$ is small; it is more than 0.999. 

You can see the plotting function having trouble rendering this joint density surface.


{:.input_area}
```python
rho = cos(theta)
rho
```




{:.output_data_text}
```
0.99939082701909576
```




{:.input_area}
```python
Plot_bivariate_normal([0, 0], [[1, rho], [rho, 1]])
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_18_0.png)


### Orthogonality and Independence ###
When $\theta$ is 90 degrees, the gold axis is orthogonal to the $X$ axis and $Y$ is equal to $Z$ which is independent of $X$.


{:.input_area}
```python
theta = 90
projection_1_2(theta)
```


![png]({{ site.baseurl }}/images/chapters/Chapter_24/01_Bivariate_Normal_Distribution_20_0.png)


When $\theta = 90$ degrees, $\cos(\theta) = 0$. The joint density surface of $(X, Y)$ is the same as that of $(X, Z)$ and has circular symmetry.

If you think of $\rho X$ as a "signal" and $\sqrt{1-\rho^2}Z$ as "noise", then $Y$ can be thought of as an observation whose value is "signal plus noise". In the rest of the chapter we will see if we can separate the signal from the noise.

### Representations of the Bivariate Normal ###
When we are working with just two variables $X$ and $Y$, matrix representations are often unnecessary. We will use the following three representations interchangeably.

- $X_1$ and $X_2$ are bivariate normal with parameters $(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$
- The standardized variables $X_1^*$ and $X_2^*$ are standard bivariate normal with correlation $\rho$. Then $X_2^* = \rho X_1^* + \sqrt{1-\rho^2}Z$ for some standard normal $Z$ that is independent of $X_1^*$. This follows from Definition 2 of the multivariate normal.
- $X_1$ and $X_2$ have the multivariate normal distribution with mean vector $[\mu_1 ~ \mu_2]^T$ and covariance matrix

$$
\begin{bmatrix}
\sigma_1^2 & \rho\sigma_1\sigma_2 \\
\rho\sigma_1\sigma_2 & \sigma_2^2
\end{bmatrix}
$$
