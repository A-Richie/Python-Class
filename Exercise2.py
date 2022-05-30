# Name: Alyssa Richie
# Date: 4/22/2022
# CIS 41A Python Programming 50Z
# Description: Takes a user input for hours and a rate to
#               calculate a gross payment (with a bonus for 40+ hrs)

BONUS_MULTIPLIER = 1.5
BONUS_HOURS = 40
#Gets user input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

#Calculation for payment - bonus for 40+ hours 
if hours > BONUS_HOURS :
    payment = (BONUS_HOURS * rate) + ((hours - BONUS_HOURS) * (BONUS_MULTIPLIER * rate))
else : 
    payment = hours * rate

#Print payment quantity
# (rounds to nearest 2nd place after decimal)
print("") # Create a new line to seperate payment
print("Pay: " + str(round(payment, 2)))


'''
My Result (#1):
Enter Hours: 45
Enter Rate: 2.48

Pay: 117.8

My Result (#2):
Enter Hours: 32
Enter Rate: 1.67

Pay: 53.44

'''