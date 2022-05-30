# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Takes a user input for an email and finds the domain of the email
#               (and handles invalid emails)

checkemail = True

#Keeps asking for a user to enter a valid email
while checkemail:
    email = input("Enter an email: ")

    #Check there is exactly one @ sign (for domain) and at least 1 "." in an email
    #AND checks that the @ sign is before a "." so it's username@domain.extention
    # CAN'T have username.domain@extention --> invalid
    if email.count("@") == 1 and email.count(".") > 0 and email.find("@") < email.rfind("."):
        checkemail = False
    else:
        print("Error. Invalid email")

atPos = email.find("@") #Gets the index of @
dotPos = email.rfind(".") #Gets index of right most "." (end of domain name) 

domain = email[atPos + 1: dotPos]
print("Email domain: " + domain)

'''
My Output(#1):
Enter an email: Kitty.Cat@gmail.com
Email domain: gmail

My Output(#2):
Enter an email: Flower.power@yahoo
Error. Invalid email
Enter an email: Flower@yahoo
Error. Invalid email
Enter an email: Flower.yahoo
Error. Invalid email
Enter an email: Flower.power@yahoo.com
Email domain: yahoo
'''