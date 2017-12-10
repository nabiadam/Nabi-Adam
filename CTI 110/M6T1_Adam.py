# CTI 110
# M6T1: Kilometer Converter
# Nabi Adam
# 10/24/17

def askUserForKilometers():
    userKilometers = float (input('Enter the distance in kilometers?'))
    return userKilometers
def convertKilometersToMiles(userKilometers):
    miles = userKilometers * 0.6214
    return miles
def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles(userKilometersTyped)

    print (userKilometersTyped, 'Kilometers converted to miles is', \
           format(convertedMiles),'miles.')

main()
