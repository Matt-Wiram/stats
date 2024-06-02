# plist = [1,2,3,4,5]
# pstring = "onomonopoeia"
# print (plist[1:4])
# if 6 in plist:
#     print ("cherry")
# else:
#     print ("taco")
# for x in plist:
#     print (x)
# for x in pstring:
#     print (x)
# print(len(pstring))
import scipy

# x = [0]
# def fibonacci():
#
#     while len(x) < 30:
#          if len(x) == 1:
#              x.append(1)
#              print (x)
#          else:
#             x.append(x[-1] + x[-2])
#             print(x)
#
# def kiloToMiles(x):
#     return x * 0.62137119
#
# def milesToKilo(x):
#     return x /  0.62137119
#
# print (kiloToMiles(3))
#
# print (milesToKilo(1.8641135699999998))
#
# def triarea(l,w):
#     return (l*w)/2
# print (triarea(3,5))
#
# name = input("What is your name? ")
# print ("Hello " + name)

print(scipy.stats.ttest_ind_from_stats(64.98,23.95,30,76.59,26.21,35,True,"two-sided"))