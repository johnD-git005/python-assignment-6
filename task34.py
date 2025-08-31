"""→ # 34
def task34_capitalize_names(names):
    
    Task 34:
    Write a function that accepts a list of names in lowercase
    and returns a new list with each name capitalized.
    Example: ["john", "mary"] → ["John", "Mary"]
    
    pass"""

def task34_capitalize_names(names):

	new_names = []

	for name in names:
		capitalized_name = name.capitalize()
		new_names.append(capitalized_name)

	return f"{names} →  {new_names}"

print(task34_capitalize_names(["john", "mary"]))
 
