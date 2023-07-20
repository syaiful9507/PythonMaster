person = {'name': 'SYAIFUL', 'age': 28}
print(person)
dict1 = {}
print(dict1)
dict2 = {1: 'one'}
print(dict2)

# contain three items
dict3 = {1: 10, 'greet': ['Hey', 'Hello'], 'one': 1}
print(dict3)
print(len(dict3))

# invalid dict (list cannot use as a key
# dict4 = {[1,2]:'hey'}
# print(dict4)
# invalid key (duplicate key)
dict5 = {1: 'one', 1: 'two', 1: 'three'}
print(dict5)
print(len(dict5))

# add item
student_info = {
    'name': 'SYAIFUL',
    'university': 'Binus University',
    'major': 'Computer Science', 'age': 28}
print(student_info)
student_info['name'] = 'Abizar Sarfraz Faizan Alansya'
print(student_info)
student_info['age'] = 12
print(student_info)
student_info['hobby'] = 'golf'
print(student_info)

# delet dict items
del student_info['hobby']
print(student_info)
# del student_info

# iterate a dict
for student in student_info:
    # print(student)
    print(f'key {student} value {student_info[student]}')

# check if a key exist
print('major' in student_info)
print('major' not in student_info)
print('name' in student_info)
print('score' in student_info)
print('score' not in student_info)

# dict method
print(student_info.get('name'))
print(student_info.get('namex'))
student_info.clear()
print(student_info)
student_info = dict3.copy()
print(student_info)

cubes = {'one': 1, 'two': 2, 'three': 3}
if 'two' in cubes:
    print(cubes['two'])

