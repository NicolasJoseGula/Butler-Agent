# Entry point
from butler.agent import run_agent_loop

context = []

while True:
    user_input = input("\n[USER]: ")
    
    if user_input.lower() in ["q", "quit", "exit"]:
        print("Goodbye!")
        break
    
    context.append({"role": "user", "content": user_input})
    response = run_agent_loop(context)
    print(f"[ASSISTANT]: {response}")
    context.append({"role": "assistant", "content": response})

