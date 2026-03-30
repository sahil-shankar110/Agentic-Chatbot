import streamlit as st
import requests 

st.set_page_config(
    page_title="Agentic AI Chatbot",
    layout="wide"
)
st.title("Agentic AI Chatbot")
st.markdown("**Agentic AI Chatbot With Search Capability**")

system_prompt = st.text_area(placeholder="Type your system prompt here...", label="**Define Your Agent**",height=90)
groq_models = ["meta-llama/llama-4-scout-17b-16e-instruct"]
openai_models = ["openai/gpt-oss-120b"]
model_provider = st.radio("**Select Model**", ["Groq", "OpenAI"])

if model_provider == "Groq":
    selected_model = st.selectbox("Select Groq Model", groq_models)
else:
    selected_model = st.selectbox("Select OpenAI Model", openai_models)

allow_search = st.checkbox("Allow Search Capability")    

URL_BACKEND = "https://your-app-name.onrender.com/chat" # Update with your actual backend URL
query = st.text_area(placeholder="Type your query here...", label="**Enter Your Query**",height=150)

button = st.button("Search")

if button:
    if query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": model_provider.lower(),
            "system_prompt": system_prompt,
            "messages": [query],
            "search_allow": allow_search
        }
        response = requests.post(URL_BACKEND, json=payload)
        if response.status_code == 200:
            st.markdown("**Response:**")
            response_data = response.json()
            if isinstance(response_data, dict) and "error" in response_data:
                st.error("Error from backend: " + response_data["error"])
            else:
                st.subheader("Agent Response")
                st.write(response_data)
