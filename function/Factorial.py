def compute_factorial(n):
    total = 1
    for i in range(1, n+1):
        total = total * i
    return total
number = int(input())
total = compute_factorial(number)
print(total)