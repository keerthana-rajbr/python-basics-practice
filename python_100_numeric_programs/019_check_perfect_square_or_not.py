"""
019 - Check whether a number is a perfect square

Testcases:
Input: 5
Output: 5 is not a perfect square

Input: 49
Output: 49 is a perfect square

Input: -4
Output: -4 is not a perfect square
"""

import math

def perfect_square(num):
    if num < 0 :
        return False
    root = math.sqrt(num)
    return root == int(root)

num = int(input('Enter a number: '))
result = perfect_square(num)

if not result:
    print(f'{num} is not a perfect square')
else:
    print(f'{num} is a perfect square')