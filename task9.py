"""# 9
def task9_count_vowels(word):
    
    Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
    
    pass"""

def task9_count_vowels(word):

	list_word = []
	vowels = "aeiou"
	flag = False

	for vowel in word:
		if vowel in vowels:
			list_word.append(vowel)
			flag = True
	else:
		if flag == False:
			return f"Vowel not found in {word}"

	return f"{word} has {len(list_word)} vowel(s)"

print(task9_count_vowels("apple"))

