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

 def add(a,b):
     print(a+b)
     
add(10,20)

# def sub(a,b):
#     print("The difference is",a-b)

# sub(20,10)

# 2. Keyword Arguments:
# def f1(a,b):
#     ....... 
#     ..... 
#     f1(a=10, b = 20)
#     f1(a = 20, b =)