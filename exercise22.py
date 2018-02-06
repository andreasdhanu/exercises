number = 600851475143
primes=[]
for i in range(2,1000):
    if number % i == 0:
        number /= i
        primes.append(i)

print(primes[len(primes)-1])