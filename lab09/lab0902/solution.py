x = input("Enter 5 inputs: ").split()
n = input("Enter an integer number of rotations (0-4): ")
def LeftRotate(x, n):
    return x[n:] + x[:n]
def RightRotate(x, n):
    return x[-n:] + x[:-n]
try:
    n = int(n)
    if 0 <= n <= 4:
        l = LeftRotate(x, n)
        r = RightRotate(x, n)
        print("The left-rotated list:", l)
        print("The right-rotated list:", r)
    else:
        raise ValueError()
    
except ValueError:
    print("Error!")