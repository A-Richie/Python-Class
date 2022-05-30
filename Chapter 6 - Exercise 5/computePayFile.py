# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Uses user-modules & dictionary to compute payment for a company

BONUS_MULTIPLIER = 1.5
BONUS_HOURS = 40
UNDEFINED_VALUE = -1 #undefined value isn't a valid number that's possible

# Computes the pay for a dictonary with a key : [list]
# Paramaters: a dictionary
# Returns: the same dictionary in the form key : value <- value = payment amount
def computePay(theDict):

    #First gets the values and puts them into variables to make it easier
    CompanyKey = UNDEFINED_VALUE
    rateValue = UNDEFINED_VALUE
    hoursValue = UNDEFINED_VALUE
    for key in theDict:
        CompanyKey = key
        for value in theDict[key]:
            if hoursValue == UNDEFINED_VALUE:
                hoursValue = value
            elif rateValue == UNDEFINED_VALUE:
                rateValue = value

    #Calculation for payment - bonus for 40+ hours 
    if hoursValue > BONUS_HOURS:
        payment = (BONUS_HOURS * rateValue) + ((hoursValue - BONUS_HOURS) * (BONUS_MULTIPLIER * rateValue))
    else: 
        payment = hoursValue * rateValue
    
    theDict[CompanyKey] = payment
    return theDict

    
