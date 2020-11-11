#-This will shuffle the values in a list around when placed through the list

import random

from random import*


def shuffle(inputList):
    shuffledList=[]
    for i in range(len(inputList)):
        x = int(random() * len(inputList)) -1
        shuffledList.append(inputList[x])
        inputList.remove(inputList[x])
        
    return(shuffledList)

def main():
    inputList = [1,2,3,4,5]
    print (inputList)
    print (shuffle(inputList))


main()


