"""→ # 29
def task29_shopping_total(prices):
    
    Task 29:
    Write a function that accepts a list of item prices
    and returns the total cost of all items.
    
    pass"""


def task29_shopping_total(prices):

	total_cost = 0

	for items in list(prices):

		total_cost += items

	return f"Total Cost of Items →  {total_cost}"

print(task29_shopping_total([500, 120, 1400, 850, 500]))
