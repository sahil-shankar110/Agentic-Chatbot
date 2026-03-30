from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI
from agent import get_agent_response
import uvicorn

class RequestModel(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    search_allow: bool 


MODEL_ALLOWED = ["meta-llama/llama-4-scout-17b-16e-instruct", "openai/gpt-oss-120b"]
app = FastAPI(title="Agentic AI Chatbot")

@app.post("/chat")
def chat(request: RequestModel):
    if request.model_name not in MODEL_ALLOWED:
        return {"error": "Model not allowed"}
        
    llm_id=request.model_name
    allow_search=request.search_allow
    system_prompt=request.system_prompt
    provider=request.model_provider
    query=request.messages

    response = get_agent_response(llm_id, allow_search, system_prompt, provider, query)
    return response
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# uvicorn backend:app --reload