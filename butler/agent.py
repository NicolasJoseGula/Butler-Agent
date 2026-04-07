# Agent loop
import json
from butler.client import client
from butler.prompts import SYSTEM_PROMPT
from butler.tools import TOOLS_REGISTRY, TOOL_NAME_TO_FUNC
from butler.logger import get_logger

logger = get_logger(__name__)

MAX_ITERATIONS = 5

def run_agent_loop(context: list) -> str:    
    logger.info("Entering agent loop")
    
    for _ in range(MAX_ITERATIONS):
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions=SYSTEM_PROMPT,
            input=context,
            tools=TOOLS_REGISTRY
        )
        
        item_types = [type(item).__name__ for item in response.output]
        logger.info(f"[THINK] Model decided to return these items: {item_types}")

        for item in response.output:
            if item.type == "function_call":
                arguments = json.loads(item.arguments)
                logger.info(f'[ACT]: Calling "{item.name}" with arguments {arguments}')

                if item.name not in TOOL_NAME_TO_FUNC:
                    result =  f"Error: unknown tool '{item.name}'"
                    logger.error(f"Unknown tool requested: {item.name}")
                else:
                    try:
                        result = TOOL_NAME_TO_FUNC[item.name](**arguments)
                    except Exception as e:
                        result = f"Error executing tool: {str(e)}"
                        logger.error(f"Tool execution failed for'{item.name}': {e}")
                        
                logger.info(f"[OBSERVE]: Result {result}")
                
                context.append(item)
                context.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": result,
                })   
            elif item.type == "message":
                logger.info("Exiting agent loop")
                return item.content[0].text
    return "Max iterations reached without a final response"   
