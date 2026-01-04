# Temperature classification
# below 0 → Freezing
# 0–25 → Normal
# above 25 → Hot

temp = int(input("Enter the temperature :"))
if temp < 0 :
	print('Freezing')
elif 0 <=  temp <= 25 :
	print('Normal')
else :
	print('Hot')