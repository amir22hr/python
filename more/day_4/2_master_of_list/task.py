# List
states_of_america = [
    "Washington",
    "New York",
    "Texas",
    "Lowa",
    "Alaska",
    "Florida",
    "Indiana",
    "Ohio",
    "Tennessee",
    "Georgia",
    "Utah",
]

# index (read)
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])
# ...
print(states_of_america[-1])  # last to first
print(states_of_america[-2])

# indexError
print(states_of_america[100])  # IndexError: list index out of range
# fix
num_of_state = len(states_of_america)
print(states_of_america[num_of_state - 1])  # python index start by 0

# index - edit or write force
states_of_america[1] = "New Jersey"
states_of_america[-1] = "Delaware"

# extend
states_of_america.extend(["Pennsylvania", "Alabama", "Oklahoma"])
print(states_of_america)
# Extend the list by appending all the items from the iterable.

# append
states_of_america.append("Idaho")
print(states_of_america)  # Add an item to the end of the list.

# insert
# یک عنصر را در موقعیت مشخصی درج می‌کند
# پارامتر اول اندیسی است که عنصر قبل از آن درج می‌شود
letters = ["a", "b", "d"]
letters.insert(2, "c")
# نتیجه: ['a', 'b', 'c', 'd']


# ...
# ...
