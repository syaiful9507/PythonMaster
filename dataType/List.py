list1 = []
print(list1)
numbers = [1,2,3]
print(numbers)
mixed_list = [1,'hello', 4.6]
print(mixed_list)
print(type(mixed_list))
list2 = [1,2,3,1,3]
print(list2)
new_list2 = list2[3:5]
print(new_list2)

# omit start and end index
# omit start
print(list2[:2])
# omit end index
print(list2[2:])
# skip both
print(list2[:])
del list2[0]
print(list2)
# list method
list2.append(100)
print(list2)
numbers.extend(list2)
print(numbers)
numbers.insert(0, 10000)
print(numbers)
numbers.insert(3, 188888)
print(numbers)
new_number = numbers.copy()
print(new_number)
# nested list
list3 = [1,[2,3,4,5], 2]
print(list3)

fruits = ['strawberry','apple', 'orange']
for fruit in fruits:
    print('I like a',fruit)
if 'apple' in fruits:
    print('delicious')

check = 'kiwi' in fruits
print(check)
check = 'kiwi' not in fruits
print(check)

frontend_developers = ['Rob', 'Jane', 'Mary', 'Anne']
backend_developers = ['Jane', 'Jack', 'Lily']
both_developer = set(frontend_developers) & set(backend_developers)
print(list(both_developer))