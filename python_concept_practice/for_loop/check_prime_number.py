# Write a program to check whether a number 29 is a prime number using a for loop.
# If prime → print "Prime"
# If not prime → print "Not Prime"
# You must use for-else
# Do not use flags

num = 29
for i in range(2,num):
    if num % i == 0:
        print('It is not a prime number')
        break
else :
    print('It is a prime number')
