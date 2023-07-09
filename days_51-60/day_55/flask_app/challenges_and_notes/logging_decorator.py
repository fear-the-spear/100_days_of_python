# Create the logging_decorator() function 👇


def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
    return wrapper
# Use the decorator 👇


@logging_decorator
def multiply(*args):
    total = 1
    for num in args:
        total *= num

    return total


print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
