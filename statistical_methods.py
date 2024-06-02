import math
import numpy
import scipy




def dfgetter(n1, n2):
   return n1 + n2 -2


# pooled sigma
def pooledsigma(n1, n2, s1, s2):
    numerator = ((n1 - 1) * s1 ** 2) + ((n2 - 1) * s2 ** 2)
    denominator = n1 + n2 - 2
    print(math.sqrt(numerator/denominator))
    return math.sqrt(numerator / denominator)


# pooled t value
def tob(x1, x2, n1, n2, sigma):
    numerator = x1 - x2
    denominator = sigma * (math.sqrt((1 / n1) + (1 / n2)))
    return numerator / denominator


# pooled t crit value for invT(a,df)

def tcritval(a, df):
    if int(testtype) < 2:
         alpha = scipy.stats.t.ppf(1 - a, df)
         print(alpha)
         return alpha
    else:
        alpha = scipy.stats.t.ppf(1-(a/2),df)
        print(alpha)
        return alpha


# p value from plugging in tob to t.cdf(-100000000,-|tcrit|,0,1) equation for not equal to hypothesis
def pvalue(tcrit, df):
    if int(testtype) < 2:
        print(scipy.stats.t.cdf(tcrit,df))

    else:
        print(2 * (scipy.stats.t.cdf(-abs(tcrit), df)))


# sigmap = pooledsigma(30, 35, 23.95, 26.21)
# print(sigmap)
#
# tob1 = tob(64.98, 76.59, 30, 35, sigmap)
# print(tob1)
#
# tcritval(0.025, 63)
#
# pvalue(tob1, 63)

testtype = input("What kind of test is this? 0 = M0<MA, 1 = M0>MA, or 2 = M0 not equal MA ")
x1 = float(input("What is xbar1? "))
x2 = float(input("What is xbar2? "))
s1 = float(input("What is sigma1? "))
s2 = float(input("What is sigma2? "))
n1 = float(input("What is n1? "))
n2 = float(input("What is n2? "))
a = float(input("What is the confidence level? "))



df = dfgetter(n1,n2)
pooledS = pooledsigma(n1,n2,s1,s2)
tob = tob(x1,x2,n1,n2,pooledS)
pvalue(tob,df)
tcritval(a,df)
