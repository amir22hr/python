# casting

```py

"123"

print("123" + "456")

int(124)

print(int(123) + int(456))
# for exmaple get number(str) in db, and we need all data convert if we need, just every thing in db is TEXT or string

# easy ex: get number in cli ...

# error
int("abc")
# ===> ValueError


```

---

```py

# x = input("Enter your name: ")
# print(x)
# print(type(x))
# print(len(x))

#---

# print("Number of letters in your name: " + len(input("Enter your name: ")))

# print(type(len("amir")))


print("Number of letters in your name: " + str(len(input("Enter your name: "))))


```