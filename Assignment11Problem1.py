

#-Makes a program to keep track of Conference Attendees


class Attendee:

    def __init__(self, name, company, state, email):
        self.name = name 
        self.company = company
        self.state = state
        self.email = email
        self.Attendee = [self.name,self.company, self.state, self.email]
    
    def getName(self):
        return self.name
    
    def getCompany(self):
        return self.company
    
    def getState(self):
        return self.state
    def getEmail(self):
        return self.email
    def displayAtten(self):
        print (self.name, self.company, self.state, self.email)


class Conference:
    def __init__(self):
        self.attendees= []
    
    def makeAttendees(self, name, company, state, email):
        attendee= Attendee(name,company,state,email)
        self.attendees.append(attendee)
    
    def removeAttendee(self,name):
     for attendee in self.attendees:
            if attendee.getName():
                self.attendees.remove(attendee)
                print (name, " has been removed")
    
    def getAttendee(self,name):
        for Attendee in self.attendees:
            if Attendee.getName():
                return Attendee
    
    def findName(self,name):
        for Attendee in self.attendees:
            if Attendee.getName() == name:
                return Attendee

    def findState(self, state):
        results = []
        for Attendee in self.attendees:
            if Attendee.getState() == state:
                results.append(Attendee)
        return results
    def findCompany(self, company):
        for Attendee in self.attendees:
            if Attendee.getCompany()== company:
                return Attendee
    def findEmail(self, email):
        for Attendee in self.attendees:
            if Attendee.getEmail()== email:
                return Attendee


def addFileAttens(filename,Conference):
        file = open(filename, 'r') 
        for line in file: 
            lineList=str(line)
            a1=[]
            a1=lineList.split(",")
            Conference.attendees.append(a1)
        return Conference.attendees





def main():
    Conference1 = Conference()
    Conference1.makeAttendees("Bob", "IBM", "NY", "bob340@googlemail.com")
    Conference1.makeAttendees("Nick", "Amtrak", "NY", "NotNickAgain@googlemail.com")
    Bob= Conference1.getAttendee("Bob")
    list = Conference1.findState("NY")
    for Attendee in list:
        print (Attendee.getName())
    Conference1.removeAttendee("Nick")
    
    print(list)
    print(Bob.getName())
    print(Bob.getState())
    print(Bob.getCompany())
    print(Bob.getEmail())
    print(Bob.displayAtten())
    addFileAttens("conferencelist.txt",Conference1)
    print(Conference1.attendees)
    
main()