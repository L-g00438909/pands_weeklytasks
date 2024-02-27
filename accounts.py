# accounts.py
# This program reads in a 10 character account number and outputs the number with only the last 4 digits showing. 
# Author: Louise Ryan

numberentered = False

while numberentered == False:       # while loop to keep prompting user to enter 10 digits
    accountnumber = input("Please enter a 10 digit account number: ")  # Reads in a 10 digit number from the user
    if len(accountnumber) == 10:    # if else checks if the correct number of digits are entered                                     
         newaccountnumber = "x" *6 + accountnumber[-4:]    # last 4 characters are sliced/taken out from the end of the string-->7890
         print("Your account number is", newaccountnumber)
         numberentered = True       # exit the while loop to prevent an infinite loop
    else:
         print("Error!")
         
         









