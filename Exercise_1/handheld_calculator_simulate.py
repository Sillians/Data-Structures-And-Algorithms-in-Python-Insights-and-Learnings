# Write a Python program that simulates a handheld calculator. 
# Your pro- gram should process input from the Python console representing buttons that are “pushed,”
# and then output the contents of the screen after each op- eration is performed. Minimally, 
# your calculator should be able to process the basic arithmetic operations and a reset/clear operation

import os

def simulate_handheld_calculator():
    
    operation = []
    
    while True:
        operand = input("Enter the number or operator: ")
        if operand == "=":
            break
        if operand == 'd':
            operation.pop()
            print(operation)
            continue
        if operand == 'c':
            os.system('clear')
            # operation = []
            continue
        
        operation.append(operand)
        result = float(operation[0])
    for i in range(0, len(operation)):
        if operation[i+1] == "+":
            result += float(operation[i+2])
        if operation[i+1] == "-":
            result -= float(operation[i+2])
        if operation[i+1] == "/":
            result /= float(operation[i+2])
        if operation[i+1] == "*":
            result *= float(operation[i+2])
        if operation[i+1] == "**":
            result **= float(operation[i+2])
        if i+3 < len(operation):
            i+=3
        else:
            return result
    else:
        print("Unrecognized operand or operation")
            
print(simulate_handheld_calculator())