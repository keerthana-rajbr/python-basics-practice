"""
023 - Write a program to reverse a given number

Testcases:
Input: 1343
Output: 3431

Input: 5930
Output: 395

Input: 100
Output: 1

Input: 0
Output: 0

Input: -324
Output: 423
"""

def reverse_number(number):
    reverse_num =0
    while number > 0:
        digit = number % 10
        reverse_num = reverse_num * 10 + digit
        number //= 10
    return reverse_num

num = abs(int(input('Enter a number: ')))
result = reverse_number(num)
print(result)




