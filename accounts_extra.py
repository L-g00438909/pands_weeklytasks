# accounts_extra.py
# This program reads in an account number and outputs the number with only the last 4 digits showing
# Modifed code to deal with account numbers of any length. Refer to accounts.py for the original code that only deals with 10 digit account numbers.
# Author: Louise Ryan

numberentered = False # boolean value set to false. while loop will continue until a valid number is entered

while numberentered == False:  # while loop to keep prompting user if a non numerical value is entered
    accountnumber = input("Please enter an account number: ")
    if accountnumber.isdigit(): #isdigit to check if the number is a digit 
        newaccountnumber = "x" * (len(accountnumber)-4) + accountnumber[-4:] # "x"*len(accountnumber)-4 hides all input and -4 removes 4 digits. splicing adds 4 unhidden digits to the end of the number
        print("Your account number is", newaccountnumber)
        numberentered = True    # while loop exited when numerical value is entered, preventing an infinite loop
    else: # if any number </> 10 is entered instruction in the else statement will be carried out 
        print("Error!")



# References:
# https://www.w3schools.com/python/ref_string_isdigit.asp