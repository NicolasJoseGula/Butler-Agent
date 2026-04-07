import requests
import os

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

CHECK_WEATHER_TOOL = {
    "type": "function",
    "name": "check_weather",
    "description": "Retrieves the current weather conditions for a given city. Returns temperature, conditions, and humidity",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The name of the city to get weather for (e.g., 'Buenos Aires', 'London')"
            }
        },
        "required": ["city"]
    }
}

def check_weather(city: str) -> str:
    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={"key": WEATHER_API_KEY, "q":city}
    )
    data = response.json()
    condition = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    feels_like = data["current"]["feelslike_c"]
    humidity = data["current"]["humidity"]
    return f"{city}: {condition}, {temp_c}C (feels like {feels_like}C), humidity {humidity}%"