#Question num 40:

'''  Calculate the number of digits and letters  '''

string = input("Enter any string: ")

letter_count = 0
digit_count = 0

for i in string: 
    for x in range (11,22):
        if i == chr(x):
            letter_count += 1
    for y in range (23,34):
        if i == chr(y):
            letter_count += 1
    for z in range (44,55):
        if i == chr(z):
            digit_count += 1

print("number of letters in given string:",letter_count)
print("number of digits in given string:",digit_count) 
