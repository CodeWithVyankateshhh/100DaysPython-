# For Loops in Python
# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# The for loop does not require an indexing variable to set beforehand.
# Syntax:
# for item in sequence:
#     # do something with item
# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for Allfruit in fruits:
    print(Allfruit)
# Example 2: Iterating through a string
for Letter in "Hello":
    print(Letter)
    
# Example 3: Using range() to generate a sequence of numbers
for number in range(5):  # This will generate numbers from 0 to 4
    print(number)
    print("Loop is done!")
    
# Example 4: Using range() with a start and end value
for number in range(2, 6):  # This will generate numbers from 2 to 5
    print(number)
    
# Example 5: Using range() with a step value
for number in range(1,10,2):  # This will generate odd numbers from 1 to 9
    print(number)
    
  