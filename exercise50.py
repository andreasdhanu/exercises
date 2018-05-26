numMax=2000000
primes=[]
sum = 0
for i in range(2,numMax):
    prime = True
    for j in range(2, i):
        if i%j == 0:
            prime = False
            break
    if prime:
        primes.append(i)
        sum += i

print(primes)
print(sum)