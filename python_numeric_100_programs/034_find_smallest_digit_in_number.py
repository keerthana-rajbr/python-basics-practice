"""
034 - Write a program to find the smallest digit in a number

Testcases:
Input: 435
Output: 3

Input: 100
Output: 0

Input: 0
Output: 0

Input: -324354345
Output: 2
"""

def smallest_digit(number):
    if number == 0:
        return 0
    small_digit = 9
    while number > 0:
        digit = number % 10
        if digit < small_digit:
            small_digit = digit
        number //= 10
    return small_digit

num = abs(int(input('Enter a number: ')))
result = smallest_digit(num)
print(f'The smallest digit is {result}')