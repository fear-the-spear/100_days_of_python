# functions with outputs
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # a 'return' statement tells the computer that this is
    # the end of the function. Any code written after well
    # NOT be executed
    return f"{formatted_f_name} {formatted_l_name}"


# output of func 'format_name' is stored in var 'formatted_str'
formatted_str = format_name("dakota", "bowman")
print(formatted_str)

# multiple return values


def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name2(input("What is your first name?: "),
      input("What is your last name?: ")))

# [interactive coding excercise] days in month


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# docstrings

# recursion
# recursion is when you call a function within itself - but BE CAREFUL@
# you must make the function call happen ONLY if a condition is met, otherwise
# you can easily create an infinite loop

# calculator


def add(n1, n2):
    return n1 + n2
# Subtract


def subtract(n1, n2):
    return n1 - n2
# Multiply


def multiply(n1, n2):
    return n1 * n2
# Divide


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    num1 = float(input("What's the first number?: "))

    for symbol in operators:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
