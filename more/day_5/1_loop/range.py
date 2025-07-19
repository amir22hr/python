# Range

for number in range(1, 10):  # 1 include, 10 not include
    print(number)

# range with strp
for number in range(1, 10, 2):  # 1 include, 10 not include
    print(number)

# ---

total = 0
for number in range(1, 101):
    total += number
print(total)
