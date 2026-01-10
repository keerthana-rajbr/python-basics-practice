"""
001 - Write a program to add two numbers

Testcases:
Input: 2, 3
Output: 5

Input: -4, 5
Output: 1
"""

def add_numbers(a,b):
    return a + b

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
print(f'The sum is {add_numbers(num1,num2)}')