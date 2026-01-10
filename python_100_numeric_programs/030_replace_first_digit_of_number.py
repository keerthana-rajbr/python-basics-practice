"""
030 - Write a program to replace the first digit of a number with another digit

Testcases:
Input: 435, 3
Output: 335

Input: 100, 4
Output: 400

Input: 0, 2
Output:2

Input: -324, 5
Output: 525
"""

def count_digit(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

def replace_first_digit(number, replace_digit):
    if not(0 <= replace_digit <= 9):
        return None
    count = count_digit(number)
    divisor = 10 ** (count-1)
    remaining = number % divisor
    replaced_number = replace_digit * divisor + remaining
    return replaced_number

num = abs(int(input('Enter a number: ')))
replace_digit = abs(int(input('Enter the replacing digit: ')))
result = replace_first_digit(num, replace_digit)
if result is None:
    print('invalid digit! Enter number between 0 and 9')
else:
    print(f'After replacing first digit, the number becomes {result}')
















