# 44
def task44_calculate_age(current_year, birth_year):
    """
    Task 44:
    Write a function that accepts current year and birth year,
    and returns the age.
    Example: calculate_age(2025, 2000) → 25
    """
    age = current_year - birth_year
    return f"Age: {age}"

print(task44_calculate_age(2025, 2000))