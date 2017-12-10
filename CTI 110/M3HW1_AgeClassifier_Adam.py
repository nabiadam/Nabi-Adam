# CTI-110 
# M3HW1 - Age Classifier 
# Nabi Adam
# 09/14/2017

userAge = int(input('Please enter your age: '))
if userAge <= 1:
	print('You are an infant')
elif userAge <13:
	print('You are a child')
elif userAge <20:
	print('You are teenager')
elif userAge >=20:
	print('You are an adult')
