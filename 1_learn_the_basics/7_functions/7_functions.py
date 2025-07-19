# Built-in functions

# print(*objects, sep=' ', end='\n', file=None, flush=False)
# * -> args -> argument
# print("Hello Wold")
# print(123)
# print(True)
print("Amir", "Rooz", "Ali", sep="", end="\n\n\n")

# ------------------------------
# ------------------------------
# ------------------------------

# Functions


def amir():
    pass


amir()

# ------


# Abstraction
# تمرکز بر روی “چه کاری انجام می‌دهد” نه “چگونه انجام می‌دهد”
def sum():
    pass


sum()

# Encapsulation


# ---

# Todo: Encapsulation - Modularity
# Modularity

"""
# Main program

# Read the file
<statement_0>
<statement_1>
...
<statement_n>

# Process the file
<statement_0>
<statement_1>
...
<statement_n>

# Write the result to another file
<statement_0>
<statement_1>
...
<statement_n>
"""

# ---

# Reusability

# ---

# Maintainability

# ---

# Testability

# --------------
# --------------


# Positional Arguments
def greet(name, message):
    print(f"{message}, {name}!")


greet("Roozbeh", "Salam Kasgam")


# Keyword Arguments
def greet(name, message):
    print(f"{message}, {name}!")


greet(message="Salam Kasgam", name="Roozbeh")

# ---


# Producing Side Effects
def print_hello():
    print("Hello")


print_hello()


# Returning Values
def add(a, b):
    return a + b


result = add(2, 4)
print(result)


# Exiting Functions Early
def check_age(age):
    if age < 0:
        return "Invalid age"
    return "Valid age"


print(check_age(12))


# Returning Boolean Values
def is_even(num):
    return num % 2 == 0


print(is_even(8))


# Generator Iterators
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


print(list(count_up_to(5)))


# Closure
def make_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


# Advanced Fucntions


# Default Argument Values
def greet(name="amir"):
    print(f"hi {name}!")


greet()


# *args
def sum_all(*args):
    if "b" in args:
        return "gofti b"
    if "a" in args:
        return "gofti a"
    return "Dar command ham nist"


print(sum_all("a", "b", "c"))


# **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="amir", age=15, sex="male")


# combine
def func(*args, **kwargs):
    pass


# TODO
# (Keyword-Only)
def func(*, a, b):
    pass


# ---
