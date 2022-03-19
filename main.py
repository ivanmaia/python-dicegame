from dice import *

keepRolling = True

while keepRolling == True:
    playerChoice = input("Do you want do roll the dice? [Y/N]: ")
    if (playerChoice == "Y"):
        print(rollDice())
    else:
        keepRolling = False