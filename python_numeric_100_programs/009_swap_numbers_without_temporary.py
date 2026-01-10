"""
009 - Write a program to swap two numbers without a temporary variable

Testcases:
Input: 34, 2
Output: 2, 34
"""

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

num1, num2 = num2, num1
print(f'The swaped values are {num1}, {num2}')
