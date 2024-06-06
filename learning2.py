# from tabulate import tabulate
#
# # assign data
# mydata = [
#     ["Nikhil", "Delhi"],
#     ["Ravi", "Kanpur"],
#     ["Manish", "Ahmedabad"],
#     ["Prince", "Bangalore"]
# ]
#
# # create header
# head = ["Name", "City"]
#
# # display table
# print(tabulate(mydata, headers=head, tablefmt="grid"))
import math
import fractions
# print(fractions.Fraction(math.sin(45)).limit_denominator())
# print (fractions.Fraction(math.sin(45*math.pi/180)).limit_denominator())
def fahrconverter(x):
    fahrenheit = (x * (9/5)) +32
    print(fahrenheit)
fahrconverter(100)
def celconverter(x):
    celsius= (x - 32) * (5/9)
    print(celsius)
celconverter(212)