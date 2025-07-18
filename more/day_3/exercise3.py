# BMI Calculator with Interpretations

"""
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:
"""

# Start Coding

weight = 76
height = 1.75

bmi = weight / (height**2)
print(bmi)

# conditions
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
else:
    print("Overweight")
