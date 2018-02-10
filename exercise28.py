longest_length = 0
for start in range (1000000):
    START = start
    array =[]
    array.append(start)
    while start > 1:
        if start % 2 == 0:
            start = start/2
            array.append(start)
        else:
            start = (start*3)+1
            array.append(start)
    if longest_length < len(array):
        longest_length = len(array)
        print(longest_length, START)
