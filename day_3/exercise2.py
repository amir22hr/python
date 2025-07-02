# Even or odd number

number_to_check = int(input("Enter Your Number: "))

# normal if
if number_to_check % 2 == 0:
    print(f"{number_to_check} is Even.")
else:
    print(f"{number_to_check} is Odd.")

# one line if
# print(f"{number_to_check} is Even" if number_to_check % 2 == 0 else f"{number_to_check} is Odd")
