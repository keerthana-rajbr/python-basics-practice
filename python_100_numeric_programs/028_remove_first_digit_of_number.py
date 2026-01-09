



def digit_count(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number//= 10
    return count

def remove_first_digit(number):
    if number == 0:
        return 0
    count = digit_count(number)
    divider = 10 ** (count - 1)
    remaining = number % divider
    return remaining

num = abs(int(input('Enter a number: ')))
result = remove_first_digit(num)
print(result)