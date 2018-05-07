'''


The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''

def checkPandigital(num):
    str_num=list(str(num))
    for i in range(1,len(str_num)+1):
        i=str(i)
        if i in str_num:
            str_num.remove(i)
        else:
            return False
    if not str_num:
        return True
    else:
        return False

primes=[2,3,5,7,11,13,17]
qualified_pandigitals=[]
for i in range(100000000, 900000000):
    if checkPandigital(i):
        i=str(i)
        check=True
        print(i)
        for j in range(len(primes)):
            if int(i[j+1:j+4])%primes[j]==0:
                print(i[j+1:j + 4], primes[j])
            else:
                check=False
                break
        if check:
            qualified_pandigitals.append(i)
            print(i)

print(qualified_pandigitals)
sum=0
for qualified_pandigital in qualified_pandigitals:
    sum+=qualified_pandigital

print(sum)