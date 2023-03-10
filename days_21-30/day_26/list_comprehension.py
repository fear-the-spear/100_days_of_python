# List Comprehension
# list comprehension is something that is somewhat unique to python
# it helps to really cut down on typing and make code shorter/easier to read

# list comprehension is the concept of creating a new list from a previous one

# here's an example of how we have done this previously:
numbers = [1, 2, 3]  # <- orig. list
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)  # <- [2, 3, 4]

# now, here's that same operation, but with list comprehension
'''
EXAMPLE CODE:
NOTE: the words in asterisks are just placeholders
new_list = [*new_item* for *item* in *list*]

1. 'list': the iterable from which we want to put items from
2. 'item': the individual items in the iterable
3. 'new_item': the operation we want to perform on each item in the iterable
'''
new_list = [n + 1 for n in numbers]
print(new_list)  # [2, 3, 4]

# list comprehension with strings
name = "Dakota"
new_list = [letter for letter in name]
print(new_list)  # ['D', 'a', 'k', 'o', 't', 'a']

'''
Python Sequences:

types of sequences in python:
    list -> []
    range()
    string -> ""
    tuple -> ()

these are called sequences because they have a specific order
when a list comprehension is performed on a sequence, it goes through
that sequence in order
'''

# list comprehension with range()
num_list = [x * 2 for x in range(1, 5)]
print(num_list)  # [2, 4, 6, 8]

# Conditional List Comprehension
'''
EXAMPLE CODE:
NOTE: the words in asterisks are just placeholders
new_list = [*new_item* for *item* in *list* if *test*]
'''
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)  # ['Alex', 'Beth', 'Dave']
cap_names = [name.upper() for name in names if len(name) > 4]
print(cap_names)  # ['CAROLINE', 'ELEANOR', 'FREDDIE']

# [interactive coding exercise] squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# write one line of code that takes a list of numbers and
# returns a new list containing every number in the orig. list,
# but each number should be squared
squared_numbers = [num * num for num in numbers]
# alt. code: squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

# [interactive coding exercise] filtering even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# write one line of code that takes a list of numbers and
# returns a new list containing ONLY the even numbers from the orig. list
result = [num for num in numbers if (num % 2 == 0)]
print(result)  # [2, 8, 34]

# [interactive coding exercise] data overlap
# take a look insdie `file1.txt` and `file2.txt`. They each contain a bunch of
# numbers, with each number on a new line. create a list called `result` which
# will contain the numbers that are common in both files
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

print(result)  # [3, 6, 5, 33, 12, 7, 42, 13]
