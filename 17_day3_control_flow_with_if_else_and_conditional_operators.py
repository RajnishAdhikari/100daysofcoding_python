
# print("Welcome to the rollercoster ride!!!!!!!!!")
# height = int(input("what is your height in cm? :"))
# if height > 120:
#     print("you can ride to the rollercoster")
# else:
#     print("sorry you are not eligible to the rollercoster ride")

 # one equal sign (=) assigns value to the variable and two equal(==) this is also known as comparision operator
 # sign check equality 


# exercise 1 of day 3
# program to implement odd even using if else statement

# number = int(input("which number do you want to check for odd or even? "))
# if number%2 == 0:
#     print("this  is even .")
# else:
#     print("this  is odd")




# nested if and else statement
# to check if the age is >18 then the rate will be $15 if age<18 then the rate will be $8
# print("Welcome to the rollercoster ride!!!!!!!!!")
# height = int(input("what is your height in cm? :"))
# if height > 120:
#      print("you can ride to the rollercoster")
#      age = int(input("what is your age: "))

#      if age<12:
#          print("Your ticket price is $5")
#      elif age<=18:
#          print("Your ticket price is $7.")

#      else:
#          print("Your ticket price is $12 ")     

# else:
#     print("sorry you are not eligible to the rollercoster ride")




#BMI calculator 


# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in Kg:"))
# bmi = round(weight/height ** 2)

# if bmi< 18.5:
#     print(f"Your bmi is {bmi},You are underweight.")
    
# elif bmi <25:
#         print(f"Your bmi is {bmi},You are normal")
# elif  bmi < 30:
#         print(f" Your BMI is {bmi} , You are  slightly overweight.")
# elif bmi < 35:
#         print(f"Your bmi is {bmi}, You are obese.")
# else:
#     print("Your bmi is {bmi}, You are clinically obese.")


# program to check if the year is leap year or not
# year = int(input("Which year do you want to check? "))
# if year%4 == 0:     #first we need to check if divisible by 4 if divisible then 1condition satisfies 
#                     #then we need to check if divisible by 100 if divisible then 2nd condition fails 
#     if year%100 ==0:        # and the year is not a leap year if not satisfies then it is leap year
#         if year%400==0:     #finally we need to check if divisible by 400, if divisible then leap
#                             #year else not a leap year 
#             print(f"The year {year}, is a leap year")
#         else:
#             print(f"The year {year}, is not a leap year")
#     else:
#         print(f"The year {year}, is a leap year")
# else:
#     print(f"The year {year}, is not a  leap year")




# Multiple if statement in sucession

# to check if the age is >18 then the rate will be $15 if age<18 then the rate will be $8
# print("Welcome to the rollercoster ride!!!!!!!!!")
# height = int(input("what is your height in cm? :"))
# bill = 0
# if height > 120:
#         print("you can ride to the rollercoster")
#         age = int(input("what is your age: "))

#         if age<12:
#             bill = 5
#             print("Child ticket price is $5")
#         elif age<=18:
#             bill = 7
#             print("Youth ticket price is $7.")
#         else:
#             bill = 12
#             print("Adult ticket price is $12 ")     

#         want_photo = input("Do you want a photo taken? Y or N.")
#         if want_photo == "Y":
#             bill = bill +3     #Add $3 to their bill if they want photo bill += 3 is same as bill= bill +3
#         print(f"Your final bill is ${bill}")

# else:
#     print("sorry you are not eligible to the rollercoster ride")



#PIZZA ORDER DELIVERING
# print("Welcome to Pizza order Deliveries!!!")
# size = input("What size of pizza do you want? S, M, L-")
# add_pepperoni = input("Do you want pepperoni? Y or N-")
# extra_cheese = input("Do you want extra cheese? Y or N-")
# bill = 0
# if size == "S":
#     bill += 15

# elif size == "M":
#     bill += 20
 
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2

#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill} ")


# LOGICAL OPERATOR IMPLEMENTATION IN IF ELSE STATEMENT
# AND, OR, NOT
#roller coster example to implement logical operator
# to check if the age is >18 then the rate will be $15 if age<18 then the rate will be $8
# and if the age is between 45 and 55 then the cost is free
# print("Welcome to the rollercoster ride!!!!!!!!!")
# height = int(input("what is your height in cm? :"))
# bill = 0
# if height > 120:
#         print("you can ride to the rollercoster")
#         age = int(input("what is your age: "))

#         if age<12:
#             bill = 5
#             print("Child ticket price is $5")
#         elif age<=18:
#             bill = 7
#             print("Youth ticket price is $7.")

#         elif age >= 45 and age <= 55:
#             bill = 0
#             print("Congratulations you don't have to pay any cost.")

#         else:
#             bill = 12
#             print("Adult ticket price is $12 ")     

#         want_photo = input("Do you want a photo taken? Y or N.")
#         if want_photo == "Y":
#             bill = bill + 3     #Add $3 to their bill if they want photo bill += 3 is same as bill= bill +3
#         print(f"Your final bill is ${bill}")

# else:
#     print("sorry you are not eligible to the rollercoster ride")




# LOVE CALCULATOR CHALLANGE TO IMPLEMENT CONTROL FLOW

# print("Welcome to the Love Calculator!!!!!!!!!!")
# name1 = input("what is your name? \n")
# name2 = input("What is their name? \n") 
# combine_string = name1 + name2
# lower_case_string = combine_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love)) #we have to keep int because in next step while comparing we need integer type

# if (love_score < 10)  or (love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together." )

# else:
#     print(f"Your score is {love_score}")


#DAY - 3 PROJECT TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tresure Island")
print("Your mission is to find the treasure.")
choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake.There is and island in the middle of the lake.Type "wait" to wait for aboat.Type "swim" to swim accross.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed.There is a house with 3 doors. red, yellow and blue.which color do you want to choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire Game Over!!!!!!")
        elif choice3 == "yellow":
            print("You found the treasure. You win!!!!!")
        elif choice3 == "blue":
            print("You enter the room of beasts. Game Over!!!!!!")
        else:
            print("You chose a door that doesn't exist. Game Over!!!!!!!")

    else:
        print("You got attack by an angry trout. Game Over.")
else:
    print("You fell into the hole. Game Over!!!!!!!")
