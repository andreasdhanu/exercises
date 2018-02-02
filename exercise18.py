'''


It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''
import math


def generatePrimeNumbers(limit):
    primes = []
    num = 2
    check = True
    while num < limit:
        for i in range(2, num):
            check = True
            if num % i == 0:
                check = False
                break
        if check:
            primes.append(num)
        num += 1
    return (primes)


limit_prime = 1000000
primes = generatePrimeNumbers(limit_prime)


def checkOddComposite(num):
    if num % 2 == 0 or num in primes:
        return False
    else:
        return True


composites = []
for i in range(2, limit_prime):
    if checkOddComposite(i):
        composites.append(i)

# print(composites)
found = True
for composite in composites:
    for prime in primes:
        if prime > composite:
            break
        tmp = composite
        tmp -= prime
        tmp /= 2
        if str(math.sqrt(tmp)).split('.')[1] == '0':
            print(composite)
            found = True
            break
    if not found:
        print("error " + str(composite))
        break
