# Day 4 - Rock Paper Scissors

# random module
import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.0000000 - 0.9999999
random_float = random.random()
print(random_float)

### to specify a range, simply multiply by a number!
print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# [interactive coding excercise] heads or tails
import random 

coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
else:
    print("Tails")

# understanding the offset and appending items to lists
### a list is a data structure - a way of storing data in Python
### list can be of any mix of data types
states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas"]
print(states_of_america[0]) # first item is always '0'
### to change an item:
states_of_america[1] = "Pennsylvania"
print(states_of_america) # ['Alabama', 'Pennsylvania', 'Arizona', 'Arkansas']
### add item to end of list
states_of_america.append("Utah")
print(states_of_america) # ['Alabama', 'Pennsylvania', 'Arizona', 'Arkansas', 'Utah']
### add multiple items to end of list
states_of_america.extend(["California", "Ohio"])
print(states_of_america)
### more methods for lists at:
### docs.python.org/3/tutorial/datastructures.html

# [interactive coding excercise] banker roulette - who is going to pay the bill?
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = names[random.randint(0, len(names) - 1)]
print(f"{random_name} is going to buy the meal today!")
### this code could be made more readable by storing the smaller components
###   inside variables!

# IndexErrors and working with nested lists
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

### how can we use our list to keep them inside the same list, but separate
###   them out into fruits and vegetables?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen2 = [fruits, vegetables]

# [interactive coding excercise] treasure map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x_coord = int(position[1]) - 1
y_coord = int(position[0]) - 1

map[x_coord][y_coord] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Rock, Paper, Scissors
import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

# Player
player_choice = input("Which do you choose?\n'0' for Rock, '1' for Paper, '2' for Scissors.\n")
if int(player_choice) == 0:
    print(f"You chose: {rock}")
if int(player_choice) == 1:
    print(f"You chose: {paper}")
if int(player_choice) == 2:
    print(f"You chose: {scissors}")

# Computer
cpu_choice = random.randint(0, 2)
if cpu_choice == 0:
    print(f"Computer chose: {rock}")
if cpu_choice == 1:
    print(f"Computer chose: {paper}")
if cpu_choice == 2:
    print(f"Computer chose: {scissors}")

# Establish winner
if int(player_choice) > cpu_choice or (int(player_choice) == 0 and cpu_choice == 2):
    print("You win!")
elif int(player_choice) == cpu_choice:
    print("It's a draw! Try again")
else:
    print("You lose!")