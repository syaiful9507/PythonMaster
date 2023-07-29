def print_number(n):
    print(n)
    if n < 100:
        print_number(n+1)


print_number(1)