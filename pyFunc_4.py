# Factorial of number
# 5! = 5 * 4 * 3 * 2 * 1
# 1! = 1
# 0! = 1


# 5! = 5 * 4!
# 4! = 4 * 3!
# n! = n * (n - 1)!

def recurFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * recurFactorial(num-1)

n = int(input("Enter any number: "))
out = recurFactorial(n)
print("Factorial of {} is {}".format(n, out))

# 5 = 5 * rf(4)
# 4 = 4 * rf(3)
# 3 = 3 * rf(2)
# 2 = 2 * rf(1)
# 1 = 1

# Component C => a b c d e
