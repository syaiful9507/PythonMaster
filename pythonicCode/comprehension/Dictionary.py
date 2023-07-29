numbers = [1, 2, 3, 4]
square_number = {number:number**2 for number in numbers}
print(square_number)

# with condition
numbers = [1, 2, 3, 4]
square_number = {number:number**2 for number in numbers if number > 1}
print(square_number)