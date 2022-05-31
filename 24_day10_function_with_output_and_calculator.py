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
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didn't provide valid inputs."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name?"),input("What is your last name?")))



