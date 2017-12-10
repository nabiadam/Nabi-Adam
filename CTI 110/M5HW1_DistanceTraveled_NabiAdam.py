# CTI-110
# M5HW1 - Distance Traveled
# Nabi Adam
# 10/10/2017

vehicleSpeed = float(input('What is the speed of the vehicle in mph?: '))
timeTraveled = int (input('How many hours has it traveled?: '))

print ('Hour', '\tDistance Traveled')
for currentHour in range (1, timeTraveled +1):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour, '\t', distanceTraveled)
