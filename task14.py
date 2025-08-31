"""# 14
def task14_sum_list(numbers):
    
    Task 14:
    Write a function that accepts a list of numbers
    and returns the sum of all the elements in the list.
    Do not use Python's built-in sum() function.
    
    pass """

def task14_sum_list(numbers):
	
	summation = 0

	for num in numbers:
		summation += num

	return f"Summation of {numbers} = {summation}"

print(task14_sum_list([1, 2, 3, 4, 5]))
