#Question num 11:

'''   letter is a vowel or not   '''

letter = input('enter any letter')

vowels_word = ['a' , 'e' , 'i' , 'o' , 'u']
for i in vowels_word:
    if i == letter:
        print(letter + ' is a vowels')
        break
    else:
        print(letter + ' is a alp')