marks = int(input())
if marks < 0 or marks > 100:
    print('invalid')
elif marks > 40:
    print('Pass')
else:
    print('Fail')