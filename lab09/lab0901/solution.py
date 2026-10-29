import math

def CirArea(x):
    return math.pi * x * x

def SqArea(x):
    return x * x

x = input("Input a positive number: ")
try:
    x = float(x)
    if x <= 0:
        raise ValueError()
    c = CirArea(x)
    s = SqArea(x)
    print("The area of the circle is %.2f square units."%c)
    print("The area of the square is %.2f square units."%s)
except ValueError:
    print("Wrong Input")