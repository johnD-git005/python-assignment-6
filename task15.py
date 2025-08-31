"""# 15
def task15_average_of_list(numbers):
    
    Task 15:
    Write a function that accepts a list of numbers
    and returns the average.
    Formula: average = sum of numbers / count of numbers
    
    pass"""

def task15_average_of_list(numbers):
	
	sum_of_numbers = 0
	count_of_numbers = len(numbers)

	for num in numbers:
		sum_of_numbers += num
		
	average = (sum_of_numbers / count_of_numbers)

	return f"Average of {numbers} = {average}"

print(task15_average_of_list([1, 2, 3, 4, 5]))
