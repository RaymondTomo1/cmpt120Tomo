#-This will convert a list of strings that represent single-digit numbers into numbers.

strList= ["1","2","3", "4"]
print("strList starts out as:", strList)

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return(strList)
toNumbers(strList)
print(strList)


