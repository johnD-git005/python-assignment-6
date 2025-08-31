"""→ # 32
def task32_parking_fee(hours):
    
    Task 32:
    Write a function that calculates parking fees:
    - First 2 hours: 200 Naira flat
    - Every additional hour: 100 Naira
    Example: parking_fee(5) → 200 + 3*100 = 500
    
    pass"""


def task32_parking_fee(hours):

	first_two_hours = 2
	parking_fee = 200
	additional_hour = 100

	if hours > 0 and hours <= 2:
		new_parking_fee = (hours * parking_fee) // 2

		return f"{hours} hour(s), Parking Fee →  {new_parking_fee}"

	elif hours > 2:
		extra_hours = hours - 2
		additional_hour *= extra_hours
		new_parking_fee = parking_fee + additional_hour

		return f"{hours} hour(s), Parking Fee →  {new_parking_fee}"

	elif hours < 0:
		return f"{hours} hour(s) →  Invalid Input!"

print(task32_parking_fee(-1))
