# Write a program to calculate the sum of even numbers between 1 and 20.

i, sum = 2, 0
while i <= 20 :
    sum += i
    i += 2
print(f'The sum is {sum}')
