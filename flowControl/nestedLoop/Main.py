attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attributes:
    for car in cars:
        print(attribute, car)
    print('---------')

for i in range(3):
    for j in range(5):
        print(i, j)
    print('--------')

name = 'python'
for i in range(10):
    print(name[:i])
