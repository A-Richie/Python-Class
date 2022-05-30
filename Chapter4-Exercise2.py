# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Takes a user input for hours and a rate to
#               calculate a gross payment (with a bonus for 40+ hrs)
#               and has error handling for invalid inputs
#               uses while looops too

import random

BONUS_MULTIPLIER = 1.5
BONUS_HOURS = 40

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

#Calculation for payment - bonus for 40+ hours 
if hours > BONUS_HOURS :
    payment = (BONUS_HOURS * rate) + ((hours - BONUS_HOURS) * (BONUS_MULTIPLIER * rate))
else : 
    payment = hours * rate

#Create random doccument number
documentNumber = random.randint(1000, 2000)

#Print payment quantity
# (rounds to nearest 2nd place after decimal)
print("") # Create a new line to seperate payment

print("Your document number is: ", documentNumber )
print("Pay: $" + str(round(payment, 2)))

'''
    My Result (#1):
Enter your company name: Microsoft
Enter Hours: 27
Enter Rate: -15
Error. Please enter a positive rate value
Enter Rate: ninty
Error. Enter numeric value
Enter Rate: 4

Your document number is:  1346
Pay: $108.0

    My Result (#2):
Enter your company name: 8x8
Enter Hours: Four
Error. Enter a numeric value
Enter Hours: -4
Error. Please enter a positve value
Enter Hours: 30    
Enter Rate: 10

Your document number is:  1856
Pay: $300.0

    My Result (#3):
Enter your company name: Blue   
Enter Hours: 48
Enter Rate: 3.89

Your document number is:  1831
Pay: $202.28

'''