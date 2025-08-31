"""# 11
def task11_reverse_string(text):
    
    Task 11:
    Write a function that accepts a string as a parameter
    and returns the string reversed.
    Example: reverse_string("hello") → "olleh"
    
    pass"""


def task11_reverse_string(text):
	return f"Reverse of {text} is {text[::-1]}"

print(task11_reverse_string("hello"))
