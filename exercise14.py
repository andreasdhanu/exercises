
'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
def generatePrimeNumbers(limit):
    primes=[]
    num=2
    check=True
    while num<limit:
        for i in range(2,num):
            check=True
            if num%i==0:
                check=False
                break
        if check:
            primes.append(num)
        num+=1
    return(primes)

print(generatePrimeNumbers(10000))
prime_numbers=generatePrimeNumbers(100)
found=False
x=2
consecutive=0
while not found:
    factor=[]

    for i in prime_numbers:
        num=x
        if num%i==0:
            num/=i
            factor.append(i)
            if num==1:
                break
    if len(factor)==4:
        consecutive+=1
        if consecutive==4:
            print(x, factor)
            break
    else:
        consecutive=0

    print(x,factor)
    x+=1
