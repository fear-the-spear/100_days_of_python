# A tuple is a datatype defined with parentheses
my_tuple = (1, 3, 8)
print(type(my_tuple))  # <class 'tuple'>

# The data within a tuple can be accessed just like with lists
print(my_tuple[0])  # 1

# Unlike lists, the data in tuples cannot be changed in any way
# This is what we call 'immutable'

# Although, you can convert a tuple to a list
print(list(my_tuple))  # [1, 3, 8]
