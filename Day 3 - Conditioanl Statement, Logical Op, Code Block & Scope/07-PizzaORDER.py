# Pizza Order Program

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M OR L: ")

pepperoni = input("Do you want Pepperoni on your Pizza? Y or N: ")

extra_cheese = input("Do You want extra Cheese? Y or N: ")

PizzaPrice = 0


if size == 's':
    if pepperoni == 'y':

        PizzaPrice = 15 + 1
        if extra_cheese == 'y':
            PizzaPrice += 1
        else:
            PizzaPrice
    else:
        PizzaPrice = 15

elif size == 'm':
    if pepperoni == 'y':
        PizzaPrice = 20 + 3
        if extra_cheese == 'y':
            PizzaPrice += 1
        else:
            PizzaPrice

    else:
        PizzaPrice = 20

elif size == 'l':
    if pepperoni == 'y':

        PizzaPrice = 25 + 3
        if extra_cheese == 'y':
            PizzaPrice += 1
        else:
            PizzaPrice
    else:
        PizzaPrice = 25

print(f"Your Pizza Bill {PizzaPrice} $")
