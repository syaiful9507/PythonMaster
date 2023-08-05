# base class
class Animal:
    def eat(self):
        print('I can eat')


# the Dog Class is derived from Animal
# notice Animal inside()
class Dog(Animal):
    def bark(self):
        print('I can bark')
class Cat(Animal):
    def get_grumpy(self):
        print('i am getting grumpy')


# create object of the Dog class
dog = Dog()

# call the function of the Animal class in object Dog class
dog.eat()
# call the function of the Dog class from object dog class
dog.bark()

animal = Animal()
animal.eat()

# object of the Cat class
cat = Cat()
cat.get_grumpy()
cat.eat()
