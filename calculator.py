"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:

    expr = input("Enter an expression > ").split(" ")
    #print(len(expr))
    
    operator = expr[0]

    if operator == "q":
        break
    elif len(expr) != 3:
        print("Not enough arguments.")
    else:

        num1 = expr[1]
        num2 = expr[2]
        
        if num1.isdigit() and num2.isdigit():

            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                print(add(num1, num2))
            elif operator == "-":
                print(subtract(num1, num2))
            elif operator == "*":
                print(multiply(num1, num2))
            elif operator == "/":
                print(divide(num1, num2))
            elif operator == "square":
                print(square(num1, num2))
            elif operator == "cube":
                print(cube(num1, num2))
            elif operator == "power":
                print(power(num1, num2))   
            elif operator == "mod":
                print(mod(num1, num2))                             
            else:
                print("Operator does not exist. Try again. ")
        else:
            print("Those are not numbers. Try again.")