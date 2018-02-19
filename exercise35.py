'''


Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

'''
def checkPandigital(str_num):
    str_num=list(str_num)
    for i in range(1,10):
        i=str(i)
        if i in str_num:
            str_num.remove(i)
        else:
            return False
    if not str_num:
        return True
    else:
        return False

number=1
while number<1000000:
    str_number=''
    for i in range(1,3+1):
        str_number+=str(number*i)
        if len(str_number)>9:
            break
        elif len(str_number)==9:
            if checkPandigital(str_number):
                print(number, i, str_number)
            break
    number+=1

