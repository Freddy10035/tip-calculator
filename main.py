# print("Freddie" [3])

# counting the values of characters in a string given
# num_char = len(input("What is your name? \n"))
# new_num_char = str(num_char)
# print("Your name has "+new_num_char+" characters")

##############################################################################

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# two_digit_number = int(two_digit_number)
# digit_1 = two_digit_number // 10
# digit_2 = two_digit_number % 10
# result = digit_1 + digit_2
# print("The sum of the digits is:", result)

# print(type(two_digit_number))
# digit_1 = two_digit_number[0]
# digit_2 = two_digit_number[1]
#
# print(int(digit_1) + int(digit_2))

##############################################################################
# BODY MASS INDEX
##############################################################################

# 🚨 Don't change the code below 👇

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# val_weight = float(weight)
# val_height = float(height)**2
# result = (val_weight/val_height)
# print(int(result))

##############################################################################
# LIFE IN WEEKS
##############################################################################

# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# days = 365
# weeks = 52
# months = 12
#
# # YEARS LEFT TO 90
# age_diff = 90 - int(age)
#
# months_to_90 = months*age_diff
# weeks_to_90 = weeks*age_diff
# days_to_90 = days*age_diff
#
# print(f"You have {days_to_90} days, {weeks_to_90} weeks and {months_to_90} months left.")


##############################################################################
# TIP CALCuLATOR
##############################################################################

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator")
bill = input("What was the total bill? KES")
bill_as_float = float(bill)

percentage_input = input("What percentage would you like to give? 10, 12 or 15? ")
percentage_input_as_int = int(percentage_input)

num_people = input("How many people to split the bill? ")
num_people_as_int = int(num_people)

total_bill = bill_as_float + (bill_as_float* (percentage_input_as_int/100))

# amount_to_be_paid_rounded = round(total_bill/num_people_as_int, 2)
amount_to_be_paid = "{:.2f}".format(total_bill/num_people_as_int)

print(f"Each person should pay: KES{amount_to_be_paid}")
