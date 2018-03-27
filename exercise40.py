primes=[]
i=2
while len(primes) < 10:
    prime=True
    for j in range(2, i):
        if (i%j==0):
            prime=False
            break
    if prime:
        primes.append(i)
    i+=1


print(primes)
print(primes[len(primes)-1])