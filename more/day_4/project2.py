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

computer_choice = random.randint(0, 2)

if player_choice == computer_choice:
    print("-- Equal --")
else:
    if player_choice == 0:  # rock
        if computer_choice == 1:  # paper
            print(rock)
            print("Computer Choice:")
            print(paper)
            print("You lose")
        else:  # scissors
            print(rock)
            print("Computer Choice:")
            print(scissors)
            print("You Win")
    elif player_choice == 1:  # paper
        if computer_choice == 0:  # rock
            print(paper)
            print("Computer Choice:")
            print(rock)
            print("You Win")
        else:  # scissors
            print(paper)
            print("Computer Choice:")
            print(scissors)
            print("You lose")
    elif player_choice == 2:  # scissors
        if computer_choice == 0:  # rock
            print(scissors)
            print("Computer Choice:")
            print(rock)
            print("You lose")
        else:  # paper
            print(scissors)
            print("Computer Choice:")
            print(paper)
            print("You Win")
    else:
        print("Input Invalid !")
