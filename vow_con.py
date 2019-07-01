#Question num 34:

'''  Count the occurrences of vowels and consonant   '''

text = input('enter any text = ')

count1 = 0
count2 = 0 
for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count1 = count1 + 1
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        count2 = count2 + 1
print('vowel:' ,count1)
print('cononant:' ,count2)
