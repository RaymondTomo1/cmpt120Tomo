# This program will ask the user for a number of the Fibonacci sequence and will 



def main():
    loopNum= int(input("Insert the number of the Fibbonachi Sequence you would like to see"))
    n1, n2 = 1, 1
    count =0
    newNum= 0
    while count < loopNum - 2:
        newNum = n1 + n2
        n1 = n2
        n2 = newNum
        count += 1
    print (newNum)

main()
