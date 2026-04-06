CHECK_WEATHER_TOOL = {
    "type": "function",
    "name": "check_weather",
    "description": "Retrieves the current weather conditions for the user's location. Returns a short description of the current weather (e.g., temperature, precipitation.)",
    "parameters":{
        "type" : "object",
        "properties": {},
        "required": []
    }
}

def check_weather() -> str:
    return "Cold, rainy"