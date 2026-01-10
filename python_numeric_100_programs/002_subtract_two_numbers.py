"""
002 - Write a program to subtract two numbers

Testcases:
Input: 34, 4
Output: 30

Input: -5, -4
Output: -1
"""

def subtract_numbers(a,b):
    return a-b

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'The difference is {subtract_numbers(num1,num2)}')