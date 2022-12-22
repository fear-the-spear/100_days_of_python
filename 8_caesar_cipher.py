# functions with inputs
import math
function = '''
def my_function(something): <-- 'something' is the parameter
    Do this with something  <-- the value of the parameter is
    Then do this                  called an 'argument'
    Finally do this  
'''


def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"{name} is from {location}")


greet_with("Dakota", "Ohio")  # <== positional arguments
greet_with(name="Dakota", location="Ohio")  # <-- keyword arguments

# [interactive coding excercise] paint area calculator


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# [interactive coding excercise] prime number checker


def prime_checker(number):
    if number == 2 or number == 3:
        print("It's a prime number.")
    elif number % 6 == 1 or number % 6 == 5:
        print("It's a prime number.")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)

# NOTE: I CAME UP WITH THIS SOLUTION ON MY OWN. THIS IS NOT HOW THE
#       INSTRUCTOR DID IT, BUT IT WORKS PERFECTLY.
#       IT COULD ALSO BE WRITTEN LIKE THIS:4


def prime_checker2(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

# NOTE: ALL THIS DOES IS CHECK FOR NUMBERS BETWEEN THE CHECKED NUMBER
#       AND 2 TO SEE IF ANY OF THEM GO INTO THE CHECKED NUMBERS EVENLY.
#       IF ANY OF THEM DO, THAT MEANS IT'S NOT PRIME.
