### int

```python

x = 10
y = -5
z = 0

print(type(x)) # <class 'int'>

```

---

### float 

```python

a = 3.14
b = -0.5
c = 2.0

print(type(a)) # <class 'float'>

``` 

### complex

```python

d = 3 + 4j

print(type(d))  # <class 'complex'>
print(d.real)  # 3.0
print(d.imag)  # 4.0

```

---

### String - str

```python

s1 = 'Hello'
s2 = "World"
s3 = """ this is
    a multi
    line 
    string code """

s4 = "123"

print(type(s1))  # <class 'str'>
print(s1 + " " + s2)  # Hello World
print(s1[0])  # H (دسترسی به کاراکترها با اندیس)
print(len(s1))  # 5 (طول رشته)

```

---

### List

```python

my_list = [1, 2, 3, 'a', 'b', True]
print(type(my_list)) # <class 'list'>

# access to value on list
print(my_list[0]) # 1
print(my_list[-1]) # True

# change value in list
my_list[1] = 'python'
print(my_list) # [1, 'python', 3, 'a', 'b', True]

# add new value to list
my_list.append('new')
print(my_list)  # [1, 'python', 3, 'a', 'b', True, 'new']

# delete value in list
my_list.remove('a')
print(my_list)  # [1, 'python', 3, 'b', True, 'new']


```

---

# Tuples

```python

my_tuple = (1, 2, 3, 'a', 'b')
print(type(my_tuple))  # <class 'tuple'>

# access to value in Tuple
print(my_tuple[2])  # 3

# in Tuples we can't change value 
# my_tuple[1] = 'new'  # خطا: TypeError

# Example:
def get_user():
    return ("John", 30, "john@example.com")

name, age, email = get_user()

```

---

# Sets

```py

my_set = {1, 2, 3, 3, 4}
print(my_set)  # {1, 2, 3, 4} (تکراری‌ها حذف می‌شوند)
print(type(my_set))  # <class 'set'>

# اضافه کردن
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

# حذف
my_set.remove(2)
print(my_set)  # {1, 3, 4, 5}

# عملگرهای مجموعه
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}

```

---

# Dictionaries

```py

my_dict = {'name': 'Ali', 'age': 25, 'city': 'Tehran'}
print(type(my_dict))  # <class 'dict'>

# دسترسی به مقادیر
print(my_dict['name'])  # Ali
print(my_dict.get('age'))  # 25

# اضافه یا تغییر کلید-مقدار
my_dict['job'] = 'Developer'
my_dict['age'] = 26

# حذف
del my_dict['city']
print(my_dict)  # {'name': 'Ali', 'age': 26, 'job': 'Developer'}

# کلیدها و مقادیر
print(my_dict.keys())  # dict_keys(['name', 'age', 'job'])
print(my_dict.values())  # dict_values(['Ali', 26, 'Developer'])

```

---

# Boolean (bool)

```py

t = True
f = False
print(type(t))  # <class 'bool'>

# استفاده در شرط‌ها
if 10 > 5:
    print(t)  # True

# تبدیل به بولین
print(bool(1))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool("Hello"))  # True

```

# None

```py

x = None
print(type(x))  # <class 'NoneType'>

# استفاده معمول برای مقداردهی اولیه
result = None

```

