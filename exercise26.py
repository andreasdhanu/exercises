pascals = []
latice =[]
max = 3
h=0
while len(latice)<20+1:
    row = []
    last = h
    for i in range(h):
        if i == 0:
            row.append(1)
        elif i == last-1:
            row.append(1)
        else:
            row.append(pascals[h-1][i]+pascals[h-1][i-1])
    if(len(row)%2==1):
        latice.append(row[int(len(row)/2)])
    pascals.append(row)
    h+=1
print(pascals)
print(latice)
print(latice[len(latice)-1])