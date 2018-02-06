palindrome = []
for i in range(999, 0, -1):
    for j in range(999, 0, -1):
        if str(i*j) == ''.join(reversed(str(i*j))):
            palindrome.append(i*j)

print(palindrome[0])