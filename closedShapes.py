import math


def main():
    numPrisms = int(input("How many prisms would you like the surface area and volume of? "))
    numCylinders = int(input("How many cylinders would you like the surface area and volume of "))
    for i in range(numPrisms):
        prism()
    for i in range(numCylinders):
        cylinder()

def prism():
    baseLW = float(input("What is the base length or width assuming that they are the same length? "))
    height = float(input("What is the height of the prism? "))
    surfaceArea = 4 * (baseLW * height) + 2 * (baseLW ** 2)
    volume = (baseLW ** 2) * height
    print("From your base of", baseLW, "and height of", height, "your surface is", surfaceArea, "and your Volume is :", volume)

def cylinder():
    radius = float(input("What is the radius of the cylinder? "))
    height = float(input("What is the height of the cylinder? "))
    surfaceArea = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
    volume = math.pi * (radius ** 2) * height
    print("From your radius of", radius, "and height of", height, "Your surface area is", surfaceArea, "and your volume is", volume)

main()