'''


The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''
import itertools
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


primes=generatePrimeNumbers(10000)

print(primes)


print(len(primes))
#
# permutation=list(itertools.permutations(str(1234)))
# permutation=list(map(lambda x: ''.join(x), permutation))
#
# print(permutation)

for i in range(1000,10000):
    permutations = list(itertools.permutations(str(i)))
    permutations = list(map(lambda x: ''.join(x), permutations))
    counter=0
    prime_permutations=[]
    for permutation in permutations:
        permutation=int(permutation)
        if permutation in primes and permutation not in prime_permutations:
            counter+=1
            prime_permutations.append(permutation)

        if counter>=3:
            print(prime_permutations)
            break