# Agent loop
import json
from butler.client import client
from butler.prompts import SYSTEM_PROMPT
from butler.tools import TOOLS_REGISTRY, TOOL_NAME_TO_FUNC

MAX_ITERATIONS = 5

def run_agent_loop(context: list) -> str:    
    print("[ENTERING AGENT LOOP]")
    
    for _ in range(MAX_ITERATIONS):
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions=SYSTEM_PROMPT,
            input=context,
            tools=TOOLS_REGISTRY
        )
        
        item_types = [type(item).__name__ for item in response.output]
        print(f"[THINK]: Model decided to return these items: {item_types}")

        for item in response.output:
            if item.type == "function_call":
                arguments = json.loads(item.arguments)
                print(f'[ACT]: Calling "{item.name}" with arguments {arguments}')

                if item.name not in TOOL_NAME_TO_FUNC:
                    result =  f"Error: unknown tool '{item.name}'"
                else:
                    try:
                        result = TOOL_NAME_TO_FUNC[item.name](**arguments)
                    except Exception as e:
                        result = f"Error executing tool: {str(e)}"
                        
                print(f"[OBSERVE]: Result {result}")
                
                context.append(item)
                context.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": result,
                })   
            elif item.type == "message":
                print("[EXITING AGENT LOOP]")
                return item.content[0].text
    return "Max iterations reached without a final response"   
