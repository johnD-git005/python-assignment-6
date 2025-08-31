"""# 21
def task21_calculator(a, b, operation):
   
    Task 21:
    Write a function that works like a simple calculator.
    It should accept two numbers and an operation (+, -, *, /)
    and return the result.
    Example: calculator(4, 2, "+") → 6
   
    pass """

def task21_calculator(a, b, operation):

	if operation == "+":
		result = a + b
		return f"{a} + {b} = {result}"

	elif operation == "-":
		result = a - b
		return f"{a} - {b} = {result}"

	elif operation == "*":
		result = a * b
		return f"{a} * {b} = {result}"

	elif operation == "/":
		result =  a / b
		return f"{a} / {b} = {result}"

	else:
		return "Invalid Input"

print(task21_calculator(4, 2, "/"))
