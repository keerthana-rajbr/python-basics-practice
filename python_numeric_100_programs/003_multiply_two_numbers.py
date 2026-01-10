"""
003 - Write a program to multiply two numbers

Testcases:
Input: 4, 5
Output: 20

Input: -5, -2
Output: 10

"""

def multiply_numbers(a,b):
    return a * b

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'The product is {multiply_numbers(num1,num2)}')