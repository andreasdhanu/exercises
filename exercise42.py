'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
import sys


def isPrime(input):
    if input < 2:
        return False
    for i in range(2, input):
        if input % i == 0:
            return False
    return True


longest_primes = []
for i in range(10000, 999999):
    digit_length = len(str(i))
    for j in range(digit_length):
        for k in range(j, digit_length):
            if j != k:
                # print(j,k,string_i[j],string_i[k])

                temp_string_i = list(str(i))
                # print(''.join(temp_string_i))
                temp_primes = []
                for m in range(10):
                    temp_string_i.pop(j)
                    temp_string_i.insert(j, str(m))
                    temp_string_i.pop(k)
                    temp_string_i.insert(k, str(m))
                    temp_integer_i = int(''.join(temp_string_i))
                    if isPrime(temp_integer_i) and len(str(temp_integer_i)) == digit_length:
                        temp_primes.append(int(''.join(temp_string_i)))
                if len(temp_primes) > len(longest_primes):
                    longest_primes = temp_primes
                    print(longest_primes)
                    if len(longest_primes) == 8:
                        sys.exit()

                    # temp_number=int()
    # for digit in str(i):

    #     print(digit)

# for i in range(5):
#     for j in range(i,5):
#         if i!=j:
#             print(i,j)
