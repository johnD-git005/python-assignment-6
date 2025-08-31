"""# 7
def task7_find_max(a, b, c):
    
    Task 7:
    Write a function that accepts three numbers as parameters
    and returns the largest number.
    
    pass"""

def task7_find_max(a, b, c):
	number = [a, b, c]
	largest = number[0] 
	for num in number:
		if num > largest:
			largest = num

	return largest	

		

x = task7_find_max(17, 8, 9)
print(x)
