# Asks the user for an even numerical input to prove the Goldbach conjecture 

def isEven (num):
    if (num % 2) == 0:
        return True
    else:
        return False

def main():
    num1 = int(input("Insert an even number into the program:"))
    if isEven(num1) == True:
        primes = []
        primes = list (range(1, num1))
        print(primes)
        for i in primes:
            if (i % 2) == 0 :
                primes.remove (i)
        print(primes)
        for  i in primes:
            if (i + primes [-1]) == num1:
                print (i, primes [-1])

main()