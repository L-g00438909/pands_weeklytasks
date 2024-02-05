# bank.py
# This program reads in two money amounts in cent and prints the result in euro with the decimal point between the euro and cent amount. 
# Author: Louise Ryan
# https://www.w3schools.com/python/python_variables.asp 
# https://www.w3schools.com/python/python_datatypes.asp 
# https://www.w3schools.com/python/python_numbers.asp 
# https://www.w3schools.com/python/python_casting.asp 
# https://realpython.com/python-f-strings/

x = int(input('Enter amount 1:(in cent)'))
y = int(input('Enter amount 2:(in cent)'))
sum = (x+y)/100
print (f"The sum of these is €{sum}")