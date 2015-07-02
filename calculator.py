"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

done = False

# Your code goes here
while not done:
    tokens = raw_input()
    tokenized = tokens.split(" ")

    if tokenized[0] == "q":
        print "Goodbye!"
        done = True

    elif tokenized[0] == "add":
        add(int(tokenized[1]), int(tokenized[2]))
    
    elif tokenized[0] == "cube":
        cube(int(tokenized[1]))
    
    elif tokenized[0] == "divide":
        divide(float(tokenized[1]), float(tokenized[2]))
    
    elif tokenized[0] == "subtract":
        subtract(int(tokenized[1]), int(tokenized[2]))
    
    elif tokenized[0] == "multiply":
        multiply(int(tokenized[1]), int(tokenized[2]))
    
    elif tokenized[0] == "mod":
        mod(int(tokenized[1]), int(tokenized[2]))
    
    elif tokenized[0] == "power":
        power(int(tokenized[1]), int(tokenized[2]))
    
    elif tokenized[0] == "square":
        square(int(tokenized[1]), int(tokenized[2]))

    else:
        print "You're a dummy. Pick better inputs."
        done = True