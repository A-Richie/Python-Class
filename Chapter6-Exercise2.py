# Chapter 6 - Exercise 2
# Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Creates a dictionary of friends and compares values and inserts values into the dictionary

friends_Dictionary = {"2017": ["Fred", "Becky", "Abigail"], "2018": ["Hailey", "Alex", "Penny"]}

# Prints only the friends (No "[]" or ",")
print("Here is a list of every friend: ")
for key in friends_Dictionary:
    for friend in friends_Dictionary[key]:
        print(friend)

friend_Name = input("Enter a friend's name: ")

# Checks the friend name against the two key values
if friend_Name in friends_Dictionary["2017"]:
    print(friend_Name + " is a friend from 2017")
elif friend_Name in friends_Dictionary["2018"]:
    print(friend_Name + " is a friend from 2018")
else:
    print(friend_Name + " is not a friend.")

new_Friend = input("Please enter a new friend name to be added: ")
year = input("Enter a year to add the friend to the dictionary: ")

# Error handling for user year
while year != "2017" and year != "2018":
    year = input("Please enter either the year 2017 or 2018. ")

# Only two cases - no need for elif (error handling was done earlier)
if year == "2017":
    friends_Dictionary["2017"].append(new_Friend)
else:
    friends_Dictionary["2018"].append(new_Friend)

# Prints only the friends (No "[]" or ",")
print("Here is a list of every friend: ")
for key in friends_Dictionary:
    for friend in friends_Dictionary[key]:
        print(friend)

'''
    My Output #1
Here is a list of every friend: 
Fred
Becky
Abigail
Hailey
Alex
Penny
Enter a friend's name: Janet
Janet is not a friend.
Please enter a new friend name to be added: Jacob
Enter a year to add the friend to the dictionary: 2020
Please enter either the year 2017 or 2018. 2018
Here is a list of every friend: 
Fred
Becky
Abigail
Hailey
Alex
Penny
Jacob

    My Output #2
Here is a list of every friend: 
Fred
Becky
Abigail
Hailey
Alex
Penny
Enter a friend's name: Becky
Becky is a friend from 2017
Please enter a new friend name to be added: Casey
Enter a year to add the friend to the dictionary: 2017
Here is a list of every friend: 
Fred
Becky
Abigail
Casey
Hailey
Alex
Penny
'''