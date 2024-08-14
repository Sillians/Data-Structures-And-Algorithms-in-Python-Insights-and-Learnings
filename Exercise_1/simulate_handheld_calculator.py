
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
    
    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    # print(choice)
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter the second number: "))
    # while True:
    #     if num1 != '1' and num1 != '2' and num1 != '3' and num1 != '4' and num1 != '5' and num1 != '6' and num1 != '7' and num1 != '8' and num1 != '9' and num1 != '0' or num2 != '1' and num2 != '2' and num2 != '3' and num2 != '4' and num2 != '5' and num2 != '6' and num2 != '7' and num2 != '8' and num2 != '9' and num2 != '0':
    #         num1 = input("Enter first number: ")
    #         num2 = input("Enter second number: ")
    #     else:
    #         float(num1)
    #         float(num2)
    #         break
    
    #calculate user input numbers
    if choice == 1:
        print(num1 , " + " , num2 , " = " , add(num1,num2))
        
    elif choice == 2:
        print(num1 , " - " , num2 , " = " , subtract(num1,num2))  
    
    elif choice == 3:
        print(num1 , " * " , num2 , " = " , multiply(num1,num2))
    
    elif choice == 4:
        print(num1 , " / " , num2 , " = " , divide(num1,num2))
    
    elif choice == 5:
        print(num1 , " ^ " , num2 , " = " , power(num1,num2))
    
    elif choice == 6:
        print(num1 , " % " , num2 , " = " , remainder(num1,num2)) 
    
    elif choice == 7:
        print(num1 , " # " , num2 , " = " , terminate(num1,num2)) 
        break
    else:
        print("Not a valid number,please enter again")
        
# else:
#         print("Unrecognized operation")
        
#program ends here
# print("Done. Terminating")
# exit()