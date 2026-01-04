# Check greater of two numbers

num1 = int(input('Enter a number :'))
num2 = int(input('Enter another number :'))
if num1 > num2:
    print(f'{num1} is greater number')
elif num1 == num2:
    print('Both are equal')
else:
    print(f'{num2} is greater number')
