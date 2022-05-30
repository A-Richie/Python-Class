# Name: Alyssa Richie
# Team: RJDAY
# CIS 41A Python Programming 50Z
# Description: Menu program for De Anza Food Court

#Global constants
STUDENT_TAX_RATE = 0.00
STAFF_TAX_RATE = 0.09 # Out of 100 --> 9% == 0.09
UNDECLARED_VALUE = 0
BURGER_1_NAME = "De Anza Burger"
BURGER_2_NAME = "Bacon Cheese"
BURGER_3_NAME = "Mushroom Swiss"
BURGER_4_NAME = "Western Burger"
BURGER_5_NAME = "Don Cali Burger"
BURGER_1 = 5.25
BURGER_2 = 5.75
BURGER_3_4_5 = 5.95

#Students = no tax || 9% tax for staff

# This is the main function
# Paramaters: none
# Returns: none
def main():
    show_menu()
    quantity1, quantity2, quantity3, quantity4, quantity5, staffOrStudent = get_inputs()
    beforeBill, salesTax, finalBill = compute_bill(quantity1, quantity2, quantity3, quantity4, quantity5, staffOrStudent)
    print_bill(quantity1, quantity2, quantity3, quantity4, quantity5, staffOrStudent, beforeBill, salesTax, finalBill)




# Shows the menu for user
# Paramaters: none
# Returns: none
def show_menu():
    print("\nWelcome to the De Anza Grill! \n")
    print("1. " + BURGER_1_NAME + " - $" + str(BURGER_1))
    print("2. " + BURGER_2_NAME + " - $" + str(BURGER_2))
    print("3. " + BURGER_3_NAME + " - $" + str(BURGER_3_4_5))
    print("4. " + BURGER_4_NAME + " - $" + str(BURGER_3_4_5))
    print("5. " + BURGER_5_NAME + " - $" + str(BURGER_3_4_5))

# Gets input from user
# Paramaters: None
# Returns: input from user 5 quantities and tax amount
def get_inputs():
    # Local variables for function, gives them a all a default value of 0
    # so that if they don't order a specific item the item is already at a value of 0
    isStaff = UNDECLARED_VALUE
    quantity1 = UNDECLARED_VALUE
    quantity2 = UNDECLARED_VALUE
    quantity3 = UNDECLARED_VALUE
    quantity4 = UNDECLARED_VALUE
    quantity5 = UNDECLARED_VALUE
    selection = UNDECLARED_VALUE

    # flag1 - used to keep asking for inputs until the number entered is 6
    flag1 = True
    while flag1:
        try:
            # While the selection variable is valid or hasn't ordered yet do a while loop for quanity & selection
            selection = int(input("Select an item from the menu (1, 2, 3, 4, 5 or 6 to exit) "))
            while selection > 0 and selection < 6:

                try:
                    # Asks then checks the quanity entered is >= 0 (0 is valid and wouldn't affect a price/quanity of an item)
                    anyQuantity = int(input("How many of this item do you want to order? "))
                    while anyQuantity < 0:
                        print("Invalid quanity. Enter a quanity greater than 0 (or equal to 0)")
                        # Asks for the quanity again because the amount was invalid
                        anyQuantity = int(input("How many of this item do you want to order? "))
                    
                    # While loop for isStaff and checking a selection is valid for staff or student
                    # Won't allow there to be a word, or any other numeric value to be entered and only asks once
                    while isStaff == UNDECLARED_VALUE or isStaff != 1 and isStaff != 2:
                        try:
                            if(isStaff != UNDECLARED_VALUE):
                                print("Error, please select either \"1\" or \"2\"")
                            isStaff = int(input("Are you a student (1) or staff (2) "))
                        except:     # Catches any words
                            print("Error, use a numeric value of 1 or 2")

                    # Checks the selection to see were to add the quantity 
                    if selection == 1:
                        quantity1 += anyQuantity

                    elif selection == 2:
                        quantity2 += anyQuantity

                    elif selection == 3:
                        quantity3 += anyQuantity

                    elif selection == 4:
                        quantity4 += anyQuantity

                    elif selection == 5:
                        quantity5 += anyQuantity
                    
                    # Gets the next input (used to leave the loop)
                    selection = int(input("Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) "))
                    
                    # Checks that the selection is valid, only goes into loop if the value is invalid for the next selection
                    while selection <= 0 or selection > 6:
                        print("Error. Invalid selection try again")
                        selection = int(input("Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) "))

                # Except for if the user entered an invalid quantity (in word form)
                except:
                    print("Error. Enter a positive numeric value")
            
            # Checks the selection if it's 6 and changes the while loop flag to exit loop
            # Otherwise the selection was not 1-6  (ex -10, )
            if selection == 6:
                flag1 = False
            else:
                print("Error, invalid order number")        
        except:
            print("Try entering a positive number between 1 - 6")

    return quantity1, quantity2, quantity3, quantity4, quantity5, isStaff
            


# Computes cost of bill for user
# Paramaters: quantities for all the different burgers offered and if a student or staff is purchasing 
# Returns: cost for the bill
def compute_bill(quantity1, quantity2, quantity3, quantity4, quantity5, staffOrStudent):
    beforeTax = UNDECLARED_VALUE
    finalBill = UNDECLARED_VALUE
    salesTax = UNDECLARED_VALUE
    beforeTax = (quantity1 * BURGER_1) + (quantity2 * BURGER_2) + (quantity3 * BURGER_3_4_5) + (quantity4 * BURGER_3_4_5) + (quantity5 * BURGER_3_4_5)

    #Checks if a staff member - add tax
    if staffOrStudent == 2:
        salesTax = beforeTax * STAFF_TAX_RATE
        finalBill = beforeTax + salesTax
    else:
        salesTax = STUDENT_TAX_RATE
        finalBill = beforeTax
    return beforeTax, salesTax, finalBill

# Prints the cost of the bill
# Paramaters: quantities for each burger, cost of bill (total), stafforStudent number
# Returns: none
def print_bill(quantity1, quantity2, quantity3, quantity4, quantity5, staffOrStudent, beforeTaxBill, salesTax, AfterTaxBill):
    #Thanks the user - decided to put it in print_bill to combine as much printing into this function rather than in get_inputs
    print("~" * 50)
    print("\nThank you, we hope to see you again! \n")

    print("Quanity  | Order | Total cost for the item")
    print(str(quantity1) + " " + BURGER_1_NAME + " $" + str(BURGER_1 * quantity1))
    print(str(quantity2) + " " + BURGER_2_NAME + " $" + str(BURGER_2 * quantity2))
    print(str(quantity3) + " " + BURGER_3_NAME + " $" + str(BURGER_3_4_5 * quantity3))
    print(str(quantity4) + " " + BURGER_4_NAME + " $" + str(BURGER_3_4_5 * quantity4))
    print(str(quantity5) + " " + BURGER_5_NAME + " $" + str(BURGER_3_4_5 * quantity5))
    print("-" * 50)

    if staffOrStudent == 1:
        print("Subtotal $" + str(round(beforeTaxBill, 2))) # Uses the full cost of bill because 0 tax amount
        print("Sales Tax $" + str(round(salesTax, 2)))
    else:
        print("Subtotal $" + str(round(beforeTaxBill, 2)))
        print("Sales Tax $" + str(round(salesTax, 2)))

    print("-" * 50)
    print("Total $" + str(round(AfterTaxBill, 2)))
    

main()

'''
Output #1

Welcome to the De Anza Grill!

1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Select an item from the menu (1, 2, 3, 4, 5 or 6 to exit) 2
How many of this item do you want to order? 5
Are you a student (1) or staff (2) 2
Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) 3
How many of this item do you want to order? 1
Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thank you, we hope to see you again!

0 De Anza Burger $0.0
5 Bacon Cheese $28.75
1 Mushroom Swiss $5.95
0 Western Burger $0.0
0 Don Cali Burger $0.0
--------------------------------------------------
Subtotal $34.7
Sales Tax $3.12
--------------------------------------------------
Total $37.82

Output #2
Welcome to the De Anza Grill!

1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Select an item from the menu (1, 2, 3, 4, 5 or 6 to exit) -10
Error, invalid order number
Select an item from the menu (1, 2, 3, 4, 5 or 6 to exit) five
Try entering a positive number between 1 - 6
Select an item from the menu (1, 2, 3, 4, 5 or 6 to exit) 2
How many of this item do you want to order? -10
Invalid quanity. Enter a quanity greater than 0 (or equal to 0)
How many of this item do you want to order? ten
Error. Enter a positive numeric value
How many of this item do you want to order? 0
Are you a student (1) or staff (2) two
Error, use a numeric value of 1 or 2
Are you a student (1) or staff (2) -2
Error, please select either "1" or "2"
Are you a student (1) or staff (2) 3
Error, please select either "1" or "2"
Are you a student (1) or staff (2) 2
Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) 1
How many of this item do you want to order? 3
Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) 1
How many of this item do you want to order? 3
Select another item from the menu (1, 2, 3, 4, 5 or 6 to exit) 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thank you, we hope to see you again!

Quanity  | Order | Total cost for the item
6 De Anza Burger $31.5
0 Bacon Cheese $0.0
0 Mushroom Swiss $0.0
0 Western Burger $0.0
0 Don Cali Burger $0.0
--------------------------------------------------
Subtotal $31.5
Sales Tax $2.83
--------------------------------------------------
Total $34.34
'''