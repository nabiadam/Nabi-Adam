# CTI 110
# M5HW2: Running Total
# Nabi Adam
# 10/18/17

total = 0
userNumber = float (input ('Enter a number?'))
while userNumber >-1:
    total = total + userNumber
    userNumber = float (input('Enter a number?'))
print ('Total:',total)
