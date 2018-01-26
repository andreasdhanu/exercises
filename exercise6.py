'''


The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''
for i in range(10,100):
    for j in range(10,100):
        if(i/j<1):
            result=i/j
            for k in range(1,10):
                tmp_i=list(str(i))
                tmp_j=list(str(j))
                if str(k) in tmp_i and str(k) in tmp_j:
                    tmp_i.remove(str(k))
                    tmp_j.remove(str(k))
                    num=int(tmp_i[0])
                    denum=int(tmp_j[0])
                    try:
                        value=num/denum
                        if value == result:
                            print(i, j)
                    except ZeroDivisionError:
                        continue


    # print()