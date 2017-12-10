# CTI-110 
# M3HW1 - SoftwareSales
# Nabi Adam
# 09/14/2017

userNumberOfPackages = int( input('Please enter number of packages bought:'))
packagePrice = 99
if userNumberOfPackages < 10:
	discount = 0;
elif userNumberOfPackages < 20:
	discount = 0.10
elif userNumberOfPackages < 50:
	discount = 0.20
elif userNumberOfPackages < 100:
	discount = 0.30
else:
	discount = 0.40
subtotal = userNumberOfPackages * packagePrice
discountAmount = discount * subtotal
total = subtotal - discountAmount
print('Amount of discount: $'  ,discountAmount)
print('Total amount: $' ,total)
