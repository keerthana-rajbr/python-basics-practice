"""
035 - Write a program to check whether all digits in a number are the same

Testcases:
Input: 435
Output: Not same

Input: 100
Output: Not same

Input: 0
Output: Same

Input: 4
Output: Same
"""



def digits_same_or_not(number):
    if number < 10:
        return True
    compare_digit = number % 10
    while number > 0:
        digit = number % 10
        if compare_digit != digit:
            return False
        number //= 10
    return True

num = abs(int(input('Enter a number: ')))
result = digits_same_or_not(num)
if result:
    print('All digits are same')
else:
    print('Digits are different')