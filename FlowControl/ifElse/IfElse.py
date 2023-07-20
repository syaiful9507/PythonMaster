student_grade = int(input("Enter Grade : "))
if student_grade >100:
    print("Invalid")
elif student_grade >= 50:
    print("Successfully")
    print("You passing Examination.")
else:
    print("Failed")


student_grade = int(input('Enter grade: '))

if student_grade > 100 or student_grade < 0:
    print('Invalid grade.')
if student_grade >= 50:   # elif is changed to if
    print('You passed.')
else:
    print('You failed.')
