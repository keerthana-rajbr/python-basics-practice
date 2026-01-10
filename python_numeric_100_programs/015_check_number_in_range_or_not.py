"""
015 - Write a program to check whether a number lies within a given range

Testcases:
Input: number = 5, range = (1 to 20)
Output: 5 lies between 1 and 20

Input: number = 39, range = (1 to 20)
Output: 39 does not lie between 1 and 20

Input: number = 1, range = (1 to 20)
Output: 1 lies between 1 and 20

"""

def number_in_range(num, start_range, end_range):
    if start_range <= num <= end_range:
        return f'{num} lies between {start_range} and {end_range}'
    else:
        return f'{num} does not lie between {start_range} and {end_range}'

num = int(input('Enter a number: '))
start_range = int(input('Enter the starting range: '))
end_range = int(input('Enter the ending range: '))
result = number_in_range(num, start_range, end_range)
print(result)