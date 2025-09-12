def task42_find_mode(numbers):
    """
    Task 42:
    Write a function that finds the mode (most frequent number) in a list.
    If there are multiple modes, return any one of them.
    """
    new_dict = {}
    my_list = []

    if len(numbers ) == 0:
        return "Empty List!"
    
    else:

        for number in numbers:
            if number in new_dict:
                new_dict[number] += 1
            else:
                new_dict[number] = 1
        
        for key, value in new_dict.items():
            my_list.append(value)

        largest_number = my_list[0]

        for number in my_list:
            if number > largest_number:
                largest_number = number
    
        for key, value in new_dict.items():
            if value == largest_number:
                return f"Mode: {key}"

print(task42_find_mode([1, 2, 3]))