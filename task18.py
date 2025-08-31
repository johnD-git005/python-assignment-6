"""# 18
def task18_convert_minutes_to_hours(minutes):
    
    Task 18:
    Write a function that accepts minutes as input
    and converts it into hours and minutes.
    Example: 130 minutes → "2 hour(s) 10 minute(s)"
    
    pass """

def task18_convert_minutes_to_hours(minutes):

	if minutes < 0:
		return "Invalid Minute(s) inputed"
	
	elif minutes >= 0:
		hours  = minutes // 60
		conversion = hours * 60
		final_minutes = minutes - conversion

	else:
		return "Invalid input!"

	return f"{minutes} minute(s) →  {hours} hour(s) {final_minutes} minute(s)"

print(task18_convert_minutes_to_hours(130))
