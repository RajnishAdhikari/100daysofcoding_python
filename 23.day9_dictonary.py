# Python dictonary 


# if we want to represent key value pairs as a single entity then 
# we should go for dictonary 
# Syntax
# {key : value, key: value}
# eg
# name: roll 
# domain : ip_address 

# Properties 
# 1.in dictonary value can be duplicate but key cannot be duplicate 
# 2. heterogenous object are allowed for both keys and values
# eg {'rajnish': 100 , 100 : 7.5}
# 3.Insertio order not preserve
# this means indexing and slicing isn't possible in dictonary
# 4.dictonary are mutable 
# this means we can make changes anywhere in dictonary
# 5. Dictonary are dynamic
# this means we make dictonary of any size we want 


# how to create dictonary
# empty dictonary 
# d = {}
# print( type(d))

# or 
# d = dict()   this is also an empty dictonary

# to insert value in empty dictonary 
# d[100] = "Hello"
# d[200] = "world"     # another way given below   
# d = {300: 'ram', 400: 'shyam'}
# print(d)


# ACCESSING THE ELEMENTS OF DICTONARY WITH ASSOCIATED KEY
# d = {300: 'ram', 400: 'shyam',100:'AAAAAAAAA', 200:'BBBBBB'}
# print(d)
# print(d[100])


#update dictonary
# d = {300: 'ram', 400: 'shyam',100:'AAAAAAAAA', 200:'BBBBBB'}
# d[500]= 'hari'
# print(d)

#deleting the element of the dictonary
# d = {300: 'ram', 400: 'shyam',100:'AAAAAAAAA', 200:'BBBBBB', 500:'hari'}
# del d[200]
# print(d)
# d.clear()  #to delete all the elements of dictonary
# print(d)
# #to delete the dictonary - the empty dictonary will also be deleted 
# del d
# print(d)

#IMPORTANT FUNCTIONS OF DICTONARY
#1. TO CREATE THE EMPTY DICTONARY
# d= dict()
# # print(d)

# d[100] = "ram"
# d[200]= "shyam"
# d[300] = "Hari"
# d[400] = "arjun"
# print(d)
# print(len(d))  2. to find the length of the dictonary 

# print(d.get(100)) 3. to get the value of the key associated with it 
# print(d.get(5000, "No Key"))  4. if there is value of the key then value will be printed otherwise no key will be printed 

# 5. to remove the key value pair we use pop function 
# d.pop(100)
# print(d)

# 6.  to remove any of the item we use popitem()
# d.popitem()
# print(d)

#7. to print all the keys in our dictonary we use keys() function
# print(d.keys())
# for keys in d.keys():
#     print(keys)

#8. to print all the values in our dictonary we use values() function
# print(d.values())
# for values in d.values():
#     print(values)

#9. to print all the keys and values in our dictonary we use items() function
# print(d.items())
# for key,values in d.items():
#     print(key, "--" ,values)


# 10. to copy dictonary we use copy() function 
# print(d.copy()) 
# for x in d.keys():
#     print(x)


#11. using set default function
# d = {100 : "hello", 200: "world", 300: "hi"}
# print(d.setdefault(400, "namaste"))
# print(d)

# 12. using update() function to update 
# d = {100 : "hello", 200: "world", 300: "hi"}
# x = {400 : "sabin"}
# x.update(d)
# print(x)


# #13. Dictonary Comprehension
# d = { x:x*x for x in range(10)}
# print(d)


# day 9 of 100 video  -- loop through a dictonary
# programming_dictonary = {"bug": "an error", "function": "a piece of code that you can call over and over again"}
# for key in programming_dictonary:
#     print(key)
#     print(programming_dictonary[key])



# Grading Program
# here for every score in number we have to convery into grade as mentioned
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Darco": 74,
#     "Neville": 62,
# }

# student_grade ={}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grade[student] = "Outstanding"
#     elif score > 80:
#         student_grade[student]= "Exceeds Expectations"
#     elif score > 70:
#         student_grade[student] = "Acceptable"
#     else:
#         student_grade[student]= "Fail"
# print(student_grade)



#NESTING IN DICTONARY AND LOOP
# NESTING
capitals = {
    "france": "paris",
    "Germany": "Berlin",
}

# NESTING A LIST IN A DICTONARY
# travel_log = {
#     "france": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin","Hamburg","Stuttgart"]
# }

# NESTING A DICTONARY IN A DICTONARY
# travel_log = {
#     "France": {"city_visited":["Paris","Lille", "Dijon"], "total_visits": 12},    
#     "Germany": ["Berlin","Hamburg","Stuttgart"]
# }
# print(travel_log)


# # NESTING A DICTONARY IN A List
# travel_log = [
#     {
#         "country": "France", 
#         "city_visited": ["Paris","Lille", "Dijon"], 
#         "total_visits": 12
#     },    
#     {
#     "country": "Germany",
#     "city_visited": ["Berlin","Hamburg","Stuttgart"],
#     "total_visits":5
#     },
# ]

# PROGRAM TO ADD NEW COUNTRY, CITY VISITED  AND TOTAL VISITS IN THE TRAVLE LOG
# travel_log = [
#     {
#         "country": "France", 
#         "cities": ["Paris","Lille", "Dijon"], 
#         "total_visits": 12
#     },    
#     {
#     "country": "Germany",
#     "cities": ["Berlin","Hamburg","Stuttgart"],
#     "total_visits":5
#     },
# ]

# def add_new_country(country, cities,total_visits):
#     new_country = {}
#     new_country["country"]= country,
#     new_country["cities"] = cities,
#     new_country["total_visits"] = total_visits
#     travel_log.append(new_country)

# add_new_country("Russia",["Moscow","Saint Petersburg"],2)
# print(travel_log)


# BIDDING APP SAMPLE
from replit import clear
from art2 import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record(bidder)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid} ")

while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()























