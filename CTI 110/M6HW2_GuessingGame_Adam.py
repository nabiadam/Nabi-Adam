# 11/09/2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Nabi Adam

import random

def generateRandomNumber():
    randomNumber = random.randint (1, 100)
    return randomNumber

def askUserforNumber(message = 'Guess the Number:'):
    userNumber = int (input(message))
    return userNumber

def checkUserNumber(userNumber, randomNumber):
    if userNumber > randomNumber:
        return 'Too high'
    elif userNumber < randomNumber:
        return 'Too low'
    else:
        return 'Congratulations!'

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        userNumber = askUserforNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber (userNumber, randomNumber)

        while message != 'Congratulations!':
            print (message)
            userNumber = askUserforNumber('Try again:')
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber (userNumber, randomNumber)
        print ('It took you', userNumberOfGuesses, 'attempts to guess correctly')


        print (message)
        userCongratulated = True


main()
