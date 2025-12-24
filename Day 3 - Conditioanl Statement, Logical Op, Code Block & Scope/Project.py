# Trasurehunt Game

print("Welcome to the Treasure Hunt Game!")

choise1 = input(
    "Your at a cross road. Where do you want to go? \n Type 'Left' or 'right' ").lower()


if choise1 == 'left':
    print("You have come to a lake, There is an Island in the middle of the lake ")

    choise2 = input(
        "Type 'wait' to wait for a Boat. or \n Type 'swim' to Swim across ").lower()

    if choise2 == 'wait':
        print("You arrive at the Island unharmed..")

        print("There is a house with 3 Doors.\n Which colour do you choose? ")
        choise3 = input("1. Red, 2. Yellow, 3. Blue ").lower()
        if choise3 == 'yellow':
            print("You Win...")
        else:
            print("Game over....")
    else:  # of choise2
        print("Your Game Over.....")

else:  # of choise1
    print("Your Game Over....")
