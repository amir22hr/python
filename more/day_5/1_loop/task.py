fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)


# --- sum ---

student_scores = [150, 142, 185, 120, 171, 149, 21, 59, 199, 84]

total_exam_score = sum(student_scores)
print(total_exam_score)

# or

sum = 0
for score in student_scores:
    sum += score
print(sum)


# -- max --
print(max(student_scores))

# or

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
