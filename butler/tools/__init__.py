from butler.tools.weather import CHECK_WEATHER_TOOL, check_weather
from butler.tools.wardrobe import GET_WARDROBE_ITEMS_TOOL, WASH_CLOTHING_TOOL, get_wardrobe_items, wash_clothing

TOOLS_REGISTRY = [
    CHECK_WEATHER_TOOL,
    GET_WARDROBE_ITEMS_TOOL,
    WASH_CLOTHING_TOOL
    ]

TOOL_NAME_TO_FUNC = {
    "check_weather": check_weather,
    "get_wardrobe_items": get_wardrobe_items,
    "wash_clothing": wash_clothing
}

