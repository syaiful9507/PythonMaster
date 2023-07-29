def calculate_factorial(n):
    if n != 1:
        return n * calculate_factorial(n - 1)
    return n


n = int(input())
result = calculate_factorial(n)
print(result)
