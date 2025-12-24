# Randomization in Python
import random
# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"Random Integer between 1 and 10: {random_integer}")
print(random.randrange(1,100))

# Generate a random float between 0 and 1
random_float = random.random() * 5
print(f"Random Float between 0 and 1: {random_float}")

# Generating uniform random float between two values
uniform_random = random.uniform(1, 10)  
print(f"Uniform Random Float between 1 and 10: {uniform_random}")

# Randomly choose an element from a list
my_list = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(my_list)
print(f"Randomly chosen element: {random_choice}")

# Shuffle a list randomly
random.shuffle(my_list)
print(f"Shuffled List: {my_list}")

# Sample multiple unique elements from a list
random_sample = random.sample(my_list, 2)
print(f"Random Sample of 2 elements: {random_sample}") 

# Sample multiple elements with replacement
random_choices_with_replacement = random.choices(my_list, k=3)
print(f"Random Choices with Replacement (3 elements): {random_choices_with_replacement}")

# Seed the random number generator for reproducibility
random.seed(44) # meaningful number like your birth year and so on it prints same random number every time like a password like that
seeded_random_integer = random.randint(1, 10)
print(f"Seeded Random Integer between 1 and 10: {seeded_random_integer}")

# Note: The outputs will vary each time you run the code unless a seed is set.

print(random.uniform(1,10))
print(random.randint(1,10))
print(random.randrange(1,10))
print(random.random())
print(random.choice(['apple', 'banana', 'cherry', 'date']))
print(random.choices(['apple', 'banana', 'cherry', 'date'], k=2))
print(random.sample(['apple', 'banana', 'cherry', 'date'], 2))
print(random.shuffle(['apple', 'banana', 'cherry', 'date']))
print(random.seed(10))

