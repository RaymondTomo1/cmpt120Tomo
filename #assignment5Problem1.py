#- This program will compute the fine based on the speed limit and the speed the car was going

speedLimit= 0
givenSpeed= 0
fine= 0


def main():
    if givenSpeed <= speedLimit:
        print ("Speed is legal")
    else:
        fine = 50 + ((givenSpeed- speedLimit) *5)
        if givenSpeed > 90: # JA
            fine = fine + 200
        print ("The fine is", fine)
    
           
         

speedLimit= eval(input("Insert the speed limit here:"))   
givenSpeed= eval(input("Insert the speed the car was going here"))
main()



