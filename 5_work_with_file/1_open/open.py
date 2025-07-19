# File Handling

# mode: r: read - w: write - a: append
# extra mode: t: text, b:binary

# Write
# with open("amir.txt", "w") as f:
#     f.write("Hi")
#     f.close()

# read
# my_file = open("amir.txt", "r")
# print(my_file.read())

# with open("amir.txt", "r") as f:
#     print(f.read())
#     f.close()


# append
# with open("amir.txt", "a") as f:
#     f.write("\nWhat's Up?")
#     f.close()

# Create
# with open("rooz.txt", "x") as f:
#     f.write("hello")
#     f.close()

# readline
# with open("rooz.txt") as f:
#     word1 = f.readline()
#     word2 = f.readline()
#     print(word1)
#     f.close()

#
# with open("rooz.txt") as f:
#     for x in f:
#         print(x)

# delete
import os


os.path()
os.remove("amir.txt")
