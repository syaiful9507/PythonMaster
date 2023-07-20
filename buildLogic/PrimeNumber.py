number = int(input("Enter a number : "))
is_prime = True

for i in range(2, number):
    if (number % i) == 0:
        is_prime = False
        break
if is_prime:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')


def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


for n in range(50, 101):
    check_primes = check_prime(n)
    if check_primes:
        print(n)
