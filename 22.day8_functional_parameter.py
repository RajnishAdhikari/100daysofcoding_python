# def greet():
#     print("Good morning")
#     print("kjdkkdf")
#     print("jkdjkdf")
# greet()

# function that allows for input 



# def greet_with_name(name):  #here name is parameter, parameter is the name of the data that is passed in 
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# greet_with_name("Ram")      #here ram is argument, argument is the actual value of the data
# greet_with_name("shyam")

# Function that allows for multiple input 
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

#  greet_with("ram", "new south wales")   this is positional argument

#  KEYWORD ARGUMENT
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with(location="new south wales", name= "ram")


#AREA CALCULATOR EXERCISE 

# import math
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area/cover)
#     print(f"You'll need {num_of_cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_calc(height = test_h, width = test_w, cover = coverage)

# #program to check if the given number is prime or not
# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number):
#         if number % i ==0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")


# n = int(input("Check this number: "))
# prime_checker(number = n)


#PROGRAM TO IMPLENENT CAESAR CIPHER 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text= ""
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

from art import logo
print(logo)



# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")



# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount = shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)



# rearranging the code to reduce the repetition 

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to do again. Otherwise type 'no'. \n")
    if restart == "no":
        should_end = True
        print("Goodbye")
