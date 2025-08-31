"""# 19
def task19_find_min(numbers):
    
    Task 19:
    Write a function that accepts a list of numbers
    and returns the smallest number.
    Do not use Python's built-in min() function.
    
    pass """

def task19_find_min(numbers):
	
	smallest_number = numbers[0]

	for num in numbers:
		if num < smallest_number:
			smallest_number = num

	return f"Smallest Number {numbers} →  {smallest_number}"


print(task19_find_min([11, 92, 35, 24, 85]))
