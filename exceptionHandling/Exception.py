try:
    numerator = int(input("Enter numerator : "))
    denominator = int(input("Enter denominator : "))
    result = numerator / denominator
    print(result)

    my_list = [1, 2, 3]
    index = int(input("Enter index : "))
    print(my_list[index])
except ZeroDivisionError:
    print("Denominator cannot be 0, Try again")
except IndexError:
    print("Index is wrong")
finally:
    print('Always Printed')

total = 18+36+8+91+10
print(total)