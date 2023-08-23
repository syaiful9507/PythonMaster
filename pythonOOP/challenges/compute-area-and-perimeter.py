# Challenge:
# Compute Area and Perimeter
# Medium
# Problem Description
# Create a program to compute the area and perimeter of a square using class. If you don't know, a square is a rectangle with equal sides.
#
# Create a class
#
# Create a class named Square that has an attribute named length.
# Use __init__() to initialize the length attribute.
# Create the compute_area() method to compute the area of a square and return it.
# Create the compute_perimter() method to compute the perimeter of a square and return it.
# Outside the class
#
# Take integer input from the user and store it in the length variable.
# Create an object of the Square class by passing length as an argument.
# Call the compute_area() method and print the area.
# Call the compute_perimeter() method and print the perimeter.
# By the way, the area of a square is equal to length * length, and the perimeter of a square is equal to 4 * length.
#
# Example
# Test Input
# 2
# Expected Output
# 4
# 8




class Square:
    # define the __init__() method
    def __init__(self, lenght):
        self.length = lenght

    # define the compute_area() method
    def compute_area(self):
        area = self.length * self.length
        return area

    # define the compute_perimeter() method
    def compute_perimeter(self):
        perimeter = 4 * self.length
        return perimeter

# get integer input
lenght = int(input())

# create an object of Square
square = Square(lenght)
# call compute_area() and print the area
print(square.compute_area())
# call compute_perimeter() and print the perimeter
print(square.compute_perimeter())