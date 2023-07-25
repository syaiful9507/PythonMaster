string1 = input()
character = input()
count = 0
for i in string1:
    if i.lower() == character.lower():
        count = count + 1
print(count)
