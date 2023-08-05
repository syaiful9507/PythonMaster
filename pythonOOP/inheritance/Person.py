class Person:
    def __init__(self):
        name = input('Enter Your Name : ')
        age = input('Enter Your Age : ')
        self.name = name
        self.age = age
    def display_info(self):
        print(f'Nama : {self.name}')
        print(f'Age : {self.age}')

class Student(Person):
    def __init__(self, student_id):
        self.id = student_id
        super().__init__()
    def display_info(self):
        print(f'id : {self.id}')
        super().display_info()

s1 = Student(2)
s1.display_info()
