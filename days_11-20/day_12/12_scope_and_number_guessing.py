# -------------------------------------------------------------------------------
import random  # for the final project at bottom of file
# -------------------------------------------------------------------------------

# namespace: local vs global scope
# scope applies to basically everything - functions, variables, etc.
enemies = 1  # global variable


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()  # this will print '2'
print(f"enemies outside function: {enemies}")  # this will print '1'

# local scope


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)  # this is undefined because it was defined in a function

# global scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()  # this won't error b/c 'player_health' is accessible everywhere

# NOTE: block scope does not exist in python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
    # with block scope, the 'new_enemy' variable would only be accessible within
    # the 'if' block. but, in python, since there is no block scope, it's fully
    # accessible globally

# how to modufy a global variable
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
# NOTE: although you can do this, it's not advisable!
# here's what you should do instead:


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()

# global constants - variables that will never change
PI = 3.14159
URL = "https://google.com"

# guess the number (my solution)
# import random is at the top of the file
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

random_number = random.randint(1, 100)

print(f"HINT: The number is {random_number} :)")
easy_or_hard = input("Type 'easy' or 'hard': ")
if easy_or_hard == "easy":
    attempts = 10
else:
    attempts = 5

should_continue = True

while attempts > 0:
    print(f"You have {attempts} remaining guesses.")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high!")
        attempts -= 1
    elif guess < random_number:
        print("Too low!")
        attempts -= 1
    elif guess == random_number:
        attempts = 0
        print(f"You got it! The number was {guess}")
    if attempts == 0 and guess != random_number:
        print(f"You ran out of guesses! The number was {random_number}")

# guess the number (instructor's solution)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set difficulty.


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
