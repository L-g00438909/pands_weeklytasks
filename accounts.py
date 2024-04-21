# accounts.py
# This program reads in a 10 character account number and outputs the number with only the last 4 digits showing. 
# Author: Louise Ryan

numberentered = False # boolean value set to false. while loop will continue until a valid number is entered

while numberentered == False:       # while loop to keep prompting user to enter 10 digits
    accountnumber = input("Please enter a 10 digit account number: ")  # Reads in a 10 digit number from the user 
    if len(accountnumber)==10 and accountnumber.isdigit():    # if else checks if the correct number of digits are entered and if the number is a digit
         # if 10 digits entered, the instructions in the if statement will be carried out                                   
         newaccountnumber = "x" *6 + accountnumber[-4:]   
          # "x"*6 hides the first six characters of the account number
          # last 4 characters are sliced/taken out from the end of the string and added to the newaccountnumber
         print("Your account number is", newaccountnumber)
         numberentered = True     # exit the while loop to prevent an infinite loop when the number is 10 digits 
    else: # if any number </> 10 is entered instruction in the else statement will be carried out 
               print("Error!")
         


# Refer to accounts_extra.py for a modified version of this code that deals with account numbers of any length.
             
# assumptions:  
# account number will be numerical
# account number will be an integer   
# account numbers may be of different lengths and formats depending on which bank/country
# account number will be longer than 4 digits. last 4 digits are typically shown with the remainder hidden to protect privacy
# may need to add another verification step such as a pin number for security

# References:
# https://www.w3schools.com/python/ref_string_isdigit.asp
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/ref_func_len.asp
# https://www.w3schools.com/python/python_strings_slicing.asp
# https://www.w3schools.com/python/python_while_loops.asp



