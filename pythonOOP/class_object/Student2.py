class Student2:
    # adding the __init__() method
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def check_fail_pass(self):
        if(self.score >= 40):
            return True
        else:
            return False

# create object of the Student2
student2 = Student2("SYAIFUL", 90)
print(student2.name, student2.score, student2.check_fail_pass())