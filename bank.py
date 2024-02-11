# bank.py
# This program reads in two money amounts in cent and prints the result in euro with the decimal point between the euro and cent amount. 
# Author: Louise Ryan
# updated code to remove floating point numbers being used in the calculation to give a more accurate result. 

x = int(input('Enter amount 1:(in cent)'))
y = int(input('Enter amount 2:(in cent)'))
sum = (x + y) # /100 used previously to give a decimal value to convert from cent to euro, however this creates a floating point number that will not be as accurate. 

# floor division rounds the division to the nearest whole number and removes digits after the decimal point to give an integer value. 
#sum1 = (sum)//100
# modulus division gives the remainder 
#sum2 = (sum) % 100


#combining the two will give an accurate result. 

print(f"The sum of these is €{sum}")



