# 47


def task47_find_longest_word(sentence):
    """
    Task 47:
    Write a function that accepts a sentence
    and returns the longest word in it.
    Example: "I love programming" → "programming"
    """

    split_sentence = sentence.split()
    list_word = []
    longest_word = []
    
    for word in split_sentence:
        list_word.append(len(word))

    largest = list_word[0]

    for word in list_word:
        if word > largest:
            largest = word
    
    for word in split_sentence:
        if len(word) == largest:
            longest_word.append(word)
   
    return f"'{sentence}', Longest word(s): {longest_word}, Length: {largest}"


print(task47_find_longest_word("I love 12345678901 Programming"))