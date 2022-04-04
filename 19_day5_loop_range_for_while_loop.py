# For Loop 
# for item in list_of_items:
    #Do something to each item 

# fruits = ["apple", "Peach", "Pear"]
#if we want to access each item in this list then we will use forloop

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# for loop program to implement average height exercise 
# student_heights = input("input a list of student heights :").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(f"The height of student is: {student_heights}")
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(f"the average height is : {average_height}")

# student_heights = input("input a list of student heights :").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(f"The height of student is: {student_heights}")
# total_height = 0
# for height in student_heights:
#     total_height = total_height + height
# print(total_height)
# number_of_students = 0
# for nos in student_heights:
#     number_of_students = number_of_students + 1
# print(number_of_students)
# average_height = round (total_height / number_of_students)
# print(f"The average height is : {average_height}")



# for loop always needs sequence here sequence means 
# list string dictonary, tuples,
# sequence is also called a collection of items 
  
# syntax:
# for x in sequence :   // sequence means it can be list, dictonary or any other items
#     body.......

# for eg:
# s = 'rajnishadhikari'
# for x in s:
#     print(x)

# same example to print character with index:
# s = 'rajnishadhikari'
# i = 0
# for x in s:
#     print(f"The character {x} is in index {i}")
#     i = i+1


# for x in range(10):
#     print(x)




# while loop:
# we use while loop until and unless the given condition is true

# SyntaxError
# while condition:
#     statement

# example:

# x = 1 
# while x<= 10:
#     print(x)
#     x = x+1

# name =''
# while name!='dhiraj':
#     name = input("Enter Name:")
# print("Thank You Sir")


# infinite for loop
# while True:
#     print("this condition is ghumeko ghumai")


# nested loop
# for i in range(4):
#     for j in range(4):
#         print('i=',i,"j=",j)


# program to implement right angeled triangle
# n = int(input("Enter number of rows"))
# for i in range(1,n+1):
#     print('*'*i)

# for loop with range function
# for number in range(1,10):
#     print(number)


# # program to find the sum of number between 1 to 100
# total = 0
# for number in range(1, 101):
#     total = total + number
# print(f"The total sum between 1 and 100 is {total}")

# program to add the even numbers between 1 and 100
total = 0 
for number in range(2,101,2):
    total = total + number
print(total)

total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 = total2 + number
print(total2)

    

# finding out highest score that is obtained by student 
# student_scores = input("Enter the score of the class:").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is :{highest_score}")


