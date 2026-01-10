"""
018 - Write a program to check whether three numbers are equal

Testcases:
Input: 4, 3, 4
Output: The numbers are not equal

Input: 4,4,4
Output: The numbers are equal
"""

def numbers_equal(num1, num2, num3):
    if num1 == num2 == num3:
        return 'The numbers are equal'
    return 'The numbers are not equal'

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
result = numbers_equal(num1, num2, num3)
print(result)