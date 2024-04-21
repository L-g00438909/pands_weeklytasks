# modifed code to deal with account numbers of any length

numberentered = False # boolean value set to false. while loop will continue until a valid number is entered

while numberentered == False:  # while loop to keep prompting user if a non numerical value is entered
    accountnumber = input("Please enter an account number: ")
    if accountnumber.isdigit(): #isdigit to check if the number is a digit 
        newaccountnumber = "x" * (len(accountnumber)-4) + accountnumber[-4:] # "x"*len(accountnumber)-4 hides all input and -4 removes 4 digits. splicing adds 4 unhidden digits to the end of the number
        print("Your account number is", newaccountnumber)
        numberentered = True    # while loop exited when numerical value is entered, preventing an infinite loop
    else: # if any number </> 10 is entered instruction in the else statement will be carried out 
        print("Error!")


# assumptions:  
# account number will be numerical
# account number will be an integer   
# account numbers may be of different lengths and formats depending on which bank/country
# account number will be longer than 4 digits. last 4 digits are typically shown with the remainder hidden to protect privacy
# may need to add another verification step such as a pin number for security

# References:
# https://www.w3schools.com/python/ref_string_isdigit.asp