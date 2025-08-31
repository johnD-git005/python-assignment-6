"""# 16
def task16_factorial(n):
    
    Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
    
    pass"""

def task16_factorial(n):
	
	if n <= 0:
		return "Number must be greater than Zero"	
	else:
		factorial = 1

		for num in range(1, n + 1):
			factorial *= num	

	return f"Factorial of {n} →  {factorial}"

print(task16_factorial(5))

