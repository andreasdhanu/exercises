'''


We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

def checkPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def checkPandigital(num):
    str_num=list(str(num))
    for i in range(1,len(str_num)+1):
        i=str(i)
        if i in str_num:
            str_num.remove(i)
        else:
            return False
    if not str_num:
        return True
    else:
        return False

for i in range(2,100000):
    if checkPrime(i) and checkPandigital(i):
        print(i)

