'''

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import string

with open('p022_names.txt') as text:
    names = text.readline()

names = names.strip('"')
names = names.split('","')
names.sort()
print(names)
char_value_dict = {}
i = 1
for char in string.ascii_lowercase:
    char_value_dict[char] = i
    i += 1
total = 0
score = []
rank = 1
for name in names:
    tmp = 0
    for char in name:
        tmp += char_value_dict[char.lower()]
    score.append(tmp * rank)
    total += tmp * rank
    rank += 1
print(score)
print(total)
