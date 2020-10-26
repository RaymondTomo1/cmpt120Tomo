# This program will simulate the probabilty of rolling five of a kind when rolling six dice. 

import random

from random import randrange

die1 = 0
die2 = 0
die3 = 0
die4 = 0
die5 = 0

die1= randrange(1,6)
die2= randrange(1,6)
die3= randrange(1,6)
die4= randrange(1,6)
die5= randrange(1,6)

def main():
    print ("Your rolls are:", die1, die2,die3,die4,die5)
    if (die1 == die2 == die3 == die4 == die5):
        print ("Congratulations, you rolled five of a kind!")
    else:
        print ("You did not roll five of a kind")

main()

