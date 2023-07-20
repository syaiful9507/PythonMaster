for i in range(1, 6):
    print(i)
    break
print('outside the loop')


total = 0
while True:
    n = int(input("Enter a number : "))
    total = total + n
    print(n)
    if n == 0:
        break
print('Total is ',total)
print('outside the loop')
