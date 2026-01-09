"""
026 - Write a program to find the sum of first and last digit of a number

Testcases:
Input: 435
Output: 9

Input: 100
Output: 1

Input: 0
Output:0

Input: -324
Output: 7
"""

def sum_of_first_and_last(number):
    last_digit = number % 10
    while number >= 10:
        number //= 10
    first_digit = number
    return last_digit + first_digit

num = abs(int(input('Enter a number: ')))
result = sum_of_first_and_last(num)
print(f'The sum of first and last digit is {result}')