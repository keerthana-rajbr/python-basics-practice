"""
020 - Write a program to check whether a number is divisible by two other numbers

Testcases:
Input: number = 39, divisors = 5, 3
Output: 39 is not divisible by 5 and 3

Input: number = 100, divisors = 5, 10
Output: 100 is divisible by 5 and 10

Input: number = 12, divisors = 6, 9
Output: 12 is divisible by 6 but not 9

Input: number = 44, divisors = 5,11
Output: 44 is divisible by 11 but not 5

Input: number = 43, divisors = 4, 0
Output: Division by zero not allowed
"""

def divisible_or_not(num, a, b):
    if a == 0 or b == 0:
        return 'Division by zero not allowed'

    is_divisible_a = (num % a == 0)
    is_divisible_b = (num % b == 0)

    if is_divisible_a and is_divisible_b:
        return f'{num} is divisible by {a} and {b}'
    elif is_divisible_a:
        return f'{num} is divisible by {a} but not {b}'
    elif is_divisible_b:
        return f'{num} is divisible by {b} but not {a}'
    else:
        return f'{num} is not divisible by either {a} or {b}'

num = int(input('Enter a number: '))
divisor1 = int(input('Enter first divisor : '))
divisor2 = int(input('Enter second divisor: '))
result = divisible_or_not(num, divisor1, divisor2)
print(result)