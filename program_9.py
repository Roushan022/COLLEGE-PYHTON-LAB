def classify_weather(temperature, humidity, wind_speed):
    # Classify each reading
    if temperature >= 30:
        t = "Hot"
    elif temperature < 15:
        t = "Cold"
    else:
        t = "Moderate"

    if humidity >= 70:
        h = "Humid"
    elif humidity < 30:
        h = "Dry"
    else:
        h = "Normal"
      
    if wind_speed > 40:
        w = "Stormy"
    else:
        w = "Calm"
    # Rules for forecast
    if t == "Hot" and h == "Humid":
        forecast = "Hot and humid, possible thunderstorms in the evening."
    elif t == "Cold" and w == "Stormy":
        forecast = "Cold and stormy \u2014 stay indoors if possible."
    elif t == "Moderate" and h == "Normal" and w == "Calm":
        forecast = "Pleasant weather, good for outdoor activities."
    else:
        forecast = "Moderate weather, no special conditions."

    print(f"Temperature: {temperature} C  -> {t}")
    print(f"Humidity   : {humidity}%    -> {h}")
    print(f"Wind Speed : {wind_speed} km/h -> {w}")
    print(f"Forecast   : {forecast}")
    print("-" * 45)

# ---- Driver code: test with sample readings ----
classify_weather(temperature=38, humidity=75, wind_speed=10)
classify_weather(temperature=10, humidity=20, wind_speed=45)
classify_weather(temperature=25, humidity=50, wind_speed=8)
