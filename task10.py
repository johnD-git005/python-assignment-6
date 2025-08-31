"""# 10
def task10_multiply_list(numbers):
    
    Task 10:
    Write a function that accepts a list of numbers as a parameter
    and returns the product of all the numbers in the list.
    Example: multiply_list([1, 2, 3, 4]) → 24
    
    pass """

def task10_multiply_list(numbers):

	product = 1

	for num in numbers:
		product *= num

	return f"Product of {numbers} = {product}"

print(task10_multiply_list([1, 2, 3, 4]))
