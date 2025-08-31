""" # 33
def task33_word_count(sentence):
    
    Task 33:
    Write a function that accepts a sentence
    and returns the number of words in it.
    Example: "I love Python" → 3
    
    pass"""


def task33_word_count(sentence):

	split_sentence = sentence.split()
	number_of_words = len(split_sentence)
	return f"'{sentence}' →  Number of Words: {number_of_words}"

print(task33_word_count("I love Python"))

