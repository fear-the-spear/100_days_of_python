# creating our own custom classes (with attributes)
class User:  # first letter of every word capitalized
    # this is for syntax purposes only
    pass


user_1 = User()

# create attribute for our custom class
user_1.id = "001"
user_1.username = "dakota"
print(user_1.username)  # dakota

user_2 = User()
user_2.id = "002"
user_2.username = "jack"
# this is more error prone because a typo would
#   just create an entirely new variable

# to prevent this, we need to use a constructor
# a constructor is a part of the blueprint (class) that allows
#   us to specify what should happen when our object is being constructed
# this is also called 'initializing' an object - to set variables, counters,
#   switches, etc. to their starting values at the beginning of a program
# to initialize attributes, a special type of function is needed


class Car:
    def __init__(self):
        print("New car being created...")
        # this '__init__' function is going to be called
        # every time a new object is created from this class


car = Car()  # prints 'New car being created...'

# set attributes in the constructor


class Car2:
    def __init__(self, car_id, seats):
        self.id = car_id
        self.seats = seats
        # when creating an object from this class, you MUST
        # provide these two pieces of data - otherwise, ERROR
        self.wrecks = 0  # this is a 'default value'


car2 = Car2("002", 5)
print(car2.id)
print(car2.seats)  # 5
print(car2.wrecks)  # 0
