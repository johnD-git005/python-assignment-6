"""# 12
def task12_is_prime(n):
    
    Task 12:
    Write a function that accepts a number as a parameter
    and returns True if the number is prime, otherwise False.
    
    pass"""

def task12_is_prime(n):

	if n <= 1:
		return "False"

	else:
		for number in range(2, n):
			if n % number == 0:
				return "False"
		else:
			return "True"

print(task12_is_prime(13))
