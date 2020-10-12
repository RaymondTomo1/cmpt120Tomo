# This program will calculate the greatest common divisor between two values

def main ():
    val1= int(input("Insert the value of the first number here: "))
    val2= int(input("Insert the value of the second number here: "))
    m= val2
    n= val1
    while m != 0:
        n, m = m, (n % m)
    print (n)
main()

    
