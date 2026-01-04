# Write a function to find the factorial of a number.

def factorial(a):
    if a < 0:
        return 'Invalid number'
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
    return fact

num = int(input('Enter a number :'))
print(factorial(num))
