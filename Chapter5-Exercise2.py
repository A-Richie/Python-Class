# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Takes a user input for hours and a rate to
#               calculate a gross payment (with a bonus for 40+ hrs)
#               and has error handling for invalid inputs
#               uses while loops too AND uses functions


#Global Constants
BONUS_MULTIPLIER = 1.5
BONUS_HOURS = 40

# Main function - used as the driver method / calls other functions
# @Params - none
# @Return - none
def main():
    the_hours, the_rate = get_input()

    the_pay = compute_pay(the_hours, the_rate)

    print_output(the_pay)

# Gets input from user
# @Param - none
# @Return - inputed hours and rate from user
def get_input():

    #Loops through for valid input
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

    #Loops through for valid input
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

    return hours, rate


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

# Prints output of payment
# @Param - payment
# @return - none
def print_output(payment):
    print("") # Create a new line to seperate payment
    print("Pay: $" + str(round(payment, 2))) # rounds to nearest 2nd place after decimal


#Calls the main function
main()

'''
    My Result (#1):
Enter Hours: -12
Error. Please enter a positve value
Enter Hours: 12
Enter Rate: -42.5
Error. Please enter a positive rate value
Enter Rate: five
Error. Enter numeric value
Enter Rate: 3.5

Pay: $42.0

    My Result (#2):
Enter Hours: fifty
Error. Enter a numeric value
Enter Hours: -50
Error. Please enter a positve value
Enter Hours: 50
Enter Rate: 10

Pay: $550.0

'''