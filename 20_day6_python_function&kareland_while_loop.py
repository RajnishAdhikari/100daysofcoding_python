# Function:
# why function is needed?????
# if we write repetition of code in a single block then the 
# block is called function.
# group of repetidely used codes in a single unit is called function 


# things to consider while defining user defined function:
# def function_name():
#     function body 
#     (return statement) 

# def wish():
#     print("Hello world this is function.")
# wish()
# wish()
# wish()
# wish()
# wish()

# function with parameter 
# def wish(name):
#     print("hello", name)
# wish("Ram")
# wish("shyam")

# def squareroot(number):
#     print(number * number)
# squareroot(5)

# this is user defined function 
# def calculate(a,b):
#     print("The sum is", a + b)
#     print("The difference is", a - b)
#     print("The product is", a * b)
#     print("The difference is", a / b)

# calculate(20,10)
# calculate(500,600)
# calculate(25,35)
# calculate(54,65)

# parameters: means the input to a function
# def function_name(a):
#     print("The name is ", a)

# function_name("rajnish_adhikari")


# function with return statement: 
# def function_name():
#     ........
#     ........
#     return statement 

# def add(a,b):
#     sum = a+b
#     pro = a*b
#     div = a/b
#     diff = a-b 

#     return sum, pro, div, diff
# result = add(20,10)
# print(result)
# print(type(result))



# Types of parameter or argument


# 1. Positional 
# 2. keyword
# 3. Default 
# 4. Variable Length argument 


# 1. Positional Argument --order is important 
# - if we change the order of argument then result is different
# def add(a,b):
#     print(a+b)

# add(10,20)
# add(20,10)

# def sub(a,b):
#     print("The difference is",a-b)

# sub(20,10)
# sub(10,20)

# 2. Keyword Arguments: in this if we pass argument with parameter name then it is called keyword argument
# we can pass argument value by keyword i.e. by parameter name
# here in keyword argument order isn't important but number of argument must be matched 
# def f1(a,b):
#     ....... 
#     ..... 
#     f1(a=10, b = 20)
#     f1(a = 20, b =)

# def wish(name,msg):
#     print("hello",name,msg)
# wish(name = "ram", msg="good morning")
# wish(msg="good afternoon", name = "Hari" )

# def wish(name,msg):
#     print("Hello", name, msg)
# wish("rajnish", msg= "good morning") #valid
# wish("rajnish","good afternoon")    #valid
# # wish(msg="good night","rajnish")  invalid because positional argument is require at first
# and keyword argument at second 

# 3. Default Argument -
# if there is no argument passed then we get the default argument 
# def wish(name = 'guest'):
#     print('hello',name,'good morning')
# wish('ram') here argument is passed
# wish() here default argument is called 

# another example of same type 
# def wish(name = 'Guest',age):
#     print('hello',name,'Good morning and your age is',age)
# wish('ram',25) this is invalid because the non default argument follows the default argument 
# here name is the default argument while age is non-default argument so non-default argument 
# should be before

# def wish(age,name = 'Guest'):
#     print('hello' ,name, 'Good morning and your age is',age)
# wish('ram',25) this is also invalid although we get output because this is positional argument but not
# keyword argument so, 25 need to be before the name 


# def wish(age,name = 'Guest'):
#     print('hello' ,name, 'Good morning and your age is',age)
# wish(25, 'ram')



# WAP to calculate using positional, default and keyword argument 
# def calc(a,b,c,d):
#     sum = a+b
#     sub = c-d
#     mul = a*d
#     div = d/b
#     return sum,sub,mul,div
# t = calc(10,20,30,40)
# m = calc(a = 10, c = 20, b = 30, d= 40)
# n = calc(10, 20, c = 30, d= 40) #here 10 and 20 are positional argument and other are default argument
# print(t)
# print(m)
# print(n)

  
# 4. variable length argument 
