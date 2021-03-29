#Function as a PARAMETER

def mySquare(num):
    return num * num

# mySquare(10)

def myCube(n):
    return n * n * n

def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result

def WrapperFunction(funcAsParam, num):
    print("Type of funcAsParam: ", type(funcAsParam))
    return funcAsParam(num)


result = WrapperFunction(mySquare, 5)
print("Result: ", result)

# Functions are also first class objects in Python
# Closures
# Decorators

lstFunc = [mySquare, myCube, iterFactorial]

for item in lstFunc:
    print("Result: ", item(5))