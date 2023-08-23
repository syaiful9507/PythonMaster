# create the Animal class
class Animal:
    def eat(self):
        print('I can eat food')

# create the Dog class
class Dog(Animal):
    def bark(self):
        print('I can bark')
# create an object of Dog
dog = Dog()
# call the eat() method using the object
dog.eat()