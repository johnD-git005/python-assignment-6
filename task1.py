"""# 1
def task1_sum_of_two_numbers(a, b):
    Task 1:
    Write a *function that accepts two numbers (a and b) as parameters
    and returns their sum.
    Test the function by calling it with different numbers.
  
    pass """

def task1_sum_of_two_numbers(a, b):
	result = a + b
	return f"{a} + {b} = {result}"

print(task1_sum_of_two_numbers(2.5, 5))
print(task1_sum_of_two_numbers(7, 3))
print(task1_sum_of_two_numbers(8, 4.4))
print(task1_sum_of_two_numbers(9, 1))
print(task1_sum_of_two_numbers(6, 0))
