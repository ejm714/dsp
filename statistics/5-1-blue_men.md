[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Problem: Determine the number of U.S. males between two heights. Solve this by defining a normal distribution according to the mean and standard deviation given, and then find the difference between the CDFs at these two heights (as each CDF gives the share of population below that height).

```python

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

x = dist.cdf(185.42) - dist.cdf(177.8)

print('%f percent of the U.S. male population is between 5’10” and 6’1.”' % (x*100))
```

34.274684 percent of the U.S. male population is between 5’10” and 6’1.”
