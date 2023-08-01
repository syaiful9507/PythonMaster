class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_persoon_attributes(self, person):
        print(self.name, self.age)
        print(person.name, person.age)

# create object
person1 = Person('A', 18)

# create another object
person2 = Person('B', 28)

# calling print_persoon_attributes() using person1 object
# person2 is used as an argument
person1.print_persoon_attributes(person2)
