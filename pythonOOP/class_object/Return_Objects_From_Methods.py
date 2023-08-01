class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def return_anoter_person(self):
        person = Person('S',11)
        return person
person1 = Person('A', 33)
another_person = person1.return_anoter_person()
print(another_person.name)
print(another_person.age)
