total = 0;
while True:
    n = int(input("Enter a Number : "))
    if n > 0:
        total = total + n
    elif n == 0:
        break
    else:
        continue
print('total is',total)
