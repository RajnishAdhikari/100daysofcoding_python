#inputting two digit number and adding the first and second part of that digit
two_digit_number= input("enter two digit number ")
print(type(two_digit_number))
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = (first_digit) + ( second_digit)
print(two_digit_number)




#second method
two_digit_number= input("enter two digit number ")
#print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)