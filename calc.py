on = True
def add():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    print("Addition of {} and {} is {}".format(a,b,a+b))
def sub():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    print("Subtraction of {} and {} is {}".format(a,b,a-b))
def mul():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    print("Multiplication of {} and {} is {}".format(a,b,a*b))
def div():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    print("Division of {} and {} is {}".format(a,b,a/b))
while on:
    operation=input("Enter operation +, _,*, / or q")
    if operation=='+':(
        add())
    elif operation=='-':
        sub()
    elif operation=='*':
        mul()
    elif operation=='/':
        div()
    elif operation=='q':
        on=False
    else:
        print("Invalid operation")