# This will simulate a game of craps

import random

from random import*



def rollGiver():
    rollDie = randrange (1,6) + randrange (1,6)
    return rollDie

def crapsGame():
    diceRoll = rollGiver()
    if diceRoll in (2,3,12):
        return (False)
    elif diceRoll in (7,11):
        return (True)
    else:
        diceRoll1 = rollGiver()
        while diceRoll1 != 7 or diceRoll1 != diceRoll:
            if diceRoll1 == 7:
                return False
            elif diceRoll1 == diceRoll:
                return True
            else:
                diceRoll1 = rollGiver()

def simCraps(numGames):
    wins = 0
    counter = 0
    while counter != numGames:
        if crapsGame() == True:
            wins = wins + 1
            counter= counter +1
        else:
            counter= counter +1
    return wins

def main():
    numGames = int(input("Please input the number of games you would like to simulate:"))
    win = simCraps(numGames)
    prob = win / numGames
    print ("The probabilty of you winnning", numGames, "games is:", prob)

main()





