

vehicleSpeed = float(input('What is the speed of the vehicle in mph?: '))

timeTraveled = int (input('How many hours has it traveled?: '))
print ('Hour', '\tDistance Traveled')
for currentHour in range (1, timeTraveled +1):
    distanceTraveled = vehicleSpeed * currentHour
    print (currentHour, '\tdistanceTraveled')


