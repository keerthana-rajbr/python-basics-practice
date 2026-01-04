# Write a program to print factorial of a number.

num = int(input('Enter your number :'))
i = fact = 1
if num < 0 :
    print('Invalid number')
else :
    while i <= num :
        fact = fact * i
        i += 1
    print(f'The factorial of number {num} is {fact}')
