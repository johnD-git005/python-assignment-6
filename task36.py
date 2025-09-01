"""→ # 36
def task36_calculate_fine(days_late):
    
    Task 36:
    Write a function that calculates library book fine:
    - First 5 days: 20 per day
    - 6–10 days: 50 per day
    - Beyond 10 days: 100 per day
    Example: calculate_fine(7) → 5*20 + 2*50 = 200
    
    pass"""

def task36_calculate_fine(days_late):
	if days_late > 0 and days_late <= 5:
		first_five_days = 20
		library_book_fine = first_five_days * days_late

		return f"Days: {days_late} →  Library Book Fine: {library_book_fine}"

	elif days_late >= 6 and days_late <= 10:
		first_five_days = 5
		fine_first_five_days = 20
		fine_after_five_days = 50
		days = days_late - first_five_days

		library_book_fine = (first_five_days * fine_first_five_days) + (fine_after_five_days * days)

		return f"Days: {days_late} →  Library Book Fine: {library_book_fine}"

	elif days_late > 10:
		first_five_days = 5
		fine_first_five_days = 20
		fine_for_days_greater_than_ten = 100
		days_greater_than_ten = days_late - first_five_days
		
		library_book_fine = (fine_first_five_days * first_five_days) + (fine_for_days_greater_than_ten * days_greater_than_ten)

		return f"Days: {days_late} →  Library Book Fine: {library_book_fine}"

	else:
		return "Invalid Input for Days!"


print(task36_calculate_fine(7))
