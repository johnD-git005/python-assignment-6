# 49
def task49_calculate_grade_point(score):
    """
    Task 49:
    Write a function that converts score (0–100) into grade points:
    - 70–100 → 5
    - 60–69 → 4
    - 50–59 → 3
    - 45–49 → 2
    - 40–44 → 1
    - <40 → 0
    """
    if score >= 70 and score <= 100:
        return 5

    elif score >= 60 and score <= 69:
        return 4

    elif score >= 50 and score <= 59:
        return 3

    elif score >= 45 and score <= 49:
        return 2

    elif score >= 40 and score <= 44:
        return 1
    
    elif score >= 0 and score <= 39:
        return 0
    
    else:
        return "Invalid score!"

print(task49_calculate_grade_point(40))