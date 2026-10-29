xList = []
def UserInput():
    try:
        while True:
            x = input("Enter an input: ")
            if x == "Done":
                break
            if float(x) < 0:
                raise ValueError()
            xList.append(int(x))
    except ValueError:
        print("Error")
        exit()

def SumOut():
    print("The summation is", sum(xList))

def MinOut():
    print("The minimum is", min(xList))

def MaxOut():
    print("The maximum is", max(xList))

UserInput();
SumOut();
MinOut();
MaxOut();
