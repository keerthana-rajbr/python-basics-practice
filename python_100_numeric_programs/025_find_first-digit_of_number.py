"""
024 - Write a program to find the first digit of a number

Testcases:
Input: 435
Output: 4

Input: 100
Output: 1

Input: 0
Output:0

Input: -324
Output: 3
"""

def first_digit_of_num(number):
    if number == 0:
        return 0
    while number >= 10:
        number //= 10
    return number

num = abs(int(input('Enter a number: ')))
result = first_digit_of_num(num)
print(f'The first digit of the number is {result}')