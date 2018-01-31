sum=0
for number in range(1,1000000):
    str_number_2=str(bin(number)).lstrip('0b')
    reverse_str_number_2=''.join(reversed(str_number_2))
    str_number_10=str(number)
    reverse_str_number_10=''.join(reversed(str_number_10))
    if str_number_10==reverse_str_number_10 and str_number_2==reverse_str_number_2:
        print(str_number_10)
        print(str_number_2)
        sum+=number

print(sum)
