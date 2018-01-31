'''


Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

'''
result=[]
for h in range(10):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    output=h**5+i**5+j**5+k**5+l**5
                    if output in result:
                        continue

                    tmp_output=list(str(output))
                    if str(h) in tmp_output:
                        tmp_output.remove(str(h))
                        if str(i) in tmp_output:
                            tmp_output.remove(str(i))
                            if str(j) in tmp_output:
                                tmp_output.remove(str(j))
                                if str(k) in tmp_output:
                                    tmp_output.remove(str(k))
                                    if str(l) in tmp_output:
                                        print(h,i,j,k,l,output)
                                        result.append(output)




print(result)
sum=0
for number in result:
    sum+=number

print(sum)