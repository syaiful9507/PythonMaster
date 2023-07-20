# create a function
def salam(name, n1):
    print('assalamualaikum', name, n1)


# call a function
salam('SYAIFUL', 1000)
print('Hello')
salam('ABIZAR', 9)


def compute_sum(number):
    total = 0
    # iterate loop from 1 to number
    for i in range(1, number + 1):
        total = total + i
    return total


total = compute_sum(10)
print(total)
total = compute_sum(100)
print(total)

scores = [1, 2, 5, 2]
count = len(scores)
print(count)
sum = sum(scores)
print(sum)