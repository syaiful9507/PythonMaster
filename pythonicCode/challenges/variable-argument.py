# Problem Description
# Write a program to create a function that can take a variable number of arguments and returns the product of numbers passed as arguments.
#
# Create a function named multiply_numbers() that can take any number of arguments (0 or more).
# Inside the function, calculate the product of numbers passed as arguments and return the result.
# Outside the function
#
# Take three integer inputs from the user.
# Call the multiply_numbers() function with these three integers and print the return value.
# Example
# Test Input
#
# 1
# 2
# 3
# Expected Output
#
# 6

# Replace ___ with your code

# create the function
def multiply_numbers(x, y, z):
    data = x * y * z
    return data

# get three integer inputs
n1 = int(input())
n2 = int(input())
n3 = int(input())

# call the function
result = multiply_numbers(n1,n2,n3)

# print the result
print(result)