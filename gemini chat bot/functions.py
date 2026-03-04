import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from functions import map_role, get_reply

load_dotenv()

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("🤖 Gemini AI Chatbot")

for msg in st.session_state.chat.history:
    with st.chat_message(map_role(msg.role)):
        st.markdown(msg.parts[0].text)

user_input = st.chat_input("Ask something")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        reply = get_reply(user_input)
        st.markdown(reply)