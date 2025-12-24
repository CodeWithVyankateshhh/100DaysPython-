# Rock Paper Scissors Game
import random
import sys  # for exiting the program in case of invalid input #IMP#
# Rocks wins against Scissors
# Scissors wins against Paper
# Paper wins against Rocks

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissors!")
print("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors.")


GameImage = [rock, paper, scissors]
choice_names = ["Rock", "Paper", "Scissors"]
userChoice = int(input(" "))


if userChoice < 0 or userChoice > 2:
    print("Invalid input! Please choose 0, 1, or 2.")
    sys.exit()
else:
    print(f"\nYou chose: {choice_names[userChoice]}")
    print(GameImage[userChoice])


ComputerChoise = random.randint(0, 2)
print(f'\nComputer Choice : {choice_names[ComputerChoise]}')
print(GameImage[ComputerChoise])


if ComputerChoise == userChoice:
    print("Its Draw.")


elif (ComputerChoise == 0 and userChoice == 2) or \
     (ComputerChoise == 2 and userChoice == 1) or \
     (ComputerChoise == 1 and userChoice == 0):
    print("Computer Wins")
else:
    print("You win....")
