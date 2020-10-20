#-This is a program that will simulate a one bit adder

def and_g(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def or_g(a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def not_g(a):
    if a == 1:
        return 0
    else:
        return 1

def nand_g(a,b):
    if a ==1 and b == 1:
        return 0
    else:
        return 1

def xor_g(a,b):
    if a == 1 and b == 1:
        return 0
    if a == 1 and b == 0:
        return 1
    if a== 0 and b == 1:
        return 1
    if a == 0 and b == 0:
        return 0

def one_bit_adder(a,b,ci):
 # Calculate sumAdder
    XOR1 = (xor_g(a,b))
    sumAdder = (xor_g(XOR1, ci))

 # Calculate co

    AND1= and_g(XOR1,ci)
    AND2= and_g(a,b)
    co= or_g(AND1, AND2)

    print (sumAdder)
    print (co)

one_bit_adder(1,1,0)