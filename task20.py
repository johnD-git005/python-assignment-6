"""# 20
def task20_simple_interest(principal, rate, time):
    
    Task 20:
    Write a function that calculates simple interest.
    Formula: (principal * rate * time) / 100
    
    pass"""

def task20_simple_interest(principal, rate, time):

	simple_interest = (principal * rate * time) / 100

	return f"Simple Interest →  {simple_interest}"

print(task20_simple_interest(60, 4, 10))
