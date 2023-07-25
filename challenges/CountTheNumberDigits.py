# Replace ___ with your code

number = int(input())

count = 0

# run loop as long as number != 0
while number != 0:
    # divide number by 10
    number = number // 10

    # increase count by 1
    count = count + 1

# print count
print(count)