# Replace ___ with your code

# create the function
def multiply_numbers(list):
    data = 1
    for i in list:
        data = data *i
    return data

# get three integer inputs
n1 = int(input())
n2 = int(input())
n3 = int(input())

# call the function
result = multiply_numbers([n1,n2,n3])

# print the result
print(result)