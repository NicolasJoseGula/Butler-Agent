# Entry point
from butler.agent import run_agent_loop

user_query = "What is the weather today?"

print(f"[USER]: {user_query}")
print(f"[ASSISTANT]: {run_agent_loop(user_query)}")

