# Problem Description
# Create a program to find the cube of a number using a lambda function.
#
# Create the lambda function and assign it to a variable named num_cube.
# Take one integer input and assign it to number.
# Call the lambda function with number as argument and print the result.
# Example
# Test Input
#
# 2
# Expected Output
#
# 8

num_cube = lambda number: number**3
numbers = int(input())
print(num_cube(numbers))