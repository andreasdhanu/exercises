triangle = 1
factor = []
while len(factor)<500:
    result = 0
    for i in range(triangle+1):
        result += i
    print(result)

    factor = []
    number = result
    for i in range(1,number+1):
        if number % i == 0:
            factor.append(i)

    print(len(factor))
    triangle+=1