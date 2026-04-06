from butler.tools.weather import CHECK_WEATHER_TOOL, check_weather

TOOLS_REGISTRY = [CHECK_WEATHER_TOOL]

TOOL_NAME_TO_FUNC = {
    "check_weather": check_weather
}