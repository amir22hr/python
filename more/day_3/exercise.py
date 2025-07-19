# BMI Calculator
# BMI formula : Weight in kg / (Height in meter)^2

height = 1.65  # m
weight = 84  # kg

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height * height)
# bmi = weight / (height) ** 2

print(bmi)

print(int(bmi))  # downner number or flooring

print(round(bmi))  # round up and down by .number

print(round(bmi, 2))  # number.[2] ==> 30.85

# ---

print(round(12.1))  # 12
print(round(12.4))  # 12
print(round(12.5))  # 12
print(round(12.6))  # 13
print(round(12.9))  # 13
