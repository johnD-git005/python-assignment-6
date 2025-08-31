"""→ # 31
def task31_find_median(numbers):
    
    Task 31:
    Write a function that accepts a list of numbers
    and returns the median value.
    (Hint: Sort the list first, then handle odd/even length cases.)
    
    pass"""


def task31_find_median(numbers):

	if numbers == []:
		return "List Cannot be Empty!"

	elif len(numbers) % 2 == 0:
		even = sorted(numbers)
		print(f"\n {even}")
		half = len(even) // 2

		first_half = even[:half]
		second_half = even[half:]

		index_first_half = len(even[:half]) - 1
		index_second_half = second_half[0]

		first_middle_number = first_half[index_first_half]
		second_middle_number = second_half[0]

		median = (first_middle_number + second_middle_number) // 2

		return f"\n Median →  {median}"

	else:
		even = sorted(numbers)
		print(f"\n {even}")

		index_of_median = len(even) // 2

		median = even[index_of_median]
		return f"\n Median →  {median}"
		
print(task31_find_median([3, 2, 4, 5]))
