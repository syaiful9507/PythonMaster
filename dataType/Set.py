animal = {'girafe', 'cat'}
print(animal)
mixed_set = {4, 'lion', 3.6}
print(mixed_set)
numbers = {1, 2, 3, 4, 5, 1, 3, 6}
print(numbers)
# empty set
my_set = set()
print(my_set)

# add set item
numbers2 = {1, 2}
print(numbers2)
numbers2.add(100)
print(numbers2)

# update set
numbers.update(numbers2)
print(numbers)

# remove item of set
numbers.discard(100)
print(numbers)
print(3 in numbers)
print(3 not in numbers)
print(100 not in numbers)
domestic_animal = {'cat', 'chicken', 'elephant'}
wild_animal = {'lion', 'tiger', 'elephant'}
# set operator (union)
new_animal = domestic_animal | wild_animal
print(new_animal)
# set operator (intersection)

new_animal = domestic_animal & wild_animal
print(new_animal)

