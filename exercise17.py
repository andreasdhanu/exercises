number = 100
result=1
for i in range (1,number+1):
    result *= i
print(result)
result = str(result)
sum=0
for i in result:
    sum += int(i)
print(sum)