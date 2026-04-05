# Entry point
from butler.agent import run

user_query = "What is the weather today?"

print(f"[USER]: {user_query}")
print(f"[ASSISTANT]: {run(user_query)}")

