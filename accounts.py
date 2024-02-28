# accounts.py
# This program reads in a 10 character account number and outputs the number with only the last 4 digits showing. 
# Author: Louise Ryan
"""
numberentered = False

while numberentered == False:       # while loop to keep prompting user to enter 10 digits
    accountnumber = input("Please enter a 10 digit account number: ")  # Reads in a 10 digit number from the user
    if len(accountnumber) == 10:    # if else checks if the correct number of digits are entered  
         # if 10 digits entered, the instructions in the if statement will be carried out                                   
         newaccountnumber = "x" *6 + accountnumber[-4:]   
          # "x"*6 hides the first six characters 
          # last 4 characters are sliced/taken out from the end of the string
         print("Your account number is", newaccountnumber)
         numberentered = True     # exit the while loop to prevent an infinite loop when the number is 10 digits 
    else: # if any number </> 10 is entered instruction in the else statement will be carried out
               print("Error!")
         
 """        
# modifed code to deal with account numbers of any length

numberentered = False

while numberentered == False:  # while loop to keep prompting user if a non numerical value is entered
    accountnumber = input("Please enter an account number: ")
    if accountnumber.isdigit(): #isdigit to check if the number is a digit (Reference:https://www.w3schools.com/python/ref_string_isdigit.asp)
        newaccountnumber = "x" * (len(accountnumber)-4) + accountnumber[-4:] # "x"*len(accountnumber)-4 hides all input and -4 removes 4 digits. splicing adds 4 unhidden digits to the end of the number
        print("Your account number is", newaccountnumber)
        numberentered = True    # while loop exited when numerical value is entered, preventing an infinite loop
    else:
        print("Error!")


# assumptions:
        
# account numbers may be of different lengths and formats depending on which bank/country
# account number will be longer than 4 digits. last 4 digits are typically shown with the remainder hidden to protect privacy
# may need to add another verification step such as a pin number for security
# 
             









