# Write a function to check whether a number is even or odd.

def even_or_odd(a):
    if a % 2 == 0:
        return 'Even number'
    return 'Odd number'

num = int(input('Enter a number :'))
print(f'{num} is {even_or_odd(num)}')
