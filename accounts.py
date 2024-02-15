# accounts.py
# This program reads in a 10 character account number and outputs the number with only the last 4 digits showing. 
# Author: Louise Ryan




accountnumber = int(input("Enter a 10 digit number:"))                   # eg:1234567890
accountnumber2 = str(accountnumber)                                      # convert to string as account numbers can be stored as strings. 
numberlength = len(accountnumber2)                                       # len can determine number of characters of the account number
a = numberlength -4                                                      # subtracting 4 from the account number length to give 123456
b = accountnumber2[a:]                                                   # slices the string to omit the first 6 characters to give 7890
c = ("x" *a + b)                                                         # string a(123456)* x to give xxxxxx +b(7890)
                        


while len(accountnumber2) !=10:         # while loop will allow the program to keep prompting the user to enter a 10 digit number if a number != 10 is used
     print("Error")
     accountnumber = int(input("Enter a 10 digit number:"))
        

if len(accountnumber2) == 10:           # when 10 characters are entered the program will print xxxxxx7890
     print("your account number is", c)





