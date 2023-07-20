# list to set
name = [1, 2, 3.5]
result = set(name)
print(result)

# string to set
result = set('wulan')
print(result)

# tuple to set
name = ('cat', 'chicken', 'horse')
print(name, type(name))
result = set(name)
print(result, type(result))

numbers = [1, 2, 3, 3, 4, 4, 5, 65, 5657, 43, 24, 7, 56, 86, 5, 8, 96, 4, 562, 56, 7, 4, 67, 46, 4]
print(numbers, type(numbers))
numbers = list(set(numbers))
print(numbers)
