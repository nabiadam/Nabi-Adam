# CTI 110
# M6T2: Feet to Inches Converter
# Nabi Adam
# 10/26/17

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter the number in feet:'))
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
def feet_to_inches(feet):
    return feet* INCHES_PER_FOOT
main ()


    


