"""
027 - Write a program to remove the last digit from a number

Testcases:
Input: 435
Output: 43

Input: 100
Output: 10

Input: 0
Output:0

Input: -324
Output: 32

"""

def remove_last_digit(number):
    return number // 10

num = abs(int(input('Enter a number: ')))
result = remove_last_digit(num)
print(f'After removing last digit, the number becomes {result}')