# CTI-110 
# M5HW3 - Factorial
# Nabi Adam
# 10/12/2017


userInteger = int(input('Enter a nonnegative integer? '))
factorial = 1
for currentNumber in range (1, userInteger +1):
	factorial = factorial * currentNumber
print ('\nThe factorial of', userInteger, 'is', factorial)
