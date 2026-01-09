"""
016 - Write a program to check whether a number is an integer or a decimal number

Testcases:
Input: 4
Output: 4 is integer

Input: 5.2
Output: 5.2 is decimal

Input: .2
Output: .2 is decimal

Input: 0.0
Output: 0 is integer

"""
# Method 1
def decimal_or_integer(num):
    if num.is_integer():
        return f'{int(num)} is Integer'
    else:
        return f'{num} is Decimal'

num = float(input('Enter a number: '))
result = decimal_or_integer(num)
print(result)

"""
# Method 2
def decimal_or_integer(num):
    if num == int(num):
        return f'{int(num)} is Integer'
    else:
        return f'{num} is Decimal'

num = float(input('Enter a number: '))
result = decimal_or_integer(num)
print(result)

# Method 3
def decimal_or_integer(num):
    if num % 1 == 0:
        return f'{int(num)} is Integer'
    else:
        return f'{num} is Decimal'

num = float(input('Enter a number: '))
result = decimal_or_integer(num)
print(result)
"""

