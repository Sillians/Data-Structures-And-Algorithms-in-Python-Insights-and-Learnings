# Input: number(int, float), operator: "+, -, /, *, ="
# Algorithm: A simple calculator (Each input in a separate line)
# Output: Output in the Python console what will be displayed in the calculator

def calculator():
    operation = []
    
    while True:
        operand = input('Enter the number or operator: ')
        if operand == "=":
            break
        
        operation.append(operand)
        result = float(operation[0])
        # try:
        #     if operand
        #     break
        # except ValueError:
        #     print("Input value must be a number or an operator")
    
    for i in range(0, len(operation)):
        if operation[i+1] == "+":
            result += float(operation[i+2])
        if operation[i+1] == "-":
            result -= float(operation[i+2])
        if operation[i+1] == "*":
            result *= float(operation[i+2])
        if operation[i+1] == "/":
            result /= (operation[i+2])
        if i+3 < len(operation):
            i+=3
        else:
            return result
    
        
print(calculator())    