def UserInput():
    w = input("Input your weight (kilogram): ")
    h = input("Input your height (meter): ")
    return float(w), float(h)

def FindBMI(hh, ww):
    return ww / (hh ** 2)

def ShowBMI(MyBMI):
    print("The user BMI is %.2f"% MyBMI)

weight, height = UserInput()
UserBMI = FindBMI(height, weight)
ShowBMI(UserBMI)