# defining and calling python functions
print("Hello")  # <-- function name followed by parens
len("Hello")  # <-- these are both built-in python functions
# making our own functions:


def my_function():  # <-- define function and give it a name
    print("Hello")  # <-- executed when function is called
    print("Bye")  # <-- function body MUST be indented!


my_function()  # <-- this calls the function for execution
# the hurdles loop challenge
challenge_code = '''
# THIS CHALLENGE IS RUN ON
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()

# ALTERNATIVELY
for step in range(6):
    jump()
'''

# indentation in python
indentation_notes = '''
in python, it is suggested to use spaces rather than tabs
for indentation. in  your code editor, you should be able to
set it up to indent the exact way you wnat it done. as a note,
in python3, you cannot have a file with mixed indentation types.
you can choose either spaces or tabs, it's your preference. just
stick to one type per file
'''

# while loops
# NOTE: When questioning whether to use a 'for' or 'while' loop,
# consider this:
# A for loop is used for when you want to iterate over something
#   and you need to do something with each thing that you are
#   iterating over (think a list of items),
# A while loop is used when you want to repeatedly run a certain
#   line or block of code until the specified condition is no
#   longer true. Also, while loops can be dangerous because you can
#   easily create an infinite loop, like:
#   while 5 < 10:
#       print("Hello")
# This would print "Hello" infinitely because 5 will always be
#   less than 10.


def jump():
    print("jump")


number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
# while something_is_true:
#   do something repeatedly
# hurdles challenge usings while loops (hurdles 2)
hurdle_with_while_loop = '''
# the following code can be used as a replacement for the
# for loop in the hurdle challenge above. The link to the
# challenge is also listed above (click the dropdown and go
# to 'hurdle 2').
while at_goal() == False: # <-- can also write 'while not at_goal():'
    jump()
'''

# hurdles 3
hurdles_three = '''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
'''

# jumping over hurdles with varialbe heights
my_code = '''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    

while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle()

# Coincidentally, this is also exactly how the instructor wrote the code
'''
# escaping the maze
my_code = '''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''
