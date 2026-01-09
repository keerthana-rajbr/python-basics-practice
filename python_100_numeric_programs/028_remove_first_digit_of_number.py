"""
028 - Write a program to remove the first digit from a number

Testcases:
Input: 435
Output: 35

Input: 100
Output: 0

Input: 0
Output:0

Input: -324
Output: 24

"""

def digit_count(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number//= 10
    return count

def remove_first_digit(number):
    if number == 0:
        return 0
    count = digit_count(number)
    divider = 10 ** (count - 1)
    remaining = number % divider
    return remaining

num = abs(int(input('Enter a number: ')))
result = remove_first_digit(num)
print(f'After removing the first digit, the number is {result}')






