my_list = [1, 2, 3, 4]
reverse = []
for i in range(1, len(my_list)+1):
    reverse.append(my_list[-i])
print(reverse)