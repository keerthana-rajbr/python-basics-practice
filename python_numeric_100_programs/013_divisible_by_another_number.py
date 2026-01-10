"""
013 - Write a program to check whether a number is divisible by another number

Testcases:
Input: 4, 5
Output: 4 is not divisible by 5

Input: 40, 5
Output: 40 is divisible by 5

Input: 5,0
Output: Division by zero not allowed
"""

def divisible_or_not(num1, num2):
    if num2 == 0:
        return None
    elif num1 % num2 == 0:
        return 'divisible'
    else:
        return 'not divisible'

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result = divisible_or_not(num1, num2)
if result is None:
    print('Division by zero not allowed')
else:
    print(f'{num1} is {result} by {num2}')