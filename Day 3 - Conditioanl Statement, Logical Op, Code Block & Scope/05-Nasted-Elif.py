# Nested if-elif-else statements
# nested if-elif-else statements are used to check multiple conditions in a sequential manner.
#######   Syntax: ######### 
# if condition1:
#     # code to execute if condition1 is True
# elif condition2:
#     # code to execute if condition1 is False and condition2 is True
# else:
#     # code to execute if both condition1 and condition2 are False   
###########################
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is Your age? = "))

if height >= 120: 
  print("You can ride ....")
  if age < 12:
    print("pay 5$.")
  elif age<= 18:
    print("pay 7$.")
  else:
    print("pay 12$.")
else:
  print("You cant ride....")
  