"""# 22
def task22_string_length(text):
    
    Task 22:
    Write a function that accepts a string
    and returns its length without using len().
    
    pass"""

length = 0
def task22_string_length(text):
	
	word_list = list(text)	
	word_dict = {}
	length = 0

	for word in word_list:
		if word in word_dict:
			word_dict[word] += 1

		else:
			word_dict[word] = 1

	for char in word_dict:
		length += word_dict[char]

	return f"Length of '{text}' →  {length}"

print(task22_string_length("programming"))
