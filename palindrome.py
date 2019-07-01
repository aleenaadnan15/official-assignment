#Question num 36:

'''  Given input is palindrome or not   '''

palindrome = input('enter any alp = ')

def is_Palindrome (text):
    reversedtext = ""
    for i in reversed(text):
        reversedtext += i
    
    if reversedtext == text:
        return True

if palindrome == palindrome[::-1]:
    print("The given input is Palindrome")
else:
    print("The given input is not Palindrome") 
