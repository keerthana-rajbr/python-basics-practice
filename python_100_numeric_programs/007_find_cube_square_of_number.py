"""
007. Write a program to calculate power, cube and square of a number

Testcases:
Input: 4, 5
Output: cube - 64, square - 16

Input: 3, 0
Output: cube - 27, square - 9

Input: -4, 3
Output: cube - -64, square - 16
"""

def cube_of_number(a):
    return a ** 3

def square_of_number(a):
    return a ** 2

num = int(input('Enter a number: '))
print(f'The cube is {cube_of_number(num)}')
print(f'The square is {square_of_number(num)}')
