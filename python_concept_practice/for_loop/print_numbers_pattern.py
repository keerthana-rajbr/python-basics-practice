# Write a program that prints this exact output using nested for loops:
# 1
# 22
# 333
# 4444

for i in range(1,5):
    for _ in range(i):
        print(i, end='')
    print()
