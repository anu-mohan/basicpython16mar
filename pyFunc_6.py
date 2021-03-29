# Lambda Functions
# Anonymous functions
# Functions which have got NO names,
# They are used to write one-line functions

def mySquare(num):
  print(mySquare(7))


f = lambda num: num * num
print(f)
print(type(f))
result = f(5)
print("Square of number: ", result)

print("Square of number: ", (lambda num: num * num)(10))
    #return num * num
