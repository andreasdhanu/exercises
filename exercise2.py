total=10000
sums = {}
amicables = []
for number in range(1, total + 1):
    divisor = []
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor.append(i)
            sum += i
    sums[number] = sum

for k, v in sums.items():
    for number in range(1, total + 1):
        # print(sums[number])
        if sums[number] == k and v == number and k!=number:
            amicables.append(k)
            amicables.append(v)
print(amicables)
amicables=list(set(amicables))
print(amicables)
sum_amicable=0
for amicable in amicables:
    sum_amicable+=amicable

print(sum_amicable)
