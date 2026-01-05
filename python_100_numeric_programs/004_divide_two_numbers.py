"""
004 - Write a program to divide two numbers

Testcases:
Input: 4, 2
Output: 2.0

Input: 23, 0
Output: Division by zero not allowed
"""

def divide_numbers(a,b):
    if b == 0:
        return None
    return a / b

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result = divide_numbers(num1,num2)

if result is None:
    print('Division by zero not allowed')
else:
    print(f'The result is {result}')