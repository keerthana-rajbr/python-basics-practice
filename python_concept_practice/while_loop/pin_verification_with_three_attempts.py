# Write a program that allows user 3 attempts to enter correct PIN.

correct_pin = 1234
attempts = 3

while attempts > 0:
    pin = int(input("Enter your pin: "))
    attempts -= 1
    if pin == correct_pin :
        print('Login successful')
        break
    if attempts > 0 :
        print(f'Wrong pin. You have {attempts} attempts left.')
else :
    print('Account locked')
