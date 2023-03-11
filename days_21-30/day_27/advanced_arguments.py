# Keyword Arguments vs Arguments With Default Values

# keyword arguments:
def my_function(a, b, c):
    print(a, b, c)


my_function(c=5, a=12, b=8)  # 12 8 5
# the order they're given doesn't matter, and they're all defined


# arguments with default values
def my_second_function(a=1, b=2, c=3):
    print(a, b, c)


my_second_function()  # 1 2 3
my_second_function(b=7)  # 1 7 3

# the default values provided mean the arguments are optional


# *args: unlimited positional arguments
def add(*args):  # any name can be used, but convention says use `args`
    # the asterisk means the function can accept any number of arguments!
    for n in args:
        print(n)


add(1, 2, 3, 4, 5)  # 1 2 3 4 5 (all on a new line)


# **kwargs: many keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# what this allows us to do is look through the inputs and find the
# ones that we want and then use them to do something


calculate(5, add=1, multiply=2)
# {'add': 1, 'multiply': 2}
# 12

# so the function took 'n' (5) and added 1 (our 'add' keyword), which is 6
# then it took 6 and multiplied it by two (our 'multiply' keyword)
