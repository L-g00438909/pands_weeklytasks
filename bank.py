# bank.py
# This program reads in two money amounts in cent and prints the result in euro with the decimal point between the euro and cent amount. 
# Author: Louise Ryan

x = int(input('Enter amount 1:(in cent)'))
y = int(input('Enter amount 2:(in cent)'))
sum = (x+y)/100
print (f"The sum of these is €{sum}")