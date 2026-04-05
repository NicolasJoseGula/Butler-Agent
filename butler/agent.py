# Agent loop
from butler.client import client
from butler.prompts import SYSTEM_PROMPT

def run(user_query: str) -> str:
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=SYSTEM_PROMPT,
        input=user_query,
    )
    
    for item in response.output:
        if item.type == "message":
            return item.content[0].text
        
