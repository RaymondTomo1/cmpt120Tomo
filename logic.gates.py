#-This is a program that will simulate several logic gates 

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

