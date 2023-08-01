# create class
class Student:
 
    # add method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False


# outside the class
# create object of Student
student1 = Student()
student1.name = 'SYAIFUL'
student1.score = 20

print(student1.name, student1.score, student1.check_pass_fail())

student2 = Student()
student2.name = 'ABIZAR'
student2.score = 100
print(student2.name, student2.score, student2.check_pass_fail())
