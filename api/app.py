from fastapi import FastAPI
from api.models import ChatRequest, ChatResponse
from butler.agent import run_agent_loop
from butler.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Buttler Agent API")

sessions: dict[str, list[str]] = {}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    context = sessions.get(request.session_id, [])
    context.append({"role": "user", "content": request.message})
    
    logger.info(f"Session '{request.session_id}' - user: {request.message} ")
    
    response = run_agent_loop(context)
    context.append({"role": "assistant", "content": response})
    
    sessions[request.session_id] = context
    
    logger.info(f"Session '{request.session_id}' - assistant: {response}")
    
    return ChatResponse(session_id=request.session_id, response=response)

@app.delete("/session/{session_id}")
def clear_session(session_id: str):
    sessions.pop(session_id, None)
    logger.info(f"Session '{session_id}' cleared")
    return {"message": f"Session '{session_id}' cleared"}

