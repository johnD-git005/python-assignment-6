"""→ # 25
def task25_scope_counter():
    
    Task 25:
    Create a counter function that uses a global variable.
    Each time the function is called, it should increase
    the counter by 1 and print the current count.
    This demonstrates modifying global variables inside functions.
    
    pass"""

counter = {1:0}
def task25_scope_counter():
	
	for count in counter:
		counter[count] += 1

	return (counter[count])

print(task25_scope_counter())
print(task25_scope_counter())
print(task25_scope_counter())
