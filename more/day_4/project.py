# Day 4 Project: Rock Paper Scissors

import random

# 0 for Rock, 1 for Paper, 2 for Scissors
art_RPS = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

# Player Input
player_choose = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
)

# Computer Think (random)
list_RPS = ["Rock", "Paper", "Scissors"]
computer_choose = random.choice(list_RPS)

# Compare
if list_RPS[player_choose] == computer_choose:
    print(art_RPS[player_choose])
    print("-- Equal --")
    exit()

if list_RPS[player_choose] == list_RPS[0]:  # Rock
    print(art_RPS[0])
    print("Computer Chose:")
    if computer_choose == list_RPS[1]:  # Paper
        print(art_RPS[1])
        print("You lose")
    else:  # Scissors
        print(art_RPS[2])
        print("You Win")

if list_RPS[player_choose] == list_RPS[1]:  # Paper
    print(art_RPS[1])
    print("Computer Chose:")
    if computer_choose == list_RPS[2]:  # Scissors
        print(art_RPS[2])
        print("You lose")
    else:  # Rock
        print(art_RPS[0])
        print("You Win")

if list_RPS[player_choose] == list_RPS[2]:  # Scissors
    print(art_RPS[2])
    print("Computer Chose:")
    if computer_choose == list_RPS[0]:  # Rock
        print(art_RPS[0])
        print("You lose")
    else:  # Paper
        print(art_RPS[1])
        print("You Win")
