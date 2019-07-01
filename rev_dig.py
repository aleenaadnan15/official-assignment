#Question num 37:

'''  Reverse the digits of a given number and add it to the original, 
         If the sum is not a palindrome repeat this procedure   '''

number = int(input('enter any digits = '))

# def palindrome (number):
#     reversed_number = int(str(number)[::-1])
#     sum_num = int(number) + reversed_number

#     if sum_num == int(str(sum_num)[::-1]):
#         return sum_num
#     else:
#         return palindrome (sum_num)

# print('palindrome')

while True:
    num = str(number)
    if num == num[::-1]:
        print("The Number",number,"is a Palidrome")
        break
    else:
        reverse_number = int(num[::-1])
        number += reverse_number
        print(number) 
