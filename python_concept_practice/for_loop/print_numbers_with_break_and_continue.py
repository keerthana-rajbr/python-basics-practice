# Write a program to print numbers from 1 to 10, but:
# Stop the loop completely when the number becomes 7
# Do not print 5
# Output should be on separate lines

for i in range(1,11) :
    if i == 5 :
        continue
    elif i == 7 :
        break
    print(i)