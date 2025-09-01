"""# 37
def task37_convert_currency(amount, rate):
    
    Task 37:
    Write a function that converts money from one currency to another
    using a given conversion rate.
    Example: convert_currency(100, 1500) → 150000
    
    pass"""


def task37_convert_currency(amount, rate):
	
	currency_conversion = amount * rate
	return f"Amount: (amount), Rate: {rate} →  {currency_conversion}"

print(task37_convert_currency(100, 1500))
