"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print("""
Please enter an expression.
Use (= - * / pow mod square cube) followed by two digits.
Press \"q\" to exit.
""")

while True:

    expr = input("\texpression: ").split(" ")        
    operator = expr[0]

    if operator == "q":
        break
    elif len(expr) != 3:
        print("\tNot enough or more than needed arguments.\n")
        continue 

    num1 = expr[1]
    num2 = expr[2]
    result = None

    if num1.isdigit() and num2.isdigit():

        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "square":
            result = square(num1, num2)
        elif operator == "cube":
            result = cube(num1, num2)
        elif operator == "pow":
            result = power(num1, num2)
        elif operator == "mod":
            result = mod(num1, num2)
        else:
            print("\tPlease enter an operator followed by two integers.\n")
        
        print(f"\tanswer: {result}\n")        
    else:
        print("\tThose are not numbers. Try again.\n")    
    