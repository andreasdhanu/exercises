'''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
longests=[]
p_value=1
while p_value<=1000:
    solutions=[]
    for c in range(1,p_value):
        found=False
        for a in range(1,c):
            for b in range(1,c):
                pythagoras=a**2+b**2
                p = a + b + c
                if c**2 == pythagoras and p==p_value:
                    found=True
                    solutions.append([a,b,c,p])
                    break
            if len(longests)<len(solutions):
                longests=solutions
            if found:
                break
    p_value+=1

for longest in longests:
    print(longest)