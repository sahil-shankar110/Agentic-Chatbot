# Setup API key 
# Setup LLM and tools
# Setup agent with LLM and tools

from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages import AIMessage


def get_agent_response(llm_id , allow_search, system_prompt, provider, query):

    if provider == "groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY , temperature=0.7 , max_tokens=2048)
    elif provider == "openai":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY , temperature=0.7 , max_tokens=2048)
    else:
        raise ValueError(f"Unknown provider: {provider}")
   
    tools = [TavilySearch(max_results=3)] if allow_search else []
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )
    state = {"messages" : query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_message[-1] if ai_message else "No response from agent"
