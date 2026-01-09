"""
006 - Write a program to perform floor division

Testcases:
Input: 4, 9
Output: 0

Input: 5, 0
Output: Division by zero not allowed

Input: 434, 54
Output: 8

Input: -8, 3
Output: -3
"""

def floor_division(a,b):
    if b == 0:
        return None
    return a//b

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
quotient = floor_division(num1,num2)

if quotient is None:
    print('Division by zero not allowed')
else:
    print(f'The quotient is {quotient}')


