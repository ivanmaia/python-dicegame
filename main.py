from dice import *
from diceImages import getDiceImage

keepRolling = True

while keepRolling == True:
    playerChoice = input("Do you want do roll the dice? [Y/N]: ")
    if (playerChoice == "Y"):
        print(getDiceImage(rollDice()))
    else:
        keepRolling = False