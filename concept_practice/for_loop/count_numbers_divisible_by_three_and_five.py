# Write a program to count how many numbers between 1 and 50 (both included):
# are divisible by 3
# but not divisible by 5
# Finally, print the count only.

count = 0
for num in range(1,51):
    if num % 3 == 0 and num % 5 != 0:
        count += 1
print(count)
