# 50
def task50_weather_advice(temperature, raining):
    """
    Task 50:
    Write a function that gives advice based on weather:
    - If raining → "Take an umbrella"
    - Else if temperature > 30 → "Wear light clothes"
    - Else if temperature < 15 → "Wear a jacket"
    - Else → "Weather is fine"
    """

    if raining:
        return "Take an Unbrella"

    elif temperature > 30:
        return "Wear light clothes"

    elif temperature < 15:
        return "Wear a jacket"

    else:
        return "Weather is fine"

print(task50_weather_advice(60, False))