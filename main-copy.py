def agent_loop(user_query, system_prompt, tools):
    """
    Core agentic loop: Thought -> Act -> Observe
    """
    
    conversation_history = [{"role": "user", "content": user_query}]
    
    while True:
        #THOUGHT: LLM decides what to do next
        llm_response = call_llm(system_prompt, conversation_history, tools)
        conversation_history.append({"role":"agent", "content": llm_response})
        
        #Check if LLM wants to use a tool
        if llm_response.has_tool_calls():
            # ACT: Execute the tool
            tool_result = execute_tool(llm_response.tool_call)
            
            #OBSERVE: Add result to history
            conversation_history.append({"role":"tool", "content":tool_result})
            
            # Loop continues -> back to THOUGHT
            continue
    else:
        # No tool call -> final answer reached
        return llm_response.content

    
    