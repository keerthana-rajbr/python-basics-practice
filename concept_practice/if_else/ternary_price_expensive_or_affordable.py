# Take a price from user.
# Display “Expensive” if price is greater than or equal to 1500, otherwise “Affordable”.

price = int(input('Enter your price : '))
print('Expensive') if price >= 1500 else print('Affordable')