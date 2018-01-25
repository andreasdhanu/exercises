'''


The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''
number=2
primes=[]
while number<1000000:
    str_number=list(str(number))
    # print(str_number)
    int_number=0
    check = True
    for i in range(len(str_number)):
        result=str_number[i]
        for j in range(len(str_number)-1,0,-1):
            result+=str_number[i-j]
        int_number=(int(result))

        for k in range(2,int_number):
            if int_number%k==0:
                check=False
                break
        if check==False:
            break
    if check:
        primes.append(int_number)

    number+=1
print(len(primes))