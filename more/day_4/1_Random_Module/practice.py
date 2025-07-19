# Heads or Tails
# Create coin flip program ...
import random

coin = random.randint(0, 1)

if coin == 0:
    print(f"Heads - {coin}")
else:
    print(f"Tails - {coin}")
