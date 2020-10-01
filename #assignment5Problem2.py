#- Computates the date of easter in a given year

year= eval(input("Enter a year between 1982-2048 "))


def main():
    if year > 2048 :
        print ("Value not in range")
    if year < 1982 :
        print ("Value not in range")
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e =  (2*b + 4*c + 6*d + 5) % 7
    f = d + e
    g= 22 + f
    if g <= 31:
        print ("The date of Easter is ",  "March" ,   g ,  year)
    else:
        print ("The date of Easter is ",  "April" ,   (g-31) ,  year)
main()