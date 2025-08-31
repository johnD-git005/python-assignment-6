"""→ # 28
def task28_movie_ticket_price(age):
    
    Task 28:
    Write a function that determines ticket price based on age:
    - Age < 12: 500
    - 12 <= Age < 18: 700
    - 18 <= Age < 60: 1000
    - Age >= 60: 600
    Return the ticket price.
    
    pass"""

def task28_movie_ticket_price(age):
	
	if age >= 60:
		return f"Age: {age} year(s) Ticket Price →  600"

	elif age >= 18 and age < 60:
		return f"Age: {age} year(s) Ticket Price →  1000"

	elif age >= 12 and age < 18:
		return f"Age: {age} year(s) Ticket Price →  700"

	elif  age >= 0 and age < 12:
		return f"Age: {age} year(s) Ticket Price →  500"

	elif age < 0:
		return f"Age: {age} year(s) →  Invalid Age!"

print(task28_movie_ticket_price(18))
