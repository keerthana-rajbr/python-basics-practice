"""
031 - Write a program to replace the first digit of a number with another digit

Testcases:
Input: 435
Output: 1

Input: 100
Output: 2

Input: 0
Output: 1

Input: -324354345
Output: 4
"""

def count_even_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        digit = number % 10
        number //= 10
        if digit % 2 == 0:
            count += 1
    return count

num = abs(int(input('Enter a number: ')))
result = count_even_digits(num)
print(f'The count of even digits is {result}')