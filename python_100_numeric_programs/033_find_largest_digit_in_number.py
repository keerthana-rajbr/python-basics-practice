"""
034 - Write a program to find the largest digit in a number

Testcases:
Input: 435
Output: 5

Input: 100
Output: 1

Input: 0
Output: 0

Input: -324354345
Output: 5
"""

def largest_digit(number):
    large_digit = 0
    while number > 0:
        digit = number % 10
        if digit >= large_digit:
            large_digit = digit
        number //= 10
    return large_digit

num = abs(int(input('Enter a number: ')))
result = largest_digit(num)
print(f'The largest digit is {result}')