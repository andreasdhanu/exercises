
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
multiplicands=[]
multipliers=[]
products=[]
pandigitals=[]
result=0
for a in range(300):
    for b in range(300):
        result=a*b
        list_a=list(str(a))
        list_b = list(str(b))
        list_result=list(str(result))
        check=True
        for i in range(1,10):
            if str(i) in list_a:
                list_a.remove(str(i))
            elif str(i) in list_b:
                list_b.remove(str(i))
            elif str(i) in list_result:
                list_result.remove(str(i))
            else:
                check=False
                break
        if check and result not in products and not list_a and not list_b and not list_result:
            products.append(result)
            multiplicands.append(a)
            multipliers.append(b)
            # pandigitals.append([a,b,result])

sum=0
for i in range(len(products)):
    print(multipliers[i], multiplicands[i], products[i])
    sum+=products[i]

print(sum)