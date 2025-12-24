# Modulo Operator
# The modulo operator (%) returns the remainder of a division operation.
a = 10
b = 3
print(a % b)  # Output: 1, because 10 divided by 3 leaves a remainder of 1
# Example Usage
x = 25
y = 4
print(x % y)  # Output: 1, because 25 divided by 4 leaves a remainder of 1


##### You can use the modulo operator to determine if a number is even or odd.#########
number = int(input("Enter a number: "))

checkEven = number % 2
if checkEven == 0:
  print("its even number")
else:
  print("its not even numer")
  ################################