# Name: Alyssa Richie
# Date: 4/11/2022
# CIS 41A Python Programming 50Z
# Description: Takes a user input for hours and a rate to
#               calculate a gross payment


#Gets user input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

#Calculation for payment (rounds to nearest 2nd place after decimal)
payment = hours * rate
payment = round(payment, 2)

#Print payment quantity
print("") # Create a new line to seperate payment
print("Pay: " + str(payment))


'''
My Result (#1):
Enter Hours: 34
Enter Rate: 2.48

Pay: 84.32

My Result (#2):
Enter Hours: 32
Enter Rate: 1.67

Pay: 53.44

'''