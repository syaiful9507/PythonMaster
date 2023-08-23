# Problem Description
# Create a program to print the value present at the given key. If the key is out of bounds, print Key is not available.
#
# Create a dictionary of three items: {'Nepal' : 'Kathmandu', 'Sweden' : 'Stockholm', 'Italy' : 'Rome'}
# Take string input from the user and store it in the key variable.
# Print the value present at that key if the key is present in the dictionary.
# However, if the key is not in the dictionary, print Key is not available.
# Note: Use exception handling to solve this problem.
#
# Example
# Test Input
#
# Japan
# Expected Output
#
# Key is not available


# create a try block
try:
    countries = {'Nepal': 'Kathmandu', 'Sweden': 'Stockholm', 'Italy': 'Rome'}

    # take string input
    key = input()

    # print the value present at key
    print(countries[key])
# create the except block
except:
    print('Key is not available')
