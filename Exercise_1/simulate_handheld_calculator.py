
import sys
from os import system

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def power(x, y):
  return x ** y

def remainder(x, y):
  return x % y

def terminate():
    return sys.exit()



print("Select operation.")
print("1.Add    : + ")
print("2.Subtract : - ")
print("3.Multiply : * ")
print("4.Divide : / ")
print("5.Power : ^ ")
print("6.Remainder: % ")
print("7.Terminate: # ")
print("8.Reset : $ ")


while True:
    operation = []
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter the second number: "))
    
     # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    
    #calculate user input numbers
    if choice == "1":
        print(num1 , " + " , num2 , " = " , add(num1,num2))
    if choice == "2":
        print(num1 , " - " , num2 , " = " , subtract(num1,num2))
    if choice == "3":
        print(num1 , " * " , num2 , " = " , multiply(num1,num2))
    if choice == "4":
        print(num1 , " / " , num2 , " = " , divide(num1,num2))
    if choice == "5":
        print(num1 , " ^ " , num2 , " = " , power(num1,num2))
    if choice == "6":
        print(num1 , " % " , num2 , " = " , remainder(num1,num2)) 
    if choice == "7":
        # terminate() 
        print("Done. Terminating")
        exit()
        # break
    else:
        print("Unrecognized operation")

        
#program ends here
# print("Done. Terminating")
# exit()