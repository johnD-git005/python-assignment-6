"""# 23
def task23_grade_student(score):
    
    Task 23:
    Write a function that accepts a score (0–100)
    and returns the grade based on this scale:
    A: 70–100
    B: 60–69
    C: 50–59
    D: 40–49
    E: 30–39
    F: 0–29
    pass"""

def task23_grade_student(score):

	if score >= 70 and score <= 100:
		return "Grade →  A"

	elif score >= 60 and score <= 69:
		return "Grade →  B"

	elif score >= 50 and score <= 59:
		return "Grade →  C"

	elif score >= 40 and score <= 49:
		return "Grade →  D"

	elif score >= 30 and score <= 39:
		return "Grade →  E"

	elif score >= 0 and score <= 29:
		return "Grade →  F"

	else:
		return "Invalid Score!"

print(task23_grade_student(1000))
