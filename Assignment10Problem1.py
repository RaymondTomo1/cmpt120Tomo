#- This will create fuctions to mimic other python commands 

def count (inputList, x):
    counter = 0
    for i in inputList:
        if i == x:
            counter = counter + 1
    return counter

def isin(inputList, x):
    for i in inputList:
        if i == x:
            return True

def index (inputList,x):
    for i in range (len(inputList)):
        if inputList[i] == x:
            return i
            


def reverse(inputList):
    reverseList= []
    for i in range (len(inputList)):
        x = inputList[-1 * (i + 1)]
        reverseList.append(x)
    return (reverseList)

def sort(inputList):
    sortList = []
    for i in range(len(inputList)):
        x = min(inputList)
        sortList.append(x)
        inputList.remove(x)
    return sortList



def main():
    ListTest = [7,5,8]
    print (isin(ListTest, 5))
    print (index(ListTest,8))
    print (reverse(ListTest))
    print (count (ListTest,7))
    print (sort(ListTest))
main()


    
