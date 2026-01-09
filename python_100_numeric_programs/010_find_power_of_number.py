"""
010 - Write a program to calculate cube and square of a number

Testcases:
Input: 4, 5
Output: cube - 64, square - 16

Input: 3, 0
Output: cube - 27, square - 9

Input: -4, 3
Output: cube - -64, square - 16
"""

def power_of_number(a,b):
    return a ** b

base = int(input('Enter a number: '))
exponent = int(input('Enter another number: '))
print(f'The power is {power_of_number(base, exponent)}')
