# Nested if-else statements
# nested if-else statements are used to check multiple conditions in a hierarchical manner.
#######   Syntax: #########
# if condition1:
#     if condition2:
#         # code to execute if both condition1 and condition2 are True
#     else:
#         # code to execute if condition1 is True and condition2 is False
# else:
#     # code to execute if condition1 is False
###########################


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is Your age? = "))

if height >= 120: # Condition to check if height is 120 cm or more
  
  print("You can ride the rollercoaster!!!!")
  if age <= 18:
    print("Please pay 7$")
  else:
    print("Please pay 12$")
else:
  print("Sorry, you have to grow taller before you can ride.")