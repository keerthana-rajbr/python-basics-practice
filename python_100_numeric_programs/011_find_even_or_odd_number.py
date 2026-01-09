"""
011 - Write a program to check whether a number is even or odd

Testcases:
Input: 5
Output: 5 is Odd number

Input: 0
Output: 0 is Even number

Input: -4
Output: -4 is Even number
"""

def even_or_odd(num):
    if num % 2 == 0:
        return 'Even number'
    else:
        return 'Odd number'

num = int(input('Enter a number: '))
result = even_or_odd(num)
print(f'{num} is {result}')