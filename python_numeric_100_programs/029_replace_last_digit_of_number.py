"""
029 - Write a program to replace the last digit of a number with another digit

Testcases:
Input: 435, 3
Output: 433

Input: 100, 4
Output: 104

Input: 0, 2
Output:2

Input: -324, 5
Output: 325
"""

def replace_last_digit(number, replace_digit):
    if not (0 <= replace_digit <= 9):
        return None
    number //= 10
    number = number * 10 + replace_digit
    return number

num = abs(int(input('Enter a number: ')))
replace_digit = abs(int(input('Enter the replacing digit: ')))
result = replace_last_digit(num, replace_digit)
if result is None:
    print('invalid digit! Enter number between 0 and 9')
else:
    print(f'After replacing last digit, the number becomes {result}')









