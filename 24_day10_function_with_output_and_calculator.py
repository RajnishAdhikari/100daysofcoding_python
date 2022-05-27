#Functions with Outputs 
# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("ram","ADHIKARI")

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return "f{formatted_f_name} {formatted_l_name}"
print(format_name("ram","ADHIKARI"))


