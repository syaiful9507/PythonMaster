# Challenge:
# Create a Dictionary
# Easy
# Problem Description
# Create a program to create a dictionary using dictionary comprehension.
#
# Create a list with the following data items 1, 2, 3, 4, and assign it to the numbers variable.
# Create a new dictionary using comprehension where the keys are items of the list, and their corresponding values are equal to key+1.
# Print the dictionary.
# Example
# Expected Output
#
# {1: 2, 2: 3, 3: 4, 4: 5}

# Replace ___ with your code

numbers = [1, 2, 3, 4]
# create the dictionary using comprehension
dictionary = {number:number+1 for number in numbers }
# print the dictionary
print(dictionary)