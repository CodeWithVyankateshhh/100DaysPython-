# Multiple if-else statements
# multiple if-else statements are used to check several conditions independently.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is Your age? = "))

bill = 0
if height >= 120:
    print("You can ride ....")
    if age < 12:
        bill = 5
        print(f"You pay {bill}")
    elif age <= 18:
        bill = 7
        print(f"You pay {bill}")

    else:
        print(f"You pay {bill}")

    wantPhoto = input(
        'Do you want to have a photo take? Type "Y" for Yes and "N" for No.')
    if wantPhoto == "y":
        bill += 3
        print(f"You pay {bill}")

    else:

        bill = bill
        print(f"You pay {bill}")

else:
    print("You cant ride....")
