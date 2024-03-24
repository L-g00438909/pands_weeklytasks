# sqrt.py
# This program takes a positive floating point number as input and outputs an approximation of its square root.
# Newton Raphson method used to approximate square root. For any number N, the square root is 0.5 * (X + N/X)
# Author: Louise Ryan


def sqrt(number):    # defines a function called sqrt with the parameter number to calculate the square root of the entered value. 
                     # A function is a block of code that only runs when it is called. 
    
     
    guess = number / 2.0   # Initial guess for the square root
    
    while (guess * guess - number) > 0.0001 and number > 0:   #  guess*guess-number-->the difference between the squared guess and actual number we want to approximate
                                                              #  checks if the squared value of the guess minus the original number is >0.0001. if >0.0001 iterations continue
                                                              #  number > 0 ensures a positive number 
        guess = 0.5 * (guess + number / guess)  # works with (guess*guess-number)> 0.0001 and number > 0 to iteratively refine the guess 
                                                # until its close enough to the square root to be considered accurate. 
                                                # when condition is met, while loop returns guess 

    return guess


while True:
      enternumber = float(input("Please enter a positive number: ")) # Take a positive floating-point number as input
      result = sqrt(enternumber)
      if enternumber > 0:
            print(f"The square root of {enternumber} is approximately {result}")
            break
      else:
          print("Try again!")
            


