
# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Uses user-modules & dictionary to compute payment for a company

# Company database list
COMPANYLIST = ["Amazon", "Google", "Apple", "Facebook", "Uber"]

# Gets the inputs from a user for a company and hours + rate worked
# Paramaters: none
# Returns: a dictionary in the form key : [list]
def getInputs():
    inputDict = dict()          # Input dictionary for return value
    listValue = list() 

    validateFlag = True
    validateAttempts = 0
    while validateFlag and validateAttempts <= 1:
        #Asks for user to input their company name
        userCompany = input("Enter your company Name: ")

        if userCompany in COMPANYLIST:
            validateFlag = False
        else:
            validateAttempts += 1
            if validateAttempts == 2:
                print(COMPANYLIST)

    checkerHours = True
    while checkerHours:
        #Uses try - except to make sure user enters a valid input
        try:
            #Gets user input
            hours = float(input("Enter Hours: "))
            if hours > 0:
                checkerHours = False
            else:
                print("Error. Please enter a positve value")
        except:
            print("Error. Enter a numeric value")

    checkerRate = True
    while checkerRate:
        try:
            rate = float(input("Enter Rate: "))
            if rate > 0 :
                checkerRate = False
            else:
                print("Error. Please enter a positive rate value")
        except:
            print("Error. Enter numeric value")
    
    listValue = [hours, rate]
    inputDict[userCompany] = listValue
    return inputDict
    
