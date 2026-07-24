"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese
"""
#code here (1)
weight = float(input("input your weight (Kg): "))
height = float(input("input your height (Meter): "))

bmi = weight / (height ** 2)  

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25.0:
    category = "Normal weight"
elif bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"

print(f"Bmi : {bmi:.1f}")      
print("Category : ", category)