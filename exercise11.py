'''


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''
import math

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    if i == 0 and j == 0 and k == 0:
                        result = + math.factorial(l) + math.factorial(m)
                        tmp_l = str(l)
                        tmp_m = str(m)
                        tmp_result = str(result)
                        if tmp_result == tmp_l + tmp_m:
                            print(l, m, result)
                    elif i == 0 and j == 0:
                        result = math.factorial(k) + math.factorial(l) + math.factorial(m)
                        tmp_k = str(k)
                        tmp_l = str(l)
                        tmp_m = str(m)
                        tmp_result = str(result)
                        if tmp_result == tmp_k + tmp_l + tmp_m:
                            print(k, l, m, result)
                    elif i == 0:
                        result = math.factorial(j) + math.factorial(k) + math.factorial(l) + math.factorial(m)
                        tmp_j = str(j)
                        tmp_k = str(k)
                        tmp_l = str(l)
                        tmp_m = str(m)
                        tmp_result = str(result)
                        if tmp_result == tmp_j + tmp_k + tmp_l + tmp_m:
                            print(j, k, l, m, result)
                    else:
                        result = math.factorial(i) + math.factorial(j) + math.factorial(k) + math.factorial(
                            l) + math.factorial(m)
                        tmp_i = str(i)
                        tmp_j = str(j)
                        tmp_k = str(k)
                        tmp_l = str(l)
                        tmp_m = str(m)
                        tmp_result = str(result)
                        if tmp_result == tmp_i + tmp_j + tmp_k + tmp_l + tmp_m:
                            print(i, j, k, l, m, result)
