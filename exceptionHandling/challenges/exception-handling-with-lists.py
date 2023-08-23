# Challenge:
# Exception Handling With Lists
# Easy
# Problem Description
# Create a program to print the item present at a given index. If the index is out of bounds, print Wrong index.
#
# Create a list of four strings: 'BMW', 'Ferrari', 'Audi', 'Tesla'.
# Take an integer input from the user and store it in the index variable.
# Print the item present at that index.
# However, if the index is out of bounds, instead of showing the default error, print Wrong Index.
# Note: Use exception handling to solve this problem.
#
# Example
# Test Input
#
# 10
# Expected Output
#
# Wrong Index




# Replace ___ with your code

# create a try block
try:
    cars = ['BMW', 'Ferrari', 'Audi', 'Tesla']

    # take integer input
    index = int(input())

    # print the item from the cars list
    print(cars[index])
# create the except block
except:
    print('Wrong Index')