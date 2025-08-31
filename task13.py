"""# 13
def task13_scope_demo():
    
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
    
    pass"""

global_scope = "global_scope_outside_the_function"

def task13_scope_demo():
	global_scope = "local_scope_inside_the_function"


print(global_scope)

task13_scope_demo()

print(global_scope)

	
