"""→ # 30
def task30_convert_to_seconds(hours, minutes, seconds):
    
    Task 30:
    Write a function that accepts hours, minutes, and seconds
    and converts the entire time to total seconds.
    Example: 1h 1m 1s → 3661 seconds
    
    pass"""

def task30_convert_to_seconds(hours, minutes, seconds):

	if hours < 0 and minutes < 0 and seconds < 0:
		return "Invalid Input for Hour(s), Minute(s), Second(s)"

	elif hours < 0 and minutes < 0:
		return "Invalid Input for Hour(s), Minute(s)"

	elif hours < 0 and seconds < 0:
		return "Invalid Input for Hour(s), Second(s)"

	elif minutes < 0 and seconds < 0:
		return "Invalid Input for Minute(s), Second(s)"

	elif hours < 0:
		return "Invalid Input for Hours"

	elif minutes < 0:
		return "Invalid Input for Minutes"

	elif seconds < 0:
		return "Invalid Input for Seconds"

	else:
		
		convert_hours_to_second = hours * 3600
		convert_minutes_to_second = minutes * 60
		total_seconds = convert_hours_to_second + convert_minutes_to_second + seconds

		return f"{hours} hr(s), {minutes} min(s), {seconds} sec(s) →  {total_seconds} secs"

print(task30_convert_to_seconds(1, 1, 1))
