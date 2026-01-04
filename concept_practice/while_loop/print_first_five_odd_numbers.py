# Write a program to print first 5 odd numbers.

i = 1
count = 0
while i > 0 :
    if i % 2 != 0 :
        print(i)
        count += 1
        if count == 5 :
            break
    i += 1
