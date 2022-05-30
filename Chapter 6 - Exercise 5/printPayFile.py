# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Uses user-modules & dictionary to compute payment for a company

# Prints the payment for a dictonary with one key to one value
# Paramaters: a dictionary
# Returns: the same dictionary
def printPay(theDict):

    print("---" * 20)
    for key in theDict:
        print("Company worked at: " + key)
        print("Payment amount: $" + str(theDict[key]))
    print("---" * 20)
    return theDict