'''


In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

'''

# currency = {'1p': 1,
#             '2p': 2,
#             '5p': 5,
#             '10p': 10,
#             '20p': 20,
#             '50p': 50,
#             '£1': 100,
#             '£2': 200,
#             }
coins=[]
for i in range(2):
    for j in range(3):
        for k in range(5):
            for l in range(11):
                for m in range(21):
                    for n in range(41):
                        for o in range(101):
                            for p in range(201):
                                sum=k*50+j*100+i*200+l*20+m*10+n*5+o*2+p*1
                                print(i,j,k,l,m,n,o,p,sum)
                                if sum == 200:
                                    coins.append([i,j,k,l,m,n,o,p])
                                    break
                                elif sum > 200:
                                    break


print(len(coins))