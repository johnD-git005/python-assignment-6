""" # 24
def task24_swap_values(a, b):
   
    Task 24:
    Write a function that accepts two values
    and returns them swapped.
    Example: swap_values(3, 7) → (7, 3)
   
    pass"""


def task24_swap_values(a, b):
	
	value_list = []

	for values in a, b:
		value_list.append(values)

	return f"({a}, {b}) →  {tuple(value_list[::-1])}"

print(task24_swap_values(33, 47))


