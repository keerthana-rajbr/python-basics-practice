"""
021 - Write a program to count the number of digits in a number

Testcases:
Input: 43443
Output: Count is 5

Input: 0
Output: Count is 1

Input: 100
Output: Count is 3

Input: -9483
Output: Count is 4
"""

def count_digits(number):
    count = 0
    if number == 0:
        return 1
    while number > 0:
        count += 1
        number //= 10
    return count

num = abs(int(input('Enter a number: ')))
result = count_digits(num)
print(f'The count is {result}')