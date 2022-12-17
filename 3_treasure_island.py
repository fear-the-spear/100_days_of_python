# Day 3 - Treasure Island

### control flow with if / else and conditional operators
# if condition:
#   do this
# else:
#   do this:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!") # runs if 'height >= 120' is true
else:
  print("Sorry, you can't ride the rollercoaster.") # runs if false
  # everything after the colon that's indented is part of that code block!

### [interactive coding excercise] odd or even? introducing the modulus operator
number = int(input("Which number do you want to check? "))
if (number % 2) == 0: 
    # modulus operator checks remainder of division
    # if remainder is 0, number is even
    # if remainder is anything but 0, number is odd
    print("This is an even number.")
else:
    print("This is an odd number.")

### nested if statements and elif statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
  # nested if statement to check another condition upon meeting height req.
    print("Please pay $5.")
  elif age <= 18:
  # we can use as many elif conditions between 'if and else' as we like
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you can't ride the rollercoaster.")

### [interactive coding excercise] BMI 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

### [interactive coding excercise] leap year
year = int(input("Which year do you want to check? "))

if (year % 100) == 0:
    if (year % 400) == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
elif (year % 4) == 0:
    print("Leap year.")
else:
    print("Not leap year.")

### multiple if statements in succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("You're having a midlife crisis - your ticket is free!")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is {bill}")
else:
  print("Sorry, you can't ride the rollercoaster.")

### [interactive coding excercise] pizza order practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
    pizza = "small"
if size == "M":
    bill += 20
    pizza = "medium"
if size == "L":
    pizza = "large"
    bill += 25

if add_pepperoni == "Y":
    if pizza == "small":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

# [interactive coding excercise] love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_str = name1 + name2
lower_case_str = combined_str.lower()

t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")

true = str(t + r + u + e)

l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")

love = str(l + o + v + e)

true_love = true + love
score = int(true_love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

### Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nYou're walking down the path and see a fork in the road.")

left_or_right = input("Which way will you go? 'left' or 'right': \n").lower()
if left_or_right == 'right':
    print("You fell into a sinkhole...\nGame over.")

swim_or_wait = input("Your path is interrupted by a river. You can either wait for a boat or try to swim across. 'swim' or 'wait': \n").lower()

if swim_or_wait == 'swim':
    print("You were eaten by piranha...\nGame over.")

door = input("You make it across safely, and come to a house with three doors. Choose the 'red', 'blue', or 'yellow' door: \n").lower()

if door == 'red':
    print("You just walked into a room full of lions... Game over.")
elif door == 'blue':
    print("You found the treasure... YOU WIN!")
    print("Thanks for playing!")
else:
    print("A wizard has turned you into a rabbit... Game over.")