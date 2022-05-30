# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Uses user-modules & dictionary to compute payment for a company

# Imports other files
from getInputsFile import getInputs
from computePayFile import computePay
from printPayFile import printPay

# Function is used to call other functions
# Paramaters: None
# Returns: None
def payProcess():
    '''
    This function is to process all other fucntions to get inputs,
    calculate and print the pay stub
    '''

    theDict = getInputs()
    theDict = computePay(theDict)
    printPay(theDict)

if __name__ == '__main__':
    payProcess()
    

'''
My Output #1
Enter your company Name: Amazon
Enter Hours: 45
Enter Rate: 2.5
------------------------------------------------------------
Company worked at: Amazon
Payment amount: $118.75
------------------------------------------------------------

My Output #2
Enter your company Name: Little Ceasers
Enter your company Name: Google
Enter Hours: 20
Enter Rate: 2
------------------------------------------------------------
Company worked at: Google
Payment amount: $40.0
------------------------------------------------------------
'''