def generateSpiralNumber(s):
    bucket=[]
    for i in range(s+2):
        bucket.append([0]*(s+2))
    mid=int((s+2)/2)
    i=1
    x = mid
    y = mid
    direction='r'
    while i<s**2+1:
        if i==1:
            bucket[y][x] = i
            i += 1
            continue
        elif direction=='r':
            x+=1
            if bucket[y+1][x]==0:
                direction='d'
        elif direction=='d':
            y+=1
            if bucket[y][x-1]==0:
                direction='l'
        elif direction=='l':
            x-=1
            if bucket[y-1][x]==0:
                direction='u'
        elif direction=='u':
            y-=1
            if bucket[y][x+1]==0:
                direction='r'

        bucket[y][x]=i
        i+=1

    return bucket

def sumDiagonal(a,size):
    result=0
    for i in range(size+2):
        result+=a[i][i]
        result+=a[i][6-i]
    print(result-1)


size=1001
x=generateSpiralNumber(size)
sumDiagonal(x,size)
# for i in range(size+2):
#     print(x[i])


