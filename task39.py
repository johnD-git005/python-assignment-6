"""# 39

def task39_is_leap_year(year):
    
    Task 39:
    Write a function that accepts a year and returns True if it is a leap year,
    otherwise False.
    Rule: Year divisible by 4 → leap year, but divisible by 100 → not leap,
    unless divisible by 400.
    
    pass"""

def task39_is_leap_year(year):

	if year % 4 == 0 and year % 100 != 0:
		return f"Year: {year} →  True"

	elif year % 400 == 0:
		return f"Year: {year} →  True"

	else:
		return f"Year: {year} →  False"

print(task39_is_leap_year(1900))
