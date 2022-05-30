# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Takes a user input for hours and a rate to
#               calculate a gross payment (with a bonus for 40+ hrs)
#               and has error handling for invalid inputs
#               uses while loops too AND uses functions with a company

import random

BONUS_MULTIPLIER = 1.5
BONUS_HOURS = 40
DOCUMENT_NUMBER = random.randint(1000, 2000)

# Main function - used as the driver method / calls other functions
# @Params - none
# @Return - none
def main():
    hours, rate, company = get_input()

    the_pay = compute_pay(hours, rate)

    print_output(the_pay, company, hours, rate)

# Gets input from user
# @Param - none
# @Return - inputed company name, hours and rate
def get_input():
    #Ask about company name - can include numbers or letters
    company = input("Enter your company name: ")
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

    return hours, rate, company


# Calculates the payment given an hours and rate
# @Param - hours worked, rate for payment
# @Return - computed payment total
def compute_pay(hours, rate):
    #Calculation for payment - bonus for 40+ hours 
    if hours > BONUS_HOURS :
        payment = (BONUS_HOURS * rate) + ((hours - BONUS_HOURS) * (BONUS_MULTIPLIER * rate))
    else : 
        payment = hours * rate
    return payment

#Prints output of payment
# @Param - payment
# @return - none
def print_output(payment, companyName, hours, rate):
    print("-" * 20) # Create a new line to seperate payment
    print("Company: " + companyName)
    print("Hours: ", hours)
    print("Rate: ", rate)
    print("Your document number is: ", DOCUMENT_NUMBER)
    print("Your " + companyName + " gross pay is " + str(round(payment, 2)) + " dollars.") # (rounds to nearest 2nd place after decimal)

#Calls the main function
main()

'''
    My Result (#1):
    Enter your company name: Google
    Enter Hours: ten
    Error. Enter a numeric value
    Enter Hours: 5
    Enter Rate: three
    Error. Enter numeric value
    Enter Rate: -3
    Error. Please enter a positive rate value
    Enter Rate: 3
    --------------------
    Company: Google
    Hours:  5.0
    Rate:  3.0
    Your document number is:  1479
    Your Google gross pay is 15.0 dollars.

        My Result (#2):
    Enter your company name: Microsoft
    Enter Hours: -45
    Error. Please enter a positve value
    Enter Hours: 46
    Enter Rate: -10
    Error. Please enter a positive rate value
    Enter Rate: ten
    Error. Enter numeric value
    Enter Rate: 10
    --------------------
    Company: Microsoft
    Hours:  46.0
    Rate:  10.0
    Your document number is:  1198
    Your Microsoft gross pay is 490.0 dollars.


        My Result (#3):
    Enter your company name: Blue
    Enter Hours: 48
    Enter Rate: 3.89
    --------------------
    Company: Blue
    Hours:  48.0
    Rate:  3.89
    Your document number is:  1415
    Your Blue gross pay is 202.28 dollars.

'''