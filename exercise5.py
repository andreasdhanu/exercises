'''


The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

'''
import string

with open('p042_words.txt') as text_file:
    words=text_file.readline()

words=words.strip('"').split('","')


word_dic={}
for i,c in enumerate(string.ascii_uppercase, start=1):
    word_dic[c]=i

words_values=[]
for word in words:
    value=0
    for char in word:
        value+=word_dic[char]
    words_values.append(value)

triangle_numbers=[]
triangle_number=0
n=1

while triangle_number<max(words_values):
    triangle_number=n/2*(n+1)
    triangle_numbers.append(triangle_number)
    n+=1

print(triangle_numbers)

print(len(words_values))

sum_triangle=0
for word_value in words_values:
    if word_value in triangle_numbers:
        sum_triangle+=1
        print(word_value)
print(sum_triangle)