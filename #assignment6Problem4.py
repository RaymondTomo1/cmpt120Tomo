# This will print the Syracuse sequence for a number someone inputs


def main():
    initalNum = int(input("Insert integer value for the Syracuse equation to start with:"))
    print (initalNum)
    equationList = [initalNum]
    while initalNum != 1:
        if (initalNum % 2) == 0:
            newValue = initalNum//2
            print(newValue)
            initalNum = newValue
        else:
            newValue = initalNum * 3 + 1
            print(newValue)
            initalNum = newValue
main()




