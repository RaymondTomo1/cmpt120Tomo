#- This program will take the first two and last two characters of a given string and combine them into a new character

def main():
    a = eval(input("Insert a string in quotes here:"))
    print(len(a))
    aFirst2= a[0:2]
    positon1 = (len(a)-2)
    positon2 = len(a)
    aLast2= a[positon1 : positon2]
    a = aFirst2 + aLast2
    print (a)
main()