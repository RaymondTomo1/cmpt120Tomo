#- In this program, the first letter of the string after the first occurance will be changed to a different character.
def main():
    #- We will have the user input a string first.
    a = eval(input("Input String Here (Put In Quotes):"))
    aFirstChar = a[0]
    aLen= len(a)
    print (aFirstChar)
    aSep= a[1:aLen]
    print (aSep)
    aSep = aSep.replace(aFirstChar, "$")
    a= aFirstChar + aSep
    print (a)
main()