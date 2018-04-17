import math
numbers = []
a = 1
found = False
while True:
    for b in range(a):
        c=math.sqrt(a**2+b**2)
        if c.is_integer():
            result=a+b+c
            numbers.append(result)
            if result==1000:
                print(a,b,c)
                found =True
                break
    if found:
        break
    a+=1

print(numbers)