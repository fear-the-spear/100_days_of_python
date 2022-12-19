#! using the for loop with Python lists
# for item in list_of_items:   <-- assign variable to each item in list
#   print(item)                <-- do something to each item
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  # this assigns a variable name (fruit) to each list item
    print(fruit)
  # this will run as many times as they are list items, and
  # the variable 'fruit' is reassigned on each execution

#! [interactive coding excercise] average height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
persons = 0
for height in student_heights:
    total += height
    persons += 1

print(round(total / persons))
# the instructor actually wrote two separate for loops
# for this excercise, but one works just fine
# but, for naming convention and to keep variables separated,
# writing two separate loops would be more readable in larger code

#! [interactive coding excercise] high score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")

#! for loops and the range() function
# for number in range(a, b):  <-- get ahold of each number within the range
#   print(number)  <-- do something to each number
for number in range(1, 11):   # <-- up to, but not including the last number
    print(number)             # <-- prints 1 2 3 4 5 6 7 8 9 10

for number in range(1, 11, 3):  # <-- third num specifies the step
    print(number)               # <-- prints 1 4 7 10

# how would we add all the numbers from 1 - 100 using code
total = 0  # <-- this is called an accumulator
for number in range(1, 101):
    total += number
print(total)  # <-- prints 5050
#! [interactive coding excercise] adding even numbers
even_num_sum = 0
for number in range(2, 101, 2):
    even_num_sum += number

print(even_num_sum)  # <-- prints 2550

# it can also be done with the modulus operator
even_num_sum2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_num_sum2 += number

print(even_num_sum2)  # <-- prints 2550

#! [interactive coding excercise] the fizzbuzz job interview question
# print all numbers from 1 - 100
# if number is divisible by 3, print Fizz
# if number is divisible by 5, print Buzz
# if number is divisible by both, print FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#! Create A Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chosen_chars = []
for n in range(0, nr_letters):
    chosen_chars.append(letters[random.randint(0, len(letters) - 1)])
print(chosen_chars)

for n in range(0, nr_numbers):
    chosen_chars.append(numbers[random.randint(0, len(numbers) - 1)])
print(chosen_chars)

for n in range(0, nr_numbers):
    chosen_chars.append(symbols[random.randint(0, len(symbols) - 1)])
print(chosen_chars)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in chosen_chars:
    password += char
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_ordered_password = "".join(random.sample(password, len(password)))
print(f"Your new passowrd is: {random_ordered_password}")

# CAN ALSO BE SOLVED LIKE THIS:
password = ""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)