## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: <Matthew Wiram>
import math


# The purpose of this function is to take user input of a number and calulate the summation of all numbers divisible by three
# input is the upper bound user inputted number
# output is the summation of all the numbers divisible by three less than or equal to said number
def sumOfThrees():
    upperBound = int(input(
        "Please give me a number and I will give the summation of numbers that are less than or equal to said number and multiples of 3: "))
    sum = 0
    for i in range(0, (upperBound + 1), 3):
        sum += i
    print("This is your summation ", sum)


# The purpose of the multiplication table is to create a table that solves 1x1 all the way to 12x12
# There is no user input for this one
# The output is a for loop inside a for loop ranging from 1 to 12 for both loops to achieve 1x1 to 12x12
def multiplicationTable():
    for i in range(1, 13):

        print(i, end=":    ")

        for j in range(1, 13):
            if (j  == 0):

                print(i,end="  ")
            else:
                print(i * j, end="    ")
        # print(i, "*", j, "=", i * j, end = "         ")
        print()


# The purpose of this function is to find the area of a triangle given its 3 sides
# input is three parameters relating to the length of three sides of a triangle
# output is the final product and root of using the three sides and area formula
def triangleArea():
    side1 = float(input("Give me the length for side 1"))
    side2 = float(input("Give me the length for side 2"))
    side3 = float(input("Give me the length for side 3"))
    # fixed the error for not having user inputs
    totalS = (side1 + side2 + side3) / 2
    finalProduct = totalS * (totalS - side1) * (totalS - side2) * (totalS - side3)
    area = math.sqrt(finalProduct)
    print(area)


# purpose of this function is to take user input of a lower range and upper range and find the summation of the numbers squared
# input is the two numbers given by a user a lower bound and an upper bound
# output is the total of the range between two numbers squared
def sumSquares():
    print(
        "Give me two numbers the upper range and lower range and I will give you the summation of numbers inbetween squared")
    lowerRange = int(input("Please give me a number for the lower range "))
    upperRange = int(input("Please give me a number for the upper range "))
    summation = 0
    for i in range(lowerRange, (upperRange + 1)):
        summation += (i ** 2)
    print(summation)


# fixed not printing error


# The purpose of this function is to do a manual power calculator using a for loop
# The input involved in this is to ask the user to give a base and power
# The output is the exponential value of the base and power
def power():
    print("Give me a base and an exponent(whole numbers only) and i will give you the total of said numbers")
    base = int(input("Give me your base "))
    power = int(input("Give me your exponent"))
    finalAnswer = 1
    for i in range(1, (power + 1)):
        finalAnswer *= base

    print(base, "^", power, "=", finalAnswer)


def helloWorld():
    print("Hello, world!")


def main():
    # helloWorld()
    # sumOfThrees()
    multiplicationTable()
    # triangleArea(3,3,5)
    # sumSquares()
    # power()


main()
