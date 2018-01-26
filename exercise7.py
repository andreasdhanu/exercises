'''


There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr =
n!
r!(n−r)!
	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

'''
import math

def combinatoric(n, r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

counter=0
for i in range(1,101):
    for j in range(1,i):
        combinatoric_value=combinatoric(i,j)
        if combinatoric_value<=1000000:
            continue

        print(i,j,combinatoric_value)
        counter+=1

print(counter)
