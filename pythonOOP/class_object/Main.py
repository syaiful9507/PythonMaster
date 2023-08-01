class Main:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person_attributes(self, main1, main2):
        print(self.name, self.age)
        print(main1.name, main1.age)
        print(main2.name, main2.age)
main = Main('SUI', 10)
main1 = Main('KLH', 17)
main2 = Main('uuu', 67)

# calling method and set object as an arguments
main.print_person_attributes(main1, main2)

number = 2
print(dir(number))
result = number.__add__(5)
result2 = number.__mul__(5)
print(result)
print(result2)

# the id() function
print(id(number))
print(id(result))
x = 5
y = x
print(id(x), id(y))

# how do variable actually work
list1 = [1,2,3]
list2 = list1
list1.append(4)
print(list1)
print(list2)
list3 = list1.copy()
list1.append(6)
print(list1)
print(list3)
