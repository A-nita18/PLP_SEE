#Greet the user
print("Hello! Feel free to use the calculator for upto two numbers arithmetic✨.")
#Ask for details
num1=float(input("What is the first number?"))
num2=float(input("What is the second number?"))
operation=(input("What is the operator? Addition(+),subtraction(-),division(/), multiplication(*), or even(**,// and %) etc."))

#Do the math
if operation=="+":
    result=num1+num2
    print(f"{num1} + {num2} = {result}")
elif operation=="-":
    result=num1+num2
    print(f"{num1} - {num2} = {result}")
elif operation=="/":
    result=num1+num2
    print(f"{num1} / {num2} = {result}")
elif operation=="*":
    result=num1+num2
    print(f"{num1} * {num2} = {result}")
elif operation=="%":
    result=num1+num2
    print(f"{num1} % {num2} = {result}")
elif operation=="**":
    result=num1+num2
    print(f"{num1} ** {num2} = {result}")
elif operation=="//":
    result=num1+num2
    print(f"{num1} // {num2} = {result}")
else:
    print("Error, division by zero is not allowed, please try again")