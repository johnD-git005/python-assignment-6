# 46
def task46_water_bill(units):
    """
    Task 46:
    Write a function to calculate water bill based on units:
    - First 30 units → 50 per unit
    - Next 20 units → 75 per unit
    - Beyond 50 units → 100 per unit
    """
    if units < 0:
        return "Invalid Input for Units!"

    elif units > 0 and units <= 30:
        first_thirty_minutes = 30
        per_unit = 50
        water_bill_thirty = first_thirty_minutes * per_unit

        return f"Units: {units}, Water Bill: {water_bill_thirty}"

    elif units > 30 and units <= 50:
        first_thirty_minutes = 30
        per_unit_thirty_minutes = 50

        extra_units = units - first_thirty_minutes
        per_unit_next_twenty_minutes = 75

        water_bill = (extra_units * per_unit_next_twenty_minutes) + (first_thirty_minutes * per_unit_thirty_minutes)

        return f"Units: {units}, Water Bill: {water_bill}"

    elif units > 50:
        first_thirty_minutes = 30
        per_unit_thirty_minutes = 50

        extra_units = units - first_thirty_minutes
        per_unit_next_twenty_minutes = 75

        

        water_bill = (extra_units * per_unit_next_twenty_minutes) + (first_thirty_minutes * per_unit_thirty_minutes)

        return f"Units: {units}, Water Bill: {water_bill}"



print(task46_water_bill(30))