# Lists in Python
my_list = ["apple", "banana", "cherry", "date"]
print(f"Original List: {my_list}")

# Accessing elements
first_element = my_list[0]
second_element = my_list[1]
print(f"First Element: {first_element}")
print(f"Second Element: {second_element}")

# Modifying elements
my_list[1] = "blueberry"
my_list[2] = "Kiwi"
print(f"Modified List: {my_list}")

# Adding elements
my_list.append("elderberry")
my_list.append("Pineapple")
print(f"List after Appending: {my_list}")

my_list.insert(2, "fig")
my_list.insert(0, "Orange")
print(f"List after Inserting: {my_list}")

my_list.extend(["Litchi", "Pear", "Chiku"])
print(f"List after Extending: {my_list}")

# Removing elements
my_list.remove("Kiwi")
print(f"List after Removing 'Kiwi': {my_list}")

# Popping elements
popped_element = my_list.pop()
print(f"Popped Element: {popped_element}")
print(f"List after Popping: {my_list}")

# Length of the list
list_length = len(my_list)
print(f"Length of the List: {list_length}")

# Slicing the list
sliced_list = my_list[1:4]
print(f"Sliced List (index 1 to 3): {sliced_list}")
