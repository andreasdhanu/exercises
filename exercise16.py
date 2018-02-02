data = []
i = 0
sum = 0
while True:
    if i<2:
        data.append(i+1)
    else:
        data.append(data[i-2]+data[i-1])
    if data[i] > 4000000:
        # data.remove(data[data.index(data[i])])
        break
    value = data[i]
    if (i+1)%2 == 0:
        sum+=value
    i += 1


print(data)
print(sum)