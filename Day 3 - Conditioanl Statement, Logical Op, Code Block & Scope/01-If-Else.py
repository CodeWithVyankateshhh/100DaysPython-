# If-Else Statement
# An if-else statement is used to execute a block of code based on a condition.

#######   Syntax: #########
# if condition: 
#     # code to execute if condition is True
# else:
#     # code to execute if condition is False 
###########################



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: # Condition to check if height is 120 cm or more
  print("You can ride the rollercoaster!!!!")
else:
  print("Sorry, you have to grow taller before you can ride.")