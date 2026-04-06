WARDROBE = {
    "blue sweater": "dirty",
    "brown jacket": "dirty"
}

GET_WARDROBE_ITEMS_TOOL = {
    "type": "function",
    "name": "get_wardrobe_items",
    "description": "Returns a list of all clothing items in the wardrobe along with their current status (clean o dirty)",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

WASH_CLOTHING_TOOL = {
    "type": "function",
    "name": "wash_clothing",
    "description": "Washes a dirty clothing item, changing its status to clean. Requires the exact item name as it appears in the wardrobe",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The exact name of the clothing item to wash (e.g., 'blue sweater')"
            }
        },
        "required": ["item_name"]
    }
}

def get_wardrobe_items() -> str:
    return "; ".join(f"Item {item} is {status}" for item,status in WARDROBE.items())

def wash_clothing(item_name: str) -> str:
    if item_name not in WARDROBE:
        return f"Item '{item_name}' not found in wardrobe"
    WARDROBE[item_name] = "clean"
    return f"{item_name} is washed"