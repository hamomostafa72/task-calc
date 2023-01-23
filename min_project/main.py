from calc import *

def recursive1(x, y):
    if hamo == 1:
        print(Add(x, y))
    elif hamo == 2:
        print(Sub(x, y))
    elif hamo == 3:
        print(Multi(x, y))
    elif hamo == 4:
        print(div(x, y))
    else:
        print("invalid number.")

x = 1
while x == 1:
    y = float(input("enter first num : "))
    x = float(input("enter second num : "))
    hamo = int(input("enter number of operation: "))
    recursive1(x, y)
    x = int(input("Do you want con press 1 or 2 to exit program: "))

print("your program End")