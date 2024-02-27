# collatz.py
# This program asks the user to input a positive integer
# if even the value is divided by 2, if odd the value is multiplied by 3 and add one. 
# collatz program ends when the value 1 is reached
# Author: Louise Ryan
# Reference: https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/


number = int(input("Please enter a positive integer:"))

while number != 1:                          # while loop as long as number is not equal to 1
    print(number,end=' ')                   # end='' gives space between values instead of a new line
    if number % 2 == 0:                     # remainder is 0--> even, therefore divide by 2
        number = number // 2                # floor division used to give whole number and remove floating point numbers
    else: 
        number = 3*number + 1               # odd number, therefore multiply by 3 and add 1
print(number)                                  