### if / elif / else

```py

if condition1:
  do A
elif condition2:
  do B
else:
  do C

```

> Just Run only one `do`

---

### Multiple if

```py

if condition1:
  do A
if condition2:
  do B
if condition3:
  do C

```

> Run All `do` if is valid

---

### one line condition (if)

```py
fruit = 'Apple'

isApple = True if fruit == 'Apple' else False
```
---

# Logical Operators

| Operator | Meaning |
| --- | --- |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=`  | Less than or equal to |
| `==`  | Equal to |
| `!=`  | Not equal to |

```py
a = 10
b = 15
c 20

if a >= 5 and a <= 15:
  print("a between 5 - 15")

if b <= 15 or c <= 15:
  print("b or c less than or equal 15")
else:
  print("b or c not less than or equal 15")

# we are have `and` , `or` logical

print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)


# we have already `not`

print(not False)
print(not True)

a = True
if not a == False:
  print("a is True")

```

---
> exercise 2 and 3 and 4