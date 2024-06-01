import math
import numpy
import scipy
# pooled sigma
def pooledsigma(n1,n2,s1,s2):
    numerator = ((n1-1)*s1**2)+((n2-1)*s2**2)
    denominator = n1 + n2 - 2
    return math.sqrt(numerator/denominator)
# pooled t value
def tob(x1,x2,n1,n2,sigma):
    numerator = x1-x2
    denominator = sigma * (math.sqrt((1/n1)+(1/n2)))
    return numerator/denominator
# pooled t crit value

def tcritval(a,df):
    alpha = scipy.stats.t.ppf(1-a,df)
    print (alpha)

# p value from plugging in tob to t.cdf equation for not equal to hepothesis
def pvaluenotequal(tcrit,df):
    print (2*(scipy.stats.t.cdf(tcrit,df)))

sigmap = pooledsigma(30,35,23.95,26.21)
print (sigmap)

tob1 = tob(64.98,76.59,30,35,sigmap)
print (tob1)

tcritval(0.025,63)

pvaluenotequal(tob1,63)