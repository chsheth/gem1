import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Text - Chat data

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(input):
    response = chat.send_message(input, stream=True)
    return response

st.set_page_config(page_title="Gemini LLM Application")
st.header("Gemini LLM Application - Chat Demo")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] =[]

input = st.text_input("Please ask a question: ", key="input")
submit = st.button("Submit")

if submit and input: #input needs to be available and submit should be clicked
    response = get_gemini_response(input)
    st.session_state["chat_history"].append(("You", input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat History:")

for role, text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')

