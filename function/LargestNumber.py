def find_largest_number(n1, n2, n3):
    result = 0
    if n1 > n2 and n1 > n3:
        result = n1
    elif n2 > n3:
        result = n2
    else:
        result = n3
    return result

n1 = int(input())
n2 = int(input())
n3 = int(input())

result = find_largest_number(n1,n2,n3)
print(result)