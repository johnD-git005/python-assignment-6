"""→ # 35
def task35_student_pass_fail(score):
    
    Task 35:
    Write a function that accepts a student's score
    and returns "Pass" if score >= 50, otherwise "Fail".
    
    pass"""


def task35_student_pass_fail(score):
	
	if score >= 50:
		return f"Score:{score} →  Pass"

	elif score < 0:
		return f"Score:{score} →  Invalid score!"

	else:
		return f"Score:{score} →  Fail"

print(task35_student_pass_fail(49))
