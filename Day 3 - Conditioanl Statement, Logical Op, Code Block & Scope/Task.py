print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height < 120:
  print("Sorry, you have to grow taller before you can ride.")
else:
    age = int(input("What is your age? "))

    Ticket = 5
    print("You can ride the rollercoaster!!!!")
    
    # Free ride condition must come first
    if age > 55:
      print("You cant ride ...")
    elif age >= 45 and age <= 55:
        Ticket = 0
        print(f"You can Enjoy Ride Freeeee. {Ticket}$")
    
    else:
      Photo = input("Do you want photo? (y/n): ").lower()

      
      if age < 12:
        if Photo == 'y':
            Ticket += 3
        print(f"Please pay {Ticket}$")

      elif age >= 12 and age <= 18:
        Ticket += 2
        if Photo == 'y':
            Ticket += 3
        print(f"Please pay {Ticket}$")

      elif age > 18:
        Ticket += 7
        if Photo == 'y':
            Ticket += 3
        print(f"You pay {Ticket}$")
  
      else:
        print("You are too old for this Ride...")


