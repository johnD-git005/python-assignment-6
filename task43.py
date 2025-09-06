# 43
def task43_student_average(scores):
    """
    Task 43:
    Write a function that accepts a dictionary of subject:score
    and returns the student's average score.
    Example: {"math": 80, "english": 70} → 75.0
    """
    total = 0
    
    for key, value in scores.items():
        total += value
        average = total / len(list(scores)) 

    return f"Average: {average}"

print(task43_student_average({"math": 80, "english": 70,}))