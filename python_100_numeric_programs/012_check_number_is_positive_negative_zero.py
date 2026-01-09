"""
012 - Write a program to check whether a number is positive, negative, or zero

Testcases:
Input: 4
Output: 4 is a positive number

Input: -8
Output: -8 is a negative number

Input: 0
Output: Number is zero
"""

def positive_or_negative(num):
    if num == 0:
        return 'Number is zero'
    elif num > 0:
        return 'positive number'
    else:
        return 'negative number'

num = int(input('Enter a number: '))
result = positive_or_negative(num)

if num == 0:
    print(result)
else:
    print(f'{num} is {result}')