"""# 8
def task8_even_or_odd(n):
    
    Task 8:
    Write a function that accepts a number and returns
    "Even" if the number is even, and "Odd" if the number is odd.
    
    pass"""

def task8_even_or_odd(n):
	if n % 2 == 0:
		return "Even"

	else:
		return "Odd"

print(task8_even_or_odd(20))
print(task8_even_or_odd(23))
print(task8_even_or_odd(18))
print(task8_even_or_odd(7))
