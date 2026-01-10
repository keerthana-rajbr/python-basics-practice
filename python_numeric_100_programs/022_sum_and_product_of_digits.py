"""
022 - Write a program to find the sum and product of digits of a number

Testcases:
Input: 434
Output: sum = 11, product = 48

Input: 0
Output: sum = 0, product = 0

Input: -432
Output: sum = 9, product = 24
"""

def sum_of_digits(number):
    if number == 0:
        return 0, 0
    result, product = 0, 1
    while number > 0:
        digit = number % 10
        result += digit
        product *= digit
        number //= 10
    return result, product

num = abs(int(input('Enter a number: ')))
digit_sum,digit_product = sum_of_digits(num)
print(f'The sum is {digit_sum} and product is {digit_product}')





