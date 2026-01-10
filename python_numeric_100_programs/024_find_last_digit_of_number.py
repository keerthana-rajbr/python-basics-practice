"""
024 - Write a program to find the last digit of a number

Testcases:
Input: 435
Output: 5

Input: 100
Output: 0

Input: 0
Output:0

Input: -324
Output: 4
"""

def last_digit_of_num(number):
    last_digit = number % 10
    return last_digit

num = abs(int(input('Enter a number: ')))
result = last_digit_of_num(num)
print(f'The last digit of the number is {result}')