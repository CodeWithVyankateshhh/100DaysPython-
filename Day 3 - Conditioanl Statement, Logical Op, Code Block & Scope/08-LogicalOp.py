# Logical Operators in Python
# and, or, not
a = True
b = False
print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False
print("not b:", not b)      # True

# False and False = False
print("False and False:", False and False)  # False
# False or False = False  
print("False or False:", False or False)    # False
# True and True = True
print("True and True:", True and True)      # True
# True or True = True
print("True or True:", True or True)        # True

# not True = False
print("not True:", not True)                  # False
# not False = True
print("not False:", not False)                # True  

# Example usage in conditional statements
age = 16
has_id = True
if age >= 18 and has_id:
    print("You are allowed to enter the club.")
else:
    print("You are not allowed to enter the club.")
if age < 18 or not has_id:

    print("You cannot enter the club.")
else:
    print("You can enter the club.")


# logical operators with numbers
num = 16
if num > 5 and num < 15:
    print("Number is between 5 and 15.")
if num < 5 or num > 15:
    print("Number is outside the range of 5 to 15.")  
else:
    print("Number is within the range of 5 to 15.")