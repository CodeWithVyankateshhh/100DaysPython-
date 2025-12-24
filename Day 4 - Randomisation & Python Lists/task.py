fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Grape"]
vegetables = ["Asparagus", "Broccoli", "Carrot", "Daikon", "Eggplant", "Fennel", "Garlic"]

dirty_dozen = [fruits,vegetables] # Create a nested list containing fruits and vegetables
# Accessing elements from the nested list
print(dirty_dozen[0][2])  # Accessing "Cherry" from fruits
print(dirty_dozen[1][4])  # Accessing "Eggplant" from vegetables

print(dirty_dozen)