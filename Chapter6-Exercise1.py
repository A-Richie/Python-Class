# Chapter 6 - Exercise 1
# Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Creates two lists of friends and compares values and inserts values into the lists


Twenty_Seventeen_Friends = ["Abigail", "Penny", "Sebastian", "Leah", "Sam"]
Twenty_Eighteen_Friends = ["Alex", "Maru", "Emily", "Shane", "Harvey"]

print(Twenty_Seventeen_Friends + Twenty_Eighteen_Friends)

find_Friend = input("Enter a name of a friend: ")

#Checks for the inputted friend for both lists and has a case for not being in either list
if find_Friend in Twenty_Seventeen_Friends:
    print("The friend " + find_Friend + " was found in the 2017 friend list\n")
elif find_Friend in Twenty_Eighteen_Friends:
    print("The friend " + find_Friend + " was found in the 2018 friend list\n")
else:
    print("The friend " + find_Friend + " NOT was found in either the 2017 friend list or 2018 friend list\n")

#asks for a new friend to be added to a list and what list to add it to
insert_Friend = input("Enter a new friend name to insert into a list ")
list_for_insert = input("What list should you add it to? (2017 or 2018) ")

#Checks the user input to add the friend to the correct list (does not add if not 2017 or 2018)
if list_for_insert == "2017":
    Twenty_Seventeen_Friends.append(insert_Friend)
elif list_for_insert == "2018":
    Twenty_Eighteen_Friends.append(insert_Friend)
else:
    print("That is not a valid year for the list")

#prints both friend lists
print("2017 Friend List: ",  Twenty_Seventeen_Friends)
print("2018 Friend List: ", Twenty_Eighteen_Friends)


'''
Output #1
['Abigail', 'Penny', 'Sebastian', 'Leah', 'Sam', 'Alex', 'Maru', 'Emily', 'Shane', 'Harvey']
Enter a name of a friend: Sam      
The friend Sam was foud in the 2017 friend list

Enter a new friend name to insert into a list Robin
What list should you add it to? (2017 or 2018) 2017
2017 Friend List:  ['Abigail', 'Penny', 'Sebastian', 'Leah', 'Sam', 'Robin']
2018 Friend List:  ['Alex', 'Maru', 'Emily', 'Shane', 'Harvey']

Output #2 
['Abigail', 'Penny', 'Sebastian', 'Leah', 'Sam', 'Alex', 'Maru', 'Emily', 'Shane', 'Harvey']
Enter a name of a friend: Mariah
The friend Mariah NOT was found in either the 2017 friend list or 2018 friend list

Enter a new friend name to insert into a list Casey
What list should you add it to? (2017 or 2018) 2017
2017 Friend List:  ['Abigail', 'Penny', 'Sebastian', 'Leah', 'Sam', 'Casey']
2018 Friend List:  ['Alex', 'Maru', 'Emily', 'Shane', 'Harvey']
'''