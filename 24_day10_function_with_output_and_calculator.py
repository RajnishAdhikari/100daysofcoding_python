#Functions with Outputs 
# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("ram","ADHIKARI")

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return "f{formatted_f_name} {formatted_l_name}"
#     print("This is never printed")  #it is never printed because after return the code wont be executed 
# print(format_name("ram","ADHIKARI"))

# MULTIPLE RETURN VALUE 
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "you didn't provide valid inputs."

#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"

# print(format_name(input("What is your first name?"),input("What is your last name?")))


#returning true if it is leap year and returning false if it is not a leap year

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     # if month > 12 or month < 1:       this is really not necessary
#     #     return "Invalid month"
#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]


# year = int(input("Enter a year:"))
# month = int(input("Enter a month:"))
# days = days_in_month(year, month)
# print(days)



# Doc strings in python
# this is basically used for documenting for the function 


# Calculator Project using function and dictonary 
#add
def add (n1, n2):
    return n1 + n2