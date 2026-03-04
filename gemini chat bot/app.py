import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load environment variables
load_dotenv()

# 2. Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. Helper Functions
def map_role(role):
    # Gemini uses 'model', Streamlit chat bubbles use 'assistant'
    return "assistant" if role == "model" else role

# 4. Streamlit UI Setup
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini AI Chatbot by Kishanth")

# Initialize Chat Session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display Chat History
for msg in st.session_state.chat.history:
    with st.chat_message(map_role(msg.role)):
        st.markdown(msg.parts[0].text)

# Chat Input
user_input = st.chat_input("Ask something...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(user_input)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")