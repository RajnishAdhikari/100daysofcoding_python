#program to calculate how many weeks and days are left in our life if we live upto 90 from our present age
'''
age = input("what is your present age? ")
age_as_int = int(age)

years_remaining = 90 - age_as_int   #let us suppose we live for 90 years
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12

print(f"You have {days_remaining} days , {weeks_remaining} weeks and {months_remaining } months left.")


'''
'''print("Welcome to tip calculator !!! ")
total_bill  = float(input("what was the total bill? $"))
tip_percentage = int( input("what percentage of tip would you like to give? 10,12, or 15 ? "))
people = int(input("How many people to split the bill? "))
amount_without_tip = total_bill/ people
final_amount_without_tip=  round(amount_without_tip, 3)
print(f"Each person should pay $ {final_amount_without_tip} without tip.")

bill_with_tip = total_bill + (tip_percentage/100)*total_bill
amount = bill_with_tip / people
final_amount = round(amount , 2)
print(f"Each person should pay ${final_amount} with tip.\n")
print("Thanks a lot.......")'''

print("Welcome to tip calculator !!! ")
total_bill  = float(input("what was the total bill? $"))
tip_percentage = int( input("what percentage of tip would you like to give? 10,12, or 15 ? "))
people = int(input("How many people to split the bill? "))
final_amount_without_tip = total_bill/ people
                                                            # final_amount_without_tip=  round(amount_without_tip, 3)
final_amount_without_tip = "{:.2f}".format(final_amount_without_tip)
print(f"Each person should pay $ {final_amount_without_tip} without tip.")

bill_with_tip = total_bill + (tip_percentage/100)*total_bill
amount = bill_with_tip / people
                                                            # final_amount = round(amount , 2) 
final_amount = "{:.2f}".format(bill_with_tip)
print(f"Each person should pay ${final_amount} with tip.\n")
print("Thanks a lot.......")



















