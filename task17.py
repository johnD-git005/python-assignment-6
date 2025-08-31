"""# 17
def task17_palindrome_check(word):
    
    Task 17:
    Write a function that checks if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    Example: palindrome_check("madam") → True
    
    pass"""

def task17_palindrome_check(word):

	if word[:] == word[::-1]:
		return f"{word} is Pallindrome"

	else:
		return f"{word} not a Pallindrome!"

print(task17_palindrome_check("madam"))
