# Type Error and Conversion
# This script demonstrates how to handle TypeErrors and perform type conversion in Python.
# Attempting to add a string and an integer will raise a TypeError
string_num = "100"
integer_num = 50  

# Uncommenting the next line will raise a TypeError
# result = string_num + integer_num  # This will raise TypeError
# To fix this, we need to convert one of the types
# Convert string to integer

converted_string_num = int(string_num)
result = converted_string_num + integer_num
print("Result after converting string to integer:", result)


# cheking data types
print(type(123))          # integer
print(type(45.67))        # float 
print(type("Python"))     # string
print(type(False))       # boolean
print(type(2 + 3j))     # complex number

