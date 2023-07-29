def greet(*message):
    print(message, type(message))


greet()
greet('Hi')
greet('Hi', 'Hello')
greet(1, 2, 3, 4)


# add number
def add_number(*number):
    total = 0
    for numbers in number:
        total = total + numbers
    return total

# function call
result = add_number(1, 2, 3, 4, 4)
print(result)
result = add_number(100, 3, 34, 3, 34, 34, 34, 34, 32, 24, 242, 5, 36, 46, 46, 4, 35, 3525, 347, 58, 6, 85747)
print(result)

print('\n')
# **kwargs
# It's also possible to pass a variable number of keyword arguments in Python.
# To accept these arguments in the function definition, we use ** before the argument name.

def print_info(**person):
    print(person, type(person), sep=' = ')

print_info()
print_info(name= 'SYAIFUL')
print_info(name = 'ABIZAR', Univ = 'Harvard', age = 20)

def test(**data):
    my_data = data
    return data

list_data = test(satu = 'one', dua = 'two', tiga = 'three')
for list in list_data:
    print(list_data[list])


