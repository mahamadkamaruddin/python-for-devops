import sys

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

num1 = float(sys.argv[1])
num2 = float(sys.argv[3])

operation = sys.argv[2]


match operation:
    case "add":
        print(add(num1, num2))
    case "sub":
        print(sub(num1, num2))
    case "mul":
        print(mul(num1, num2))
    case "div":
        print(div(num1, num2))
    case _:
        print("Enter the valid operation")
