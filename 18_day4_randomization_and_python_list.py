from ctypes import Structure
import random
# random_integr = random.randint(1,10) #for random integer
# print(random_integr) 

# for creating random floating point number 0.00000000 to 0.9999999999
# random_float = random.random() #this gives random floating point number between 0 and 1 but not 1
# print(random_float) #random() function generates random floating point number 

# to create random decimal number between 0 and 5, 0.000000000 to 4.99999999
# we can get it by multiplying random_float by 5 i.e. random_float*5 not including 5
# random_float_upto5 =  random_float*5
# print(random_float_upto5)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")


# PROGRAM TO CREATE VIRTUAL COIN TOSS 
# random_side = random.randint(0,1)
# if random_side == "0":
#     print("tails")
# else:
#     print("heads")

# PYTHON LIST 
# list is a data Structure which is a common way of organizing and storing data in python
# if we need to store multiple data or grouped data then we use list
# we can store data in order to maintain structure 
# it is just  a set of square bracket in which many data or items stored inside  
# example of defining a list                       list = [item1, item2, .....]
# these items can be any data type or it can be mixed data type 



# states_of_america = ["california","delaware","pennsylvania", "alaska", "hawaii"]
# print(states_of_america[0])
# print(states_of_america[-1])

# if we want to edit the item in the list then we can do following 

# states_of_america[1] = "deelaware"
# print(states_of_america[1])
# print(states_of_america)

# we can do add an item then we can do so   suppose to add an item in end of the list then we do use append function
# with .append() function we can use only one argument 
# states_of_america.append("ramland")
# print(states_of_america)

# if we want to add two or more than two item in the list then we use .extend() function
# states_of_america.extend(["rajnishland","usnepal", "pkrnepal"])
# print(states_of_america)
#here 3 more items are added to the list and the list is extended

#we can use google to see many other function in the list

# program to print who is going to pay for the meal from split string method
# names_string = input("Give me everybody's names, separated by a comma.")

# names = names_string.split(",")
# num_items = len(names)
# random_choice = random.randint(0,num_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to buy the meal today")
# print(len(states_of_america))


# LIST WITHIN A LIST IS KNOWN AS NESTED LIST 
# fruits = ["apples", "grapes", "cherries", "pears", "orange"]
# vegetabales = ["spanich", "kale", "Tomatoes", "potatoes"]
# # meal = ["chicken", "mutton"]
# dirty_dozen = [fruits, vegetabales]
# print(dirty_dozen)

# program to show where to insert x box in the list of 3x3 matrix
# row1 = ["😂","😂","😂"]
# row2 = ["😂","😂","😂"]
# row3 = ["😂","😂","😂"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# row1 = ["😂","😂","😂"]
# row2 = ["😂","😂","😂"]
# row3 = ["😂","😂","😂"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")


# ROCK PAPER AND SCISSOR GAME 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
if user_choice >=3 or user_choice < 0:
    print("You type an invalid number, you lose!!!.")
else:
    print(game_images[user_choice ])
    computer_choice = random.randint(0,2)
    print("computer chose: ")
    print(game_images[computer_choice])


if computer_choice == 0 and user_choice ==2:
    print("You Lose!!!!")
elif computer_choice == 2 and user_choice ==0:
    print("You Win!!!!")
elif computer_choice > user_choice :
    print("You Lose!!!!")
elif computer_choice == user_choice:
    print("It's draw.")
elif computer_choice < user_choice:
    print("You won!!!!")
else:
    print("You type an invalid number, you lose!!!!!!!!!!!!!")
