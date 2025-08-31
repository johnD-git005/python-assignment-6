""" # 27
def task27_discounted_price(price, discount_percent):
    
    Task 27:
    Write a function that accepts an item's price and discount percentage,
    and returns the final price after discount.
    Example: discounted_price(1000, 20) → 800
    
    pass"""


def task27_discounted_price(price, discount_percent):

	discount_percentage = (price) * (discount_percent / 100)
	final_discount = price - discount_percentage

	return f"Price: {price}, Discount: {discount_percent}% DISCOUNTED PRICE →  {final_discount}"

print(task27_discounted_price(1000, 20))
