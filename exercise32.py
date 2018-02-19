'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
max=int(28123/2)


abundants=[]
for number in range(1, max):
    sum = 0
    divisors = []
    for i in range(1,number):
        if number%i==0:
            divisors.append(i)
            sum+=i
    if number < sum:
        abundants.append(number)

print(abundants)
abundant_sums=[]
for abundant in abundants:
    for abundant2 in abundants:
        abundant_sums.append(abundant+abundant2)
abundant_sums.sort()
abundant_sums=list(set(abundant_sums))
print(abundant_sums)
print(abundant_sums[len(abundant_sums)-1])

sum_abundant=0
non_abundants=[]
for i in range(1,28123+1):
    if i in abundant_sums:
        continue
    non_abundants.append(i)
    sum_abundant+=i

print(non_abundants)
print(sum_abundant)