# weekday.py
# This program outputs whether or not today is a weekday
# Author: Louise Ryan

# https://docs.python.org/3/library/datetime.html#format-codes
# https://www.programiz.com/python-programming/datetime

import datetime

from datetime import datetime

def isaweekday():                                     # defines a function called isaweekday(). A function is a block of code which only runs when it is called.  Reference: (https://www.w3schools.com/python/python_functions.asp)
                                                      # the current date and time  can be obtained using datetime.now(). Reference: (https://www.toppr.com/guides/python-guide/tutorials/python-date-and-time/datetime/current-datetime/how-to-get-current-date-and-time-in-python/)
    today = datetime.now()

                                                      # Check if today is a weekday (Monday to Friday). The function returns the data as a result.if it is a weekday the result will be <5
    return today.weekday() < 5                        # weekday() gives an integer representing days of the week, where monday is 0 and sunday is 6.to check if its a weekday compare the result of weekday to <5.            
                                          
if isaweekday():                                      # the function is called in an if else statement. an if else statement executes the code depending on if the information is true or false. if it is true the code in the if statement is executed and if false the code in the else statement is executed
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")


