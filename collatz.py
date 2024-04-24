# collatz.py
# This program asks the user to input a positive integer
# if even the value is divided by 2, if odd the value is multiplied by 3 and add one. 
# collatz program ends when the value 1 is reached
# Author: Louise Ryan



number = input("Please enter a positive integer:")  


while not number.isdigit() or int(number) <= 0:  # while not loop to continue executing the  error code as long as the user input is not a positive integer or a digit. 
    print("Error: Please enter a positive integer.")  # error message if input is not a positive integer.
    number = input("Please enter a positive integer:")  # reenter user input after the error message.

number = int(number)                        # convert input to integer

while number != 1:                          # while loop as long as number is not equal to 1
    print(number,end=' ')                   # end='' gives space between values instead of a new line
    if number % 2 == 0:                     # remainder is 0--> even, therefore divide by 2
        number = number // 2                # floor division used to give whole number and remove floating point numbers
    else: 
        number = 3*number + 1               # odd number, therefore multiply by 3 and add 1
print(number)                                  





# References: 
# https://www.w3schools.com/python/ref_string_isdigit.asp
# https://realpython.com/python-do-while/
# https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/
# https://www.w3schools.com/python/python_while_loops.asp
# https://realpython.com/python-while-loop/
# https://www.youtube.com/watch?v=094y1Z2wpJg&t=1s&ab_channel=Veritasium
# https://en.wikipedia.org/wiki/Collatz_conjecture
