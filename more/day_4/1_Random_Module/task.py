import random

# import my_module

random_number = random.randint(1, 10)  # all number between 1 - 10
print(random_number)

# print(my_module.my_favourite_number)

# ----random.random()----

# between 0 inclusive and up to 1, not inclusive
random_number_0_to_1 = random.random()

print(random_number_0_to_1)

# ---random.random()---
# # between 0 inclusive and up to 10, not inclusive
random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

# ---random.uniform()---
random_float = random.uniform(1, 10)
print(random_float)
