## Question 1:
#### Given the following list:

```py
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

```

#### Which line of code will give you `Apples`?

- [ ] fruits[3]
- [ ] fruits[4]
- [ ] fruits.Apples()
- [ ] fruits[-5]
- [ ] fruits[-4]

---

## Question 2:
#### Given the following list:

```py
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
```

#### What do you think will be printed?

- [ ] `["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Lemons"]`
- [ ] `["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Lemons"]`
- [ ] `["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Melons", Lemons"]`
- [ ] `["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]`

---

## Question 3:
#### Given the following list:

```py
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
```

#### What will be printed?

##### What's going on?

This question combines several of the Python List concepts that we’ve seen in the previous lessons in isolation. If the code above is at all confusing, I recommend breaking down what’s going on using several print statements using repl.it. First, try printing out:

print(dirty_dozen)
Then print out:

print(dirty_dozen[0])
print(dirty_dozen[1])
To see what happens at the next stage print out:

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
I hope this helps clarify how nested lists work. 🙂

- [ ] Spinach
- [ ] Strawberries
- [ ] Kale 
- [ ] ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"] 
- [ ] Nectarines 

---

