# Dictionary Comprehension
# dictionary comprehension is just a way of creating a dictionary
# using a shorter syntax
'''
EXAMPLE CODE:
new_dict = {*new_key*:*new_value* for *item* in *list* if *test*}
'''

# a new dictionary can also be creating by using the values of
# an EXISTING dictionary
'''
EXAMPLE CODE:
new_dict = {*new_key*:*new_value* for *(key, value)* in *dict.items()* if *test*}
'''

# create new dictionary from a list of names and generate
# a random score for each name
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
# {'Alex': 56, 'Beth': 23, 'Caroline': 94, 'Dave': 24, 'Eleanor': 37, 'Freddie': 22}

# look through 'students_scores' and create a new dictionary containing
# only those who have a score of 60 or higher
passed_students = {student: score for (
    student, score) in students_scores.items() if score >= 60}
print(passed_students)  # {'Caroline': 94}

# [interactive coding exercise] dictionary comprehension 1
# create a dictionary called `result` that takes each word in the given sentence
# and calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
result = {word: len(word) for word in words_list}
print(result)
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

# [interactive coding exercise] dictionary comprehension 2
# use dictionary comprehension to create a dictionary called `weather_f` that
# takes each temp in degrees celsius and converts it into fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
