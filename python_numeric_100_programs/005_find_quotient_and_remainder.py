"""
005 - Write a program to find quotient and remainder

Testcases:
Input: 8, 3
Output: Quotient = 2, Remainder = 2

Input: 5, 0
Output: Division by zero not allowed
"""

def find_quotient(a,b):
    if b == 0:
        return None
    return a // b

def find_remainder(a,b):
    if b == 0:
        return None
    return a % b

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
quotient = find_quotient(num1, num2)
remainder = find_remainder(num1, num2)

if quotient is None:
    print('Division by zero not allowed')
else:
    print(f'Quotient is {quotient}')
    print(f'Remainder is {remainder}')








