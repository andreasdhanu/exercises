bases = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
ten_beyonds = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
count = 0
number = 1000

for i in range(1, number + 1):
    if i < 10:
        count += bases[i]
        print(i, bases[i])
        print()
    elif i < 20:
        base = i % 10
        count += tens[base]
        print(i, tens[base])
        print()
    elif i < 100:
        ten = int(i / 10) % 10
        base = i % 10
        start = count

        count += bases[base]
        count += ten_beyonds[ten]

        print(i, count - start)
        print()
    elif i < 1000:
        hundred = int(i / 100) % 10
        ten = int(i / 10) % 10
        base = i % 10
        start = count
        count += bases[hundred]
        count += 7
        if ten == 0 and base == 0:
            count += 0
        elif ten == 0:
            count += 3
            count += bases[base]
        elif ten < 2:
            count += 3
            count += tens[base]
        else:
            if base > 0:
                count += 1
            count += 3
            count += ten_beyonds[ten]
            count += bases[base]
        print(i, count - start)
        print()
    elif i == 1000:
        start = count
        count += 11
        print(i, count - start)
        print()

print(count)
