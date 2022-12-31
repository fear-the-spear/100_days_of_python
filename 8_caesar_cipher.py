# functions with inputs
from art import logo
import math
function = '''
def my_function(something): <-- 'something' is the parameter
    Do this with something  <-- the value of the parameter is
    Then do this                  called an 'argument'
    Finally do this  
'''


def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"{name} is from {location}")


greet_with("Dakota", "Ohio")  # <== positional arguments
greet_with(name="Dakota", location="Ohio")  # <-- keyword arguments

# [interactive coding excercise] paint area calculator


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# [interactive coding excercise] prime number checker


def prime_checker(number):
    if number == 2 or number == 3:
        print("It's a prime number.")
    elif number % 6 == 1 or number % 6 == 5:
        print("It's a prime number.")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)

# NOTE: I CAME UP WITH THIS SOLUTION ON MY OWN. THIS IS NOT HOW THE
#       INSTRUCTOR DID IT, BUT IT WORKS PERFECTLY.
#       IT COULD ALSO BE WRITTEN LIKE THIS:4


def prime_checker2(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

# NOTE: ALL THIS DOES IS CHECK FOR NUMBERS BETWEEN THE CHECKED NUMBER
#       AND 2 TO SEE IF ANY OF THEM GO INTO THE CHECKED NUMBERS EVENLY.
#       IF ANY OF THEM DO, THAT MEANS IT'S NOT PRIME.

# caesar cipher part 1 - encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(encrypt, text):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    encoded_message = ""
    for letter in text:
        shifted_text = alphabet.index(letter) + shift
        encoded_message += alphabet[shifted_text]
    print(f"The encoded text is {encoded_message}")

    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(encrypt, text)
# caesar cipher part 2 - decryption
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    print(f"The decoded text is {cipher_text}")

    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(plain_text=text, shift_amount=shift)


# caesar cipher part 3 - reorganizing our code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amt, dir):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if dir == "encode":
            shift_amt *= -1
        new_position = position + shift_amt
        end_text += alphabet[new_position]
    print(f"The {dir}d text is {end_text}")


caesar(start_text=text, shift_amt=shift, dir=direction)

# caesar cipher part 4 - user experience improvements & final touches
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

is_running = "yes"
while is_running == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    is_running = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
