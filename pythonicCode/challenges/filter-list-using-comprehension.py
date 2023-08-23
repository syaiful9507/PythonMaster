# Challenge:
# Filter List Using Comprehension
# Easy
# Problem Description
# Create a program to create a list of odd numbers from a list of numbers using list comprehension.
#
# Create a list with the following data items 12, 17, 28, 19, 11, and assign it to the numbers variable.
# Create a new list and only print 17, 19, 11 (odd numbers) using list comprehension.
# Print newly created list.
# Example
# Expected Output
#
# [17, 19, 11]

numbers = [12, 17, 28, 19, 11]
odd_number = [n for n in numbers if n%2 != 0]
print(odd_number)