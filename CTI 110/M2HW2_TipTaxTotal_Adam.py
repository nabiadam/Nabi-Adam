
# CTI-110 
# M2HW2 - Tip Tax Total 
# Nabi Adam
# 09/07/2017
foodCharge = float(input('Please enter the charge of the food:'))
tip  =  0.18 * foodCharge
salesTax  =  0.07 * foodCharge
total = foodCharge + tip + salesTax

print ("Food Charge: $" ,foodCharge)
print ("Tip: S" ,tip)
print ("Sales Tax: $" ,salesTax)
print ("Total: $", total)
