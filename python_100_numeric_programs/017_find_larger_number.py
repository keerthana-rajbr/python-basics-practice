"""
017 - Write a program to compare two numbers and print the larger one

Testcases:
Input: 4, 2
Output: 4 is the larger number

Input: 5,5
Output: Both numbers are equal
"""

def find_large_number(num1, num2):
    if num1 == num2:
        return 'Both numbers are equal'
    elif num1 < num2:
        return f'{num2} is the larger number'
    else:
        return f'{num1} is the larger number'

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
result = find_large_number(num1, num2)
print(result)