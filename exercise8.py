'''


The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

primes=generatePrimeNumbers(1000000)
result=0
result_elements=[]
for i in range(len(primes)):
    sum=0
    sum_elements=[]
    for j in range(i):
        sum+=primes[j]
        sum_elements.append(primes[j])
        if sum==primes[i] and len(sum_elements)>=len(result_elements):
            result=sum
            result_elements=sum_elements
            break
        elif sum>primes[i]:
            break

print(result, result_elements, len(result_elements))



