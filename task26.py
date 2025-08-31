"""→ # 26
def task26_calculate_bmi(weight, height):
    
    Task 26:
    Write a function that accepts weight (kg) and height (m),
    and returns the Body Mass Index (BMI).
    Formula: BMI = weight / (height^2)
    Round the result to 2 decimal places.
    
    pass"""

def task26_calculate_bmi(weight, height):

	BMI = weight / (height ** 2)

	return f"Weight: {weight}kg, Height: {height}m BMI →  {BMI:.2f}"

print(task26_calculate_bmi(60, 5.6))
