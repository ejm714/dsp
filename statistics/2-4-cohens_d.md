[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Problem: Determine whether first babies are lighter or heavier than others. This is a mean difference. Then compare the difference between groups to the variability within groups (i.e. Cohen's d).

``` python
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# mean difference
print('First babies weigh on average %f lbs' % firsts.totalwgt_lb.mean())

print('Non-first borns weight on average %f lbs' % others.totalwgt_lb.mean() )

# Cohen's d
diff = firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
var1 = firsts.totalwgt_lb.var()
var2 = others.totalwgt_lb.var()
n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)
pooled_var = (n1*var1 + n2*var2)/(n1+n2)
d = diff / math.sqrt(pooled_var)
print(d)

# alternate way
import thinkstats2
cohen_d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

```

First babies are lighter by .12 pounds. The difference between first borns and others is -.09 standard deviations. This difference in weight is greater than that of pregnancy length.
