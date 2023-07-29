def display_name(name, age):
    print(f'name is {name}')
    print(f'age is {age}')


display_name(age=23, name='SYAIFUL')



# Default argument
def greet(message='Helo'):
    print(message)


greet()


def display(symbol='*', number=5):
    print(f'Symbol = {symbol}')
    print(f'Number = {number}')

display()
display('#')
display('%', 100)
display(number=1000)

# Default Arguments in print()
print('Hello', 'Guys')
print('Hello', 'Guys', sep='#')