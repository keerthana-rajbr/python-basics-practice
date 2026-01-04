# Write a program to count digits in a given number.

num = int(input('Enter a number :'))
if num == 0 :
    print('The count is 1')
else :
    count = 0
    while num > 0 :
        count += 1
        num //= 10
    print(f'The count is {count}')
