import streamlit as st
import requests

st.set_page_config(
    page_title="Agentic AI Chatbot",
    layout="wide"
)

# Session state to store conversation history
if "query_history" not in st.session_state:
    st.session_state.query_history = []
    
if "selected_query" not in st.session_state:
    st.session_state.selected_query = ""

# Sidebar for conversation history
with st.sidebar:
    st.header("Conversation History")
    st.markdown("---")
    if len(st.session_state.query_history) == 0:
        st.info("No conversations yet. Start by asking a question!")
    else:
        # Clear history button
        if st.button("Clear History"):
            st.session_state.query_history = []
            st.session_state.selected_query = ""
            st.rerun()
            
        # Reuse previous queries
        st.markdown("**Click on a previous query to reuse it:**")   
        # Show last 5 queries in reverse order (most recent first)
        for i , past_query in enumerate(reversed(st.session_state.query_history[-5:])):
            display_text = past_query[:30] + "..." if len(past_query) > 30 else past_query    
            if st.button(f"💬 {display_text}", key=f"history_{i}", use_container_width=True):
                st.session_state.selected_query = past_query
                st.rerun()
                
                
st.title("Agentic AI Chatbot")
st.markdown("**Agentic AI Chatbot With Search Capability**")

system_prompt = st.text_area(placeholder="Type your system prompt here...", label="**Define Your Agent**", height=90)
gemini_models = ["gemini-2.5-flash-lite"]
llama_models = ["llama-3.3-70b-versatile"]
model_provider = st.radio("**Select Model**", ["Gemini", "Llama"])

if model_provider == "Gemini":
    selected_model = st.selectbox("Select Gemini Model", gemini_models)
else:
    selected_model = st.selectbox("Select Llama Model", llama_models)

allow_search = st.checkbox("Allow Search Capability")

URL_BACKEND = "https://agentic-chatbot-280p.onrender.com/chat"
query = st.text_area(placeholder="Type your query here...", label="**Enter Your Query**", 
                    height=150 , value=st.session_state.selected_query) # Pre-fill with selected query from history


button = st.button("Search")

if button:
    if query.strip():
        if query not in st.session_state.query_history:
            st.session_state.query_history.append(query)
            
        if len(st.session_state.query_history) > 5:
            st.session_state.query_history = st.session_state.query_history[-5:]    # Keep only the last 5 queries in history
            
        # Clear selected query after submission   
        st.session_state.selected_query = ""
         
        payload = {
            "model_name": selected_model,
            "model_provider": model_provider.lower(),
            "system_prompt": system_prompt,
            "messages": [query],
            "search_allow": allow_search
        }
        try:
            with st.spinner("Thinking... (This may take few seconds)"):
                response = requests.post(URL_BACKEND, json=payload, timeout=120)  

            if response.status_code == 200:
                st.markdown("**Response:**")
                response_data = response.json()
                if isinstance(response_data, dict) and "error" in response_data:
                    st.error("Error from backend: " + response_data["error"])
                else:
                    st.subheader("Agent Response")
                    st.write(response_data)
            else:
                st.error(f"Backend error: Status {response.status_code} — {response.text}")

        except requests.exceptions.Timeout:
            st.error("Request timed out. Please try again in 30 seconds.")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Please check if the API is running.")
    else:
        st.warning("Please enter a query first!")