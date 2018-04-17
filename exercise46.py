data = 0
h = 1
while True:
    check = True
    for i in range(1, 20+1):
        if h % i != 0:
            check = False
            break
    if check:
        data = h
        break
    h+=1

print(data)