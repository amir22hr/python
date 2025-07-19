# Day 4 Project: Rock Paper Scissors

import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Player Input
player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
)

game_images = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print(game_images[player_choice])
print("Computer Choice:")
print(game_images[computer_choice])

# logic
if player_choice >= 3 and player_choice < 0:
    print("Input Invalid, you lose!")
elif player_choice == computer_choice:
    print("Equal")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice < computer_choice:
    print("You lose!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
else:
    pass
