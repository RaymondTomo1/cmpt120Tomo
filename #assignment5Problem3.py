#- This calculates the day of the year based on user input

month=0
day=0
year=0
date = input("Enter the month, date, year in the following order(month/day/year):")
if  "/" not in date:
    print("Incorrect Input, please format the date")

date= date.split("/")

month=int(date[0])
day=int(date[1])
year= int(date[2])
leapyear= year
dayNum= 0

print(month)

def main():
    dayNum= (31 * (month- 1) + day)
    if month > 2:
        dayNum= dayNum - (( 4 *(month)+ 23) // 10)
    else:
        pass
    if ((int(leapyear) % 4) == 0):
        dayNum= dayNum +1
    print("The numeric date of this year is", dayNum)
       
    
    
    
main()
    