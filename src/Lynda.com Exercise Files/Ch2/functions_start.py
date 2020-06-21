#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x,y):
    return x*y

# function with default value for an argument
def exponent(base, power=1):
    result = 1
    for i in range(power):
        result = result * base
    return result
# print (exponent(power=4,base=3))

#function with variable number of arguments
def cume(*args):
    runningsum = 0
    for x in args:
        runningsum = runningsum + x
    return runningsum
# print (cume(5,5,5))

#function with variable number of arguments
def prod(*args):
    runningprod = 1
    for x in args:
        runningprod = runningprod * x
    return runningprod
print (prod(5,5,5))


# Execution commands
# func1()
# print (func1())
# print (func1)

# func2(10,20)
# print (func2(10,20))

# print (cube(3,3))

# print (power(3,1))
# print (power(3,3))
# power(x=4, base=3)