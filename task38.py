"""→ # 38
def task38_gas_station_bill(liters, price_per_liter):
    
    Task 38:
    Write a function that accepts the number of liters purchased
    and the price per liter, then returns the total cost.
    
    pass"""

def task38_gas_station_bill(liters, price_per_liter):

	if liters < 0 and price_per_liter < 0:
		return "Invalid Input for Liter(s) and Price Per Litre"

	elif liters < 0:
		return "Invalid Input for Liter(s)"

	elif price_per_liter < 0:
		return "Invalid Input for Price Per Litre"

	else:
		total_cost = liters * price_per_liter
		return f"Liter(s): {liters}, Price per liter: {price_per_liter} →  Total cost: {total_cost}"

print(task38_gas_station_bill(5, 500))
