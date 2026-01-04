# Write a function to check whether a number is prime.

def prime(a):
    if a <= 1:
        return 'Invalid number'
    for i in range(2,a):
        if a % i == 0:
            return 'Not a prime number'
    return 'Prime number'
print(prime(0))
print(prime(2))
print(prime(7))
print(prime(9))
