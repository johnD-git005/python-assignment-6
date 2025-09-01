"""# 41
def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
    
    Task 41:
    Write a function to calculate the total price of a shirt order.
    - If quantity >= discount_threshold, apply discount_rate.
    Example: shirt_order(12, 2000) → discounted price
    
    pass"""

def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):

	if quantity < 0:
		return "Invalid Entry for Quantity!"

	elif price_per_shirt < 0:
		return "Invalid Entry for Price!"

	elif quantity >= discount_threshold:
		threshold_discount_price = price_per_shirt * discount_rate
		discount_price = price_per_shirt - threshold_discount_price

		return f"Quantity: {quantity}, Price Per Shirt: {price_per_shirt} →  Discount Price: {discount_price}"

	else:
		price = quantity * price_per_shirt
		return f"Quantity: {quantity}, Price Per Shirt: {price_per_shirt} →  Price: {price}"

print(task41_shirt_order(5, 1000))
