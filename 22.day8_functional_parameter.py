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

#program to check if the given number is prime or not
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number = n)