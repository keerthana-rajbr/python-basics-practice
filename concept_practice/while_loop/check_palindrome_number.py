# Write a program to check whether a number is palindrome.

num = int(input('Enter a number :'))
palnum = num
rev = 0
while num > 0 :
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
if palnum == rev :
    print(f'{palnum} is a palindrome number')
else :
    print(f'{palnum} is not a palindrome number')
