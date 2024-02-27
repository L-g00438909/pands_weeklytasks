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
         
         



#while len(accountnumber2) !=10:         # while loop will allow the program to keep prompting the user to enter a 10 digit number if a number != 10 is used
     #print("Error")
     #ccountnumber = int(input("Enter a 10 digit number:"))
        

#if len(accountnumber2) == 10:           # when 10 characters are entered the program will print xxxxxx7890
    # print("your account number is", c)
     






