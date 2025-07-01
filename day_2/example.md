# Example to Convert Data Types (Type Conversion)

```py

# رشته به عدد
num_str = "123"
num_int = int(num_str)
print(num_int + 7)  # 130

# عدد به رشته
num = 456
str_num = str(num)
print("Number is: " + str_num)  # Number is: 456

# لیست به تاپل
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3)

```

---

# Dictionary For Counter

```py

text = "hello world hello python"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'hello': 2, 'world': 1, 'python': 1}

```

---

# Using a set to remove duplicates

```py

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]

```

---

# Data type check (type checking)

```py

x = [1, 2, 3]
if isinstance(x, list):
    print("x is a list")

y = "hello"
if type(y) == str:
    print("y is a string")

```
