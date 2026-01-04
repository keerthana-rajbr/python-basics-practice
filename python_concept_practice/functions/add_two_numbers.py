# Write a function to add two numbers and return the result.

def add(a,b):
    return a + b

num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))
result = add(num1,num2)
print(f'The sum of {num1} and {num2} is {result}')