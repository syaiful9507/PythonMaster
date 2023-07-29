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
student1.name = 'SYAIFU'
student1.score = 100

print(student1.name)
print(student1.score)

passorfail = student1.check_pass_fail()
print(passorfail)
