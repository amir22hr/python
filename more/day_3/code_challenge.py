# Write a Pizza Delivery Program

print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need yo pay based on their size choice.

# todo: work out how much to add to their bill based on their peperoni choice.

# todo: work out their final amount based on whether if they want extra cheese.

# first write , and your final answer compare in mine

bill = 0

# size
size = input("What size pizza do you want? S, M or L: ")
if size.lower() == "s":
    bill += 15
    size = "Small"
elif size.lower() == "m":
    bill += 20
    size = "Medium"
elif size.lower() == "l":
    bill += 25
    size = "Large"
else:
    print("Invalid Input.")
    exit(1)

# pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni.upper() == "Y":
    bill += 2 if size == "S" else 3
    pepperoni = True
elif pepperoni.upper() == "N":
    pepperoni = False
else:
    print("Invalid Input.")
    exit(1) 

# extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese.upper() == "Y":
    bill += 1
    extra_cheese = True
elif extra_cheese.upper() == "N":
    extra_cheese = False
else:
    print("Invalid Input.")
    exit(1) 


# final answare:
print(f"Your Bill: [Pizza Size: {size} -- extra pepperoni: {"Yes" if pepperoni else "No"} -- extra cheese: {"Yes" if extra_cheese else "No"}]")
print(f"--> Please Pay ${bill}")
