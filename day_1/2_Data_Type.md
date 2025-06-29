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


