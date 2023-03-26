# Example of Handling an Error
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:  # specifies the exception we want to catch
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as key:
    print(f"The key {key} does not exist...")
else:
    content = file.read()
    print(content)
# Raising Your Own Exceptions
# finally:
#     raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height >= 3:
    raise ValueError("Human height should not exceed 3 meters!")

bmi = weight / height ** 2
print(bmi)
