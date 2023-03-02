# read a file
file = open("my_file.txt", mode="r")
contents = file.read()
print(contents)
file.close()

# use the 'with' keyword to save yourself from having to close the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to a file (this will override any existing data!)
with open("my_file.txt", mode="w") as file:
    file.write("Here is some new text.")

# append to a file
with open("my_file.txt", mode="a") as file:
    file.write("\nAgain, here is some new text.")

# NOTE: when attempting to open/write to a file that doesn't
#         exist, python will create the file for you

# create new file
with open("new_file.txt", mode="w") as file:
    file.write("New text...")
