"""
014 - Write a program to check whether a number is a multiple of another number

Testcases:
Input: 4, 5
Output: 4 is not multiple of 5

Input: 40, 5
Output: 40 is multiple of 5

Input: 5,0
Output: Division by zero not allowed

Input: 0, 5
Output: 0 is multiple of 5
"""

def multiple_or_not(num1, num2):
    if num2 == 0:
        return None
    elif num1 % num2 == 0:
        return 'multiple'
    else:
        return 'not multiple'

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result = multiple_or_not(num1, num2)
if result is None:
    print('Division by zero not allowed')
else:
    print(f'{num1} is {result} of {num2}')


