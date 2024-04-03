# es.py
# This program will read in a txt file and output the number of e's it contains. 
# The program takes the filename from an argument on the command line. 
# Author: Louise Ryan

# https://realpython.com/python-command-line-arguments/
# https://docs.python.org/3/library/sys.html#module-sys
# http://spronck.net/pythonbook/pythonbook.pdf

import sys                                           # by importing sys module you can access command line arguments in the program via sys.argv
                                                     # sys.argv is a list that contains command-line arguments passed to a script when it is executed. 
if len(sys.argv) != 2:                              
    print("Please enter: python es.py <filename>")   #2 entries expected(script-file containing code and filename-txt_file). 
    sys.exit(1)                                      #if len != 2, correct number of arguments were not inputted-->error message
    

filename = sys.argv[1]                         

if not filename.endswith('txt'):                     #if filename entered does not end with 'txt'-->error message
        print('Not a txt file!')


try:
    with open(filename, 'r') as f:                   #script opens file from command line input and counts the number of e's in the txt file
        content = f.read()
        number_of_es = content.count('e')
        print(number_of_es)
except FileNotFoundError:                             # if file not found-->error message
    print("File not found")
    sys.exit(1)


# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://www.w3schools.com/python/ref_string_count.asp
# https://docs.python.org/3/library/exceptions.html
    