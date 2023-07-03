import time

# first-class objects are objects that can be passed around
#   as arguments, just as you can with int/str/float/etc.


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(multiply, 7, 23)
print(result)
# ---------------------------------------------------------------------------- #
# Nested Functions


def outer_function():
    print("I'm outer")

    def nested_function():
        # this function is only accessible INSIDE this function (scope)
        print("I'm inner")

    nested_function()


outer_function()  # <- will print out both lines

# functions can also be returned as the output from other functions


def outer_function(x: int):
    print("I'm outer", x)

    def nested_function(y: int):
        print("I'm inner", y)

    return nested_function
    # no parens means it's not being called, but rather returned as output
    # the return value of this function now becomes the output of 'nested_function'


inner = outer_function(20)     # <- I'm outer 20
inner(30)                      # <- I'm inner 30
# adding parens to the variable is the activator
# ---------------------------------------------------------------------------- #
# Python Decorator Functions are functions that wrap a function and add
#  functionality to other functions

# def decorator_function(function):
#     def wrapper_function(function):
#         function()
#     return wrapper_function


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before the function gets executed
        function()
        # do something after the function gets executed
    return wrapper_function

# using the '@' symbol to decorate a function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")

# the alternative way of decorating


def say_greeting():
    print("How are you?")


decorated_greeting = delay_decorator(say_greeting)

say_hello()
say_bye()
decorated_greeting()
# both ways will decorate the function with extra functionality
