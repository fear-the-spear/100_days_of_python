# the python dictionary - a deep dive
# a dictionary is a collection of key-value pairs
my_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}
# now, retrieve a value from the dictionary
print(my_dictionary["Bug"])

# adding new items to dictionary
my_dictionary["Loop"] = "The action of doing something over and over again"
print(my_dictionary)

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
my_dictionary2 = {"Key": "Value"}
my_dictionary2 = {}

# edit an item in dictionary
my_dictionary["Bug"] = "A moth in your computer"

# looop thru a dictionary
for key in my_dictionary:
    print(key)  # this will print the keys
    print(my_dictionary[key])  # this will print it's values

# [interactive coding excercise] grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

################################################################################
# NOTE: A KEY CAN ONLY HAVE ONE VALUE
# nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10},
}

# nesting a dictionary in a list
travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
]

# [interactive coding excercize] dictionary in list
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

# my solution


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})

# instructor solution


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# the secret auction (my solution)
# from replit import clear
# from art import logo


# print(logo)

guests = {}
more_guests = "yes"
while more_guests == "yes":
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")

    guests[name] = bid

    more_guests = input("Are there any more bidders? Type 'yes' or 'no': ")

    # clear()

max_value = max(guests.values())

max_key = max(guests, key=guests.get)

# clear()
print(f"The winner is {max_key} with a bid of ${max_value}!")

# the secret auction (instructor solution)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
