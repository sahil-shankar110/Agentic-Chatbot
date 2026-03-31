from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import get_agent_response
import uvicorn
import os

class RequestModel(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    search_allow: bool 


MODEL_ALLOWED = ["llama-3.3-70b-versatile", "openai/gpt-oss-120b"]
app = FastAPI(title="Agentic AI Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Status": "Welcome to the Agentic AI Chatbot API. Use the /chat endpoint to interact with the agent."}
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
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0" , port=port)

# uvicorn backend:app --reload